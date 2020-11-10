*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${SEARCH_FIELD}    name=q
${YA_FIELD}    css=#text
&{SEARCH_ENGINES}    yandex.ru=${YA_FIELD}    google.ru=${SEARCH_FIELD}    bing.com=${SEARCH_FIELD}    duckduckgo.com=${SEARCH_FIELD}    go.mail.ru=${SEARCH_FIELD}


*** Keywords ***
Verify Page Title Contains [Arguments] ${VALUE}
    ${TITLE}    Get Title
    Should Contain      ${TITLE}    ${VALUE}

Input And Submit Search [Arguments] ${SELECTOR} ${VALUE}
    Input Text    ${SELECTOR}     ${VALUE}
    Press Keys    ${SELECTOR}   ENTER

Check Search Engine [Arguments] ${ENGINE} ${SEARCH_FIELD} ${REQUEST}
    Go To    https://${ENGINE}
    Input And Submit Search    ${SEARCH_FIELD}    ${REQUEST}
    Wait Until Keyword Succeeds    3 sec    1 sec    Verify Page Title Contains    ${REQUEST}
