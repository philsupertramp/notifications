import json
import re
from commands.weather import Weather


def get_message(update):
    text = update.message['text']
    text = re.sub(r'/\w*', '', text)
    return re.sub(r'^[ \t]+', '', text)


def start(bot, update):
    user = update.message.from_user
    update.message.reply_text(
        f'Hey {user.first_name},\nthanks for choosing GoodMorningSunshine for being your trusted source of daily '
        f'information.'
    )
    print(user)


def hello(bot, update):
    username = update.message.from_user.first_name
    update.message.reply_text(
        'Hello {}, how can I serve you?'.format('babes :kissing_heart:' if username == 'Roberta' else username))


def morning(bot, update):
    pass


def weather(bot, update):
    clients_weather = Weather('Berlin', 'de')
    update.message.reply_text(
        f'Hey {update.message.from_user.first_name}, \n'
        + f'sorry for my late response. I\'ve been working for some time '
        + f'fulfilling other users requests. {"good" if clients_weather.is_good() else "bad"} '
        + f'right now. Current temp: {str(clients_weather.current_temp)}°C'
    )


def help(bot, update):
    update.message.reply_text(
        '/help    : This message.\n'
        '/start   : Sign up for the bot\'s service.\n'
        '/morning : Coming soon.\n'
        '/weather : Coming sooner!\n'
        '/income  : Keep track of your income\n'
        '/outflow : Keep track of your financial state\n'
        '/balance : Keep track of your total balance\n'
    )


def income(bot, update):
    user = update.message.from_user['id']
    userfile = f'../userdata/{user}.json'
    addend = float(get_message(update) or 0)
    with open(userfile, 'r') as file:
        content = json.load(file)

    inc = float(content['income'] or 0)
    total_income = inc + addend

    content.update({'income': total_income})
    with open(userfile, 'w') as file:
        file.write(json.dumps(content))

    update.message.reply_text(
        f'Your current income is {total_income}. \n'
        f'This results in a total balance of {total_income - content["outflow"]}.'
    )


def outflow(bot, update):
    user = update.message.from_user['id']
    userfile = f'../userdata/{user}.json'
    addend = float(get_message(update) or 0)
    with open(userfile, 'r') as file:
        content = json.load(file)

    inc = float(content['outflow'] or 0)
    total_income = inc + addend

    content.update({'outflow': total_income})
    with open(userfile, 'w') as file:
        file.write(json.dumps(content))

    update.message.reply_text(
        f'Your current outflow is {total_income}. \n'
        f'This results in a total balance of {total_income - content["outflow"]}.'
    )


def balance(bot, update):
    user = update.message.from_user['id']
    userfile = f'../userdata/{user}.json'
    with open(userfile, 'r') as file:
        content = json.load(file)
    update.message.reply_text(
        f'This results in a total balance of {content["income"] - content["outflow"]}.'
    )
