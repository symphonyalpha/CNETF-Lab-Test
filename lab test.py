import pandas as pd
import numpy as np
import csv

#saving names from CSV into full
df = pd.read_csv('TA11.csv', header=None, usecols=[0,1], names=['Name','ID'])
full_list = df.Name.tolist()
#saving names from signup.txt into signup
df2 = pd.read_csv('Sign_Up.txt', header=None, usecols=[1], names=['Name'])
signup = df2.Name
df3 = pd.DataFrame() #columns={"Signup Name", "Name", "ID"}
print(df3)

index = 0
while index < 19:
    name = df2.at[index,'Name']
    name_split = name.upper().split()
    #loop through all full names
    for fullname in full_list:
        counter = 0
        #compare the parts of name_split with fullname
        for partname in name_split:
            #if partname is in fullname, add to counter
            if partname in fullname:
                counter += 1
        #if all parts of the name matches fullname
        if counter == len(name_split):
            #add the row (both full name and ID) to a new dataframe
            #print(df.loc[df['Name']==fullname])
            df3 = df3.append(df.loc[df['Name']==fullname])
            #df3 = df2['Name'].copy()
            break
        #v no match found
        elif fullname in df.iloc[-1]['Name']:
            #add the name as row in the new dataframe
            x = pd.Series(name)
            df3 = df3.append(x, ignore_index=True)
            df3 = df3[[0, 'Name', 'ID']]
    
    index += 1

df3.columns = ['Signup name', 'Name', 'ID']

#replace all the nans as empty space
df3 = df3.fillna('')
index = 0
while index < 19:
    signup_name = df2.at[index,'Name']
    check_empty = df3.at[index, 'Signup name']
    #replace the empty cell with the name used for signup
    if check_empty == '':
        df3 = df3.set_value(index, 'Signup name', signup_name)
        index += 1
    else:
        index += 1
        
print(df3)