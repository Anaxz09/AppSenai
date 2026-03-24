import flet
from flet import ThemeMode, Text, TextField, Button, Column, CrossAxisAlignment, OutlinedButton, ElevatedButton, \
    TextButton, Container, Colors, FontWeight
from flet.controls.border_radius import horizontal
from flet.controls.material import button
from datetime import datetime


def main(page: flet.Page):
    #configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK # Ou ThemeMode.Dark
    page.window.width = 400
    page.window.height = 700

    #funções
    def salvar_nome():
        text.value = f'Olá , {input_nome.value} {input_sobrenome.value}'

    def vericar_parimpar():
        numero = int(input_numero.value)
        if numero % 2 == 0:
            text_parimpar.value = f'O {numero} é par'
        else:
            text_parimpar.value = f'O {numero} é impar'

    def calcular_idade():
        ano_nascimento = int(input_data_nascimento.value)
        idade = datetime.now().year - ano_nascimento
        if idade >= 18:
            text_idade.value = f'Você tem {idade} e é maior de idade'
        else:
            text_idade.value = f'Você tem {idade} e menor de idade'




    #componentes
    text = Text()
    text_parimpar = Text()
    text_idade = Text()
    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="sobrenome")
    input_numero= TextField(label="Digite um numero", hint_text="Verifique se é par ou impar")
    input_data_nascimento= TextField(label="Digite o ano de nascimento", hint_text="EX:2000")
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)
    btn_verificar = ElevatedButton("Verificar", on_click=vericar_parimpar)
    btn_calcular = TextButton("Calcular idade", on_click=calcular_idade)




    #Construção de tela

    page.add(
        Column([
            Container(
                Column(
                    [
                    Text("Atividade 1", weight=FontWeight.BOLD, size=24),
                    input_nome,
                    btn_salvar,
                    text,

                    ],
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                ),
                bgcolor=Colors.RED_ACCENT_700,
                padding=15,
                border_radius=10,
                width=400,
            ),

        ],
        width=400,
        horizontal_alignment=CrossAxisAlignment.CENTER
        ),
        Container(
            Column(
                [
                    input_numero,
                    btn_verificar,
                    text_parimpar,
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
            bgcolor=Colors.ORANGE_900,
            padding=15,
            border_radius=10,
            width=400,

        ),
        Container(
            Column(
                [
                    input_data_nascimento,
                    btn_calcular,
                    text_idade

                ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
            ),
            bgcolor=Colors.YELLOW_900,
            padding=15,
            border_radius=10,
            width=400,
        ),
    )

flet.run(main)
