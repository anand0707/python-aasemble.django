import os
import re

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test.utils import override_settings, skipIf

from aasemble.django.apps.buildsvc.tasks import poll_one

from aasemble.django.tests import create_session_cookie

from aasemble.django.apps.buildsvc.page.baseWebObject import PageObject

import selenium.common.exceptions as Exceptions

import aasemble.django.apps.buildsvc.page.pages.SourcePage as SourcePage

from selenium.webdriver.common import by
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select


@skipIf(os.environ.get('SKIP_SELENIUM_TESTS', '') == '1',
        'Skipping Selenium based test, because SKIP_SELENIUM_TESTS=1')
class RepositoryFunctionalTests(PageObject):
    fixtures = ['complete.json']

    # def test_user_signs_up_for_signup(self):
        # self.driver.get('%s%s' % (self.live_server_url, '/accounts/signup/'))
        # username_input = self.driver.find_element_by_id('id_email')
        # username_input.send_keys('newuser@linux2go.dk')
        # password1_input = self.driver.find_element_by_id('id_password1')
        # password1_input.send_keys('secret')
        # password2_input = self.driver.find_element_by_id('id_password2')
        # password2_input.send_keys('secret')
        # signup_form = self.driver.find_element_by_id('signup_form')
        # signup_form.submit()
        # page_header = self.driver.find_element_by_class_name('page-header')
        # text_found = re.search(r'Dashboard', page_header.text)
        # self.assertNotEqual(text_found, None)

    # def test_secured_pages_open_after_login(self):
        # session_cookie = create_session_cookie(username='test@email.com', password='top_secret')
        # self.driver.get(self.live_server_url)
        # self.driver.add_cookie(session_cookie)

        # # test whether sources page opens after user logs in
        # self.driver.get('%s%s' % (self.live_server_url, '/buildsvc/sources/'))
        # page_header = self.driver.find_element_by_class_name('page-header')
        # text_found = re.search(r'Sources', page_header.text)
        # self.assertNotEqual(text_found, None)

    def test_source_package(self):
        '''This test performs a basic package addition and deletion.
           This test consists of following steps:
           1. Create a session cookie for given user. We are using a existing
               user 'Dennis' which is already added as fixture.
           2. Try to create a package.
           3. Verify if the package has been created.
           4. Try to delete the package
           5. Verify if the package has been deleted'''
        sourcePage = SourcePage(self.driver)
        sourcePage.create_login_session('brandon')
        # test whether sources page opens after user logs in
        sourcePage.driver.get(self.live_server_url)
        sourcePage.sources_button.click()
        git_url = "https://github.com/aaSemble/python-aasemble.django.git"
        sourcePage.create_new_package_source(git_url=git_url, branch='master', series='brandon/aasemble')
        sourcePage.assertEqual(self.verify_package_source(git_url=git_url), True, 'Package not created')
        sourcePage.delete_package_source()
        sourcePage.assertEqual(self.verify_package_source(git_url=git_url), False, 'Package not deleted')

    # def test_profile_button(self):
        # '''This test verifies the "Profile" button.
        # 1. Create a session cookie for given user. We are using a existing
               # user 'brandon' which is already added as fixture.
        # 2. Press 'Profile' button.
        # 3. Verify page by username'''
        # self.create_login_session('brandon')
        # # test whether sources page opens after user logs in
        # self.driver.get('%s%s' % (self.live_server_url, '/buildsvc/sources/'))
        # self.driver.set_window_size(1024, 768)
        # self.profile_button.click()
        # self.assertEqual(self.verify_profile_page('brandon'), True, "Profile Name not verified")

    # def test_new_mirrors(self):
        # ''' This tests validates if non public mirror is created'''
        # new_mirror_button = (by.By.LINK_TEXT, 'New')
        # self.create_login_session('brandon')
        # self.driver.get('%s%s' % (self.live_server_url, '/mirrorsvc/mirrors/'))
        # self.driver.set_window_size(1024, 768)
        # self.assertTrue(self._is_element_visible(new_mirror_button), "Mirror New Button is not Visible")
        # self.driver.find_element(*new_mirror_button).click()
        # self.driver.find_element(by.By.ID, 'id_url').send_keys('%s%s' % (self.live_server_url, '/apt/brandon/brandon'))
        # self.driver.find_element(by.By.ID, 'id_series').send_keys('brandon/aasemble')
        # self.driver.find_element(by.By.ID, 'id_components').send_keys('aasemble')
        # self.driver.find_element(by.By.XPATH, './/button[@type="submit" and contains(.,"Submit")]').click()
        # self.assertTrue(self._is_element_visible((by.By.LINK_TEXT, '%s%s' % (self.live_server_url, '/apt/brandon/brandon'))))
        # # Test if public flag is false
        # self.assertTrue(self._is_element_visible((by.By.XPATH, ".//table/tbody/tr[1]/td[5][contains(text(), False)]")))

    # def test_mirror_another_user(self):
        # self.test_new_mirrors()
        # self.create_login_session('aaron')
        # self.driver.get(self.live_server_url)
        # self.driver.set_window_size(1024, 768)
        # self.mirror_button.click()
        # self.assertFalse(self._is_element_visible((by.By.LINK_TEXT, '%s%s' % (self.live_server_url, '/apt/brandon/brandon'))))

    # @override_settings(CELERY_ALWAYS_EAGER=True)
    # # This tests needs celery so overriding the settings
    # def test_build_packages(self):
        # '''This test perform a package addtion and check whether a build
        # started for the same.
        # 1. Create a session cookie for given user. We are using a existing
               # user 'brandon' which is already added as fixture.
        # 2. Try to create a package.
        # 3. Poll the task for package creation. Polling should start the build
        # 4. Verify that Building started and it is visible via GUI'''
        # self.create_login_session('brandon')
        # # test whether sources page opens after user logs in
        # self.driver.get('%s%s' % (self.live_server_url, '/buildsvc/sources/'))
        # self.driver.set_window_size(1024, 768)
        # self.sources_button.click()
        # git_url = "https://github.com/aaSemble/python-aasemble.django.git"
        # self.create_new_package_source(git_url=git_url, branch='master', series='brandon/aasemble')
        # from .models import PackageSource
        # # Only one package is added with this url
        # P = PackageSource.objects.filter(git_url=git_url)[0]
        # try:
            # poll_one(P.id)
        # except:
            # # Marking Pass even if we got some exception during package build.
            # # Our verification is limited to UI inteface. Form UI, It should
            # # be visible (even if it has just started)
            # pass
        # finally:
            # self.driver.get('%s%s' % (self.live_server_url, '/buildsvc/sources/'))
            # self.build_button.click()
            # self.assertEqual(self.verify_build_displayed(packageName='python-aasemble.django.git'), True, 'Build not started')

    # def test_overview_button(self):
        # '''This test performs the test for overview button
        # 1. Create a session cookie for given user. We are using a existing
               # user 'brandon' which is already added as fixture.
        # 2. Press 'Overview' button.
        # 3. Verify whether 'Dashboard' came.'''
        # self.create_login_session('brandon')
        # # test whether sources page opens after user logs in
        # self.driver.get('%s%s' % (self.live_server_url, '/buildsvc/sources/'))
        # self.driver.set_window_size(1024, 768)
        # self.overview_button.click()
        # pageHeader = self.get_page_header_value()
        # self.assertEqual(pageHeader.text, "Dashboard", "Dashboard didn't showed up")

    
    # def test_logout_button(self):
        # '''This test perform a logout from given seesion
        # 1. Create a session cookie for given user. We are using a existing
               # user 'brandon' which is already added as fixture.
        # 2. Press logout.
        # 3. Verify that we came to login page.'''
        # self.create_login_session('brandon')
        # # test whether sources page opens after user logs in
        # self.driver.get('%s%s' % (self.live_server_url, '/buildsvc/sources/'))
        # self.driver.set_window_size(1024, 768)
        # self.logout_button.click()
        # self.assertEqual(self.verify_login_page(), True, "Logout didn't work")

    