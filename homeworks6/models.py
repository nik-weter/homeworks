# -*- coding: utf-8 -*-

__author__ = 'sobolevn'

from utils import get_input_function


class Storage(object):  # storage = Storge()
    obj = None

    items = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.items = []
        return cls.obj


class BaseItem(object):
    def __init__(self, heading):
        self.heading = heading
        self.done = False

    def __repr__(self):
        return self.__class__


    @classmethod
    def construct(cls):
        raise NotImplemented()


class ToDoItem(BaseItem):
    def __str__(self):
        if self.done == False:
            state = '-'
        else:
            state = '+'
        return 'ToDo: {} {}'.format(
            self.heading,
            state
        )

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        return ToDoItem(heading)


class ToBuyItem(BaseItem):
    def __init__(self, heading, price):
        super(ToBuyItem, self).__init__(heading)
        self.price = price
        self.done = False

    def __str__(self):
        if self.done == False:
            state = '-'
        else:
            state = '+'
        return 'ToBuy: {} for {} {}'.format(
            self.heading,
            self.price,
            state
        )

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        price = input_function('Input price: ')
        return ToBuyItem(heading, price)

class ToReadItem(BaseItem):
    def __init__(self, heading, url):
        super(ToReadItem, self).__init__(heading)
        self.url = url,
        self.done = False

    def __str__(self):
        if self.done == False:
            state = '-'
        else:
            state = '+'
        return 'ToRead: {} on {}'.format(
            self.heading,
            self.url,
            state
        )

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        url = input_function('Input url: ')
        return ToReadItem(heading, url)