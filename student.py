class Student:
    __roll_no = None
    __name = None
    __gmeet_names = []

    def __init__(self,roll_no,name,gmeet_names):
        self.__roll_no = roll_no
        self.__name = name
        self.__gmeet_names = gmeet_names

    def get_roll_no(self):
        return self.__roll_no
    
    def get_name(self):
        return self.__name

    def get_gmeet_names(self):
        return self.__gmeet_names

    def set_roll_no(self,roll_no):
        self.__roll_no = roll_no
    
    def set_name(self,name):
        self.__name = name
    
    def set_gmeet_names(self,gmeet_names):
        self.__gmeet_names = gmeet_names