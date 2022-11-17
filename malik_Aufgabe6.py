
test_test = [1,3,5,7,9]

varcopy = var[:]
print("ID: ", id(var), # ID: 139919586427136
"ID: ", id(varcopy)) # ID: 139919584695104
var = "Klausur"
varcopy = var[:]
print("ID: ", id(var), # ID: 139919585342896
"ID: ", id(varcopy)) # ID: 139919585342896