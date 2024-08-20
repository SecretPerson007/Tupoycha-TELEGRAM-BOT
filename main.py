from telegram import Update
from telegram.ext import CommandHandler, Application, MessageHandler, filters, ContextTypes
from typing import Final
from datetime import date, datetime

TOKEN: Final = '7166055588:AAFq7SLr0rDJyu_HJmVLuLGBww4VhJ1odbQ'
BOT_USERNAME: Final = '@SecretPerson007_bot'

# Command Handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Salom, balalar!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Help kere bosa bzga ke!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Harhil custom!')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now()
    date_time = now.strftime("%m/%y, %H:%M:%S")
    await update.message.reply_text(date_time.title())

# Message Handler
def handle_response(text: str) -> str:
    if 'salom' in text.lower():
        return 'Vaalekum assalom!'
    return 'Cumadim.'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    response = handle_response(text)
    await update.message.reply_text(response)

if __name__ == '__main__':
    print('Starting the bot...')

    app = Application.builder().token(TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('time', time_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start polling
    print('Polling...')
    app.run_polling(poll_interval=3)
