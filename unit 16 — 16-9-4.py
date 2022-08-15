class Klient:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'"{self.name} {self.surname}.{self.city}.Баланс: {self.balance} руб."'


    def get_list (self):
        return f'"{self.name} {self.surname}.{self.city}"'


klient_1 = Klient("Иван","Петров","Москва",50)
klient_2 = Klient("Семен","Иванов","Москва",70)
klient_3 = Klient("Петр","Смирнов","Уфа",150)
klient_4 = Klient("Николай","Семенов","Пенза",600)

print("\n",klient_1,"\n",klient_2,"\n",klient_3,"\n",klient_4,"\n")

klient_list=[klient_1,klient_2,klient_3,klient_4]


for klient in klient_list:
    print(klient.get_list())