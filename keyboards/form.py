from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

form_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Контрактная"), KeyboardButton(text="Бюджетная")]
    ],
    resize_keyboard=True
)

confirm_form_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✅ Подтвердить форму обучения")],
        [KeyboardButton(text="✏️ Изменить форму обучения")]
    ],
    resize_keyboard=True
)