import flet as ft
        
def main(page: ft.Page):
    page.title = "HomeTimer"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    button_status = "Start"

#не меняет цвет потому что разрабы не фиксят этот баг, не трогать - ждать обнову
    def change_main_button_style(e):
        if main_button.data:
            main_button.bgcolor = ft.colors.GREEN_200
            button_status = "Stop"
        else:
            main_button.bgcolor = ft.colors.RED_200
            button_status = "Start"
        
        main_button.data = not main_button.data
        main_button.text = button_status
        page.update()

    main_button = ft.ElevatedButton(text=button_status, 
                                    data=True, 
                                    bgcolor = ft.colors.GREEN_200, 
                                    width = 300,
                                    height = 300,
                                    on_click=change_main_button_style)
    main_button.width = 300
    main_button.height = 300

    page.add(
        ft.Row(
            [
                ft.Container(
                    main_button,
                    alignment=ft.alignment.center,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

ft.app(main)
