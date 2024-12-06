import flet as ft
from modal import Timer
from view import get_timer_value, create_main_button, create_finish_button

def main(page: ft.Page):
    page.title = "HomeTimer"
    _timer_value = get_timer_value()
    _timer = Timer()

    async def stopwatch():
        await _timer.update_timer(page, _timer_value)

    async def change_main_button_style(e):
        if not _timer.timer_is_run:
            _timer.start()
            _main_button.bgcolor = ft.Colors.RED_200
            _main_button.text = "Stop"
            await stopwatch()
        else:
            _timer.stop()
            _main_button.bgcolor = ft.Colors.GREEN_200
            _main_button.text = "Start"
        page.update()

    _main_button = create_main_button(change_main_button_style) 
    _finish_button = create_finish_button()

    page.add(
        ft.Column(
            [
                ft.Container(
                    _timer_value,
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    _main_button,
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    _finish_button,
                    alignment=ft.alignment.center,
                )
            ],
           
        ),
    )

ft.app(main)