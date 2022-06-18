from create_bot import dp, bot   

import sqlite3 as sq   

def sql_start():
	global base, cur  
	base = sq.connect('news.db')
	cur = base.cursor()
	if base:
		print('Data base connected OK!')
	base.execute('CREATE TABLE IF NOT EXISTS news(img TEXT, name PRIMARY KEY, article TEXT)')
	base.commit()


async def sql_add_command(state):
	async with state.proxy() as data:
		cur.execute('INSERT INTO news VALUES (?, ?, ?)', tuple(data.values()))
		base.commit()


async def sql_read(message):
	for ret in cur.execute('SELECT * FROM news').fetchall():
		await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n {ret[2]}\n')


async def sql_read2():
	return cur.execute('SELECT * FROM news').fetchall()


async def sql_delete_command(data):
	cur.execute('DELETE FROM news WHERE name == ?', (data,))
	base.commit()
	