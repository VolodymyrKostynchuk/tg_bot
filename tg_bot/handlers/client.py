from aiogram import types, Dispatcher
from create_bot import bot, dp  
from keyboards import kb_client
from keyboards import in_client
from database import sqlite_db


async def start_command(message:types.Message):
	text = 'Bot launched successfully!'
	await message.answer(text, reply_markup=kb_client)


async def address_command(message:types.Message):
	photo = open('D:\\Python\\tg_bot_kursova\\img\\photo_collage.jpg', 'rb')
	info_about_collage = '''Корпуси:
	2 корпус - вул. О. Кульчицької,2
	1 корпус - вул. Хуторівка, 15
	Для студентів які живуть у гуртожитку: 

	23 тролейбус,
	11 маршутка,
	131 маршутка,
	25 маршутка,
	22 тролейбус,
	14 маршутка,
	32 маршутка,
	287 маршутка.

	Сайт коледжу: '''
	href_site_collage = 'https://tc.lviv.ua/'

	await bot.send_photo(message.from_user.id, photo, info_about_collage)
	await message.answer(href_site_collage)


async def call_schedule_command(message:types.Message):
	call_schedule = '''Розклад дзвінків
	1 пара: 8:30-9:50
	2 пара: 10:00-11:20
	3 пара: 11:50-13:10
	4 пара - 13:20-14:40
	5 пара: 14:50-16:10
	6 пара: 16:30-17:50
	7 пара: 18:00-19:20

	Великі перерви після 2 пари (30 хв) і після 5 пари (20 хв)
	'''

	await message.answer(call_schedule)


async def list_of_teachers_command(message:types.Message):
	teachers_list = '''Директор – Костюк Іван Васильович
	Завідувач відділенням - Колосов Володимир Романович
	Голова комісії – Павліш Любов Михайлівна.
	 
	1.  Барахтян Олена Іванівна - операційні системи
	2.  Білінська Валентина Львівна – математика, вища математика
	3.  Боровик Юрій Іванович - фізична культура
	4.  Боценюк Мар'яна Юріївна - математика, вища математика, дискретна математика
	5.  Бучин Марія Миколаївна - математика, вища математика
	6.  Ващинський Віталій Михайлович - основи теорії електричних кіл
	7.  Гапаляк Зіновій Іванович - охорона праці 
	8.  Гембара Ганна Антонівна - математика, вища математика
	9.  Грабовенська Любов Володимирівна - технології, комп’ютерна графіка
	10.  Дерев'янченко Юрій Григорович – комп'ютерна схемотехніка
	11.  Драбік Наталія Василівна - біологія
	12.  Жарковська Ольга Романівна - біологія
	13.  Капарник Наталія Ярославівна - снови програмної індженарії
	14.  Климкович Тамара Анатоліївна - алгоритмізація та програмування
	15.  Ковтонюк Ольга Григорівна - організація баз даних та знань
	16.  Колосов Володимир Романович - мікропроцесорні системи
	17.  Корнілова Олена Сергіївна - екологія
	18.  Костюк Іван Васильович - практика 
	19.  Кулицька Тетяна Володимирівна - програмування, об’єктно-орієнтоване програмування
	20.  Леськів Володимир Володимирович - фізична культура
	21.  Макух Тетяна Володимирівна - фізика
	22.  Мельник Богдан Володимирович - практика
	23.  Николів Тарас Йосипович - фізична культура
	24.  Павліш Любов Михайлівна - теорія алгритмів, технологія створення програмних продуктів
	25.  Почтарук Микола Миколайович - системне програмування
	26.  Романко Світлана Миколаївна - охорона праці
	27.  Руц Сергій Іванович - комп’ютерна схемотехніка та архітектура комп’ютерів
	28.  Світлик Василь Володимирович – фізична культура
	29.  Семенюк Віра Володимирівна - фізична культура
	30.  Синюк Сергій Романович - архітектура комп’ютерів, технології захисту інформації
	31.  Сташків Наталія Вікторівна - хімія
	32.  Сявавко Ігор Євгенович - технології, комп’ютерні мережі
	33.  Талатура Володимир Васильович - захист України
	34.  Трухан Володимир Володимирович – фізична культура
	35.  Трухан Тарас Володимирович – фізична культура
	36.  Хамець Мар'яна Йосипівна - тестування програмних систем і комплексів, WEB-технології та WEB-дизайн
	37.  Штаюра Сесілія Мирославівна - фізика'''

	await message.answer(teachers_list)


async def list_of_students(message:types.Message):
	text = 'Виберіть відділення та групу'
	await message.answer(text, reply_markup=in_client.in_departament_student_button)

@dp.callback_query_handler(text_contains='departament_student_')
async def choise_departament(call:types.CallbackQuery):
	in_departament_1_button_text = 'Студенти відділення КН'
	in_departament_2_button_text = 'Студенти відділення КІ'
	choise_dep = call.data
	match choise_dep:
		case 'departament_student_1':
			await call.message.answer(in_departament_1_button_text, reply_markup=in_client.in_departament_student_1_button)
			await call.answer()
		case 'departament_student_2':
			await call.message.answer(in_departament_2_button_text, reply_markup=in_client.in_departament_student_2_button)
			await call.answer()


@dp.callback_query_handler(text_contains='group_student_')
async def send_schedule_group(call:types.CallbackQuery):
	name_photo = call.data 
	photo = open(f'D:\\Python\\tg_bot_kursova\\img\\{name_photo}.jpg', 'rb')
	await bot.send_photo(call.from_user.id, photo=photo)
	await call.answer()


async def schedule_of_couples_command(message:types.Message):
	text = 'Виберіть відділення та групу'
	await message.answer(text, reply_markup=in_client.in_departament_button)

@dp.callback_query_handler(text_contains='departament_schedule_')
async def choise_departament(call:types.CallbackQuery):
	in_departament_1_button_text = 'Розклад для відділення КН'
	in_departament_2_button_text = 'Розклад для відділення КІ'
	choise_dep = call.data
	match choise_dep:
		case 'departament_schedule_1':
			await call.message.answer(in_departament_1_button_text, reply_markup=in_client.in_departament_1_button)
			await call.answer()
		case 'departament_schedule_2':
			await call.message.answer(in_departament_2_button_text, reply_markup=in_client.in_departament_2_button)
			await call.answer()

@dp.callback_query_handler(text_contains='group_schedule_')
async def send_schedule_group(call:types.CallbackQuery):
	name_photo = call.data 
	photo = open(f'D:\\Python\\tg_bot_kursova\\img\\{name_photo}.jpg', 'rb')
	await bot.send_photo(call.from_user.id, photo=photo)
	await call.answer()

@dp.message_handler(commands=['Новини'])
async def show_news_command(message:types.Message):
	await sqlite_db.sql_read(message)


async def heads_of_diplom_command(message:types.Message):
	heads_of_diplom_list = '''Керівники диплому:
	1. Колосов Володимир Романович
	2. Костюк Іван Васильович 
	3. Ващинський Віталій Михайлович 
	4. Деревянченко Юрій Григорович
	5. Мандзевич Тарас Дмитрович
	6. Сявавко Ігор Євгенович
	7. Руц Сергій Іванович
	8. Синюк Сергій Романович
	9. Павліш Любов Михайлівна 
	10. Хамець Мар’яна Йосипівна
	11. Климкович Тамара Анатоліївна 
	12. Кулицька Тетяна Володимирівна 
	13. Капарник Наталія Ярославівна
	14. Грабовенська Любов Володимерівна 
	15. Барахтян Олена Іванівна
	16. Ковтонюк Ольга Григорівна
	17. Матвійків Світлана Володтмерівна 
	18. Почтарук Микола Миколайович''' 

	await message.answer(heads_of_diplom_list)
	
	
def register_handlers_client(dp:Dispatcher):
	dp.register_message_handler(start_command, commands=['start', 'help'])
	dp.register_message_handler(address_command, commands=['Адреса'])
	dp.register_message_handler(call_schedule_command, commands=['Розклад_дзвінків'])
	dp.register_message_handler(list_of_teachers_command, commands=['Список_викладачів'])
	dp.register_message_handler(list_of_students, commands=['Список_студентів'])
	dp.register_message_handler(schedule_of_couples_command, commands=['Розклад_пар'])
	dp.register_message_handler(show_news_command, commands=['Новини'])
	dp.register_message_handler(heads_of_diplom_command, commands=['Керівники_диплому'])