*** Settings ***
Documentation    Suite description
Library  Steps.SearchPageObjectSteps.SearchRobotSteps


Suite Setup

*** Test Cases ***
Ensure the capital of a country displayes
    open    https://google.com
    search      python
    ${text}=  get text first result
    Should Be Equal As Strings      ${text}     Welcome to Python.org