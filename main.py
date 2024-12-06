import flet as ft
import time
import asyncio
       
timer_is_run = False
left_time = 0.0

async def update_timer(page, timer_text):
    global timer_is_run
    global left_time
    start_time = time.time()

    while timer_is_run:
        left_time += time.time() - start_time
        start_time = time.time()

        timer_text.value = f"{left_time:.2f} seconds"
        page.update()
        await asyncio.sleep(0.1)

def main(page: ft.Page):
    page.title = "HomeTimer"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    timer_value = ft.Text(
        value="0.00 sec",
        style=ft.TextStyle(weight=ft.FontWeight.BOLD),
    )

    async def start_timer():
        await update_timer(page, timer_value)
        

    async def change_main_button_style(e):
        global timer_is_run

        if not timer_is_run:
            timer_is_run = True
            main_button.bgcolor = ft.Colors.RED_200
            main_button.text = "Stop"
            await start_timer()
        else:
            timer_is_run = False
            main_button.bgcolor = ft.Colors.GREEN_200
            main_button.text = "Start"
        
        page.update()

    main_button = ft.ElevatedButton(
        text = "Start", 
        bgcolor = ft.colors.GREEN_200, 
        width = 300,
        height = 300,
        on_click=change_main_button_style
    )

    finish_button = ft.ElevatedButton(
        text = "Finish", 
        bgcolor = ft.colors.GREY_100, 
        width = 80,
        height = 80,
    )

    page.add(
        ft.Column(
            [
                ft.Container(
                    timer_value,
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    main_button,
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    finish_button,
                    alignment=ft.alignment.center,
                )
            ],
           
        ),
    )
    

ft.app(main)
