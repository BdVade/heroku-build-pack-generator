from django.test import TestCase, RequestFactory


# Create your tests here.

class BaseTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self) -> None:
        self.req_factory = RequestFactory()


class TestModel(BaseTest):
    pass


class TestViews(BaseTest):
    pass


class TestForm(BaseTest):
    pass
