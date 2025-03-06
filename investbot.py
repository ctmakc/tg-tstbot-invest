import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, Message

# ВСТАВЬ СВОЙ ТОКЕН СЮДА
TOKEN = "7842175490:AAHkOVyDcWfDLK_kjpIxVCAsdMgllOc6aYA"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- КНОПКИ ---
menu_buttons = [
    [KeyboardButton(text="📢 Спикеры"), KeyboardButton(text="📅 Программа")],
    [KeyboardButton(text="📩 Контакт с админом"), KeyboardButton(text="📚 Обучение")],
    [KeyboardButton(text="🤝 Партнерство"), KeyboardButton(text="🏢 Инвестиции")]
]
main_menu = ReplyKeyboardMarkup(keyboard=menu_buttons, resize_keyboard=True)

# --- ОБРАБОТЧИКИ ---
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("👋 Привет! Добро пожаловать в инвестиционный бот. Давай зарегистрируемся!", 
                         reply_markup=ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Отправить номер телефона", request_contact=True)]], 
        resize_keyboard=True))

@dp.message(lambda message: message.contact)
async def register_user(message: Message):
    phone = message.contact.phone_number
    await message.answer(f"✅ Спасибо! Ваш номер {phone} зарегистрирован.", reply_markup=main_menu)
    logging.info(f"User {message.from_user.id} registered with phone {phone}")

@dp.message(lambda message: message.text == "📢 Спикеры")
async def speakers_info(message: Message):
    await message.answer("🎤 Наши эксперты: Иван Петров, Анна Смирнова, Майкл Джонс.")

@dp.message(lambda message: message.text == "📅 Программа")
async def program_info(message: Message):
    await message.answer("📆 Программа:\n- День 1: Введение в инвестирование\n- День 2: Анализ рынка недвижимости.")

@dp.message(lambda message: message.text == "📩 Контакт с админом")
async def contact_admin(message: Message):
    await message.answer("📬 Свяжитесь с администратором: @InvestAdmin")

@dp.message(lambda message: message.text == "📚 Обучение")
async def training_request(message: Message):
    await message.answer("📌 Ваша заявка на обучение принята! Мы свяжемся с вами.")
    logging.info(f"User {message.from_user.id} подал заявку на обучение")

@dp.message(lambda message: message.text == "🤝 Партнерство")
async def partnership_request(message: Message):
    await message.answer("✅ Ваша заявка на партнерство принята! Мы свяжемся с вами.")
    logging.info(f"User {message.from_user.id} подал заявку на партнерство")

@dp.message(lambda message: message.text == "🏢 Инвестиции")
async def investment_quiz(message: Message):
    await message.answer("💰 Пройдите короткий тест: \n1. В каком регионе хотите инвестировать?\n2. Какой у вас бюджет?")
    logging.info(f"User {message.from_user.id} начал квиз по инвестициям")

@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer("ℹ️ Этот бот помогает вам узнавать о спикерах, программе и оставлять заявки.")

@dp.message(Command("cancel"))
async def cancel_command(message: Message):
    await message.answer("❌ Действие отменено.", reply_markup=ReplyKeyboardRemove())

# --- ЗАПУСК БОТА ---
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())