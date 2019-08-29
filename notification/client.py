import os

from telegram.ext import Updater
from environs import Env

from commands import funs
from commands.command import Command

env = Env()
env.read_env()


class Client(Updater):
    COMMANDS = [
        Command('hello', funs.hello),
        Command('start', funs.start),
        Command('morning', funs.morning),
        Command('weather', funs.weather),
        Command('help', funs.help),
        Command('income', funs.income),
        Command('outflow', funs.outflow),
        Command('balance', funs.balance)
    ]

    def __init__(self, **kwargs):
        super().__init__(token=os.environ.get('TELEGRAM_KEY', 'XXX'), **kwargs)
        self.__init_client()

    def __init_client(self):
        for command in self.COMMANDS:
            self.__add_command(command())

    def __add_command(self, command):
        self.dispatcher.add_handler(command)

    def run(self):
        self.start_polling()
        self.idle()


def main():
    updater = Client()

    updater.run()
    print('run')


if __name__ == '__main__':
    main()
