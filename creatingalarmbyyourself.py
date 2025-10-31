print("creating own alarm ")
import playsound3
import time
import datetime

n=input("enter time for set alarm like 19:17    ")
print(f"alarm seted at time {n}")
while True:
    current_time=datetime.datetime.now().strftime("%H:%M")
    if current_time==n:
        playsound3.playsound("alarmsound.wav")
        break
    time.sleep(1)
        



































