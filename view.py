import flet as ft

def get_timer_value():
    timer_value = ft.Text(
        value="0.00 sec",
        style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    )
    return timer_value

def create_main_button(use_change_style_func):
    main_button = ft.ElevatedButton(
        text = "Start", 
        bgcolor = ft.colors.GREEN_200, 
        width = 300,
        height = 300,
        on_click=use_change_style_func,
    )
    return main_button

def create_finish_button():
    finish_button = ft.ElevatedButton(
        text = "Finish", 
        bgcolor = ft.colors.GREY_100, 
        width = 80,
        height = 80,
    )
    return finish_button