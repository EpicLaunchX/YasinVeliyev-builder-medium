class Burger:
    bread:str = "bread"
    patty:str="patty"
    sauce:str = 'sauce'
    toppings:list=[]


    def __str__(self):
        return f"Burger{{{self.bread}\n\t{self.sauce or "no sauce"}\n\t{self.patty}\n\t{self.toppings or "no toppings"}\n\t}}"


burger = Burger()

print(burger)