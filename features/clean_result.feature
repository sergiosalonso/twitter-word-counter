Feature: Reset the results

  Scenario: we have done an execution
     Given we have searched for a twitter account
      When we click the clean button
      Then the page gets cleaned up

  Scenario: we havent done a execution
     Given we are connected to the page
      When we click the clean button
      Then we dont get any result
