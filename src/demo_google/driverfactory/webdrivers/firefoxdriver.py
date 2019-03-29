from driverfactory.driverinterface import DriverInterface
from selenium import webdriver
import allure


class FirefoxDriver(DriverInterface):
    @allure.step("Initiate the Firefox")
    def initiate_driver(self):
        return webdriver.Firefox()
