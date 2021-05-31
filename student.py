from typing import Sequence


class Student:

    __name = None
    __date = None
    __present = False
    __email = None
    __comments = None
    __arrival_time =None
    __last_teen = None
    __no_of_checks = None
    __joined = None
    __details = None

    def __init__(self):
        pass

    def get_email(self):
        return self.__email

    def set_email(self,email):
        self.__email = email
