import os
def rename_file():
     file_list = os.listdir(r"C:\Users\user\Downloads\prank")
     print(file_list)
     for file_name in file_list:
         os.rename(file_name,file_name.translate(none,"0123456789")


rename_file();

    
