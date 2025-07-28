user_info = {
    'age': 20,
    'name': 'Hung'
}
class user:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def on_screen(self):
        print(self.__name, self.__age)


    