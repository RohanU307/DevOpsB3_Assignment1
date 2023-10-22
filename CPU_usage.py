
import psutil

def check_cpu():
    usage=psutil.cpu_percent()
    return usage < 80

while True:
    per_cpu=psutil.cpu_percent(2)
    print("The CPU usage is: ", f"{per_cpu}%")

    if not check_cpu():
        print("Error!! The CPU usage is over 80%")




