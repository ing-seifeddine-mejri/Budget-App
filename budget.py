class Category:
  
  def __init__(self, category):
    self.category = category
    self.ledger = []

  #1. Deposit method
  def deposit(self, amount: float, description = None):
    if description == None:
      self.ledger.append({'amount':(amount), 'description': ''})
    else:
      self.ledger.append({'amount':(amount), 'description': (description)})  

  #2. Withdraw method
  def withdraw(self, amount: float, description = None):
    if self.check_funds(amount) == True:
      if description == None:
        self.ledger.append({'amount':-(amount), 'description':''})
      else:
        self.ledger.append({'amount':-(amount), 'description': (description)})   
      return True
    else:
      return False

  #3. Get balance method
  def get_balance(self):
    balance = 0
    for i in self.ledger:
      balance += i['amount']
    return balance  

  #4. Transfer method
  def transfer(self, amount: float, budget_category: str):
    if self.check_funds(amount) == True:
      self.withdraw(amount, f"Transfer to {budget_category.category}")
      budget_category.deposit(amount, f"Transfer from {self.category}")
      return True
    else:
      return False

  #5. Check funds method
  def check_funds(self, amount: float):
    return amount <= self.get_balance()  

  #Setting the display output 
  def __str__(self):
    category = self.category
    ln = category.center(30, '*') + '\n'
    for i in self.ledger:
      ln += f"{i['description'][:23].ljust(23)}"+ "{:.2f}".format(i['amount']).rjust(7) + "\n"
    total = self.get_balance()
    ln += "Total: " + "{:.2f}".format(total)
    return ln

#Spend chart

def create_spend_chart(categories):
  category_name = []
  spent_budget = []
  spent_percentage = []

#Calculating total for each category
  for category in categories:
    total = 0
    for i in category.ledger:
      if i['amount'] < 0:
        total -= i['amount']
    spent_budget.append(round(total, 2))
    category_name.append(category.category)

#Calculating percentages
  for amount in spent_budget:
    tot_spent = sum(spent_budget)
    spent_percentage.append(round(amount/ tot_spent, 2)* 100)

#Creating output display

  spend_chart = 'Percentage spent by category' + '\n'
  labels = range(100, -10, -10)
  
  for label in labels:
    spend_chart += str(label).rjust(3) + "| "
    for percent in spent_percentage:
      if percent >= label:
        spend_chart += 'o  '
      else:
        spend_chart += '   '
    spend_chart += '\n'

  spend_chart += "    ----" + ("---" * (len(category_name) - 1))
  spend_chart += '\n     '

 #Calculating spacing for names' output
  spacing = 0

  for name in category_name:
    if spacing < len(name):
      spacing = len(name)

  for i in range(spacing):
    for name in category_name:
      if len(name) > i:
        spend_chart += name[i] + '  '
      else:
        spend_chart += '   '
    if i < spacing-1:
      spend_chart += '\n     '

  return(spend_chart)    







