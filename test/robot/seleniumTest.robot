*** Settings ***
Documentation    Suite description
Library  Selenium2Library

Suite Setup  Go to google
Suite Teardown  Close all browsers

*** Test Cases ***
Ensure the capital of a country displayes
    search and check        Russia      Moscow
    search and check        France      Paris

*** Keywords ***
Go to google
    Open Browser    https://www.google.com/     chrome

search and check
    [Arguments]     ${query}    ${expexted_result}
    Input Text      name=q      ${query}
    Press Key       name=q      \\13
    Wait Until Page Contains    ${expexted_result}

