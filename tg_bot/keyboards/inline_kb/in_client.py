from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


in_departament_1 = InlineKeyboardButton(text='КН', callback_data='departament_schedule_1')
in_departament_2 = InlineKeyboardButton(text='КІ', callback_data='departament_schedule_2')

in_departament_button = InlineKeyboardMarkup(row_width=1).add(in_departament_1, in_departament_2)

in_departament_1_group_1 = InlineKeyboardButton(text='КН-11', callback_data='group_schedule_1')
in_departament_1_group_2 = InlineKeyboardButton(text='КН-12', callback_data='group_schedule_2')
in_departament_1_group_3 = InlineKeyboardButton(text='КН-21', callback_data='group_schedule_3')
in_departament_1_group_4 = InlineKeyboardButton(text='КН-22', callback_data='group_schedule_4')
in_departament_1_group_5 = InlineKeyboardButton(text='КН-31', callback_data='group_schedule_5')
in_departament_1_group_6 = InlineKeyboardButton(text='КН-32', callback_data='group_schedule_6')
in_departament_1_group_7 = InlineKeyboardButton(text='КН-41', callback_data='group_schedule_7')
in_departament_1_group_8 = InlineKeyboardButton(text='КН-42', callback_data='group_schedule_8')

in_departament_2_group_9 = InlineKeyboardButton(text='КІ-11', callback_data='group_schedule_9')
in_departament_2_group_10 = InlineKeyboardButton(text='КІ-12', callback_data='group_schedule_10')
in_departament_2_group_11 = InlineKeyboardButton(text='КІ-13', callback_data='group_schedule_11')
in_departament_2_group_12 = InlineKeyboardButton(text='КІ-21', callback_data='group_schedule_12')
in_departament_2_group_13 = InlineKeyboardButton(text='КІ-22', callback_data='group_schedule_13')
in_departament_2_group_14 = InlineKeyboardButton(text='КІ-23', callback_data='group_schedule_14')
in_departament_2_group_15 = InlineKeyboardButton(text='КІ-31', callback_data='group_schedule_15')
in_departament_2_group_16 = InlineKeyboardButton(text='КІ-32', callback_data='group_schedule_16')
in_departament_2_group_17 = InlineKeyboardButton(text='КІ-41', callback_data='group_schedule_17')
in_departament_2_group_18 = InlineKeyboardButton(text='КІ-42', callback_data='group_schedule_1')


in_departament_1_button = InlineKeyboardMarkup(row_width=1).add(
	in_departament_1_group_1,
	in_departament_1_group_2,
	in_departament_1_group_3,
	in_departament_1_group_4,
	in_departament_1_group_5,
	in_departament_1_group_6,
	in_departament_1_group_7,
	in_departament_1_group_8,
	)

in_departament_2_button = InlineKeyboardMarkup(row_width=1).add(
	in_departament_2_group_9,
	in_departament_2_group_10,
	in_departament_2_group_11,
	in_departament_2_group_12,
	in_departament_2_group_13,
	in_departament_2_group_14,
	in_departament_2_group_15,
	in_departament_2_group_16,
	in_departament_2_group_17,
	in_departament_2_group_18,
	)


in_departament_student_1 = InlineKeyboardButton(text='КН', callback_data='departament_student_1')
in_departament_student_2 = InlineKeyboardButton(text='КІ', callback_data='departament_student_2')

in_departament_student_button = InlineKeyboardMarkup(row_width=1).add(in_departament_student_1, in_departament_student_2)


in_departament_1_student_group_1 = InlineKeyboardButton(text='КН-11', callback_data='group_student_1')
in_departament_1_student_group_2 = InlineKeyboardButton(text='КН-12', callback_data='group_student_2')
in_departament_1_student_group_3 = InlineKeyboardButton(text='КН-21', callback_data='group_student_3')
in_departament_1_student_group_4 = InlineKeyboardButton(text='КН-22', callback_data='group_student_4')
in_departament_1_student_group_5 = InlineKeyboardButton(text='КН-31', callback_data='group_student_5')
in_departament_1_student_group_6 = InlineKeyboardButton(text='КН-32', callback_data='group_student_6')
in_departament_1_student_group_7 = InlineKeyboardButton(text='КН-41', callback_data='group_student_7')
in_departament_1_student_group_8 = InlineKeyboardButton(text='КН-42', callback_data='group_student_8')

in_departament_2_student_group_9 = InlineKeyboardButton(text='КІ-11', callback_data='group_student_9')
in_departament_2_student_group_10 = InlineKeyboardButton(text='КІ-12', callback_data='group_student_10')
in_departament_2_student_group_11 = InlineKeyboardButton(text='КІ-13', callback_data='group_student_11')
in_departament_2_student_group_12 = InlineKeyboardButton(text='КІ-21', callback_data='group_student_12')
in_departament_2_student_group_13 = InlineKeyboardButton(text='КІ-22', callback_data='group_student_13')
in_departament_2_student_group_14 = InlineKeyboardButton(text='КІ-23', callback_data='group_student_14')
in_departament_2_student_group_15 = InlineKeyboardButton(text='КІ-31', callback_data='group_student_15')
in_departament_2_student_group_16 = InlineKeyboardButton(text='КІ-32', callback_data='group_student_16')
in_departament_2_student_group_17 = InlineKeyboardButton(text='КІ-41', callback_data='group_student_17')
in_departament_2_student_group_18 = InlineKeyboardButton(text='КІ-42', callback_data='group_student_18')


in_departament_student_1_button = InlineKeyboardMarkup(row_width=1).add(
	in_departament_1_student_group_1,
	in_departament_1_student_group_2,
	in_departament_1_student_group_3,
	in_departament_1_student_group_4,
	in_departament_1_student_group_5,
	in_departament_1_student_group_6,
	in_departament_1_student_group_7,
	in_departament_1_student_group_8,
	)

in_departament_student_2_button = InlineKeyboardMarkup(row_width=1).add(
	in_departament_2_student_group_9,
	in_departament_2_student_group_10,
	in_departament_2_student_group_11,
	in_departament_2_student_group_12,
	in_departament_2_student_group_13,
	in_departament_2_student_group_14,
	in_departament_2_student_group_15,
	in_departament_2_student_group_16,
	in_departament_2_student_group_17,
	in_departament_2_student_group_18,
	)

