*** Settings ***
Resource    base.robot

Test Setup        Nova sessão           # After
Test Teardown     Encerra sessão        # Before

*** Variables ***
${check_thor}            id:thor
${check_ironman}         css:input[value='iron-man']
${check_blackpanther}    xpath://*[@id='checkboxes']/input[7]


*** Test Cases ***
Marcando opção com ID
    Go To                          ${url}/checkboxes
    Select Checkbox                ${check_thor}
    Checkbox Should Be Selected    ${check_thor}

Marcando opção com CSS Selector
    Go To                          ${url}/checkboxes
    Select Checkbox                ${check_ironman}
    Checkbox Should Be Selected    ${check_ironman}

Marcando opção com X-Path
    [Tags]                         black-panther
    Go To                          ${url}/checkboxes
    Select Checkbox                ${check_blackpanther}
    Checkbox Should Be Selected    ${check_blackpanther}

