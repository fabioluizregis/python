*** Settings ***
Library        app.py

*** Test Cases ***
Deve retornar mensagem de boas vindas
    ${result}=            Welcome        Fabio
    Log To Console        ${result} 
    Should Be Equal       ${result}    Olá Fabio, bem vindo ao curso básico de Robot Framewok!