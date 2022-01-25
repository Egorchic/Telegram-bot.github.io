import telebot
import config
import geo
import datab_statisctic
from telebot import types

i = {}
categ = {}
list_of_rests = {}
pos = {}
address = {}

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands = ['start'])
def welcome(massage):
	global i, categ
	i[massage.from_user.id] = 0
	sticker = open('C:/Users/egora/Desktop/Файлы/sticker.webp', 'rb')
	bot.send_sticker(massage.from_user.id, sticker)

	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	for c in config.categories:
		item = types.KeyboardButton(c)
		markup.add(item)

	bot.send_message(massage.from_user.id, 'Привет, я бот созданный для подбора ресторанов.'
										   'Итак, какие кухни и блюда предпочитаете🍽?', reply_markup = markup)


@bot.message_handler(content_types = ['text'])
def chat_categ(massage):
	global i
	global categ
	if massage.text in config.categories:
		if i[massage.from_user.id] == 0:
			loc_btn = types.KeyboardButton('Отправить геолокацию', request_location=True)
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			markup.add(loc_btn)

			categ[massage.from_user.id] = massage.text[:-1]
			bot.send_message(massage.from_user.id, 'Хорошо теперь отправьте свою геолокацию.', reply_markup = markup)
			bot.register_next_step_handler(massage, get_adress)

def get_adress(massage):
	try:
		global address

		lat = massage.location.latitude
		lon = massage.location.longitude
		address[massage.from_user.id] = (lat, lon)
		res = geo.distance(lon, lat, categ[massage.from_user.id])

		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		item1 = types.KeyboardButton('Следующий')
		item2 = types.KeyboardButton('Выбрать')
		markup.add(item1, item2)

		el = res[0]
		t = f'{el[2] / 4 * 60:.0f}'

		it = int(t)
		hours = it // 60
		minutes = it - (it // 60 * 60)

		bot.send_message(massage.from_user.id,
						 f'Название: {el[0]}\n'
						 f'Адресс: {el[1]}\n'
						 f'Расстояние: {f"{el[2]:.2f}"} км\n'
						 f'Премерное время пешком: {calc_time(hours, minutes)}',
						 reply_markup=markup)
		global pos
		pos[massage.from_user.id] = 0

		i[massage.from_user.id] += 1
		list_of_rests[massage.from_user.id] = res
		bot.register_next_step_handler(massage, send_next)

	except Exception:
		invalid_address(massage)

def send(massage):
	global list_of_rests

	try:
		nex = types.KeyboardButton('Следующий')
		prev = types.KeyboardButton('Предыдущий')
		chose = types.KeyboardButton('Выбрать')
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)

		spis = list_of_rests[massage.from_user.id]
		restoraunt = spis[pos[massage.from_user.id]]

		t = f'{restoraunt[2] / 4 * 60:.0f}'
		it = int(t)
		hours = it // 60
		minutes = it - (it//60*60)

		if pos[massage.from_user.id] == 0:
			markup.add(nex, chose)
			bot.send_message(massage.from_user.id, f'Название: {restoraunt[0]}\n'
												   f'Адресс: {restoraunt[1]}\n'
												   f'Расстояние: {f"{restoraunt[2]:.2f}"} км\n'
												   f'Премерное время пешком: {calc_time(hours, minutes)}',
							                       reply_markup = markup)
		else:
			markup.add(prev, nex, chose)
			bot.send_message(massage.from_user.id, f'Название: {restoraunt[0]}\n'
												   f'Адресс: {restoraunt[1]}\n'
												   f'Расстояние: {f"{restoraunt[2]:.2f}"} км\n'
												   f'Премерное время пешком: {calc_time(hours, minutes)}',
							                       reply_markup=markup)

		bot.register_next_step_handler(massage, send_next)

	except Exception:
		bot.send_message(massage.from_user.id, 'Ближайшие рестораны закончились')

def send_next(massage):
	if massage.text == 'Следующий':
		pos[massage.from_user.id] += 1
		send(massage)
	elif massage.text == 'Предыдущий':
		pos[massage.from_user.id] -= 1
		send(massage)
	elif massage.text == 'Выбрать':
		latlon = address[massage.from_user.id]
		spis = list_of_rests[massage.from_user.id]
		restoraunt = spis[pos[massage.from_user.id]]
		name = restoraunt[0]
		datab_statisctic.add(categ[massage.from_user.id], name, geo.get_region(latlon[0], latlon[1]))

		pos.pop(massage.from_user.id)
		list_of_rests.pop(massage.from_user.id)
		i.pop(massage.from_user.id)
		categ.pop(massage.from_user.id)

		gif = open('C:/Users/egora/Desktop/Файлы/gif_for_bot.mp4', 'rb')
		bot.send_video(massage.from_user.id, gif, None, 'Приятного аппетита!😎')
		gif.close()

def invalid_address(massage):
	bot.send_message(massage.from_user.id, 'Вы отправили несуществующий адресс. Отправьте другой.')
	bot.register_next_step_handler(massage, get_adress)

def calc_time(hours, minutes):
	if hours == 0 and minutes == 1:
		time = f'{minutes} минута'

	elif hours == 0 and minutes < 5:
		time = f'{minutes} минуты'

	elif hours == 0 and minutes > 4:
		time = f'{minutes} минуты'

	elif hours == 1 and minutes == 1:
		time = f'{hours} час, {minutes} минута'

	elif hours == 1 and minutes < 5:
		time = f'{hours} час, {minutes} минуты'

	elif hours == 1 and minutes > 4:
		time = f'{hours} час, {minutes} минут'

	elif hours < 5 and minutes == 1:
		time = f'{hours} часа, {minutes} минута'

	elif hours < 5 and minutes < 5:
		time = f'{hours} часа, {minutes} минуты'

	elif hours < 5 and minutes > 4:
		time = f'{hours} часа, {minutes} минут'

	elif hours > 4 and minutes == 1:
		time = f'{hours} часов, {minutes} минута'

	elif hours > 4 and minutes < 5:
		time = f'{hours} часов, {minutes} минуты'

	else:
		time = f'{hours} часов, {minutes} минут'

	return time

bot.polling()
