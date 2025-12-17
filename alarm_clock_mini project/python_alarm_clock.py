import time
import datetime
import subprocess

def set_alarm(alarm_time):
    sound_file = "sound_file.mp3"
    print(f"Alarm is set for: {alarm_time}")
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("Wake up!")
            subprocess.Popen(["start", "", sound_file], shell=True)
            break
        time.sleep(1)
            
if __name__ == "__main__":
    alarm_time = input("enter the alarm time (hh:mm:ss): ")
    set_alarm(alarm_time)