#args is a tupel type
def add(*args):
	sum=0
	for n in args:
		sum+=n
	return sum
# print(add(1,2,3,4))

def calc(**keyargs):
	return keyargs
# print(type(calc(add=2,multy=5)))

class Car:
	def __init__(self,**kw):
		self.make = kw.get("make")
		self.model=kw.get("model")
		self.color=kw.get("color")
		self.seats =kw.get("seats")
my_car=Car(make="BMW",model="GR-R")
# print(my_car.make)
