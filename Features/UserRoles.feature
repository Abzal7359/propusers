Feature: performing different operations and validating in user roles section
  @u
  Scenario: user role adding and validating user role added or not
    When click on user roles under user management
    And click create user role button
    And fill user role realted details
    And select Access rights
    And click save button
    Then validate the user role created or not
  @u
  Scenario:cloning the user role we create
    When click on clone link
    Then valiadte the clone is added or not
  @u
  Scenario: delete the user role and validate
    When click on delete button of user role
    Then valaidate the user role deleted or not
  @u
  Scenario:adding duplicate user role and checking the error user role already exists
    When click create user role button
    And fill user role realted details
    And select Access rights
    And click save button
    Then validate error of user role already exists
  @u
  Scenario: edit the user role and check the updates reflected or not
    When click on edit button
    And fill user editing details
    And select different acces rights
    And click save button
    And validate user role edited or not
    Then valaidte user role edited or not by checking access rights


  @u
  Scenario: deleting the user role which has users assigned
    Then click on delete button of user role which has users assigned and validate error
  @u
  Scenario:Applying filter to reports and check filters applied or not
    Then apply filters and validate the filters applied and giving good result or not
  @u
  Scenario: in create user role check reset functionality
    When click on select all in filters
    And click create user role button
    And fill user role realted details
    And select Access rights
    And click on reset button
    Then validate the data is reseted or not
  @u
  Scenario: in create user role select access rights with out basic selection it throws error
    When click create user role button
    And fill user role realted details
    And select Access rights without basic selection
    Then validate error displayed or not

  Scenario:Add users functionality checking by random mail and validating in users the mail is displayed and got invited option or not
    When click on Add user option on any user role
    And fill email and select reporting manager
    Then validate in users section under USER MANAGEMENT

  Scenario: Add user with same mail which invited before check duplicate error throwing or not
    When click on user roles under user management
    When click on Add user option on any user role
    And fill email and select reporting manager
    Then validate duplicate error showing or not











