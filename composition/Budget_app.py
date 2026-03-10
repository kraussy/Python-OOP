class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = "" ):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):        
            self.ledger.append({'amount': -(amount), 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(entry["amount"] for entry in self.ledger)

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            other_category.deposit(amount, description=f"Transfer from {self.name}")
            self.withdraw(amount, description=f"Transfer to {other_category.name}")
            return True
        return False

       
        
    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False

    def __str__(self):
        title = f"{self.name:*^30}\n"
        datas = ""
        for data in self.ledger:
            description = data["description"][:23]
            amount = f"{data['amount']:.2f}"
            datas += f"{description:<23}{amount:>7}\n"
            
        
        total = f"Total: {self.get_balance():.2f}"
        return f"{title + datas + total}"

   
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food) 

clothing.withdraw(45, 'underwear shopping')

auto = Category('Auto')
clothing.transfer(5, auto)
auto.deposit(120, 'allowance from parents')
auto.withdraw(110, 'purchased bicycle')



def withdrawal_amount(category):
    total_withdraw = 0
    for withdrawals in category.ledger:
        if withdrawals["amount"] < 0:
            total_withdraw += withdrawals['amount']
    return abs(total_withdraw)
    


def create_spend_chart(categories):
    
    withdrawals = [withdrawal_amount(cat) for cat in categories]
    total = sum(withdrawals)

    percentages = [(int(w / total * 100) // 10) * 10 for w in withdrawals]

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for p in percentages:
            if p >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    names = [c.name for c in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        chart += "     "
        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip("\n")
        
    
    
    
    
print(create_spend_chart([food, clothing, auto])  ) 



#output
"""
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more food -15.89
Transfer to Clothing    -50.00
Total: 923.96

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60|          
 50|          
 40|       o  
 30| o     o  
 20| o  o  o  
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     

"""












