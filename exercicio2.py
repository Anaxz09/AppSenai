import asyncio

import flet
import route
from flet import ThemeMode, Text, TextField, Button, Column, CrossAxisAlignment, OutlinedButton, ElevatedButton, \
    TextButton, Container, Colors, FontWeight, View, AppBar
from flet.controls.border_radius import horizontal
from flet.controls.material import button
from datetime import datetime

def main(page: flet.Page):
    #Configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK # Ou ThemeMode.Dark
    page.window.width = 400
    page.window.height = 700

    #Funções
    def salvar_informacoes():
        text.value = (f'Funcionário: {input_nome.value} ')
        text1.value = (f'CPF: {input_cpf.value} ')
        text2.value = (f'EMAIL: {input_email.value} ')
        text3.value = (f'SALÁRIO: R${input_salario.value} ')

        tem_erro = False
        if input_nome.value:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "Obrigatório responder"

        if input_cpf.value:
            input_cpf.error = None
        else:
            tem_erro = True
            input_cpf.error = "Obrigatório responder"

        if input_email.value:
            input_email.error = None
        else:
            tem_erro = True
            input_email.error = "Obrigatório responder"

        if input_salario.value:
            input_salario.error = None
        else:
            tem_erro = True
            input_salario.error = "Obrigatório responder"

        if not tem_erro:
            input_nome.value = ""
            input_cpf.value = ""
            input_email.value = ""
            input_salario.value = ""
            navegar(route="/mensagem")
    #Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)

        )
    #Gerenciar as telas(routes)
    def route_change():
        page.views.clear()


        page.views.append(
            View(
                route="/",
                controls=[
                    AppBar(
                        title="Atividade 2",
                        bgcolor=Colors.TEAL_ACCENT_700,
                    ),
                    input_nome,
                    input_cpf,
                    input_email,
                    input_salario,
                    btn_salvar,
                ]
            )
        )
        if page.route == "/mensagem":
            page.views.append(
                View(
                    route="/mensagem",
                    controls=[
                        AppBar(
                            title="Segunda página",
                        ),
                        text,
                        text1,
                        text2,
                        text3

                    ]
                )
            )

    #Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    text=Text()
    text1 = Text()
    text2 = Text()
    text3 = Text()
    input_nome = TextField(label="NOME")
    input_cpf = TextField(label="CPF")
    input_email = TextField(label="EMAIL")
    input_salario = TextField(label="SALÁRIO")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_informacoes)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)
