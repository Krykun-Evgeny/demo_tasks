from values import integers
from values import strings


class DriverInterface:
    def initiate_driver(self):
        pass

    def __init__(self):
        self.instance = self.initiate_driver()

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.implicitly_wait(integers.default_timeout)
            self.instance.get(url)
        else:
            raise TypeError(strings.url_type_error_message)

