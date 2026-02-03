Feature: Login Feature

  Scenario: Successful login
    # Given - current state
    Given user launches the application

    # When - input/condition
    When user logs in with "student" and "Password123"

    # Then - outcome/assertion
    Then dashboard should be displayed


