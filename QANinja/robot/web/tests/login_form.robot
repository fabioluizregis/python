*** Settings ***
Resource    base.robot

Test Setup        Nova sessão           # After
Test Teardown     Encerra sessão        # Before


*** Test Cases ***
Login com sucesso
    Go To                         ${url}/login
    Login with                    stark    jarvis!
    Should Contain Login Alert    Olá, Tony Stark. Você acessou a área logada!

Senha inválida
    Go To                         ${url}/login
    Login with                    stark    nonExiste
    Should Contain Login Alert    Senha é invalida!

Usuário não existe
    [tags]                        login_error
    Go To                         ${url}/login
    Login with                    nonExiste    jarvis!
    Should Contain Login Alert    O usuário informado não está cadastrado!

*** Keywords ***
Login with
    [Arguments]               ${uname}    ${pass}

    Input Text                css:input[name=username]    ${uname}
    Input Text                css:input[name=password]    ${pass}
    Click Element             class:btn-login

Should Contain Login Alert
    [Arguments]    ${expect_message}

    ${message}=               Get WebElement            id:flash
    Should Contain            ${message.text}           ${expect_message}
