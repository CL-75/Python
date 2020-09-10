class Store:
    def __init__(self, salary, bonusRate):
        self._salary = salary     # protected
        self.__bonusRate = bonusRate    # private
        
    def printBonusRate(self):
        print(self.__bonusRate)

    def salaryWithBonus(self):
        total = (self._salary * self.__bonusRate) + self._salary
        print(total)



A = Store(30000, .05)
print(A._salary)
A.printBonusRate()
A.salaryWithBonus()
