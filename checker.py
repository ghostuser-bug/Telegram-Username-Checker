from pyrogram import Client
from pyrogram.raw import functions
import os
import time
import requests

api_id = 19236456  # <============Your API ID here https://my.telegram.org/apps
api_hash = '12892cfcsfd7d7b4af1c0ab18567e6a'  # <============Your API Hash here https://my.telegram.org/apps
bot_token = '0752289740:ANEnIs2V22GEIo0edeKbO5grGRLt0kFjBck'  # Your bot token
chat_id = '1584123455'  # Replace with your chat ID, find it at Telegram Bot @userinfobot

os.system("clear")

print("""
████████╗███████╗██╗░░░░░███████╗░██████╗░██████╗░░█████╗░███╗░░░███╗
╚══██╔══╝██╔════╝██║░░░░░██╔════╝██╔════╝░██╔══██╗██╔══██╗████╗░████║
░░░██║░░░█████╗░░██║░░░░░█████╗░░██║░░██╗░██████╔╝███████║██╔████╔██║
░░░██║░░░██╔══╝░░██║░░░░░██╔══╝░░██║░░╚██╗██╔══██╗██╔══██║██║╚██╔╝██║
░░░██║░░░███████╗███████╗███████╗╚██████╔╝██║░░██║██║░░██║██║░╚═╝░██║
░░░╚═╝░░░╚══════╝╚══════╝╚══════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝

██╗░░░██╗░██████╗███████╗██████╗░███╗░░██╗░█████╗░███╗░░░███╗███████╗
██║░░░██║██╔════╝██╔════╝██╔══██╗████╗░██║██╔══██╗████╗░████║██╔════╝
██║░░░██║╚█████╗░█████╗░░██████╔╝██╔██╗██║███████║██╔████╔██║█████╗░░
██║░░░██║░╚═══██╗██╔══╝░░██╔══██╗██║╚████║██╔══██║██║╚██╔╝██║██╔══╝░░
╚██████╔╝██████╔╝███████╗██║░░██║██║░╚███║██║░░██║██║░╚═╝░██║███████╗
░╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝

░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
""")
print("Code by Jen")
print("⚠️ Warning: Please use a user account (phone number) for this script to work as Telegram will not allow bots to check usernames!")


with open("words.txt", "r") as file:
    words_list = [line.strip() for line in file.readlines()]

with Client("generator_session", api_id=api_id, api_hash=api_hash) as app:
    for word in words_list:
        random_username = word.strip()
        print(f"\033[94m Using {random_username}")

        try:
            result = app.invoke(functions.account.CheckUsername(username=random_username))

            if result:
                print(f"\033[92m {random_username} is available!")
                message = f"Username available: @{random_username}"
                requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage", data={"chat_id": chat_id, "text": message})
            else:
                print(f"\033[91m {random_username} is already taken.")

            time.sleep(10)

        except Exception as e:
            print(f"\033[91m Error: {e}")
            time.sleep(10)
