class JobService:
    def __init__(self, driver):
        self._driver = driver

    def get(self, id):
        with self._driver.session() as session:
            return None
