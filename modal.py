import datetime
import json
import time
import asyncio

class Timer:
    def __init__(self):
        self.clear()

    async def update_timer(self, page, timer_text):
        start_time = time.time()

        while self.timer_is_run:
            self.left_time += time.time() - self.start_time
            self.start_time = time.time()
            formated_total_time = str(datetime.timedelta(seconds=int(self.left_time)))
            timer_text.value = f"{formated_total_time}"
            page.update()
            await asyncio.sleep(0.1)
    
    def clear(self):
        self.timer_is_run = False
        self.left_time = 0.0
        self.start_time = 0.0
        self.stop_time = 0.0
        self.date = None
    
    def start(self):
        self.timer_is_run = True
        self.date = datetime.datetime.now().strftime("%d.%m.%Y")
        self.start_time = time.time()

    def stop(self):
        self.timer_is_run = False
        
    def finish(self):
        self.stop_time = time.time()
        write_to_json(self)
        self.clear()

def write_to_json(timer: Timer):

    total_time = str(datetime.timedelta(seconds=int(timer.left_time)))

    data = {
        "projectName": {
            "sessions": [
                {
                    "date": timer.date,
                    "start-time": datetime.datetime.fromtimestamp(timer.start_time).strftime("%H:%M:%S"),
                    "stop-time": datetime.datetime.fromtimestamp(timer.stop_time).strftime("%H:%M:%S"),
                    "total_time": total_time
                }
            ]
        }
    }
    
    with open("user_projects.json", "w") as file:
        json.dump(data, file)
    return total_time