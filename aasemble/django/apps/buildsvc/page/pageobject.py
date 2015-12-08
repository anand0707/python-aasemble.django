#from openstack_dashboard.test.integration_tests import basewebobject


#class PageObject(basewebobject.BaseWebObject):
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class PageObject(StaticLiveServerTestCase):
    """Base class for page objects."""

     @classmethod
    def setUpClass(cls):
        super(RepositoryFunctionalTests, cls).setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(RepositoryFunctionalTests, cls).tearDownClass()