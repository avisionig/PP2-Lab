import string


class MyString:
    def __init__(self):
        self.string=""
    def get_string(self):
        self.string=input()
    def printString(self):
        print(self.string.upper())
string=MyString()
string.get_string()
string.printString()