import time

my_seconds = int(input("Please enter a time in seconds: "))

for x in range (my_seconds, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME'S UP.")
