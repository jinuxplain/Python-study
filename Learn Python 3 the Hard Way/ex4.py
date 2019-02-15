# We mow set the variables. And print them with some example string

#variables
cars=100#<class 'int'>
sapce_in_a_car=4.0#<class 'float'>
drivers=30#<class 'int'>
passengers=90#<class 'int'>
cars_not_driven=cars-drivers#<class 'int'>
cars_driven=drivers#<class 'int'>
carpool_capacity=cars_driven*sapce_in_a_car#<class 'float'>
average_passengers_per_car=passengers/cars_driven#<class 'float'>


#prints
print("There are",cars,"cars available.")
print("There are only",drivers,"drivers available")
print("There will be", cars_not_driven, "enpty cars today.")
print("We can tranport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,"in each car.")
