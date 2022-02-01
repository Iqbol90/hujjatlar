from loader import dp, bot
from aiogram.types import ContentType, Message
from pathlib import Path

# kerakli hujjatlar(rasm/audio/video/....) downloads/categories papkasiga tushadi
download_path=Path().joinpath("downloads", "categories")
download_path.mkdir(parents=True, exist_ok=True)
# parents=True --> bitta yuqoridagi papka, ya'ni yaratilishi kerak bo'lgan papkalar ketma-ket yaratishini bildiradi
# exist_ok=True --> bu papkalar qayta-qayta yaratilmasligi uchun

@dp.message_handler()
async def text_handler(message: Message):
    await message.reply("Siz matn yubordingiz")

@dp.message_handler(content_types=ContentType.DOCUMENT)
async def file_handler(message: Message):
    await message.document.download(destination=download_path)
    doc_id=message.document.file_id
    await message.reply("Siz hujjat yubordingiz\n" f"file_id= {doc_id}")

@dp.message_handler(content_types=ContentType.VIDEO)
async def video_handler(message: Message):
    await message.video.download(destination=download_path)
    await message.reply(f"file_id= {message.video.file_id}")

@dp.message_handler(content_types=ContentType.PHOTO)
async def photo_hadler(message: Message):
    await message.photo[-1].download(destination=download_path)
    await message.reply("Rasmqabul qilindi\n"
                        f"file_id={message.photo[-1].file_id}")

@dp.message_handler(content_types=ContentType.ANY)
async def any_handler(message: Message):
    await message.reply(f"{message.content_type} qabul qilindi")