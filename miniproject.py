#countdown timer
import time
countdown = int(input("Enter the countdown time in seconds: "))
print("/nCountdown started...")
for i in range(countdown, 0, -1):
    print(i)
    time.sleep(1)
print("Time's up!")

