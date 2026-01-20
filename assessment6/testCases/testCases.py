def test_pass(page):
    print("test_pass passed")

def test_fail():
    result = "fail"
    assert result == "pass"