import re

data = open('/Users/kaiyuwang/Desktop/sample_toronto_sales.csv','r')
read_table = data.readlines()
data.close()

#------method dealing with address formatting---
#get rid of '#' and '-' starting for index 1 
def addressformatting(address):
    unit,firstletter,block = re.split('([a-zA-Z])',address,1)
    #use regex to further split unit number and block number
    while unit[-1:] == ' ':
        unit = unit[:-1]
    if unit[:1] == '#':
        unit = unit[1:]
        if " - " in unit:
            unit = unit.replace(' - ','-')
        if " -" in unit:
            unit = unit.replace(' -','-')
            unit = unit.replace('- ','-')
    else:
        unit = unit.replace(" ","-")
        
    block = (firstletter+block).title()
    return unit+ ' ' +block


#------process data into list and dict---
table = []

for line in range(1,len(read_table),1):
    #split each line by ','
    address,price = read_table[line].split(',')
    address = addressformatting(address)
    price = int(price[:-2])
    #store address and price into a list
    table.extend([[address,price]])
    

print("The LIST is now containing %d rows" % len(table))
#transfer list to dictionary
dict_table = dict(table)
print("The DICTIONARY is now containing %d rows" % len(dict_table))
#the reason that lenght of dict is shorter than list is becuase there are same key(address) values, and dict don't store same key value.
print("The reason that lengh of dict is shorter than list is becuase"+"there are same key(address) values, and dict don't store same key value.".upper()+"\n")



#calculate windchill
def windchill(temperature, windspeed):
    windchill = 13.12+(0.6215*temperature)-(11.37*windspeed**0.16)+(0.3965*temperature*windspeed**0.16)
    return windchill

#------outprint---
for temperature in range(-35,11,5):
    print("temperature is %d" % temperature)
    for windspeed in range(0,81,5):
        print("\twindspeed is "  + str(windspeed)+" caculated wind chill is: "+ str(int(windchill(temperature, windspeed))))