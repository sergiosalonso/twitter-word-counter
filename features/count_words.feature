
Feature: Count words of the last tweets of a twitter account

  Scenario: the account exists
     Given we are connected to the page
      When we introduce a valid twitter account
      And we click the execute button
      Then we get the most repeated words


  Scenario: the account doesn't exist
     Given we are connected to the page
      When we introduce an invalid account name
      And we click the execute button
      Then we get an error message


  Scenario: not introducing any account
     Given we are connected to the page
      When we click the execute button
      Then we dont get any result
