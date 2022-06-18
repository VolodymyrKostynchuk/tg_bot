from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from create_bot import dp, bot   
from database import sqlite_db
from keyboards import kb_admin
from keyboards import kb_client

ID = None


class FSMAdmin(StatesGroup):
	photo = State()
	name = State()
	article = State()


async def make_change_command(message:types.Message):
	global ID 
	ID = message.from_user.id  
	happy_message = '''Вітаю вас назначено адміністратором бота
	Права:
	Добавляти та видаляти новини які зберігаються у боті
	Щоб добавити новину напишіть комунду /Загрузити'''
	await bot.send_message(message.from_user.id, happy_message, reply_markup=kb_admin)


async def cm_start(message:types.Message, state=FSMContext):
	if message.from_user.id == ID: 
		await FSMAdmin.photo.set()
		await message.answer('Загрузіть фото', reply_markup=kb_admin)

async def cancle_handler(message:types.Message, state:FSMContext):
	if message.from_user.id == ID:
		currecnt_state = await state.get_state()
		if currecnt_state is None:
			return  
		await state.finish()
		await message.answer('Відмінено!')


async def comeback_command(message:types.Message):
	come_back = 'Головне меню'
	await message.answer(come_back, reply_markup=kb_client)


async def load_photo(message:types.Message, state=FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['photo'] = message.photo[0].file_id
		await FSMAdmin.next()
		await message.answer('Ввседіть назву новини:')


async def load_name(message:types.Message, state=FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['name'] = message.text 

		await FSMAdmin.next()
		await message.answer('Введіть статтю новини:')


async def load_acticle(message:types.Message, state=FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['article'] = message.text  

		await sqlite_db.sql_add_command(state)
		await message.answer('Новину успішно додано')
		await state.finish()

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
	await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
	await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} видалено. ', show_alert=True)

@dp.message_handler(commands='Видалити')
async def delete_item(message:types.Message):
	if message.from_user.id == ID:
		read = await sqlite_db.sql_read2()
		for ret in read:
			await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n {ret[2]}\n')
			await bot.send_message(message.from_user.id, text='^^^^^^^^', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Видалити {ret[1]}', callback_data=f'del {ret[1]}')))
def register_handlers_admin(dp:Dispatcher):
	dp.register_message_handler(cm_start, commands=['Загрузити'], state=None)
	dp.register_message_handler(cancle_handler, state="*", commands=['Відміна'])
	dp.register_message_handler(cancle_handler, Text(equals='Відміна', ignore_case=True), state="*")
	dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
	dp.register_message_handler(load_name, state=FSMAdmin.name)
	dp.register_message_handler(load_acticle, state=FSMAdmin.article)
	dp.register_message_handler(make_change_command, commands=['get_admin'], is_chat_admin=True)
	dp.register_message_handler(comeback_command, commands=['Повернутись'])
