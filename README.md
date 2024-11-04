# Telegram Username Checker

This script checks the availability of usernames on Telegram using the Telegram API. It sends a message to a specified chat when a username is available.

## ⚠️ Warning
Please use a user account (phone number) for this script to work as Telegram will not allow bots to check usernames!

## Requirements

To run this script, you need the following:

- Python 3.7 or higher
- The following Python packages:
  - `pyrogram`
  - `requests`

You can install the required packages using pip:

```bash
pip install pyrogram requests

Telegram API Credentials
You need to obtain your Telegram API ID and API Hash by registering your application at my.telegram.org.

API ID: Your API ID
API Hash: Your API Hash
Bot Token: Create a bot using BotFather and obtain the bot token.
Chat ID: Use a bot like @userinfobot to get your chat ID.

Usage
Clone the repository:

bash

Verify

Open In Editor
Edit
Copy code
git clone https://github.com/yourusername/telegram-username-checker.git
cd telegram-username-checker
Create a file named words.txt in the same directory as the script. This file should contain a list of usernames to check, with each username on a new line.

Update the script with your credentials:

python

Verify

Open In Editor
Edit
Copy code
api_id = YOUR_API_ID  # Replace with your API ID
api_hash = 'YOUR_API_HASH'  # Replace with your API Hash
bot_token = 'YOUR_BOT_TOKEN'  # Replace with your bot token
chat_id = 'YOUR_CHAT_ID'  # Replace with your chat ID
Run the script:

bash

Verify

Open In Editor
Edit
Copy code
python script_name.py
Replace script_name.py with the actual name of your Python script.

Notes
The script will check each username from the words.txt file and will print whether the username is available or already taken.
If a username is available, a message will be sent to the specified Telegram chat.
The script pauses for 10 seconds between each username check to avoid hitting Telegram's rate limits.

License
This project is licensed under the MIT License - see the LICENSE file for details.

### Instructions for Use
1. Replace `yourusername` in the clone URL with your actual GitHub username.
2. Ensure that the `words.txt` file is formatted correctly with one username per line.
3. Make sure to test the script after setting it up to confirm that everything works as expected.

Feel free to modify the content as necessary to better fit your project or personal style!
