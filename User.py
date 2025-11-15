class User:
    def __init__(self, name, email_address, dl_num):
        self.name = name
        self.email_address = email_address
        self.dl_num = dl_num 
    def __str__(self):
        return(f'The user name is {self.name}, and their email address is {self.email_address}. The DL# is {self.dl_num}')

logan = User("Logan", "address@email.com", 123123123) 
print(logan)

notlogan = User("notlogan", "address2@email.com", 987987987)
print(notlogan)