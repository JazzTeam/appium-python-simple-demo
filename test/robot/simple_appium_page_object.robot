*** Settings ***
Documentation    Suite description
Library  appium_steps.main_page_steps_for_robot.MainSteps


Suite Setup

*** Test Cases ***
Ensure the capital of a country displayes
    ${alert_views_page}=  open alert views page
    ${alert_dialog}=   Call Method  ${alert_views_page}   open_okay_cancel_alert
    Call Method    ${alert_dialog}   cancel_alert
    quit



