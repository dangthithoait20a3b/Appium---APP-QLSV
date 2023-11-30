Feature: Login to the app
  I want to be able to log into the app

  Scenario: Login successful

    Given I am on the login page
    When I enter valid MSSV and password
    And I press the "ĐĂNG NHẬP" button
    Then I should see the official page of the app

  Scenario: Login failed with wrong MSSV

    Given I access to the student management app tc02
    When I enter wrong MSSV
    And I press the "ĐĂNG NHẬP" button
    Then I won't be able to access the official page of the app and will have an error message "incorrect MSSV or password"

  Scenario: Login failed with wrong password
    Given I access the student management app tc03
    When I enter the correct MSSV - I entered the wrong password
    And I press the "ĐĂNG NHẬP" button
    Then I won't be able to access the official page of the app and will have an error message "incorrect MSSV or password"

  Scenario: Login failed with blank password

    Given I access the student management app tc04
    When I enter MSSV
    And I don't enter the password
    And I press the "ĐĂNG NHẬP" button
    Then I won't be able to access the official page of the app and will have an error message "Lỗi đăng nhập bạn chưa nhập đủ thông tin"

  Scenario: Login failed with empty MSSV

    Given I access the student management app tc05
    When I don't enter MSSV
    And I enter the password
    And I press the "ĐĂNG NHẬP" button
    Then I won't be able to access the official page of the app and will have an error message "Lỗi đăng nhập bạn chưa nhập đủ thông tin"