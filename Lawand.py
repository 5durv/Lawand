from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import yt_dlp
import os

# دالة لتحميل الأغنية
def download_song(url):
    options = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)

# دالة /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("أهلاً بك! أرسل لي رابط الأغنية التي تريد تحميلها.")

# دالة للتعامل مع الروابط
async def handle_message(update: Update, context: CallbackContext):
    url = update.message.text
    if "youtube.com" in url or "youtu.be" in url:
        await update.message.reply_text("جارٍ تحميل الأغنية، الرجاء الانتظار...")
        try:
            file_path = download_song(url)
            await update.message.reply_text("تم التحميل! جاري إرسال الملف...")
            await update.message.reply_audio(audio=open(file_path, 'rb'))
            os.remove(file_path)  # حذف الملف بعد الإرسال
        except Exception as e:
            await update.message.reply_text(f"حدث خطأ أثناء التحميل: {str(e)}")
    else:
        await update.message.reply_text("يرجى إرسال رابط YouTube صحيح.")

# إعداد البوت
def main():
    TOKEN = "7704199903:AAG6771iYMsZBVFp1Euer9RuT1fvu68bG7I"
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    os.makedirs("downloads", exist_ok=True)
    main()
