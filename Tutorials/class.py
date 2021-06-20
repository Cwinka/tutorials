class Test():
    def __repr__(self):
        return 'check_class'
    def enter(self, word):
        if type(word) == str:
            return "string"
        elif type(word) == int or type(word) == float:
            return "float_or_integer"
        elif type(word) == list:
            return 'list'
        elif type(word) == dict:
            return 'dictionary'
        elif type(word) == tuple:
            return 'tuple'
        else:
            print(type(word))
            return "NoneType object or generator"
