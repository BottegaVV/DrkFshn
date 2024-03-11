import telebot
token = '7051873345:AAFKwCdeCb9OkpUFKU7HOYI1iaRbZbdRDqo'
bot = telebot.TeleBot(token)



markup2 = telebot.types.InlineKeyboardMarkup()

@bot.message_handler(commands=['start'])
def start (message):

    markup =telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = telebot.types.KeyboardButton('🧟Получить Шмотку')
    btn_2 = telebot.types.KeyboardButton('👔Мой Гардероб')
    btn_3 = telebot.types.KeyboardButton('🛍️Paris')
    markup.row (btn_1 , btn_2 )
    markup.row(btn_3)
    bot.send_message(message.chat.id, '🙆‍♂️ Wassup любители моды! Welcome to DRK!\n🧟 '
                                      'Эта игра сделана по мотивам высокой моды и не только!\n'
                                      '🛸 Собирай шмотки, дизайнеров, копи очки,создавай house с друзьями и обходи остальных в рейтинге и участвуй в конкурсах!\n'
                                      '🥷По-моему все очень просто и понятно, давай начинать!', reply_markup=markup )

    bot.register_next_step_handler(message , buttons)

def buttons (message):
    print('123')

    global markup2
    if message.text == 'Получить Шмотку':
        bot.send_message(message.chat.id, 'Получить Шмотку')

    elif message.text == 'Мой Гардероб':
        bot.send_message(message.chat.id, 'Мой Гардероб')

    elif message.text == '🛍️Paris':

        paris()
        bot.send_message(message.chat.id , '💭 Выберите действие по кнопкам ниже' , reply_markup=markup2)

def paris():
    global markup2
    markup2 = telebot.types.InlineKeyboardMarkup()
    markup2.add(telebot.types.InlineKeyboardButton('👔Avatar', callback_data='👔Avatar'))
    markup2.add(telebot.types.InlineKeyboardButton('📒Charts', callback_data='📒Charts'))
    markup2.add(telebot.types.InlineKeyboardButton('🔫House', callback_data='🔫House'))
    markup2.add(telebot.types.InlineKeyboardButton('🎰Casino', callback_data='🎰Casino'))
    markup2.add(telebot.types.InlineKeyboardButton('🧛Fashion Pass', callback_data='🧛Fashion Pass'))
    markup2.add(telebot.types.InlineKeyboardButton('🎭Trade', callback_data='🎭Trade'))
    markup2.add(telebot.types.InlineKeyboardButton('🛒Fashion Shop', callback_data='🛒Fashion Shop'))
    markup2.add(telebot.types.InlineKeyboardButton('🙋🏻‍♂️Реферальная программа', callback_data='🙋🏻‍♂️Реферальная программа'))








bot.infinity_polling()