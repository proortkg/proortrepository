from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

faculty_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Лечебное дело"), KeyboardButton(text="Педиатрия")],
        [KeyboardButton(text="Стоматология"), KeyboardButton(text="Фармация")],
        [KeyboardButton(text="МПД"), KeyboardButton(text="Сестринское дело")],
        [KeyboardButton(text="Медицинская инженерия")]
    ],
    resize_keyboard=True
)

confirm_faculty_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✅ Подтвердить факультет")],
        [KeyboardButton(text="✏️ Изменить факультет")]
    ],
    resize_keyboard=True
)