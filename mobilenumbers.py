
list = ["+91 8019890390","+91 9019890390","8019890399","8019890345,","+91 80198 90380","70198 90380"]

mobilenumbers=[]
for number in list:
    number=number.replace(" ","")
    number = number.replace(",", "")
    mobilenumbers.append(number[-10:])


def standardize(mobilenumbers):
    mobilenumbers.sort()
    print("Mobile Numbers in Standard Format")
    for x in mobilenumbers:
        print("+ "+"91"+" "+str(x[0:5])+" "+str(x[5:]))

standardize(mobilenumbers)
