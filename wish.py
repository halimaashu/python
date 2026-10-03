
import time
timestamp =time.strftime( '%H :%M:%S')

#elo wishing naw my brother")

current_hour = int(time.strftime('%H'))

if 5 <= current_hour < 12:
    print("Good morning! ☕")
elif 18 <= current_hour or current_hour < 5:
    print("Good night! 😴")
else:
    print("Hello! 👋") # For the afternoon