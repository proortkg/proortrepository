from aiogram.fsm.state import StatesGroup, State

class UserStates(StatesGroup):
    waiting_for_name = State()
    confirming_name = State()

    waiting_for_region = State()
    confirming_region = State()

    waiting_for_faculty = State()
    confirming_faculty = State()

    waiting_for_form = State()
    confirming_form = State()

    waiting_for_scores = State()

    waiting_for_chemistry = State()
    waiting_for_biology = State()
