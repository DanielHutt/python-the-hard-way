#Calculate the horse problem

#Prompt:
#If a horse and a half can eat a bale of hay and a half in a day and a half,
# how long will 10 horses take to eat 10 bales of hay?

#given:
base_horses = 1.5
base_bales_eaten = 1.5
base_time = 1.5 #days

#Variables in question
horses_eating = 10
bales_to_eat = 10

#Number of eating units
#Units eat 1.5 bales in 1.5 days
eating_units = horses_eating / base_horses

#Bales eaten in 1.5 days
bales_eaten = eating_units * base_bales_eaten

bales_per_day = bales_eaten / base_time

time_to_eat = bales_to_eat / bales_per_day


print "%d horses will eat %f bales of hay per day." % (horses_eating, bales_per_day)
print "It takes %d horses %f days to eat %d bales." % (horses_eating, time_to_eat, bales_to_eat)

