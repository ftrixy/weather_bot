from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btnMain = KeyboardButton('Головне меню')

# ----- Меню бота ----- #

btnCity1 = KeyboardButton('Київ')
btnCity2 = KeyboardButton('Жашків')
btnCity3 = KeyboardButton('Олевськ')
btnCity4 = KeyboardButton('Маневичі')
btnCity5 = KeyboardButton('Дзвінкове')
btnCity6 = KeyboardButton('Гребінка')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCity1, btnCity2, btnCity3, btnCity4, btnCity5, btnCity6)

# ----- Інше меню ------ #

