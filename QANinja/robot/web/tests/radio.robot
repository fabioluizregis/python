*** Settings ***
Resource    base.robot

Test Setup        Nova sessão           # After
Test Teardown     Encerra sessão        # Before

*** Variables ***


*** Test Cases ***
Selecionando por ID
    Go To                                ${url}/radios
    Select Radio Button                  movies    cap
    Radio Button Should Be Set To        movies    cap

Selecionando por Value
    Go To                                ${url}/radios
    Select Radio Button                  movies    guardians
    Radio Button Should Be Set To        movies    guardians