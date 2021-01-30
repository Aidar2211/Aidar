class UserProfile:
    name = 'Aidar'
    phone_number = '+996707314048'
    password = 'ID1234567'


    def get_password(self):
        return self.password

    def get_phone_number(self):
        return self.phone_number

account = UserProfile ()
print(UserProfile.name, account.get_password(), account.get_phone_number())