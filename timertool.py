import time

def write_current_unix_time():
    current_unix_time = int(time.time() * 1000)
    with open('time.txt', 'w') as file:
        file.write(str(current_unix_time))
