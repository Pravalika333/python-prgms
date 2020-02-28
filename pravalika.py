
"""perimeter of rectangle(2(a+b))"""
a=int(input("enter length")) 
b=int(input("enter breadth")) 
perimeter=2*(a+b)
print(perimeter)

"""input and output of all dat types"""
a=10
j=(-1)**0.5
print(a)
type(a)
b=10.5
print(b)
type(b)
c=True
print(c)
type(c)
d=a+b*j
print(d)
type(d)
e="baby"
print(e)
type(e)


"""sum of two numbers"""
a=10
b=12
c=a+b
print(c)


"""prgm of two number and perform all arithmetic operators"""
a=10
b=2
a*b
a-b
a//b
a/b
a**b
a+b



"""area of rectangle(a=lw)"""
a=int(input("enter length")) 
b=int(input("enter breadth")) 
area=a*b
print(area)



"""radius,circumference, area,diameter of circle"""
a=int(input("enter radius")) 
b=int(input("enter diameter")) 
pi=3.14
radius_of_circle=b/2
circumference_of_circle=2*pi*a
diameter_of_circle=2*a
area_of_circle=pi*a*a
print(radius_of_circle)
print(circumference_of_circle)
print(diameter_of_circle)
print(area_of_circle)



"""to enter length in centimeter and convert into meter and kilometer"""
cm=int(input("enter length in centimeter")) 
meter=cm/100
km=cm/1000
print(meter)
print(km)


"""to enter length in temperature in celsius and convert into fahrenheit"""
tm=int(input("enter temperature in celsius")) 
far=tm*1.8+32
print(far)

"""to enter length in temperature in fahrenheit and convert into celsius"""
far=input("enter temperature in fahrenheit")
type(far)
far=float(far)
far=int(far)
cel=5/9*(far-32)
print(cel)


"""write a prgm to convert days into years, week and remaining days"""
dys=int(input("enter days"))
year=dys/365
week=dys//7
remaining_days=dys-(week*7)
print(year)
print(week)
print(remaining_days)

"""to find power of an number"""
a=int(input("enter base number")) 
b=int(input("enter power number"))
power=a**b
print(power)


"""to enter an number and calculate its square root"""
a=int(input("enter sqrt number")) 
b=a**0.5
print(b)

"""write a prgm to enter two angles of triangle  and find third angle"""
a=int(input("enter first angle")) 
b=int(input("enter second angle")) 
c=180-(a+b)
print(c)



"""write a prgm to calculate are of equilateral angle"""
a=int(input("enter side")) 
area=((3)**0.5)/4*a*a
print(area)



"""prgm to enter marks of five subjs and calculate total, avg, percentage"""
a=int(input("enter marks of first subj ")) 
b=int(input("enter marks of second subj ")) 
c=int(input("enter marks of third subj ")) 
d=int(input("enter marks of fourth subj ")) 
e=int(input("enter marks of fifth subj ")) 
total_marks=600
total=a+b+c+d+e
avg=(a+b+c+d+e)/5
percentage=total/total_marks*100
print(total)
print(avg)
print(percentage)


"""enter P,T,R and calculate simple interest"""
p=int(input("enter principal")) 
t=int(input("enter time")) 
r=int(input("enter rate")) 
simple_interest=(p*t*r)/100
print(simple_interest)


"""calculate compound interest a=p(1+r)*t"""
p=float(input("enter principal")) 
t=float(input("enter time")) 
r=float(input("enter rate")) 
a=p*(1+r)*t
print(a)