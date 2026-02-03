class LoginPage:

    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.page.click("#submit")
