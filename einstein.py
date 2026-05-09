def  Main():
    m = float(input("Enter the mass of the object :"))
    print ("The Energy of the object is : ", formula(m), "10^15 J")

def formula(mass):
    c = 300000000
    e = mass * pow(c, 2) /1000000000000000
    return e
    
Main()


