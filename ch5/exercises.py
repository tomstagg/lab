#!/usr/bin/env python3
import os

class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self.name = name

# c = Color('#ff0000', 'bright red')
# print (c.name)
# c.name = 'red'


class Color2:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception('Invalid Name')
        self._name = name

    def _get_name(self):
        return self._name

    name = property(_get_name, _set_name)


class Silly:
    def _get_silly(self):
        print('you are getting silly')
        return self._silly

    def _set_silly(self,  value):
        print('you are making silly {}'.format(value))
        self._silly = value

    def _del_silly(self):
        print('you killed silly!')
        del self._silly

    silly = property(_get_silly, _set_silly, _del_silly, 'this is a silly property')


class Silly2:
    @property
    def silly(self):
        '''This is a silly property'''
        print('you are getting silly')
        return self._silly

    @silly.setter
    def silly(self,  value):
        print('you are making silly {}'.format(value))
        self._silly = value

    @silly.deleter
    def silly(self):
        print('you killed silly!')
        del self._silly

from urllib.request import urlopen


class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print('retrieving new page...')
            self._content = urlopen(self.url).read()
        return self._content

# wp = WebPage('http://google.com')
# c = wp.content
# c2 = wp.content
# c == c2


class AverageList(list):
    @property
    def average(self):
        return sum(self) / len(self)

    def calc_average(self):
        return sum(self) / len(self)










