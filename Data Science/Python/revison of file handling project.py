# from pathlib import Path

# import os

# def file_and_folder():
#     path = Path("")
#     items = list(path.rglob(''))
#     for i, items in enumerate(items):
#         print(f"{i+1} : {items}")


# def create_file():

#     try:
#         file_and_folder()
#         name = input('please tell your file name :- ')
#         p = Path(name)
#         if not p.exists():
#             with open(p, 'w') as fs:
#                  data = input("What you want to write in this file :- ")
#                  fs.write(data)
#                  print("File created successfully")
#         else:
#             print("File already exists")
    
#     except Exception as err:
#         print(f"Error occur as {err}")            
 
 
 
# def read_file():

#     try:
#         file_and_folder()
#         name = print("Which file do you want to read")
#         p = Path(name)
#         if p.exists() and p.is_file():
#             with open(p, 'r') as fs :
#                 data = fs.read()
#                 print(data)
                
#             print("REad successfully")
#         else:
#             print("File doesnot exists")        
        
#     except Exception as err:
#         print(f"Error occur as {err}")          
        
# def  update_file():

#     try:
#         file_and_folder()
#         name = input('WHich file do you want to update :- ')
#         p = Path(name)
#         if p.exists() and p.is_file():
#              print("press 1 for chmaging the name of your file")
#              print("press 2 for over writing the data of your file")
#              print('press 3 for appending some content in your file')
             
#              res = int(input("Tell your response"))
             
#              if res == 1:
#                 name2 = input("Tell me your new file name :- ")
#                 p2 = Path(name2)
#                 p.rename(p2)
                
#              if res == 2:
#                 with open(p, 'w') as fs:
#                     data = input("Tell what you want to write, this will overwrite the data ")
#                     fs.write(data)
                     
                 
#              if res == 3:
#                 with open(p,'a') as fs:
#                     data = input("Tell what you want to append")
#                     fs.append(''+data)
                    
#     except Exception as err:
#         print(f"Error occur as {err}")                 

        
# def delete_file():

#     try:
#         file_and_folder()
#         name = input("Which file do you want to delete :- ")
#         p = Path(name)
#         if p.exists() and p.is_file():
#             os.remove(name)
#             print("File remove successfully")
#         else:
#             print("File isnot removed")   
            
#     except Exception as err:
#         print(f'An error occured as {err}')    
    

# print("press 1 for creating a file")
# print("press 2 for reading a file")
# print("press 3 for updating a file")
# print("press 4 for deletion a file")

# check = int(input("Tell your response :- "))

# if check == 1:
#     create_file()
# if check == 2:
#     read_file()
# if check == 3:
#     update_file()
# if check == 4:
#     delete_file()