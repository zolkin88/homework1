*** Settings ***
Documentation     Тесты на основе своих классов на Python
Library  SeleniumLibrary
Library  ../Libs/LoginAdmin.py
Library  ../Libs/LoginClient.py
*** Variables ***
${LOGIN URL}      http://localhost/admin/
${BROWSER}        Chrome


*** Test Cases ***

Test Class Admin Python
    login_to_admin_page

Test Class Client Python
    login_to_client