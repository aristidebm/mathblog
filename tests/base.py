from flask_testing import TestCase

from mathblog import create_app
from mathblog.config import TestConfig


class BaseTestCase(TestCase):
    def create_app(self):
        return create_app(config=TestConfig)

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


class BaseViewTestCase(BaseTestCase):
    pass
