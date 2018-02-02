import os
def rename_files():
     file_list = os.listdir(r"C:\Users\user\Downloads\prank")
     print(file_list)
     savedpath=os.getcwd()
     os.chdir(r"C:\Users\user\Downloads\prank")
     
     for file_name in file_list:
         os.rename(file_name,file_name.translate(None,"0123456789"))
     os.chdir(savedpath)
 
rename_files()

    
