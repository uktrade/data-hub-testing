Feature: Create a New Company
  As a existing user
  I would like to create a new company in various locations


  @create_new_company_test
  Scenario: Create a New Foreign Organisation
    Given I am a Authenticated user logged in to datahub website
    When I create a new Foreign Organisation Company
    Then I verify my newly created company in search results

  @create_new_company_test1
  Scenario: Create a New Other type of UK organisation
    Given I am a Authenticated user logged in to datahub website
    When I create a new other type of UK Organisation Company
    Then I verify my newly created company in search results

  @create_new_company_test2
  Scenario: Create a New UK private or public limited company
    Given I am a Authenticated user logged in to datahub website
    When I create a new UK private or public limited company
    #Then I verify my newly created company in search results