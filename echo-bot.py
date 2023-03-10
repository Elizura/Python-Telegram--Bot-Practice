
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:    
    user = update.effective_user
    await update
    await update.message.reply_text(
        f"Hi {user.mention_html()}!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:    
    await update.message.reply_text("This is the Helper!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:     
    await update.message.reply_text(update.message.text)

def main() -> None:        
    application = Application.builder().token("5635774650:AAHEOuzEtmIA0ZXQY81zY7cPqDzGZofSLDQ").build()    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))    
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))    
    application.run_polling()


if __name__ == "__main__":
    main()