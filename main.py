import flet as ft
import time
import asyncio
       
async def update_timer(page, timer_text, start_time):
    while True:
        left_time = time.time() - start_time
        timer_text.value = f"{left_time:.2f} seconds"
        page.update()
        await asyncio.sleep(0.1)

def main(page: ft.Page):
    page.title = "HomeTimer"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    button_status = "Start"
    timer_value = ft.Text(value="0.00 sec")

    async def start_timer():
        start_time = time.time()
        await update_timer(page, timer_value, start_time)
        

#не меняет цвет потому что разрабы не фиксят этот баг, не трогать - ждать обнову
    async def change_main_button_style(e):
        nonlocal button_status
        #хз что это
        if main_button.data:
            main_button.bgcolor = ft.colors.RED_200
            button_status = "Stop"
            main_button.data = False
            await start_timer()
        else:
            main_button.bgcolor = ft.colors.GREEN_200
            button_status = "Start"
            main_button.data = True
        
        main_button.data = True
        # main_button.data = not main_button.data
        main_button.text = button_status
        page.update()

    main_button = ft.ElevatedButton(text=button_status, 
                                    data=True, 
                                    bgcolor = ft.colors.GREEN_200, 
                                    width = 300,
                                    height = 300,
                                    on_click=change_main_button_style)

    page.add(
        timer_value,
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
