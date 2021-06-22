from selenium import webdriver
import unittest2
import HtmlTestRunner


class LoginHRM(unittest2.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:\\Users\\lmane\\PycharmProjects\\SeleniumProject\\Drivers\\chromedriver.exe")
        cls.driver.maximize_window()

    def test_title(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.assertEqual("OrangeHRM", self.driver.title, "the title is not matching")

    def test_Login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        self.assertEqual("OrangeHRM", self.driver.title, "the title is not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest2.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\lmane\\PycharmProjects\\UnitTestHTMLReport\\Reports"))

