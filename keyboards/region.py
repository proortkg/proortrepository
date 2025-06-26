from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

region_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🟥 Бишкек (город)"),
            KeyboardButton(text="🟦 Малый город")
        ],
        [
            KeyboardButton(text="🟨 Село"),
            KeyboardButton(text="🟪 Высокогорье")
        ]
    ],
    resize_keyboard=True
)

confirm_region_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✅ Подтвердить регион")],
        [KeyboardButton(text="✏️ Изменить регион")]
    ],
    resize_keyboard=True
)