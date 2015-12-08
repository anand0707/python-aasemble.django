#from openstack_dashboard.test.integration_tests import basewebobject


#class PageObject(basewebobject.BaseWebObject):
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.webdriver.firefox.webdriver import WebDriver

from aasemble.django.tests import create_session_for_given_user

class PageObject(StaticLiveServerTestCase):
    """Base class for page objects."""

    @classmethod
    def setUpClass(self):
        super(PageObject, self).setUpClass()
        self.selenium = WebDriver()
        self.selenium.maximize_window()

    @classmethod
    def tearDownClass(self):
        cls.selenium.quit()
        super(PageObject, cls).tearDownClass()
        
        
    @classmethod
    def create_login_session(self, username):
        session_cookie = create_session_for_given_user(username)
        self.selenium.get(self.live_server_url)
        self.selenium.add_cookie(session_cookie)
