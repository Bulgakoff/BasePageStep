import math
import time

from selenium.common.exceptions import NoAlertPresentException  # � ������ �����


class BasePage():
    def __init__(self, url, browser, timeout=10):
        self.url = url
        self.browser = browser
        self.timeout = timeout

    def open(self):
        self.browser.get(self.url)
        print(self.browser.current_url)
        self.browser.implicitly_wait(self.timeout)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert

        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
