class Atm():
	def __init__(self, balance, bank_name):
		self.balance = balance
		self.bank_name = bank_name
	
	def withdraw(self, request):
		balance = self.balance
		print ("welcome to "+self.bank_name+"your current balance is: ",self.balance)
		request = int (input("enter the amount of money you want to withdraw")) 
		if request<0:
			print("invalid number")
		elif request > balance:
			print("you don't have enough balance")
		else:
			self.balance =self.balance-request
			print ("you are going to have", request, "your current balance now is:",self.balance) 
			
			while request <self.balance:
				if request %100==0:
					x= request//100
					for i in range (0,x):
						print("given 100")
					request = request%100
				if request%100>0:
					x= request//100
					for i in range(0,x):
						print("given 100")
					request = request%100
					if request//50==1:
						print("given 50")
						request = request%50
					if request!=0:
						#print "given 50"
						#request=request%50
						x=request//10
						for i in range (0,x):
							print("given 10")
						request =request%10
						if request>=5:
							print("given 5")
							request = request-5
							print ("given",request)
						elif request !=0:
							print ("given",request) 
				request=0
			return balance
			print ("your balance now is:",self.balance)

