# read retail txt
data=open('/Users/kaiyuwang/Desktop/retail.txt','r') 
read_table = data.readlines()
data.close()
#random concat first 8 rows 
retail_types = ''
#since some retail types contains ',' here 
for line in range(0,8,1):
    retail_types += read_table[line][:-2].casefold()+","
    
#deal with the last ','
retail_types =retail_types[:-1]
print(retail_types)


new_type = str(input("Add another item onto the retail list? \n")).casefold()
print('\n')
print("new_type is: \n".upper()+new_type+'\n')
retail_types += ' , '+new_type    
print('now your retail_types has updated to: \n'.upper()+ retail_types+'\n')




#make it to a list
retail_types = retail_types.split(',')
#every forth entrance
retail_fourth = [retail_types[i] for i in range(3,len(retail_types),4)]


retail_forth_tuple = tuple(retail_fourth)
print('here is the tuple of every forth entry: \n'.upper()+str(retail_forth_tuple))