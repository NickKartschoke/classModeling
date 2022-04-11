from distutils.archive_util import make_archive
from turtle import title
from unicodedata import name


class Animal:

    def __init__(self,name,age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self):
        self._age = age
        
    def move(self):
        print("Moving")

class Book():
    def __init__(self,title):
        self._title = title
        
    def get_title(self):
        return self._title

    def set_title(self):
        self._title = title

class Vehicle(object):
    def __init__(self,make,model,year):
        self._make = make
        self._model = model
        self._year = year
        
    def get_make(self):
        return self._make

    def set_make(self):
        self._make = make

    def get_model(self):
        return self._model

    def set_model(self):
        self._model = model

    def get_year(self):
        return self._year

    def set_year(self):
        self._year = year

    def move():
        print("Driving")