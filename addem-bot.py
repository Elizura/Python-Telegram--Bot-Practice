import telegram
from telegram.error import TelegramError


# Replace YOUR_TOKEN with your Telegram bot token
bot = telegram.Bot(token='6224691866:AAHmB-2bhrh0KPwx0zXq3Qxk6NDHSUVWVsM')

# Replace GROUP_CHAT_ID with the ID of the Telegram group you want to add users to
group_chat_id = '8VK0zSTS6I9hYTNk'

# List of usernames to add to the group
usernames = ['@Q1d3r3r_P']

# Loop through the list of usernames and add each user to the group
for username in usernames:
    try:        
        bot.add_chat_member(cpihat_id=group_chat_id, username=username)
        print(f'{username} added to group successfully!')
    except TelegramError as e:
        print(f'Error adding {username} to group: {e}')
