import pytest
from datetime import datetime
from pathlib import Path
import shutil
import subprocess
import os
import allure
from playwright.sync_api import sync_playwright

# ================== CONFIG ==================
MAX_REPORTS = 20

HTML_DIR = Path("reports/html")
ALLURE_RESULTS = Path("reports/allure/results")
ALLURE_REPORTS = Path("reports/allure/report")
VIDEO_DIR = Path("reports/videos")
SCREENSHOT_DIR = Path("reports/screenshots")


# ================== HELPERS ==================
def cleanup_old_reports(path: Path, keep_last: int):
    if not path.exists():
        return

    items = sorted(
        path.iterdir(),
        key=lambda x: x.stat().st_mtime,
        reverse=True
    )

    for old in items[keep_last:]:
        if old.is_file():
            old.unlink()
        else:
            shutil.rmtree(old)


# ================== PYTEST CONFIG ==================
def pytest_configure(config):
    timestamp = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")

    HTML_DIR.mkdir(parents=True, exist_ok=True)
    ALLURE_RESULTS.mkdir(parents=True, exist_ok=True)
    ALLURE_REPORTS.mkdir(parents=True, exist_ok=True)
    VIDEO_DIR.mkdir(parents=True, exist_ok=True)
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

    html_report = HTML_DIR / f"report_{timestamp}.html"
    config._html_report_path = html_report

    if hasattr(config.option, "htmlpath"):
        config.option.htmlpath = str(html_report)
        config.option.self_contained_html = True


# ================== PLAYWRIGHT FIXTURES ==================
@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context(
        viewport={"width": 1280, "height": 720},
        record_video_dir=str(VIDEO_DIR),
        record_video_size={"width": 1280, "height": 720}
    )
    yield context
    context.close()


@pytest.fixture
def page(context, request):
    page = context.new_page()
    request.node.page = page  # 🔑 store page on test node
    yield page
    page.close()              # 🔑 video finalized here


# ================== SCREENSHOT ON FAILURE ==================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = getattr(item, "page", None)

        if page:
            screenshot_path = SCREENSHOT_DIR / f"{item.name}.png"
            page.screenshot(path=str(screenshot_path))

            allure.attach.file(
                str(screenshot_path),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )


# ================== VIDEO AFTER TEARDOWN ==================
def pytest_runtest_teardown(item, nextitem):
    page = getattr(item, "page", None)

    if page and page.video:
        video_path = page.video.path()

        if os.path.exists(video_path):
            allure.attach.file(
                video_path,
                name="Failure Video",
                attachment_type=allure.attachment_type.WEBM
            )


# ================== SESSION FINISH ==================
def pytest_sessionfinish(session, exitstatus):
    cleanup_old_reports(HTML_DIR, MAX_REPORTS)

    timestamp = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
    allure_output = ALLURE_REPORTS / f"report_{timestamp}"
    allure_output.mkdir(parents=True, exist_ok=True)

    try:
        subprocess.run(
            [
                "docker", "run", "--rm",
                "--user", f"{os.getuid()}:{os.getgid()}",
                "-v", f"{ALLURE_RESULTS.absolute()}:/allure-results",
                "-v", f"{allure_output.absolute()}:/allure-report",
                "frankescobar/allure-docker-service",
                "allure", "generate",
                "/allure-results",
                "-o", "/allure-report",
                "--clean"
            ],
            check=True
        )

        cleanup_old_reports(ALLURE_REPORTS, MAX_REPORTS)
        print(f"[ALLURE REPORT GENERATED] {allure_output}")

    except Exception as e:
        print(f"[ALLURE ERROR] {e}")
