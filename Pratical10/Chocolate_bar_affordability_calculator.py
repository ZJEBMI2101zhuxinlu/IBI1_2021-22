def chocolate_calculator(total_money,price):
	bar_number=total_money//price
	left_money=total_money-bar_number*price
	return bar_number,left_money
#example
print(chocolate_calculator(100,7))