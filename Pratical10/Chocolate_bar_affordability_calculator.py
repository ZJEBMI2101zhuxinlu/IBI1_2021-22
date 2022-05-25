def chocolate_calculator(total_money,price):
	bar_number=total_money//price
	left_money=total_money-bar_number*price
	return (f'the number of chocolate is {bar_number}\nleft money is {left_money}')
#example
#you can change the total number and price here
total_money=100
price=7
print(chocolate_calculator(total_money,price))