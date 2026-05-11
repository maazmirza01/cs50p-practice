"""
i = 0          # how to use a while loop.
while i < 7:
    print("meow!")
    i += 1       #to make it more succcint

    
for _ in [0, 1, 2]: # not the best way to write. name variable _ cause its got no use outside of this.
    print("meow!")

"""
for r in range(3):  #to make it simpler way to use a list
    print("meow!")

# or

print("meow!\n" * 3, end="")

while True:
    n = int(input("What's n ? "))
    if n < 0:
        continue
    else:
        break

for m in range(n):
    print("meow!")