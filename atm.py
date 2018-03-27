totalMoney = 50000

request = input("enter the amount of money you want to withdraw") 

if request<0:
	print "invalid number"
elif request > totalMoney:
	print "you don't have enough balance"
else:
	print ("you are going to have", request)
	while request <totalMoney:
		if request %100==0:
			x= request/100
			for i in range (0,x):
				print "given 100"
			request = request%100
		if request%100>0:
			x= request/100
			for i in range(0,x):
				print "given 100"
			request = request%100
			if request/50==1:
				print "given 50"
				request = request%50
			if request!=0:
				#print "given 50"
				#request=request%50
				x=request/10
				for i in range (0,x):
					print "given 10"
				request =request%10
				if request>=5:
					print "given 5"
					request = request-5
					print ("given",request)
				elif request !=0:
					print ("given",request) 
		request=0