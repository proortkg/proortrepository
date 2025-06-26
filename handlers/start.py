from aiogram import Router, F, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from states import UserStates
from keyboards.region import region_keyboard, confirm_region_keyboard
from keyboards.faculties import faculty_keyboard, confirm_faculty_keyboard
from keyboards.form import form_keyboard, confirm_form_keyboard

router = Router()


# ──────────────────────────────────────────────
# 1. Команда /start погнали
@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("👋 Добро пожаловать!\nКак к вам можно обращаться?")
    await state.set_state(UserStates.waiting_for_name)


# ──────────────────────────────────────────────
# 2. Ввод имени
@router.message(UserStates.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    name = message.text.strip()
    await state.update_data(temp_name=name)

    await message.answer(
        f"Вы указали имя: {name}",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="✅ Подтвердить имя")],
                [KeyboardButton(text="✏️ Изменить имя")]
            ],
            resize_keyboard=True
        )
    )
    await state.set_state(UserStates.confirming_name)


# ──────────────────────────────────────────────
# 3. Подтверждение имени
@router.message(UserStates.confirming_name)
async def confirm_or_edit_name(message: Message, state: FSMContext):
    text = message.text.strip()

    if text == "✅ Подтвердить имя":
        data = await state.get_data()
        confirmed_name = data.get("temp_name")
        await state.update_data(name=confirmed_name)

        await message.answer(
            f"Приятно познакомиться, {confirmed_name}!\n\nТеперь выберите категорию вашего сертификата:",
            reply_markup=region_keyboard
        )
        await state.set_state(UserStates.waiting_for_region)

    elif text == "✏️ Изменить имя":
        await message.answer("Пожалуйста, введите имя ещё раз:")
        await state.set_state(UserStates.waiting_for_name)


# ──────────────────────────────────────────────
# 4. Выбор региона
@router.message(UserStates.waiting_for_region)
async def process_region(message: Message, state: FSMContext):
    region = message.text.strip()
    await state.update_data(temp_region=region)

    await message.answer(
        f"Вы выбрали: {region}",
        reply_markup=confirm_region_keyboard
    )
    await state.set_state(UserStates.confirming_region)


# ──────────────────────────────────────────────
# 5. Подтверждение региона
@router.message(UserStates.confirming_region)
async def confirm_region(message: Message, state: FSMContext):
    text = message.text.strip()
    data = await state.get_data()

    if text == "✅ Подтвердить регион":
        confirmed_region = data.get("temp_region")
        await state.update_data(region=confirmed_region)

        await message.answer(
            f"Категория сертификата подтверждена: {confirmed_region}\n\nТеперь выберите факультет:",
            reply_markup=faculty_keyboard
        )
        await state.set_state(UserStates.waiting_for_faculty)

    elif text == "✏️ Изменить регион":
        await message.answer("Выберите регион заново:", reply_markup=region_keyboard)
        await state.set_state(UserStates.waiting_for_region)


# ──────────────────────────────────────────────
# 6. Выбор факультета
@router.message(UserStates.waiting_for_faculty)
async def process_faculty(message: Message, state: FSMContext):
    faculty = message.text.strip()
    await state.update_data(temp_faculty=faculty)

    await message.answer(
        f"Вы выбрали факультет: {faculty}",
        reply_markup=confirm_faculty_keyboard
    )
    await state.set_state(UserStates.confirming_faculty)


# ──────────────────────────────────────────────
# 7. Подтверждение факультета
@router.message(UserStates.confirming_faculty)
async def confirm_faculty(message: Message, state: FSMContext):
    text = message.text.strip()
    data = await state.get_data()

    if text == "✅ Подтвердить факультет":
        confirmed_faculty = data.get("temp_faculty")
        await state.update_data(faculty=confirmed_faculty)

        await message.answer(
            f"Факультет подтверждён: {confirmed_faculty}\n\nТеперь выберите форму обучения:",
            reply_markup=form_keyboard
        )
        await state.set_state(UserStates.waiting_for_form)

    elif text == "✏️ Изменить факультет":
        await message.answer("Выберите факультет заново:", reply_markup=faculty_keyboard)
        await state.set_state(UserStates.waiting_for_faculty)


# ──────────────────────────────────────────────
# 8. Выбор формы обучения
@router.message(UserStates.waiting_for_form)
async def process_form(message: Message, state: FSMContext):
    form = message.text.strip()
    await state.update_data(temp_form=form)

    await message.answer(
        f"Вы выбрали форму обучения: {form}",
        reply_markup=confirm_form_keyboard
    )
    await state.set_state(UserStates.confirming_form)


# ──────────────────────────────────────────────
# 9. Подтверждение формы обучения
@router.message(UserStates.confirming_form)
async def confirm_form(message: Message, state: FSMContext):
    text = message.text.strip()
    data = await state.get_data()

    if text == "✅ Подтвердить форму обучения":
        confirmed_form = data.get("temp_form")
        await state.update_data(form=confirmed_form)

        await message.answer(
            f"Форма обучения подтверждена: {confirmed_form}\n\nТеперь введите балл за основной тест (от 110 до 245):",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.set_state(UserStates.waiting_for_scores)

    elif text == "✏️ Изменить форму обучения":
        await message.answer("Выберите форму обучения заново:", reply_markup=form_keyboard)
        await state.set_state(UserStates.waiting_for_form)

# ──────────────────────────────────────────────
# 10. Ввод баллов за основной тест
@router.message(UserStates.waiting_for_scores)
async def process_main_score(message: Message, state: FSMContext):
    try:
        main_score = int(message.text.strip())
    except ValueError:
        await message.answer("Пожалуйста, введите число от 110 до 245.")
        return

    if main_score < 110:
        await message.answer(
            "❌ К сожалению, вы не набрали минимальный порог по основному тесту (110 баллов).\n"
            "Вы не можете участвовать в конкурсе. "
            "Если вам нужна помощь — напишите нашему консультанту: @your_consultant_username"
        )
        return

    await state.update_data(main_score=main_score)
    await message.answer("✅ Основной тест сохранён. Теперь введите балл за химию:")
    await state.set_state(UserStates.waiting_for_chemistry)


# ──────────────────────────────────────────────
# 11. Ввод баллов за химию
@router.message(UserStates.waiting_for_chemistry)
async def process_chem_score(message: Message, state: FSMContext):
    try:
        chem_score = int(message.text.strip())
    except ValueError:
        await message.answer("Пожалуйста, введите число от 60 до 150.")
        return

    if chem_score < 60:
        await message.answer(
            "❌ К сожалению, вы не набрали минимальный порог по химии (60 баллов).\n"
            "Вы не можете участвовать в конкурсе. "
            "Если вам нужна помощь — напишите нашему консультанту: @your_consultant_username"
        )
        return

    await state.update_data(chem_score=chem_score)
    await message.answer("✅ Химия сохранена. Теперь введите балл за биологию:")
    await state.set_state(UserStates.waiting_for_biology)


# ──────────────────────────────────────────────
# 12. Ввод баллов за биологию
@router.message(UserStates.waiting_for_biology)
async def process_bio_score(message: Message, state: FSMContext):
    try:
        bio_score = int(message.text.strip())
    except ValueError:
        await message.answer("Пожалуйста, введите число от 60 до 150.")
        return

    if bio_score < 60:
        await message.answer(
            "❌ К сожалению, вы не набрали минимальный порог по биологии (60 баллов).\n"
            "Вы не можете участвовать в конкурсе. "
            "Если вам нужна помощь — напишите нашему консультанту: @your_consultant_username"
        )
        return

    await state.update_data(bio_score=bio_score)
    await message.answer("✅ Все баллы успешно сохранены!\n\nТеперь бот рассчитает ваши шансы...")

    # 👉 здесь будет переход к модулю расчёта
    # from logic.shans import calculate_shans()
    # await calculate_shans(...)

    await state.clear()