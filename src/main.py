import flet as ft
from flet import *

def main(page: Page):
    page.theme_mode = 'dark'
    page.title = 'Ley de Ohm'
    page.window_height = 400
    page.window_width = 500
    page.window_resizable = False

    #! Funcion con Corriente
    def corriendo_clicked(e):
        if chk_corriente.value == True:
            i_1.value = (f'Voltaje')
            d_1.value = (f'Volts')
            i_2.value = (f'Resistencia')
            d_2.value = (f'Ohms')

            chk_voltaje.value = False
            chk_resistencia.value = False

            page.update()
        else:
            i_1.value = (f'')
            d_1.value = (f'')
            i_2.value = (f'')
            d_2.value = (f'')
            page.update()

    #! Funcion con Voltaje
    def voltaje_clicked(e):
        if chk_voltaje.value == True:
            i_1.value = (f'Corriente')
            d_1.value = (f'Amperios')
            i_2.value = (f'Resistencia')
            d_2.value = (f'Ohms')
            chk_corriente.value = False
            chk_resistencia.value = False
            page.update()
        else:
            i_1.value = (f'')
            d_1.value = (f'')
            i_2.value = (f'')
            d_2.value = (f'')
            page.update()

    #! Funcion con Resistencia
    def resistencia_clicked(e):
        if chk_resistencia.value == True:
            i_1.value = (f'Voltaje')
            d_1.value = (f'Volts')
            i_2.value = (f'Corriente')
            d_2.value = (f'Amperios')
            chk_voltaje.value = False
            chk_corriente.value = False
            page.update()
        else:
            i_1.value = (f'')
            d_1.value = (f'')
            i_2.value = (f'')
            d_2.value = (f'')
            page.update()

    #! Funcion para calcular
    def calcular_clicked(e):
        txt_1.value = int(txt_1.value)
        txt_2.value = int(txt_2.value)
        
        if chk_corriente.value == True:
            # Corriente = Voltaje / Resistencia
            resultado = txt_1.value / txt_2.value
            lbl_resultado.value = (f'{resultado} Amperios')
            page.update()
        
        elif chk_voltaje.value == True:
            # Voltaje = Corriente * Resistencia
            resultado = txt_1.value * txt_2.value
            lbl_resultado.value = (f'{resultado} Volts')
            page.update()
        
        elif chk_resistencia.value == True:
            # Resistencia = Voltaje / Corriente
            resultado = txt_1.value / txt_2.value
            lbl_resultado.value = (f'{resultado} Ohms')
            page.update()

    #! Titulo
    title= Text('Ley de Ohm', size=25, width=500, text_align='center')

    #! Checkboxs
    chk_voltaje = Checkbox(label="Voltaje", value=False, on_change=voltaje_clicked)
    chk_corriente = Checkbox(label="Corriente", value=False, on_change=corriendo_clicked)
    chk_resistencia = Checkbox(label="Resistencia", value=False, on_change=resistencia_clicked)

    #! Texts
    i_1 = Text("")
    i_2 = Text("")
    d_1 = Text("")
    d_2 = Text("")

    #! TextFields
    txt_1 = TextField(label="Ingrese valor")
    txt_2 = TextField(label="Ingrese valor")

    #! Boton para calcular
    btn_Calcular = ElevatedButton('Calcular', width=500, on_click=calcular_clicked)

    #! Resultado
    lbl_resultado = Text("", size=25, width=500, text_align='center')

    #! Page add
    page.add(
        title,
        Row([
            chk_voltaje, chk_corriente, chk_resistencia],alignment='spaceBetween'),

        Row([
            i_1, txt_1, d_1], alignment='spaceBetween'),

        Row([
            i_2, txt_2, d_2], alignment='spaceBetween'),

        btn_Calcular,
        lbl_resultado
        )

ft.app(target=main, assets_dir='assets')
# ft.app(target=main, assets_dir='assets', port=5000, view=ft.WEB_BROWSER)