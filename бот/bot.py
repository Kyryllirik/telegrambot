import telebot
import config
import random


from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Новини зі старостату")
    item2 = types.KeyboardButton("Список підручників")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Вас вітає телеграм бот 10-Б класу Першої міської гімназії."
    .format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup )

    @bot.message_handler(content_types=['text'])
    def lalala(message):
        if message.chat.type == 'private':
            if message.text == 'Новини зі старостату':
                bot.send_message(message.chat.id, 'Носити маски.\n У четвер збір макулатури. \n ')
            elif message.text == 'Список підручників':
                bot.send_message(message.chat.id, '<a href="https://pidruchnyk.com.ua/1130-biologiya-ekologiya-10-klas-sobol.html">Біологія</a> \n <a href="https://pidruchnyk.com.ua/1184-geografiya-10-klas-boyko.html">Географія</a> \n <a href="https://pidruchnyk.com.ua/1186-gromadyanska-osvita-10-klas-bakka.html"> Громадянська освіта</a> \n <a href="https://pidruchnyk.com.ua/410-svtova-lteratura-kovbasenko-10-klas.html">Зарубіжна література </a> \n <a href="https://pidruchnyk.com.ua/434-nformatika-rven-standartu-rivknd-lisenko-chernkova-shakotko-10-klas.html">Інформатика </a> \n <a href="https://pidruchnyk.com.ua/1124-spanska-6-redko-10-klas.html">Іспанська мова</a> \n <a href="https://lib.imzo.gov.ua/wa-data/public/site/books2/pidruchnyky-10-klas-2018/06-istoriya-ukraina-i-svit-10-klas/istoriia-ukraina-i-svit-riven-standartu-pidruchnyk-dlia-10-klasu-zzso-hisem.pdf">Історія</a> \n <a href="https://pidruchnyk.com.ua/1154-matematyka-10-klas-ister.html">Математика</a> \n <a href="https://pidruchnyk.com.ua/395-tehnologyi-kobernik-tereschuk-gervas-10-klas.html">Технології</a> \n <a href="https://pidruchnyk.com.ua/392-ukrayinska-lteratura-avramenko-paharenko-10-klas.html">Українська література</a> \n <a href="https://pick.net.ua/ru/10-class/2199-ukrainska-mova">Українська мова</a> \n <a href="https://uchebniki-online.net/435-fizika-10-klass-baryahtar.html">Фізика</a> \n <a href="https://pidruchnyk.com.ua/380-himiya-yaroshenko-10-klas.html">Хімія</a>' .format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup )


bot.polling(none_stop=True)
