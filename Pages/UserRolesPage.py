import random
import string
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def generate_random_email():
    domain = "@example.com"
    username_length = random.randint(5, 10)
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(username_length))
    return username + domain


class UserRolesPage:
    def __init__(self, driver):
        self.driver = driver

    # XPaths

    USER_ROLES_LINK = "//a[normalize-space()='User Roles']"
    CREATE_USER_ROLE_BUTTON = "//a[normalize-space()='Create User Role']"
    SAVE_BUTTON = "//button[normalize-space()='Save']"
    CLONE_BUTTON = "(//a[normalize-space()='Clone'])[1]"

    DELETE_BUTTON = "(//a[normalize-space()='Delete'])[1]"
    CONFIRM_DELETE_BUTTON = "//button[normalize-space()='Yes']"
    EDIT_BUTTON = "(//a[normalize-space()='Edit'])[1]"
    ACCESS_RIGHTS_BUTTON = "(//form/div/div[4]/div/button/span[2])[2]"
    USER_ROLE_TABLE = "//table/tbody/tr"
    ERROR_MESSAGE = "//app-toasts-container/div/div/div/div/div/div[2]/p[2]"
    CANCEL_BUTTON = "//button[normalize-space()='Cancel']"
    SELECT_ALL_FILTER = "(//app-select-dropdown/div/div/div/div/label)"
    REPORT_TO_FILTER = "//span[normalize-space()='REPORTEE']"
    RESET_BUTTON = "//span[text()='Reset']"
    ADD_USERS = "(//a[normalize-space()='Add Users'])[1]"
    random_email = generate_random_email()

    # Methods

    def is_duplicate_error_got(self):
        error = self.driver.find_element(By.XPATH, "//app-toasts-container/div/div/div/div/div/div[2]/p[2]").text
        return self.random_email in error


    def is_user_invited(self):
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Users']").click()
        time.sleep(2)
        valing_mail = self.driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[1]/span").text
        status = self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]").text
        return valing_mail == self.random_email and status == "Invited"


    def fill_add_user_details(self):
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys(self.random_email)
        drop = Select(self.driver.find_element(By.ID, "reportedmanager"))
        drop.select_by_visible_text("Venkatesh Iyer")
        self.driver.find_element(By.XPATH, self.SAVE_BUTTON).click()
        self.driver.find_element(By.XPATH, self.CONFIRM_DELETE_BUTTON).click()
        time.sleep(1)

    def click_on_AddUser(self):
        self.driver.find_element(By.XPATH, "//tbody/tr[4]/td[5]/div/div/button/*[local-name()='svg' ]").click()
        self.driver.find_element(By.XPATH, self.ADD_USERS).click()
        time.sleep(3)

    def Is_error_got(self):
        alert = self.driver.find_element(By.XPATH, "//app-notification-alert/div/div[2]/div/div/div[1]/div[2]/div/p")
        if alert.is_displayed():

            self.driver.find_element(By.XPATH, "//button[normalize-space()='Ok']").click()
            self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
            return True
        else:

            self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
            return False

    def accesRights_without_basic_selection(self):
        self.driver.find_element(By.XPATH, "//span[normalize-space()='CRM']").click()
        self.driver.find_element(By.XPATH, "(//form/div/div[4]/div[3]/div/div/button)[2]").click()

    def is_data_reset(self):
        c = self.driver.find_element(By.ID, "first-name").text
        self.driver.find_element(By.XPATH, self.CANCEL_BUTTON).click()
        time.sleep(3)
        return c != user_role

    def click_reset_button(self):
        self.driver.find_element(By.XPATH, self.RESET_BUTTON).click()
        self.driver.find_element(By.XPATH, self.CONFIRM_DELETE_BUTTON).click()

    def click_select_all_filter(self):
        self.driver.find_element(By.XPATH, self.SELECT_ALL_FILTER).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.REPORT_TO_FILTER).click()

    def is_applied_filters_visible(self):
        l = []
        for i in range(1, 4):
            self.driver.find_element(By.XPATH, "//span[text()='Reports To']").click()
            usrole_text = self.driver.find_element(By.XPATH,
                                                   f"(//app-select-dropdown/div/div/div/div/label)[{i + 1}]").text
            self.driver.find_element(By.XPATH, f"(//app-select-dropdown/div/div/div/div/label)[{i + 1}]").click()

            time.sleep(2)

            if len(self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]")) == 0:
                print("no users present test is also pass")
                self.driver.find_element(By.XPATH, f"(//app-select-dropdown/div/div/div/div/label)[{i + 1}]").click()
                time.sleep(1)

            elif (len(self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]")) >= 1):
                roles = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]")
                check = True
                for j in roles:
                    if j.text == usrole_text:
                        pass
                    else:
                        check = False
                        break

                l.append(check)
                self.driver.find_element(By.XPATH, "//span[text()='Reports To']").click()

                self.driver.find_element(By.XPATH, f"(//app-select-dropdown/div/div/div/div/label)[{i + 1}]").click()

                time.sleep(1)
        return False not in l

    def click_delete_button_users_assigned(self):
        # deleting user role which has users assigned
        c = self.driver.find_elements(By.XPATH, "//tbody/tr/td[4]/div/div")
        for i in range(1, len(c)):
            if self.driver.find_element(By.XPATH, f"(//tbody/tr[{i + 1}]/td[4]/div/div)[{i}]").is_displayed():
                self.driver.find_element(By.XPATH,
                                         f"//table/tbody/tr[{i + 1}]/td[5]/div/div/button//*[local-name()='svg' ]").click()
                time.sleep(3)
                self.driver.find_element(By.XPATH, "(//a[normalize-space()='Delete'])[1]").click()
                cc = self.driver.find_element(By.XPATH, "(//p[@class='text-sm text-gray-500'])[1]").is_displayed()

                self.driver.find_element(By.XPATH, "//button[normalize-space()='Ok']").click()
                return cc

    def is_duplicate_error_displayed(self):
        error = self.driver.find_element(By.XPATH, self.ERROR_MESSAGE).text
        self.driver.find_element(By.XPATH, self.CANCEL_BUTTON).click()
        return error == "User role already exist."

    def is_user_role_edited_in_accessRights(self):
        self.scroll_into_view(ind)

        self.driver.find_element(By.XPATH,
                                 f"//table/tbody/tr[{ind}]/td[5]/div/div/button//*[local-name()='svg' ]").click()
        self.driver.find_element(By.XPATH, self.EDIT_BUTTON).click()
        time.sleep(2)
        color = self.driver.find_element(By.XPATH, self.ACCESS_RIGHTS_BUTTON).get_attribute("ng-reflect-ng-class")
        self.driver.find_element(By.XPATH, self.CANCEL_BUTTON).click()
        return color == "bg-green-400"

    def is_user_role_edited(self):
        global ind
        for i in range(len(after_delete)):
            if self.driver.find_element(By.XPATH, f"{self.USER_ROLE_TABLE}[{i + 1}]/td[1]").text == user_role_edit:
                ind = i + 1
                return True

        return False

    def select_different_access_rights(self):
        self.driver.find_element(By.XPATH, self.ACCESS_RIGHTS_BUTTON).click()

    def fill_user_editing_details(self):
        global user_role_edit
        user_role_edit = "Engineering Civil"
        time.sleep(1)
        self.driver.find_element(By.ID, "first-name").clear()
        time.sleep(1)
        self.driver.find_element(By.ID, "first-name").send_keys(user_role_edit)

        drop = Select(self.driver.find_element(By.ID, "reportedmanager"))
        drop.select_by_visible_text("CRM Admin")
        self.driver.find_element(By.XPATH, "//label[normalize-space()='Reports To']").click()

    def scroll_into_view(self, indexx):
        ele = self.driver.find_element(By.XPATH, f"{self.USER_ROLE_TABLE}[{indexx}]/td[1]")
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        time.sleep(2)

    def click_edit_button(self):
        self.scroll_into_view(index)
        self.driver.find_element(By.XPATH,
                                 f"//table/tbody/tr[{index}]/td[5]/div/div/button//*[local-name()='svg' ]").click()
        self.driver.find_element(By.XPATH, self.EDIT_BUTTON).click()

    def is_user_role_deleted(self):
        global after_delete
        after_delete = self.driver.find_elements(By.XPATH, self.USER_ROLE_TABLE)
        for j in after_delete:
            if j.text == "Clone 1 of " + user_role:
                return False
        return True

    def click_delete_button(self):
        self.scroll_into_view(index + 1)
        self.driver.find_element(By.XPATH,
                                 f"//table/tbody/tr[{index + 1}]/td[5]/div/div/button//*[local-name()='svg' ]").click()
        self.driver.find_element(By.XPATH, self.DELETE_BUTTON).click()

        self.driver.find_element(By.XPATH, self.CONFIRM_DELETE_BUTTON).click()
        time.sleep(3)

    def is_clone_added(self):
        clone_name = "Clone 1 of " + user_role
        clone_element_xpath = f"//table/tbody/tr[{index + 1}]/td[1]"
        return self.driver.find_element(By.XPATH, clone_element_xpath).text == clone_name

    def click_clone_link(self):
        self.scroll_into_view(index)
        # ele = self.driver.find_element(By.XPATH, f"{self.USER_ROLE_TABLE}[{index}]/td[1]")
        # self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        # time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 f"//table/tbody/tr[{index}]/td[5]/div/div/button//*[local-name()='svg' ]").click()
        self.driver.find_element(By.XPATH, self.CLONE_BUTTON).click()
        time.sleep(5)

    def click_user_roles_link(self):
        self.driver.find_element(By.XPATH, self.USER_ROLES_LINK).click()
        time.sleep(2)

    def click_create_user_role_button(self):
        self.driver.find_element(By.XPATH, self.CREATE_USER_ROLE_BUTTON).click()
        time.sleep(2)

    def fill_user_role_details(self, user_role_name, manager_option):
        global user_role
        user_role = user_role_name
        first_name_input = self.driver.find_element(By.ID, "first-name")
        first_name_input.clear()
        first_name_input.send_keys(user_role)

        manager_dropdown = Select(self.driver.find_element(By.ID, "reportedmanager"))
        manager_dropdown.select_by_visible_text(manager_option)

    def select_access_rights(self):
        # dropdown of crm
        self.driver.find_element(By.XPATH, "//span[normalize-space()='CRM']").click()
        for i in range(1, 7):
            self.driver.find_element(By.XPATH, f"(//form/div/div[4]/div[3]/div/div/button)[{i}]").click()

        self.driver.find_element(By.XPATH, "//span[normalize-space()='Admin']").click()
        self.driver.find_element(By.XPATH, "(//form/div/div[4]/div[4]/div/div/button)[5]").click()

    def click_save_button(self):
        self.driver.find_element(By.XPATH, self.SAVE_BUTTON).click()
        time.sleep(3)

    def is_user_role_created(self):
        global index
        index = 0
        list_elements = self.driver.find_elements(By.XPATH, "//table/tbody/tr/td[1]")
        for i in range(len(list_elements)):
            if self.driver.find_element(By.XPATH, f"//table/tbody/tr[{i + 1}]/td[1]").text == user_role:
                index = i + 1
                return True
        return False
