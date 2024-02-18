from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Define your Telegram Bot token here
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# Define the function to handle the /get_mp4 command
def get_mp4(update: Update, context: CallbackContext) -> None:
    # Replace CHANNEL_USERNAME with your channel username
    channel_username = 'CHANNEL_USERNAME'
    # Replace FILE_ID with the ID of the video file you want to convert
    file_id = 'FILE_ID'
    # Get the file object using the bot's get_file method
    file = context.bot.get_file(file_id)
    # Generate the direct link to the video file
    video_link = f"https://api.telegram.org/file/bot{TOKEN}/{file.file_path}"
    # Assuming the file is already in mp4 format, just return the link
    mp4_link = video_link
    # Send the mp4 link to the user
    update.message.reply_text(mp4_link)

# Set up the Telegram bot and add the command handler
def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("get_mp4", get_mp4))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
