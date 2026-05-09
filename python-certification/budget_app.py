class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount,
                'description': description
            })
            return True
        return False

    def get_balance(self):
        # total = 0
        # for item in self.ledger:
        #     total += item['amount']
        # return total

        return sum(item["amount"] for item in self.ledger)


    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # fill empty space with *
        # center the text with ^
        # make the total width 30 characters
        title = f"{self.name:*^30}\n"
        items = ""

        for item in self.ledger:
            desc = item['description'][:23]    # use 23 characters total
            amt = f"{item['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"    # left-align with < and right-alight with >

        total = f"Total: {self.get_balance():.2f}"

        return title + items + total

def create_spend_chart(categories):
    title = "Percentage spent by category\n"

    # Calculate spending per category
    spent = []

    for category in categories:
        # total = sum(
        #     -item["amount"]
        #     for item in cat.ledger
        #     if item["amount"] < 0
        # )
        # spent.append(total)

        total = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total += -item['amount']

        spent.append(total)

    total_spent = sum(spent)

    percentages = []

    for amount in spent:
        percent = int((amount / total_spent) * 100)
        percentages.append(percent // 10 * 10)    # Round number down to the nearest 10

    # Build chart
    chart = title

    for i in range(100, -1, -10):
        chart += f"{i:>3}| "    # right-align and take a width of 3 characters

        for p in percentages:
            if p >= i:
                chart += "o  "
            else:
                chart += "   "

        chart += "\n"

    # Bottom line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category names vertically
    names = [category.name for category in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        chart += "     "

        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "

        if i != max_len - 1:
            chart += "\n"

    return chart
    
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')
clothing.deposit(1000, 'initial deposit')
clothing.withdraw(230.15, 'supreme')
clothing.withdraw(112.15, 'sneaqkers')
clothing.withdraw(157.15, 'jackets')
food.transfer(50, clothing)

print(food)
print(clothing)

print(create_spend_chart([food, clothing]))

