from driverfactory.driverinterface import DriverInterface
from selenium import webdriver
import allure


class ChromeDriver(DriverInterface):
    @allure.step("Initiate the Chrome")
    def initiate_driver(self):
        return webdriver.Chrome()
