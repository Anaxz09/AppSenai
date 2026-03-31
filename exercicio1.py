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
    def salvar_nome():
        text.value = f'Olá , {input_nome.value}'
        input_nome.value = ""
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
                        title="Atividade 1",
                        bgcolor=Colors.TEAL_ACCENT_700,
                    ),
                    input_nome,
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
                        text

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
    input_nome = TextField(label="Nome")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)

    # Eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()

flet.run(main)
