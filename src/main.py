import os

import pyperclip

from const import designations
from translations import hello, text_input, text_copied

while True:
    try:
        language = int(input("Enter your language\n"
                             "1. Русский\n"
                             "2. English\n"
                             "> "))
        if language == 1 or language == 2:
            break
        print("Enter 1 or 2!")
    except ValueError:
        print("Enter the number!")
while True:
    print(hello[language-1])
    text = input(text_input[language-1])
    for color, color_code in designations.items():
        text = text.replace(color, color_code)

    os.system("cls")
    pyperclip.copy(f"playerradio Radio \"{text}\"")
    print(text_copied[language-1])
