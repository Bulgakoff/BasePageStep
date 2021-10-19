class BasePage():
    def __init__(self, url, browser, timeout=10):
        self.url = url
        self.browser = browser
        self.timeout = timeout

    def open(self):
        self.browser.get(self.url)
        self.browser.implicitly_wait(self.timeout)
