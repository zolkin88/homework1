*** Settings ***
Documentation     My tests on Robot
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      http://localhost/admin/
${BROWSER}        Chrome
${USERNAME}       user
${PASSWORD}       bitnami

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Administration

Input Username
    [Arguments]    ${username}
    Input Text    input-username    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    input-password    ${password}

Submit Credentials
    Click Button    //*[@type='submit']

Welcome Page Should Be Open
    Title Should Be    Dashboard



*** Test Cases ***
Check AdminPage Title
    Open Browser  ${LOGIN URL}    ${BROWSER}
    Title Should Be    Administration
    [Teardown]    Close Browser

Invalid Password
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Input Username    ${USERNAME}
    Input Password    bad_pass
    Submit Credentials
    [Teardown]    Close Browser

Invalid UserName
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Input Username    bad_name
    Input Password    ${PASSWORD}
    Submit Credentials
    [Teardown]    Close Browser

Valid Login
    Open Browser    ${LOGIN URL}    ${BROWSER}    options=add_argument("--ignore-certificate-errors")
    Input Username    ${USERNAME}
    Input Password    ${PASSWORD}
    Submit Credentials
    Welcome Page Should Be Open
    [Teardown]    Close Browser


Check Logout
    Open Browser    ${LOGIN URL}    ${BROWSER}    options=add_argument("--ignore-certificate-errors")
    Input Username    ${USERNAME}
    Input Password    ${PASSWORD}
    Submit Credentials
    Welcome Page Should Be Open
    SeleniumLibrary.click element      //*[@class='fa fa-sign-out']
    title should be    Administration
    [Teardown]    Close Browser

