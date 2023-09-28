Feature: checking functionalities in users section under ->user management

  Scenario: click on users and Verify user is able to see the table with columns like:
  Name, Role, Reports to,Reportees,Status (Off by default),Last Active on (Off by default)
    When click on users under user role management
    Then verify name,role,reports to,reportees,status are visibile or not

  Scenario: Verify user is able to Add and remove columns like: Last Active on
    When click on plus symbol and select last Active one
    Then verify Last Active on coloumn is displayed or not

  Scenario: Verify user is able to filter the table data based on Role, Reports to and Status
    When click on role and select some options
    And validate based on the role they are displayed or not
    When choose any some  Reports to filter
    And Verify in the Reports To column if the chosen person has been selected or not
    When selecting the status option, choose one of the status options below it
    Then validate in the status column if the applied filter is visible or not
  @l
  Scenario: search any one user role name and check It is showing correct user or not
    When enter name in search box
    Then validate in user role list it showing that name only
  @l
  Scenario: in Invite User select Role option in that dropdown check all the user roles showing or not
    When click on user roles
    And collect all user roles names
    And click on users under user role management
    And click on Invite User and click select Role
    Then verify all the user roles present or not
  @l
  Scenario: click on Add button in invite users pop up and check extra inputs available or not
    When click on Add button
    Then validate extra input box for mail open and cross symbolls are displayed or not

  @p
  Scenario: check the overflow menu of different status
    When click on overflow menu of INVITED status user
    And validate the menu items
    When click on overflow menu of ENABLED status user
    And validate the overflow menu items
    When click on overflow menu of DISABLED status user
    Then validate the overflow menu items of diabled
  @p
  Scenario: validate when clicking change manager at drop down showing selected as default value
    When click on overflow menu of ENABLED status user
    And click on change reporting manager
    Then validate default value is selected value or not
  @p
  Scenario: change  reporting manager and validate in reports to coloumn that is reflected or not
    When select any reporting manager and click save
    Then validate that change is reflected or not in reports to coloumn

  Scenario: Verify disable user button is not visible to user with the user role <ProjectAdmin>
    When click on the options of user whos role is project Admin
    Then validate you not get Disable option



  Scenario: Add reporties to enable user and validate
    When click on add reporties on user role whose status is enabled
    And select Reportie and click save
    Then validate with toaster message

  Scenario: Disable user and validate person is disabled or not
    When click on disable user option on user who doesnt have reportiees
    And click save button to disbale
    Then validate status and red colour dot on profile


  Scenario: Enable user and validate person is Enabled or not
    When click on enalbe user option on user whos status is disbaled
    And select role and reporting manager and clik save
    Then validate status and manger


  Scenario: change user role to the user who has no Reportees
    When click on change user role option of enabled person and not project admin
    And select role and select Reporting manager
    Then validate the role and reporting manger in list got selected ones or not









