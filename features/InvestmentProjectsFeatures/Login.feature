Feature: Login to Datahub
  As a existing user
  I want to login to Datahub

        @login_test
        Scenario: Login Validation
          Given I am on the Datahub website
          When I enter username
          And I enter password
          And I click on Submit button
          Then I verify user is successfully logged in
          When I enter CompanyName into Search field
          And I click search button
          Then I verify the search results display a company

