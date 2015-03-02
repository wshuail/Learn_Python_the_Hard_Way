cars = 100 # This is names and variables.
space_in_a_car = 4.0 # I think both 4 or 4.0 is OK. Besides, "_" is underscore character.
drivers = 30 # Keepping space between them is a good habit.
passages = 90
cars_not_driven = cars-drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car #carpool is a strange word.
average_passages_per_car = passages / cars_driven

print 'There are ', cars, 'cars avaiable.' # there are strings and a variable in this sentence.
print 'There are only', drivers, 'drivers avaible.' #the word 'drivers' should not be forgot.
print 'There will be', cars_not_driven, 'empty cars today.'
print 'We can transport', carpool_capacity, 'people today.'
print 'We have', passages, 'to carpool today.'
print 'We need to put about', average_passages_per_car, 'in each car today.'
