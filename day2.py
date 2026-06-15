#write a grade classifier:input marks,output a/b/c/d/f
a=int(input("enter marks:"))
if a >= 90:
    print("A")
elif a >=80:
    print("B")
elif a >=70:
    print("C")
elif a>=60:
    print("D")
else:
    print("F")


 #print multiplication table of a given number using a for loop
a=int(input("enter the number:"))
for i in range(1,10):
    print(f"{a}*{i}",a+i)


#while loop that prints even number from 1 to 50
num=2
while num<=50:
    print(num)
    num+=2


#frizzbuzz: print frizz,buzz,frzzBuzz for multiples of 3,5,both
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz") 
    elif i%5==0:
        print("buzz")
    else:
        print("i")


#number guessing game using a while loop
secret=random.randint(1,100)
while True:
    guess =int(input("guess a number(1-100)"))
    if guess==secret:
        print("wow!right")
    elif guess<secret:
        print("low")
    else:
        print("too high")   