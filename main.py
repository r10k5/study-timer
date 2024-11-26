import flet as ft

def main(page: ft.Page):
    page.title = "HomeTimer"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    global button_status
    button_status = "Start"

    def change_button_style(e):
        global button_status

        if button_status == "Start":
            main_button.bgcolor = ft.colors.GREEN_200
            button_status = "Pause"
        else:
            main_button.bgcolor = ft.colors.RED_200
            button_status = "Start"

        main_button.text = button_status
        page.update()

    main_button = ft.ElevatedButton(text=button_status, on_click=change_button_style)
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
