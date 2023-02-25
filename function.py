
def emobilis():
    print("This Is My First Function")
emobilis()
def calculatesquare():
    x=5
    y=5
    print(x*y)
calculatesquare()
emobilis()

def majina(fname,lname,age):
    print(fname + lname+ age)
majina("Xavier","Valentino","16")

answer = "Picasso"
if answer == "Picasso":
    print(answer + "is correct!")
answer = "Matise"
if answer != "Picasso":
    print(answer + "is not quite")

def maximum(a,b,c,d,e):
    return max(a,b,c,d,e)
result=maximum(5,15,67,0,89)
print(result)
def minimum(f,g,h,i,j):
    return min(f,g,h,i,j)
result=minimum(2,34,65,0,5)

def print_numbers(nambari):
    for i in range(nambari):
        print(i)
print_numbers(nambari)
