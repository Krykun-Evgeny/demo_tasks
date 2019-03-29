from values import strings
from driverfactory.webdrivers.chromedriver import ChromeDriver
from driverfactory.webdrivers.firefoxdriver import FirefoxDriver


class DriverFactory:
    @staticmethod
    def get_driver(string_browser_name):
        if isinstance(string_browser_name, str):
            if string_browser_name.lower() == strings.browser_name_chrome:
                return ChromeDriver()
            if string_browser_name.lower() == strings.browser_name_firefox:
                return FirefoxDriver()
            assert False, strings.browser_non_supported_message.format(string_browser_name)
        else:
            raise TypeError(strings.browser_type_error_message)
