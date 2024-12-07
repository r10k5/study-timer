import datetime
import flet as ft
from modal import Timer
from view import get_timer_value, create_main_button, create_finish_button

def main(page: ft.Page):
    page.title = "HomeTimer"
    _timer_value = get_timer_value()
    _timer = Timer()

    async def stopwatch():
        await _timer.update_timer(page, _timer_value)

    async def change_button_status(e):
        if not _timer.timer_is_run:
            _timer.start()
        else:
            _timer.stop()

        change_main_button_style()
        await stopwatch()

    def change_main_button_style():
        if not _timer.timer_is_run:
            _main_button.bgcolor = ft.Colors.GREEN_200
            _main_button.text = "Start"
        else:
            _main_button.bgcolor = ft.Colors.RED_200
            _main_button.text = "Stop"
        page.update()
    
    def finishing_timer(e):
        _timer.finish()
        formated_time = str(datetime.timedelta(seconds=int(_timer.left_time)))
        _timer_value.value = formated_time
        change_main_button_style()

    _main_button = create_main_button(change_button_status) 
    _finish_button = create_finish_button(finishing_timer)

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