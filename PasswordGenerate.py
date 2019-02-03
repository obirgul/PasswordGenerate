import random
a= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','{',':','>','?','}','|','!','@','#','$','%','^','&','*','(',')','-','+']

z = int(input("How many words in your password?: "))
List = []
for x in range(z):
    List.append(random.choice(a))
print("".join(List))
print("1) Yes")
print("2) No")
b = int(input("Would you like to save this password to a text file? 1 for YES, 2 for NO "))
if b == 1:
    c = input("What is this password for?: ")
    x = open("%s.txt" % c, "w")
    y = "".join(List)
    x.write(y)
    x.close
    x = open("%s.txt" % c, "r")
    x.read
    print("Saved!")
elif b == 2:
    input("Press Enter To Continue")