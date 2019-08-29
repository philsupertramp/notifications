from telegram.ext import CommandHandler


class Command:
    def __init__(self, name, fun):
        self.name = name
        self.fun = fun

    def __call__(self, *args, **kwargs):
        return CommandHandler(self.name, self.fun)

