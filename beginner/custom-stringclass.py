class Input_Out_String:
    def __init__(self):
        self.__string = ''

    def get_string(self):
        self.__string = input()

    def print_string(self):
        print(self.__string.upper())


string_object = Input_Out_String()
string_object.get_string()
string_object.print_string()
