import unittest
from selenium import webdriver


class FirstTest(unittest.TestCase):

    def test_setUp(self):
        driver = self.driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://tesco.com")
        self.driver.find_element_by_link_text("Sign in").click()

    def test_loginPage(self):
        driver = self.driver
        username = self.driver.find_element_by_name("username")
        username.send_keys("shak_bashir@hotmail.com")
        password = self.driver.find_element_by_name("password")
        password.send_keys("Aminah13")
        self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[2]/div/form/button").click()

    def test_checkPage(self):
        driver = self.driver
        assert "shakeel" in driver.title

    def test_pickingGroceries(self):
        driver = self.driver
        self.driver.find_element_by_xpath("/html/body/div[1]/div/nav/div[1]/ul/li[1]/div/div[1]/a").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/nav/div[1]/ul/li[1]/div/div[1]/div/div[2]/div[1]/ul/li[2]/a/h3/span").click()