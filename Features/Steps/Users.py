import time

from behave import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Pages.UserRolesPage import UserRolesPage

check = ["Add Reportees", "Change Reporting Manager", "Disable User", "Change User Role"]


@when(u'click on users under user role management')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[text()='Users']").click()
    time.sleep(2)


@then(u'verify name,role,reports to,reportees,status are visibile or not')
def step_impl(context):
    s = "NAME ROLE REPORTS TO REPORTEES STATUS"
    name = context.driver.find_element(By.XPATH, "//table/thead/tr/th[1]").text
    role = context.driver.find_element(By.XPATH, "//table/thead/tr/th[2]").text
    rep_to = context.driver.find_element(By.XPATH, "//table/thead/tr/th[3]").text
    rpt = context.driver.find_element(By.XPATH, "//table/thead/tr/th[4]").text
    status = context.driver.find_element(By.XPATH, "//table/thead/tr/th[5]").text
    assert name in s and role in s and rep_to in s and rpt in s and status in s


@when(u'click on plus symbol and select last Active one')
def step_impl(context):
    context.driver.find_element(By.XPATH, "(//*[name()='svg'][@class='w-6 h-6'])[2]").click()
    context.driver.find_element(By.XPATH, "//label[normalize-space()='Last Active On']").click()
    time.sleep(1)


@then(u'verify Last Active on coloumn is displayed or not')
def step_impl(context):
    last = context.driver.find_element(By.XPATH, "//table/thead/tr/th[6]").text
    if last == "Last Active On":
        context.driver.find_element(By.XPATH, "//label[normalize-space()='Last Active On']").click()
        context.driver.find_element(By.XPATH, "//table/thead/tr/th[5]").click()
        assert True
    else:
        context.driver.find_element(By.XPATH, "//table/thead/tr/th[5]").click()
        assert False


@when(u'click on role and select some options')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button/span[text()='Role']").click()


@when(u'validate based on the role they are displayed or not')
def step_impl(context):
    ll = []

    for i in range(2, 7):

        name = context.driver.find_element(By.XPATH, f"(//app-select-dropdown/div/div/div/div/label)[{i}]").text
        context.driver.find_element(By.XPATH, f"(//app-select-dropdown/div/div/div/div/label)[{i}]").click()
        time.sleep(2)
        l = len(context.driver.find_elements(By.XPATH, "//tbody/tr/td[2]"))
        if l == 0:
            pass
        else:
            flag = True

            for j in range(1, (l + 1)):

                val = context.driver.find_element(By.XPATH, f"//tbody/tr[{j}]/td[2]").text
                if val == name:
                    pass
                else:
                    flag = False
                    ll.append(flag)
                    break
        context.driver.find_element(By.XPATH, f"(//app-select-dropdown/div/div/div/div/label)[{i}]").click()

    assert False not in ll


@when(u'choose any some  Reports to filter')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@class='text-gray-900']").click()


@when(u'Verify in the Reports To column if the chosen person has been selected or not')
def step_impl(context):
    ll = []

    for i in range(2, 7):

        name = context.driver.find_element(By.XPATH, f"(//app-select-dropdown/div/div/div/div/label)[{i}]").text.lower()
        time.sleep(1)
        context.driver.find_element(By.XPATH, f"(//app-select-dropdown/div/div/div/div/label)[{i}]").click()
        time.sleep(2)
        l = len(context.driver.find_elements(By.XPATH, "//tbody/tr/td[3]"))
        if l == 0:
            pass
        else:
            flag = True

            for j in range(1, (l + 1)):

                val = context.driver.find_element(By.XPATH, f"//tbody/tr[{j}]/td[3]").text.lower()
                if val == name:

                    pass
                else:

                    flag = False

                    ll.append(flag)
                    break
        context.driver.find_element(By.XPATH, f"(//app-select-dropdown/div/div/div/div/label)[{i}]").click()

    assert False not in ll


@when(u'selecting the status option, choose one of the status options below it')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//span[normalize-space()='Status']").click()


@then(u'validate in the status column if the applied filter is visible or not')
def step_impl(context):
    ll = []

    for i in range(2, 5):

        name = context.driver.find_element(By.XPATH, f"(//app-select-dropdown/div/div/div/div/label)[{i}]").text.lower()
        time.sleep(1)
        context.driver.find_element(By.XPATH, f"(//app-select-dropdown/div/div/div/div/label)[{i}]").click()
        time.sleep(2)
        l = len(context.driver.find_elements(By.XPATH, "//tbody/tr/td[5]"))
        if l == 0:
            pass
        else:
            flag = True

            for j in range(1, (l + 1)):

                val = context.driver.find_element(By.XPATH, f"//tbody/tr[{j}]/td[5]").text.lower()
                if val == name:

                    pass
                else:

                    flag = False

                    ll.append(flag)
                    break
        context.driver.find_element(By.XPATH, f"(//app-select-dropdown/div/div/div/div/label)[{i}]").click()

    assert False not in ll


@when(u'enter name in search box')
def step_impl(context):
    global search_name
    search_name = "Sandeep Reddy"
    context.driver.find_element(By.XPATH, "//input[@id='search']").send_keys(search_name)

    time.sleep(3)
    context.driver.find_element(By.XPATH, "//input[@id='search']").send_keys(Keys.SPACE)
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//input[@id='search']").send_keys(Keys.BACKSPACE)

    time.sleep(2)


@then(u'validate in user role list it showing that name only')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//tbody/tr/td[1]/span")))
    val = element.text.lower()
    assert val == search_name.lower()
    context.driver.find_element(By.XPATH, "//input[@id='search']").clear()
    time.sleep(2)


@when(u'click on user roles')
def step_impl(context):
    context.URP = UserRolesPage(context.driver)
    context.URP.click_user_roles_link()


listt = []


@when(u'collect all user roles names')
def step_impl(context):
    global k
    k = len(context.driver.find_elements(By.XPATH, "//tbody/tr/td[1]"))
    for i in range(1, k + 1):
        tex = context.driver.find_element(By.XPATH, f"//tbody/tr[{i}]/td[1]").text
        listt.append(tex)


@when(u'click on Invite User and click select Role')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Invite User']").click()
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//select[@id='role']").click()


@then(u'verify all the user roles present or not')
def step_impl(context):
    flag = True
    for j in range(2, k + 2):
        val_tex = context.driver.find_element(By.XPATH, f"//option[{j}]").text
        if val_tex in listt:
            pass
        else:
            flag = False
            break
    assert flag


@when(u'click on Add button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='+ Add']").click()
    time.sleep(1)


@then(u'validate extra input box for mail open and cross symbolls are displayed or not')
def step_impl(context):
    li = len(context.driver.find_elements(By.XPATH, "//*[@id='email']"))
    if li == 2:
        context.driver.find_element(By.XPATH, "//form/div[1]/div/div/div[3]/div/div/*[local-name()='svg']").click()
        context.driver.find_element(By.XPATH, "//button[contains(text(),'Close')]").click()
        assert True
    else:
        context.driver.find_element(By.XPATH, "//button[contains(text(),'Close')]").click()
        assert False


@when(u'click on overflow menu of INVITED status user')
def step_impl(context):
    # //table/tbody/tr[1]/td[6]/div/*
    l = len(context.driver.find_elements(By.XPATH, "//table/tbody/tr/td[5]"))

    for i in range(1, l + 1):
        if context.driver.find_element(By.XPATH, f"//table/tbody/tr[{i}]/td[5]").text == "Invited":
            context.driver.find_element(By.XPATH, f"//table/tbody/tr[{i}]/td[6]/div/*").click()

            time.sleep(1)
            break


@when(u'validate the menu items')
def step_impl(context):
    if context.driver.find_element(By.XPATH, "//div[@class='py-1']/p[@id='menu-item-2']").text == "Resend Invite":
        context.driver.refresh()
        time.sleep(5)
        assert True
    else:
        context.driver.refresh()
        time.sleep(5)
        assert False


@when(u'click on overflow menu of ENABLED status user')
def step_impl(context):
    global report_to
    global index
    global SRRb
    # SRRb = context.driver.find_element(By.XPATH, f"//tbody/tr[{ro}]/td[3]").text

    l = len(context.driver.find_elements(By.XPATH, "//table/tbody/tr/td[5]"))

    for i in range(3, l + 1):
        val = context.driver.find_element(By.XPATH, f"//tbody/tr[{i}]/td[2]").text
        if context.driver.find_element(By.XPATH, f"//table/tbody/tr[{i}]/td[5]").text == "Enabled" and val != "Project Admin":
            index = i
            SRRb = context.driver.find_element(By.XPATH, f"//tbody/tr[{i}]/td[3]").text
            report_to = context.driver.find_element(By.XPATH, f"//table/tbody/tr[{i}]/td[3]").text
            z = context.driver.find_element(By.XPATH, f"//table/tbody/tr[{i - 2}]/td[6]/div/*")
            context.driver.execute_script("arguments[0].scrollIntoView();", z)
            time.sleep(1)

            context.driver.find_element(By.XPATH, f"//table/tbody/tr[{i}]/td[6]/div/*").click()
            time.sleep(1)
            break


@when(u'validate the overflow menu items')
def step_impl(context):
    c = context.driver.find_elements(By.XPATH, "//tr/td[6]/div/div/div/div/p")
    flag = True
    for i in range(1, len(c) + 1):
        te = context.driver.find_element(By.XPATH, f"(//tr/td[6]/div/div/div/div/p)[{i}]").text
        if te in check:
            pass
        else:
            flag = False
            break
    context.driver.refresh()
    time.sleep(5)
    assert flag


@when(u'click on overflow menu of DISABLED status user')
def step_impl(context):
    l = len(context.driver.find_elements(By.XPATH, "//table/tbody/tr/td[5]"))

    for i in range(1, l + 1):
        cc = context.driver.find_element(By.XPATH, f"//table/tbody/tr[{i}]/td[5]").text
        if cc == "Disabled":
            z = context.driver.find_element(By.XPATH, f"//table/tbody/tr[{i - 2}]/td[6]/div/*")
            context.driver.execute_script("arguments[0].scrollIntoView();", z)
            time.sleep(1)
            context.driver.find_element(By.XPATH, f"//table/tbody/tr[{i}]/td[6]/div/*").click()

            time.sleep(1)
            break


@then(u'validate the overflow menu items of diabled')
def step_impl(context):
    dis = context.driver.find_element(By.XPATH, "//tr/td[6]/div/div/div/div/p").text
    context.driver.refresh()
    time.sleep(5)
    assert dis == "Enable User"


@when(u'click on change reporting manager')
def step_impl(context):

    c = context.driver.find_elements(By.XPATH, "//tr/td[6]/div/div/div/div/p")
    for i in range(1, len(c) + 1):
        te = context.driver.find_element(By.XPATH, f"(//tr/td[6]/div/div/div/div/p)[{i}]")
        if te.text == check[1]:
            te.click()
            break


@then(u'validate default value is selected value or not')
def step_impl(context):
    time.sleep(2)
    namee = context.driver.find_element(By.XPATH, "//select").get_attribute("ng-reflect-model")

    drop = context.driver.find_element(By.XPATH, f"//option[text()=' {report_to}']").get_attribute("value")
    assert namee == drop


@when(u'select any reporting manager and click save')
def step_impl(context):
    global reporting_m
    # context.driver.find_element(By.XPATH, "//select").click()
    # reporting_m = context.driver.find_element(By.XPATH, "(//option)[4]").text
    # context.driver.find_element(By.XPATH, "(//option)[4]").click()
    context.driver.find_element(By.XPATH, "(//select)[1]").click()
    SRL = context.driver.find_elements(By.XPATH, "//option")
    srl = []
    for i in SRL:
        srl.append(i.text)
    for j in range(2, len(srl)):
        if SRRb != srl[j]:
            print(SRRb, srl[j])
            reporting_m= context.driver.find_element(By.XPATH, f"//option[{j + 1}]").text
            context.driver.find_element(By.XPATH, f"//option[{j + 1}]").click()
            break
        else:
            pass
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    time.sleep(3)


@Then(u'validate that change is reflected or not in reports to coloumn')
def step_impl(context):
    rp = context.driver.find_element(By.XPATH, f"//table/tbody/tr[{index}]/td[3]").text
    assert rp == reporting_m


@when(u'click on the options of user whos role is project Admin')
def step_impl(context):
    l = len(context.driver.find_elements(By.XPATH, "//tbody/tr/td[2]"))
    for j in range(1, (l + 1)):
        val = context.driver.find_element(By.XPATH, f"//tbody/tr[{j}]/td[2]").text
        status = context.driver.find_element(By.XPATH, f"//tbody/tr[{j}]/td[5]").text

        if val == "Project Admin" and status == "Enabled":
            if j > 3:
                z = context.driver.find_element(By.XPATH, f"//table/tbody/tr[{j - 2}]/td[6]/div/*")
                context.driver.execute_script("arguments[0].scrollIntoView();", z)
                time.sleep(1)
            else:
                context.driver.refresh()
                time.sleep(5)
            context.driver.find_element(By.XPATH, f"//table/tbody/tr[{j}]/td[6]/div/*").click()
            time.sleep(1)
            break


@then(u'validate you not get Disable option')
def step_impl(context):
    c = context.driver.find_element(By.XPATH, "//tr/td[6]/div/div/div/div/p").text
    assert c == check[0]


@when(u'click on add reporties on user role whose status is enabled')
def step_impl(context):
    l = len(context.driver.find_elements(By.XPATH, "//tbody/tr/td[2]"))
    for j in range(1, (l + 1)):
        val = context.driver.find_element(By.XPATH, f"//tbody/tr[{j}]/td[2]").text
        status = context.driver.find_element(By.XPATH, f"//tbody/tr[{j}]/td[5]").text

        if val != "Project Admin" and status == "Enabled":
            if j > 3:
                z = context.driver.find_element(By.XPATH, f"//table/tbody/tr[{j - 2}]/td[6]/div/*")
                context.driver.execute_script("arguments[0].scrollIntoView();", z)
                time.sleep(1)
            else:
                context.driver.refresh()
                time.sleep(5)
            context.driver.find_element(By.XPATH, f"//table/tbody/tr[{j}]/td[6]/div/*").click()
            time.sleep(1)
            break


@when(u'select Reportie and click save')
def step_impl(context):
    c = context.driver.find_element(By.XPATH, "(//tr/td[6]/div/div/div/div/p)[2]").text
    context.driver.find_element(By.XPATH, f"//tr/td[6]/div/div/div/div/p[text()='{c}']").click()
    context.driver.find_element(By.XPATH, "//select").click()

    context.driver.find_element(By.XPATH, "//select/option[2]").click()

    time.sleep(2)
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    time.sleep(1)


@then(u'validate with toaster message')
def step_impl(context):
    ch = "Reportee added successfully."
    vvv = context.driver.find_element(By.XPATH, "//app-toasts-container/div/div/div/div/div/div[2]/p[2]").text
    assert ch == vvv





@when(u'click on disable user option on user who doesnt have reportiees')
def step_impl(context):
    global row
    l = len(context.driver.find_elements(By.XPATH, "//tbody/tr/td[2]"))
    for j in range(1, (l + 1)):

        val = len(context.driver.find_elements(By.XPATH, f"//tbody/tr[{j}]/td[4]/div/div/div"))
        status = context.driver.find_element(By.XPATH, f"//tbody/tr[{j}]/td[5]").text

        if val == 0 and status == "Enabled":
            row = j
            if j > 3:
                z = context.driver.find_element(By.XPATH, f"//table/tbody/tr[{j - 2}]/td[6]/div/*")
                context.driver.execute_script("arguments[0].scrollIntoView();", z)
                time.sleep(1)
            context.driver.find_element(By.XPATH, f"//table/tbody/tr[{j}]/td[6]/div/*").click()
            time.sleep(1)
            break


@when(u'click save button to disbale')
def step_impl(context):
    c = context.driver.find_element(By.XPATH, "(//tr/td[6]/div/div/div/div/p)[3]").text
    context.driver.find_element(By.XPATH, f"//tr/td[6]/div/div/div/div/p[text()='{c}']").click()
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    time.sleep(2)


@then(u'validate status and red colour dot on profile')
def step_impl(context):
    st = context.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[5]").text

    red = context.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[1]/div[1]/span[2]").get_attribute(
        "ng-reflect-ng-class")
    assert st == "Disabled" and "red" in red


@when(u'click on enalbe user option on user whos status is disbaled')
def step_impl(context):
    context.driver.find_element(By.XPATH, f"//table/tbody/tr[{row}]/td[6]/div/*").click()
    context.driver.find_element(By.XPATH, "(//tr/td[6]/div/div/div/div/p)").click()
    time.sleep(2)


@when(u'select role and reporting manager and clik save')
def step_impl(context):
    global SR, RM
    context.driver.find_element(By.XPATH, "(//select)[1]").click()
    SR = context.driver.find_element(By.XPATH, "//option[3]").text
    context.driver.find_element(By.XPATH, "//option[3]").click()
    context.driver.find_element(By.XPATH, "//label[normalize-space()='Select Reporting Manager']").click()
    time.sleep(2)

    context.driver.find_element(By.XPATH, "(//select)[2]").click()
    time.sleep(2)
    RM = context.driver.find_element(By.XPATH, "(//select)[2]/option[2]").text
    context.driver.find_element(By.XPATH, "(//select)[2]/option[2]").click()

    context.driver.find_element(By.XPATH, "//label[normalize-space()='Select Role']").click()

    context.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    time.sleep(2)


@Then(u'validate status and manger')
def step_impl(context):
    RMM = context.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[3]").text
    SRR = context.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[2]").text
    s = context.driver.find_element(By.XPATH, f"//tbody/tr[{row}]/td[5]").text == "Enabled"
    print(RM == RMM and SR == SRR and s)


@when(u'click on change user role option of enabled person and not project admin')
def step_impl(context):
    global ro
    l = len(context.driver.find_elements(By.XPATH, "//tbody/tr/td[2]"))
    for j in range(1, (l + 1)):
        val = context.driver.find_element(By.XPATH, f"//tbody/tr[{j}]/td[2]").text
        status = context.driver.find_element(By.XPATH, f"//tbody/tr[{j}]/td[5]").text
        count = len(context.driver.find_elements(By.XPATH, f"//tbody/tr[{j}]/td[4]/div/div/div"))

        if val != "Project Admin" and status == "Enabled" and count == 0:
            ro = j
            if j > 3:
                z = context.driver.find_element(By.XPATH, f"//table/tbody/tr[{j - 2}]/td[6]/div/*")
                context.driver.execute_script("arguments[0].scrollIntoView();", z)
                time.sleep(1)
            context.driver.find_element(By.XPATH, f"//table/tbody/tr[{j}]/td[6]/div/*").click()
            time.sleep(1)
            break

    c = context.driver.find_element(By.XPATH, "(//tr/td[6]/div/div/div/div/p)[4]").text
    context.driver.find_element(By.XPATH, f"//tr/td[6]/div/div/div/div/p[text()='{c}']").click()

    time.sleep(2)


@When(u'select role and select Reporting manager')
def step_impl(context):
    global RM, SR
    SRRb = context.driver.find_element(By.XPATH, f"//tbody/tr[{ro}]/td[2]").text


    context.driver.find_element(By.XPATH, "(//select)[1]").click()
    SRL = context.driver.find_elements(By.XPATH, "//option")
    srl = []
    for i in SRL:
        srl.append(i.text)
    for j in range(2, len(srl)):
        if SRRb != srl[j]:
            print(SRRb, srl[j])
            SR = context.driver.find_element(By.XPATH, f"//option[{j + 1}]").text
            context.driver.find_element(By.XPATH, f"//option[{j + 1}]").click()
            break
        else:
            pass

    context.driver.find_element(By.XPATH, "//label[normalize-space()='Select Reporting Manager']").click()
    time.sleep(2)

    context.driver.find_element(By.XPATH, "(//select)[2]").click()
    time.sleep(2)
    RM = context.driver.find_element(By.XPATH, "(//select)[2]/option[2]").text
    context.driver.find_element(By.XPATH, "(//select)[2]/option[2]").click()

    context.driver.find_element(By.XPATH, "//label[normalize-space()='Select Role']").click()

    context.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    time.sleep(2)


@Then(u'validate the role and reporting manger in list got selected ones or not')
def step_impl(context):
    RMM = context.driver.find_element(By.XPATH, f"//tbody/tr[{ro}]/td[3]").text
    SRR = context.driver.find_element(By.XPATH, f"//tbody/tr[{ro}]/td[2]").text

    assert (RM == RMM and SR == SRR)
