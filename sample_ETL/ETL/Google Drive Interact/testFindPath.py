
import os

# # print(os.p('Table3.xlsx'))

# # Data_store_locate = f'{os.getcwd()}../../Data'

# # print(Data_store_locate)
b = os.path.join(os.getcwd(),'../../Data')
print(os.path.exists(f'{b}/Table3.xlsx'))



directory = 'Data From Google'
 
# iterate over files in
# that directory
for filename in os.scandir(directory):
    if filename.is_file():
        print(filename.path)