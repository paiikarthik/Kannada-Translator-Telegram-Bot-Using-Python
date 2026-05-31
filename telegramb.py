from telegram import Update #Update → contains message data from user
from telegram.ext import ApplicationBuilder, MessageHandler,CommandHandler, filters, ContextTypes #handles incoming messages decides which messages to process
from deep_translator import GoogleTranslator #translates text using deep-translator

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text(
        "ಸ್ವಾಗತ 👋\n ನನಗೆ  ಆಂಗ್ಲ ಭಾಷೆಯ ಪಠ್ಯ ಕಳುಹಿಸಿ, ನಾನು ಕನ್ನಡಕ್ಕೆ ಭಾಷಾಂತರಿಸುತ್ತೇನೆ."
    )
async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    translated = GoogleTranslator(source='en', target='kn').translate(text)

    await update.message.reply_text(translated)

app = ApplicationBuilder().token("//your token //changed token").build()

app.add_handler(CommandHandler("start",start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate))

app.run_polling()
