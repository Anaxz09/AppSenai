import asyncio

import flet
import route
from flet import ThemeMode, Text, TextField, Button, Column, CrossAxisAlignment, OutlinedButton, ElevatedButton, \
    TextButton, Container, Colors, FontWeight, View, AppBar, Row, Icon
from flet.controls.border_radius import horizontal
from flet.controls.material import button
from datetime import datetime

from flet.controls.material.icons import Icons


def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK  # Ou ThemeMode.Dark
    page.window.width = 400
    page.window.height = 700

    # Funções
    def salvar_informacoes():
        text.value = (f'Número do quarto: {input_num.value} ')
        text1.value = (f'Tipo do quarto: {input_tipo.value} ')
        text2.value = (f'Preço: R${input_preco.value} ')
        text3.value = (f'Andar: {input_andar.value} ')

        tem_erro = False
        if input_num.value:
            input_num.error = None
        else:
            tem_erro = True
            input_num.error = "Obrigatório responder"

        if input_tipo.value:
            input_tipo.error = None
        else:
            tem_erro = True
            input_tipo.error = "Obrigatório responder"

        if input_preco.value:
            input_preco.error = None
        else:
            tem_erro = True
            input_preco.error = "Obrigatório responder"

        if input_andar.value:
            input_andar.error = None
        else:
            tem_erro = True
            input_andar.error = "Obrigatório responder"

        if not tem_erro:
            input_num.value = ""
            input_tipo.value = ""
            input_preco.value = ""
            input_andar.value = ""
            navegar(route="/mensagem")

    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)

        )

    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    AppBar(
                        title="Atividade 3",
                        bgcolor=Colors.TEAL_ACCENT_700,
                    ),
                    input_num,
                    input_tipo,
                    input_preco,
                    input_andar,
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
                        Container(
                            Column([
                                Row([
                                    Icon(Icons.ONETWOTHREE_ROUNDED, color=Colors.WHITE, size=30),
                                    text,
                                ]),
                                Row([
                                    Icon(Icons.BEDROOM_PARENT, color=Colors.WHITE, size=30),
                                    text1,
                                ]),
                                Row([
                                    Icon(Icons.MONETIZATION_ON, color=Colors.WHITE, size=30),
                                    text2,
                                ]),
                                Row([
                                    Icon(Icons.ELEVATOR, color=Colors.WHITE, size=30),
                                    text3,
                                ]),

                            ]),
                            bgcolor=Colors.GREY_900,
                            padding=15,
                            border_radius=10,
                            width=400,
                        ),

                    ]
                )
            )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    text = Text()
    text1 = Text()
    text2 = Text()
    text3 = Text()
    input_num = TextField(label="Número do quarto")
    input_tipo = TextField(label="Tipo do quarto")
    input_preco = TextField(label="Preço")
    input_andar = TextField(label="Andar")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_informacoes)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
