*** Settings ***
Library  SeleniumLibrary
Library  DatabaseLibrary
Suite Setup  Connect To Database  pymysql  ${DBName}  ${DBUser}  ${DBPass}  ${DBHost}  ${DBPort}
Suite Teardown  Disconnect From Database

Test Setup  Open Browser  ${LOGIN URL}    ${BROWSER}    options=add_argument("--ignore-certificate-errors")
Test Teardown  Close Browser
*** Variables ***
${LOGIN_FORM}  css=form
${USERNAME_INPUT}  css=#input-username
${PASSWORD_INPUT}  css=#input-password
${SUBMIT_BUTTON}  css=button[type='submit']
${MENU_CATALOG}  css=#menu-catalog
${CATALOG_ITEMS}  css=#collapse1 > li > a
${ADD_NEW_PRODUCT}  xpath=//a[@data-original-title='Add New']
${SAVE_NEW_PRODUCT}  xpath=//button[@data-original-title='Save']
${DELETE_PRODUCT}  xpath=//button[@data-original-title='Delete']
${PRODUCT_NAME_INPUT}  css=#input-name1
${PRODUCT_META_INPUT}  css=#input-meta-title1
${DATA_PRODUCT_TAB}  Data
${PRODUCT_MODEL_INPUT}  css=#input-model
${LOGIN URL}      http://localhost/admin/
${BROWSER}        Chrome
${USERNAME}       user
${PASSWORD}       bitnami
${PRODUCT_DB}  oc_product
${PRODUCT_DESCRIPTION_DB}  oc_product_description
${DBName}  bitnami_opencart
${DBUser}  bn_opencart
${DBPass}
${DBHost}  127.0.0.1
${DBPort}  3306
${TEST_CHECKBOX}    xpath=//tbody/tr[20]/td[1]/input

*** Keywords ***
Login With
    Wait Until Element Is Visible  ${LOGIN_FORM}
    Input Text  ${USERNAME_INPUT}  ${USERNAME}
    Input Text  ${PASSWORD_INPUT}  ${PASSWORD}
    capture page screenshot
    Submit Form  ${LOGIN_FORM}
    capture page screenshot

Open Catalog Products
    Click Element  ${MENU_CATALOG}
    capture page screenshot
    ${catalog_items} =  Get Webelements  ${CATALOG_ITEMS}
    BuiltIn.Wait Until Keyword Succeeds  3 sec  1 sec  Click Element  ${catalog_items}[1]
    Wait Until Page Contains Element  xpath=//h1[text()='Products']
    capture page screenshot

Add Product To Catalog
    [Arguments]  ${product_name}  ${product_meta}  ${product_model}
    Open Catalog Products
    capture page screenshot
    Click Element  ${ADD_NEW_PRODUCT}
    capture page screenshot
    Input Text  ${PRODUCT_NAME_INPUT}  ${product_name}
    capture page screenshot
    Input Text  ${PRODUCT_META_INPUT}  ${product_meta}
    capture page screenshot
    Click Link  ${DATA_PRODUCT_TAB}
    capture page screenshot
    Input Text  ${PRODUCT_MODEL_INPUT}  ${product_model}
    capture page screenshot
    Click Element  ${SAVE_NEW_PRODUCT}

Check Product In Database
    [Arguments]  ${value}
    Check If Exists In Database  select model from ${PRODUCT_DB} where model = '${value}'

Check Row Count
    [Arguments]  ${number}
    DatabaseLibrary.row count   select * from ${PRODUCT_DB}

Delete Product in GUI
    capture page screenshot
    CLICK ELEMENT   ${TEST_CHECKBOX}
    capture page screenshot
    click button    ${DELETE_PRODUCT}
    capture page screenshot
    Handle Alert  ACCEPT  2 sec
    capture page screenshot

*** Test Cases ***
Add Product
    Login With
    Open Catalog Products
    Add Product To Catalog    test1    test2    test3
    Check Product in Database    test3
    Check Row Count   20


Delete Product
    Login With
    Open Catalog Products
    Delete Product in GUI
    Check Row Count   19