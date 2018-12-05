#== mimiced from JKJ vid 2018_12_05 by tt ===
class InkBaby:
    def __init__(self, whob_name):
        self.name=whob_name
    def get_whob_name(self):
        return self.name
youb=InkBaby("SayWhat")
print ("who be me", youb.get_whob_name())
               
             
class CurrentAccount:
    def __init__(self, customer_name):
        self.name=customer_name
    def get_customer_name(self):
        return self.name
account_holder=CurrentAccount("Django_Jingo")
print("customer", account_holder.get_customer_name())
account_holder=CurrentAccount("Ringo_Bingo")
print("customer", account_holder.get_customer_name())
account_holder=CurrentAccount("Obligato_Delgatto")
print("hello world", account_holder.get_customer_name())
account_holder=CurrentAccount("Alien Creature")
print("OuterSpace", account_holder.get_customer_name())

