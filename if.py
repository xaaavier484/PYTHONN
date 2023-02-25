
if statement
x=1
username=49
password=80
if(x>0):
    print("The number is positive")
#if... else statement
if(username>=50):
    print("You have included")
else:
    print("You have entered the wrong username ")
#if.. elif.. else statement
if(password>=30 and password==0):
    print("not correct")
elif password<=30 and password>=49:
    print("correct password")
elif password<=50 and password>=79:
    print("You have a credit")
elif password<=80 and password>=100:
    print("You have a distinction")
else:
    print("Wrong password entered")

stock = 600
jeans_sold = 500
target = 500

target_hit = jeans_sold == target
print("Hit jeans sales target: ")
print(target_hit)

current_stock = stock - jeans_sold
in_stock = current_stock != 0

#smart light switch

is_day = False
lights_on = not is_day

print("Daytime?")
print(is_day)

print("Lights on?")
print(lights_on)

#Kilometer Converter

miles = 500
kilometers = miles * 1.609344
print(kilometers)

#Types and comparisons

#comparing numbers
print(1 <= 3)
print(11 <= 11)
print(3099 >= 3099)
result = 1 <= 15
print(result)
min = 5
max = 10
result = min <= max
print(result)
print(10 >= 10)
battery_level = 10
low = battery_level <= 20
print("Low Battery:")
print(low)
points = 12
level_two = points >= 10
print ("level 2:")
print(level_two)
solved = 20
minimum = 10
lost_streak = solved <= minimum
print(60 >= 50)

#Comparing Strings

print("online" == "online")
print("online" != "offline")
print("apple" == "apple")
print("apple" == "orange")

print("subscribed" != "rejected")
print("subscribed" != "subscribed")
same = "subscribed" != "rejected"

previous_leader = "anna"
new_leader = "jim"
leader_changed = previous_leader != new_leader

#Discovering Types

sugar_content = "High"
score = 42


pi = 3.14159
received_newsletter = True
is_on = False

result = 1 >= 1
print(result)

#Formatting Strings

print("new" + "messages")
print(f"{2} new messages")
print(f"{6} new messages")
new_messages = 2
print(f"{2} new messages")
print(f"{5} new messages and {2} friend requests")
new = 5
status = f"{new} new messages"
print(status)
print(f"{4} dataset entries")
print(f" popularity increased by {12}%")

#Making Decisions
if True:
    print("hello!")
while False:
    print("Hello!")
if True:
    print("Show Notifications")
if True:
    print("The answer is 42")
if True:
    print("I'm a code block")
if True:
    print("Look at me")
    print("I'm two spaces away!")
greet = True
if greet:
    print("Hello!")
greet = False
if greet:
    print("hello!")
wakeup_time = True
if wakeup_time:
    print("Rise and shine,Xavier!")
paid = False
if paid:
   print("Thank you for your purchase")

#Using conditions

answer = "Picasso"
if answer == "Picasso":
    print(answer + "is correct!")
answer = "Matise"
if answer != "Picasso":
    print(answer + "is not quite")

is_day = True
if is_day == True:
    print("print lights off!")

score = 51
pass_grade = score > 50
if pass_grade:
    print(pass_grade)

song ="Dont Stop me now"
replay_times = 345

if replay_times >= 300:
    print("Your top song this week: ")
    print(song)

diet = "vegeterian"
veggie_restaurant = "root"
hour = 9
#Incorporating elif
if hour < 12:
    print("Good morning")
else:
    print("good night")
hour = 14
if hour < 12:
    print("Good morning")
elif hour < 17:
    print("Good afternoon")
hour = 14
if hour < 12:
    print("Good morning")
elif hour < 17:
    print("Good afternoon")
hour = 20
if hour < 12:
    print("Good morning")
elif hour < 17:
    pirnt("Good afternoon")
elif hour < 21:
    print("Good evening")
else:
    print("Good night")
number = 6
if number < 5:
    print("Less than five")
elif number < 10:
    print("Less than ten")
score = 75
if score < 70:
    print("You passed")
elif score <= 90:
    print("You get an A!")
score = 66
if score > 90:
    print("You get an A!")
elif score > 70:
    print("You passed!")
else:
    print("Better luck next time")
#Using Complex Decisions
age = 17
has_permit = True
if age > 16:
    print("Can drive")
age = 17
has_permit = True
if age > 16 and has_permit:
    print("Can drive")
age = 17
has_permit = True
if age > 16 and has_permit:
    print("Can drive")
#loops
#self-assigning and operators
