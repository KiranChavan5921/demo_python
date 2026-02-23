
# File Handling: day1
                
# file = open('data.txt',"w")
# file.write("welcome to python file handling")
# file.close()                 

# file = open("data.txt", "r")
# print(file.read())
# file.close()

# file = open('file.txt','w')
# file.write("we are learning python")
# file.close()

# file = open('file.txt','r')
# text = file.read()
# print(text)
# file.close()

# data = ' and data science'

# f =open('newfile.txt','a')
# f.write(data)
# f.close

# print(Data)

# f = open('file1.txt','x')
# f.write("XYZ")

# f = open('file3.txt','x')
# f.write("qwdhsbvb")
# f.close()

# text="""name : kiran chavan
# acc no : 3800112307
# address : umerga
# """
# file = open('BankDetails.txt','w')
# text = file.write(text)
# file.close()




# 2.readline():

# f = open('BankDetails.txt','r')
# data = f.read(20)
# f.close

# f = open('BankDetails.txt','r')
# data1 = f.readline()
# data2 = f.readline()
# data3 = f.readline()
# f.close

# print(type(data1))

# print(data1)
# print(data2)
# print(data3)

# print(f.readable())
# print(f.writable())

# 3.readlines():

# f =open('BankDetails.txt','r')
# text = f.readlines()
# f.close()

# print(text)
# print("***********")
# print(type(text))


# for line in text[::2]:
#     print(line)

# for index, line in enumerate(text):
#     print(index+2,line)

#############################

# mode :
# 1.write: 'w' : to create a new file    
# 2.read: 'r' : to read a file content  
# 3.aapend: 'a' : to append or add new content in an existing file.
# 4.cerate: 'x' : to create a new file  


# method:

# write(): It is used to write a content in file.
# read(): It is used to read the whole content in 
# readline(): It is used to read a line at once , It return  string.
# readlines(): It is used to read whole file line by line in list.It returns list of strung.
# close(): It is used to close the file.
# 
  

#######################  day2    #########################

# File handling : day2

# text="""
# name : kiran chavan
#  acc no : 3800112307
#  address : balsur
#  """
 
# file = open('BankDetails.txt','w')
# text = file.write(text)
# print(file.tell())
# file.close()


# *********************************

# file = open('BankDetails.txt','r')

# print(file.tell)
# text=file.read(7)
# print(text)

# print(file.tell())
# # file.close()

# file.seek(8)
# text1 =file.read(5)
# print(text1)

# print(file.tell())
# file.close()


# file = open('BankDetails.txt','r')

# print(file.tell)
# text=file.read(15)
# print(text)

# print(file.tell())
# # file.close()

# file.seek(8)
# text1 =file.read(4)
# print(text1)

# print(file.tell())

# file.seek(0)
# # text1 =file.read(4)
# # print(text1)

# print(file.tell())
# file.close()

#########################
# with open('cricket.txt','w')as file:
#   text= " i am krishna fan its god of cricket "
#   file.write(text)
  
# with open('cricket.txt','r') as f:
#     text=f.read()          
#     print(text)


# with open('cricket.txt','a') as f:
#     text="\nsunil chhetri is indian footballer"          
#     f.write(text)

# with open('sport_player.txt','w+') as f:
    
#     f.write("m s dhoni,sachin ,virat")
#     f.seek(0)
#     data=f.read()
#     print("data:",data)

# with open('sport_player.txt','r+') as f:
    
    
#     data=f.read()
#     print("data:",data)