
# Protected class
class Store(self):
    def __init__(self, employee, salary):
        self._employee = employee
        self._salary = salary


# Not entirely sure of the how correct the code below is

# Private class
class Store2(self):
    def __init__(self, employee, salary):
        self.__employee = employee
        self.__salary = salary

    def getBonus(self, bonusRate, bonusAmt):
        self.__bonusRate = bonusRate
        bonusRate = .3
        self.__bonusAmt = bonusAmt
        bonusAmt = salary * bonusRate
        print(bonusAmt)


# Creating objects
e1 = Store("John", 10000)
e2 = Store("Mary", 12000)

e1=Store2("Sarah", 11500)
e2=Store2("Mark", 10050)
e1.getBonus()
e2.getBonus()

