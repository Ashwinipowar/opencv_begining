#dictionary


# # A dictionary is a collection of key-value pairs.
# Each key is unique and points to a value
name={20:"sars", 50:"tara", 70:"siya"}
print(name[20])
print(name.get(20))
#these are the two methods where we can get the only one pair of the value
#name can get erroer if we asked out of the dictionary
# but the dot get will not the give the error for asking out ofthe dictionary it will give----none--

name={20:"sars", 50:"tara", 'maya':"siya"}
# print(name[100]) this shows the erroe
print(name.get(100))
print(name['maya'])

# if you wannnts to show the erroe then can use simple way
# you doesnt wants to show the error then use .get givess the -----none

#can print all the keys
student={"tara":"siya", "maya":"ram","pen":"pemcil"}
print(student.values())
# it gives the dict values of all by using the values
print(student.keys())



student={"tara":"siya", "maya":"ram","pen":"pemcil"}
print(student)
print(student.keys())
print(student.values())


for key in student.keys():
    print(f"the values corresponding to the key {key} is {student[key]}")
# here is ----f---- is important for printing the actul value of keys and values
#this is the syntax for use the dictionary

# when we wanna both key and values pair then just use the----item--
print(student.items())
for key, value in student.items():
    print(f"the value corresponding to the key {key}is {value}")
#the use of dictionary is to mapping 