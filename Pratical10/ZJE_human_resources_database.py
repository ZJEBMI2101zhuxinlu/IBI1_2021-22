class Staff:
	def __init__(self,first_name,last_name,location,role):
		self.first_name=first_name
		self.last_name=last_name
		self.location=location
		self.role=role
	def ZJE_resources(self):
		full_name=self.first_name+' '+self.last_name
		print(f'full name:{full_name}, location:{self.location}, role:{self.role}')
#example
#you can change the staff information here
first_name='Robert'
last_name='Young'
location='Edinburgh'
role='faculty'
Robert_Young=Staff(first_name,last_name,location,role)
Robert_Young.ZJE_resources()