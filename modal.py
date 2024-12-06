import time
import asyncio

class Timer:
    def __init__(self):
        self.timer_is_run = False
        self.left_time = 0.0

    async def update_timer(self, page, timer_text):
        start_time = time.time()

        while self.timer_is_run:
            self.left_time += time.time() - start_time
            start_time = time.time()

            timer_text.value = f"{self.left_time:.2f} seconds"
            page.update()
            await asyncio.sleep(0.1)
    
    def start(self):
        self.timer_is_run = True

    def stop(self):
        self.timer_is_run = False