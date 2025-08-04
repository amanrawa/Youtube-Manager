file=open("dsf.txt",'w')   


try:
    file.write('chai aur code.txt')
finally:
    file.close()

#method 2 using with 


with open('youtb..txt', 'w') as file:
    file.write("chai or pyhon")


