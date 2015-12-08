#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from selenium.webdriver.common import by
from selenium.webdriver.common import keys
import sys
import basewebobject
import time
from selenium.webdriver.common import by
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

class SourcePage:
    def __init__(self, driver):
        """Constructor."""
        self.driver = driver

    def create_new_package_source(self, git_url, branch, series):
        '''This is the helper method to create
        a package. This consists of following steps:
        1. Click on new button.
        2. Enter values like git_url, branch and series.
        3. Click submit.
        INPUT: git_url, branch and series (All string type)'''
        self.new_submit_button.click()
        self.git_url.send_keys(git_url)
        self.branch.send_keys(branch)
        self.select_from_dropdown_menu(series)
        self.new_submit_button.submit()

    def select_from_dropdown_menu(self, series):
        '''This is the helper method to select a given
        series from drop-down box
        INPUT: series (string type)'''
        mySelect = Select(self.driver.find_element_by_id("id_series"))
        mySelect.select_by_visible_text(series)

    def verify_package_source(self, git_url):
        '''This is the helper method to verify whether
        a package exist or not on basis on url.
        INPUT: git_url (string type)
        RETURN: TRUE if package found and FALSE on otherwise case'''
        self.sources_button.click()
        # It will report an exception if element not found
        try:
            self.driver.find_element(by.By.LINK_TEXT, git_url)
        except:
            return False
        else:
            return True
            
    def delete_package_source(self):
        '''This is the helper method to delete a package.
        This consists of followwinng steps:
        1. Click on source button.
        2. Click on edit button for package.
        3. click on delete button.'''
        self.sources_button.click()
        self.package_edit_button.click()
        self.delete_button.click()
        
    @property
    def package_edit_button(self):
        '''Finds package edit button.
        NOTE: Only one package is expected at once'''
        return self.driver.find_element(by.By.CSS_SELECTOR, '.glyphicon.glyphicon-pencil')
        
    @property
    def delete_button(self):
        '''Finds package delete button'''
        return self.driver.find_element(by.By.CSS_SELECTOR, '.btn.btn-danger')

    @property
    def sources_button(self):
        '''Finds package source button'''
        return self.driver.find_element(by.By.LINK_TEXT, 'Sources')

    @property
    def new_submit_button(self):
        '''Finds NEW and Submit button. Both buttons have same class name
        and live in diffrent views thus giving us opportunity of code reuse'''
        return self.driver.find_element(by.By.CSS_SELECTOR, '.btn.btn-primary')

    @property
    def git_url(self):
        '''Finds box for entering git url'''
        return self.driver.find_element(by.By.ID, 'id_git_url')

    @property
    def branch(self):
        '''Finds box for entering branch name'''
        return self.driver.find_element(by.By.ID, 'id_branch')
        
    
class ProfilePage:
    def __init__(self, driver):
        """Constructor."""
        self.driver = driver
        
    @property
    def profile_button(self):
        '''Finds package profile button'''
        return self.driver.find_element(by.By.LINK_TEXT, 'Profile')
    
    def verify_profile_page(self, username):
        try:
            self.driver.find_element(by.By.XPATH, "//dl[@class='dl-horizontal']/dd[contains(text(), %s)]" % username)
        except:
            return False
        else:
            return True
