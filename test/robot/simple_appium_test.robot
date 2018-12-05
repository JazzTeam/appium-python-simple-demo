*** Settings ***
Documentation    Suite description
Library  AppiumLibrary

Suite Setup  Go to app
Suite Teardown  Quit Application


*** Test Cases ***
Ensure the capital of a country displayes
    Click Element    xpath=//XCUIElementTypeStaticText[@name="Alert Views"]
    Click Element    xpath=//XCUIElementTypeStaticText[@name="Okay / Cancel"]
    Wait Until Page Contains    A message should be a short, complete sentence.     timeout=5
    Click Element    //XCUIElementTypeButton[@name="Cancel"]


*** Keywords ***
Go to app
    Open Application    http://192.168.1.153:4723/wd/hub     platformName=iOS    platformVersion=11.4    deviceName=iPhone 6s   automationName=XCUITest     app=/Users/admin/Library/Developer/Xcode/DerivedData/UICatalog-afswgjckpnkqtebkoffqyuhqtgqq/Build/Products/Debug-iphonesimulator/UICatalog.app

Open Page By Name

