from selenium import webdriver
from time import sleep, time

class ChromeAuth :
    def __init__(self, username, passwd, driver = __file__[:-7:] + 'chromedriver') :
        self.auth_token = None
        self.login = username
        self.driver = driver        
        self.passwd = passwd

    def get_auth_token(self) :
        if self.auth_token == None :
            self.auth_token = self.__obtain_token()
        return self.auth_token

    def __obtain_token(self) :
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")

        driver = webdriver.Chrome(options=options, executable_path=self.driver)

        driver.get("https://dnevnik.mos.ru")

        login_button = driver.find_element_by_xpath('//div[2]/div/a')
        login_button.click()

        sleep(1)

        password_input = driver.find_element_by_id("password")
        submit_button = driver.find_element_by_id("bind")
        login_input = driver.find_element_by_id("login")

        password_input.send_keys(self.passwd)
        login_input.send_keys(self.login)

        submit_button.click()

        auth_token = driver.get_cookie("auth_token")

        while not auth_token :
            sleep(0.25)
            auth_token = driver.get_cookie("auth_token")

        self.profile_id = int(driver.get_cookie("profile_id")["value"])

        return auth_token

class FirefoxAuth() :
    def __init__(self, username, passwd, driver = __file__[:-7:] + 'geckodriver') :
        self.auth_token = None
        self.login = username
        self.driver = driver        
        self.passwd = passwd

    def get_auth_token(self) :
        if self.auth_token == None :
            self.auth_token = self.__obtain_token()
        return self.auth_token

    def __obtain_token(self) :
        options = webdriver.FirefoxOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")

        driver = webdriver.Firefox(options=options, executable_path=self.driver)

        driver.get("https://dnevnik.mos.ru")

        login_button = driver.find_element_by_xpath('//div[2]/div/a')
        login_button.click()

        sleep(1)

        password_input = driver.find_element_by_id("password")
        submit_button = driver.find_element_by_id("bind")
        login_input = driver.find_element_by_id("login")

        password_input.send_keys(self.passwd)
        login_input.send_keys(self.login)

        submit_button.click()

        auth_token = driver.get_cookie("auth_token")

        while not auth_token :
            sleep(0.25)
            auth_token = driver.get_cookie("auth_token")

        self.profile_id = int(driver.get_cookie("profile_id")["value"])

        return auth_token
