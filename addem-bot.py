import telegram
from telegram.error import TelegramError


# Replace YOUR_TOKEN with your Telegram bot token
bot = telegram.Bot(token='YOUR_TOKEN')

# Replace GROUP_CHAT_ID with the ID of the Telegram group you want to add users to
group_chat_id = 'GROUP_CHAT_ID'

# List of usernames to add to the group
usernames = ['@Q1d3r3r_P']

# Loop through the list of usernames and add each user to the group
for username in usernames:
    try:        
        bot.add_chat_member(cpihat_id=group_chat_id, username=username)
        print(f'{username} added to group successfully!')
    except TelegramError as e:
        print(f'Error adding {username} to group: {e}')
