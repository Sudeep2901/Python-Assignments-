# Topic : JOB SCHEDULER using Windows Task Schedular
try:
    from datetime import date, time, datetime

    file = open("cron.txt", "w")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    task = f"Program Clocked at = [ {date.today()} ] & [ {current_time} ]"
    file.write(task)
except BaseException as ex:
    print(f"Error Ocurred at = {ex}")
