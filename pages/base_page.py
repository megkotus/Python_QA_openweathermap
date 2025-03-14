from header import Header


class BasePage:
    def __init__(self, driver, url, has_header=True):
        self.driver = driver
        self.url = url
        self.header = Header if has_header else None
