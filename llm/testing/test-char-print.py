import time

message = ("""Welcome to Cloud World\nHello, How may I help you?""")

for char in message:
    print(char, end='', flush=True)
    time.sleep(0.1)  # Add a delay between each character

print()  # Print a new line after the message is complete