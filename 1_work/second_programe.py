class User:

    def __init__(self, first_name, second_name, e_mail, phone_number):
        self.first_name = first_name
        self.second_name = second_name
        self.e_mail = e_mail
        self.phone_number = phone_number

    def describr_user(self):
        print(f"Dane użytkownika:\n"
              f"Imię: {self.first_name}\n"
              f"Naswisko: {self.second_name}\n"
              f"E-mail: {self.e_mail}\n"
              f"Numer telefonu: {self.phone_number}")
    def greet_user(self):
        print(f"Witam {self.first_name} {self.second_name}")



moje_dane = User('Paweł',"Enerlich","pene@vp.pl", "734415712")
moje_dane.describr_user()
moje_dane.greet_user()