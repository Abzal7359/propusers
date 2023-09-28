import random
import string
import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.UserRolesPage import UserRolesPage


@when(u'click on user roles under user management')
def step_impl(context):
    context.URP = UserRolesPage(context.driver)
    context.URP.click_user_roles_link()
    # context.driver.find_element(By.XPATH, "//a[normalize-space()='User Roles']").click()
    # time.sleep(2)


@when(u'click create user role button')
def step_impl(context):
    context.URP = UserRolesPage(context.driver)
    context.URP.click_create_user_role_button()
    # context.driver.find_element(By.XPATH, "//a[normalize-space()='Create User Role']").click()
    # time.sleep(2)


@when(u'fill user role realted details')
def step_impl(context):
    context.URP.fill_user_role_details("Engineering", "Project Admin")

    # user_role = "Engineering"
    # context.driver.find_element(By.ID, "first-name").clear()
    # context.driver.find_element(By.ID, "first-name").send_keys(user_role)
    # context.driver.find_element(By.ID, "reportedmanager").click()
    #
    # context.driver.find_element(By.XPATH, "//option[2]").click()
    # context.driver.find_element(By.XPATH, "//label[normalize-space()='Reports To']").click()


@when(u'select Access rights')
def step_impl(context):
    context.URP.select_access_rights()
    # # dropdown of crm
    # context.driver.find_element(By.XPATH, "//span[normalize-space()='CRM']").click()
    # for i in range(1, 7):
    #     context.driver.find_element(By.XPATH, f"(//form/div/div[4]/div[3]/div/div/button)[{i}]").click()
    #
    # context.driver.find_element(By.XPATH, "//span[normalize-space()='Admin']").click()
    # context.driver.find_element(By.XPATH, "(//form/div/div[4]/div[4]/div/div/button)[5]").click()


@when(u'click save button')
def step_impl(context):
    context.URP.click_save_button()
    # context.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    # time.sleep(3)


@then(u'validate the user role created or not')
def step_impl(context):
    assert context.URP.is_user_role_created()

    # global index
    # index = 0
    # listt = context.driver.find_elements(By.XPATH, "//table/tbody/tr/td[1]")
    #
    # for i in range(len(listt)):
    #     if context.driver.find_element(By.XPATH, f"//table/tbody/tr[{i + 1}]/td[1]").text == user_role:
    #         index = i + 1
    #         assert True


@when(u'click on clone link')
def step_impl(context):
    context.URP = UserRolesPage(context.driver)
    context.URP.click_clone_link()
    # ele = context.driver.find_element(By.XPATH, f"//table/tbody/tr[{index}]/td[1]")
    # context.driver.execute_script("arguments[0].scrollIntoView();", ele)
    # time.sleep(2)
    # context.driver.find_element(By.XPATH,
    #                             f"//table/tbody/tr[{index}]/td[5]/div/div/button//*[local-name()='svg' ]").click()
    # context.driver.find_element(By.XPATH, "(//a[normalize-space()='Clone'])[1]").click()
    # time.sleep(5)


@then(u'valiadte the clone is added or not')
def step_impl(context):
    assert context.URP.is_clone_added()
    # if context.driver.find_element(By.XPATH, f"//table/tbody/tr[{index + 1}]/td[1]").text == "Clone 1 of " + user_role:
    #     assert True
    # else:
    #     assert False


@when(u'click on delete button of user role')
def step_impl(context):
    context.URP = UserRolesPage(context.driver)
    context.URP.click_delete_button()
    # ele = context.driver.find_element(By.XPATH, f"//table/tbody/tr[{index + 1}]/td[1]")
    # context.driver.execute_script("arguments[0].scrollIntoView();", ele)
    # time.sleep(2)
    # context.driver.find_element(By.XPATH,
    #                             f"//table/tbody/tr[{index + 1}]/td[5]/div/div/button//*[local-name()='svg' ]").click()
    # context.driver.find_element(By.XPATH, "(//a[normalize-space()='Delete'])[1]").click()
    # context.driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
    # time.sleep(3)


@then(u'valaidate the user role deleted or not')
def step_impl(context):
    assert context.URP.is_user_role_deleted()
    # global after_delete
    # after_delete = context.driver.find_elements(By.XPATH, "//table/tbody/tr/td[1]")
    # flag = True
    # for j in after_delete:
    #     if j.text == "Clone 1 of " + user_role:
    #         flag = False
    #
    # assert flag


@when(u'click on edit button')
def step_impl(context):
    context.URP = UserRolesPage(context.driver)
    context.URP.click_edit_button()
    # ele = context.driver.find_element(By.XPATH, f"//table/tbody/tr[{index}]/td[1]")
    # context.driver.execute_script("arguments[0].scrollIntoView();", ele)
    # time.sleep(2)
    # context.driver.find_element(By.XPATH,
    #                             f"//table/tbody/tr[{index}]/td[5]/div/div/button//*[local-name()='svg' ]").click()
    # context.driver.find_element(By.XPATH, "(//a[normalize-space()='Edit'])[1]").click()


@when(u'fill user editing details')
def step_impl(context):
    context.URP.fill_user_editing_details()
    # global user_role_edit
    # user_role_edit = "Engineering Civil"
    # time.sleep(1)
    # context.driver.find_element(By.ID, "first-name").clear()
    # time.sleep(1)
    # context.driver.find_element(By.ID, "first-name").send_keys(user_role_edit)
    #
    # drop = Select(context.driver.find_element(By.ID, "reportedmanager"))
    # drop.select_by_visible_text("CRM Admin")
    # context.driver.find_element(By.XPATH, "//label[normalize-space()='Reports To']").click()


@when(u'select different acces rights')
def step_impl(context):
    context.URP.select_different_access_rights()
    # context.driver.find_element(By.XPATH, "(//form/div/div[4]/div/button/span[2])[2]").click()


@when(u'validate user role edited or not')
def step_impl(context):
    assert context.URP.is_user_role_edited()
    # global ind
    # for i in range(len(after_delete)):
    #     if context.driver.find_element(By.XPATH, f"//table/tbody/tr[{i + 1}]/td[1]").text == user_role_edit:
    #         ind = i + 1
    #         assert True


@then(u'valaidte user role edited or not by checking access rights')
def step_impl(context):
    context.URP = UserRolesPage(context.driver)
    assert context.URP.is_user_role_edited_in_accessRights()
    # ele = context.driver.find_element(By.XPATH, f"//table/tbody/tr[{ind}]/td[1]")
    # context.driver.execute_script("arguments[0].scrollIntoView();", ele)
    # time.sleep(2)
    #
    # context.driver.find_element(By.XPATH,
    #                             f"//table/tbody/tr[{ind}]/td[5]/div/div/button//*[local-name()='svg' ]").click()
    # context.driver.find_element(By.XPATH, "(//a[normalize-space()='Edit'])[1]").click()
    # time.sleep(2)
    # color = context.driver.find_element(By.XPATH, "(//form/div/div[4]/div/button/span[2])[2]").get_attribute(
    #     "ng-reflect-ng-class")
    # if color == "bg-green-400":
    #
    #     context.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
    #     assert True
    # else:
    #
    #     context.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
    #     assert False


@then(u'validate error of user role already exists')
def step_impl(context):
    context.URP = UserRolesPage(context.driver)
    assert context.URP.is_duplicate_error_displayed()

    # error = context.driver.find_element(By.XPATH, "//app-toasts-container/div/div/div/div/div/div[2]/p[2]").text
    # if error == "User role already exist.":
    #     context.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
    #     assert True
    # else:
    #     context.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
    #     assert False


@then(u'click on delete button of user role which has users assigned and validate error')
def step_impl(context):
    context.URP = UserRolesPage(context.driver)
    assert context.URP.click_delete_button_users_assigned()

    # # deleting user role which has users assigned
    # c = context.driver.find_elements(By.XPATH, "//tbody/tr/td[4]/div/div")
    # for i in range(1, len(c)):
    #     if context.driver.find_element(By.XPATH, f"(//tbody/tr[{i + 1}]/td[4]/div/div)[{i}]").is_displayed():
    #         context.driver.find_element(By.XPATH,
    #                                     f"//table/tbody/tr[{i + 1}]/td[5]/div/div/button//*[local-name()='svg' ]").click()
    #         time.sleep(3)
    #         context.driver.find_element(By.XPATH, "(//a[normalize-space()='Delete'])[1]").click()
    #         if context.driver.find_element(By.XPATH, "(//p[@class='text-sm text-gray-500'])[1]").is_displayed():
    #
    #             context.driver.find_element(By.XPATH, "//button[normalize-space()='Ok']").click()
    #             assert True
    #             break
    #         else:
    #             context.driver.find_element(By.XPATH, "//button[normalize-space()='Ok']").click()
    #             assert False


@then(u'apply filters and validate the filters applied and giving good result or not')
def step_impl(context):
    context.URP = UserRolesPage(context.driver)
    assert context.URP.is_applied_filters_visible()
    # l = []
    # for i in range(1, 4):
    #     context.driver.find_element(By.XPATH, "//span[text()='Reports To']").click()
    #     usrole_text = context.driver.find_element(By.XPATH,
    #                                               f"(//app-select-dropdown/div/div/div/div/label)[{i + 1}]").text
    #     context.driver.find_element(By.XPATH, f"(//app-select-dropdown/div/div/div/div/label)[{i + 1}]").click()
    #
    #     time.sleep(2)
    #
    #     if len(context.driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]")) == 0:
    #         print("no users present test is also pass")
    #         context.driver.find_element(By.XPATH, f"(//app-select-dropdown/div/div/div/div/label)[{i + 1}]").click()
    #         time.sleep(1)
    #
    #     elif (len(context.driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]")) >= 1):
    #         roles = context.driver.find_elements(By.XPATH, "//table/tbody/tr/td[2]")
    #         check = True
    #         for j in roles:
    #             if j.text == usrole_text:
    #                 pass
    #             else:
    #                 check = False
    #                 break
    #
    #         l.append(check)
    #         context.driver.find_element(By.XPATH, "//span[text()='Reports To']").click()
    #
    #         context.driver.find_element(By.XPATH, f"(//app-select-dropdown/div/div/div/div/label)[{i + 1}]").click()
    #
    #         time.sleep(1)
    # if False not in l:
    #     assert True
    # else:
    #     assert False


@when(u'click on select all in filters')
def step_impl(context):
    context.URP = UserRolesPage(context.driver)
    context.URP.click_select_all_filter()


@when(u'click on reset button')
def step_impl(context):
    context.URP.click_reset_button()
    # click rest
    # context.driver.find_element(By.XPATH, "//span[text()='Reset']").click()
    # context.driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
    #


@Then(u'validate the data is reseted or not')
def step_impl(context):
    assert context.URP.is_data_reset()
    # c = context.driver.find_element(By.ID, "first-name").text
    # if c != user_role:
    #     context.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
    #     assert True
    # else:
    #     context.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
    #     assert False
    # time.sleep(3)


@when(u'select Access rights without basic selection')
def step_impl(context):
    context.URP = UserRolesPage(context.driver)
    context.URP.accesRights_without_basic_selection()
    # # dropdown of crm
    #
    # context.driver.find_element(By.XPATH, "//span[normalize-space()='CRM']").click()
    # context.driver.find_element(By.XPATH, "(//form/div/div[4]/div[3]/div/div/button)[2]").click()


@then(u'validate error displayed or not')
def step_impl(context):
    assert context.URP.Is_error_got()
    # alert = context.driver.find_element(By.XPATH, "//app-notification-alert/div/div[2]/div/div/div[1]/div[2]/div/p")
    # if alert.is_displayed():
    #
    #     context.driver.find_element(By.XPATH, "//button[normalize-space()='Ok']").click()
    #     context.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
    #     assert True
    # else:
    #
    #     context.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
    #     assert False





@when(u'click on Add user option on any user role')
def step_impl(context):
    context.URP = UserRolesPage(context.driver)
    context.URP.click_on_AddUser()
    # context.driver.find_element(By.XPATH, "//tbody/tr[4]/td[5]/div/div/button/*[local-name()='svg' ]").click()
    # context.driver.find_element(By.XPATH, "(//a[normalize-space()='Add Users'])[1]").click()
    # time.sleep(3)


@when(u'fill email and select reporting manager')
def step_impl(context):
    context.URP.fill_add_user_details()
    # context.driver.find_element(By.XPATH, "//input[@id='email']").send_keys(random_email)
    # drop = Select(context.driver.find_element(By.ID, "reportedmanager"))
    # drop.select_by_visible_text("Venkatesh Iyer")
    # context.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    # context.driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
    # time.sleep(1)


@Then(u'validate in users section under USER MANAGEMENT')
def step_impl(context):
    assert context.URP.is_user_invited()
    # context.driver.find_element(By.XPATH, "//a[normalize-space()='Users']").click()
    # time.sleep(2)
    # valing_mail = context.driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[1]/span").text
    # status = context.driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]").text
    # if valing_mail == random_email and status == "Invited":
    #     assert True
    # else:
    #     assert False


@Then(u'validate duplicate error showing or not')
def step_impl(context):
    context.URP = UserRolesPage(context.driver)
    assert context.URP.is_duplicate_error_got()
    # error = context.driver.find_element(By.XPATH, "//app-toasts-container/div/div/div/div/div/div[2]/p[2]").text
    # if random_email in error:
    #     assert True
    # else:
    #     assert False
