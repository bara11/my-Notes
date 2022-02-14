phone_guied={'Amal':1111111111,'Mohammed':2222222222,'Khadijah':3333333333,'Abdullah':4444444444,'Rawan':5555555555,'Faisal':6666666666,'Layla':7777777777}
val=int(input("Please enter the value:"))
print("\n")

if val >1000000000:

    def get_key(val):
      if 1>0:
          for key,value in phone_guied.items():
             if val==value:
                 print(key)
      else:
          print("Sorry, the number is not found ")
    get_key(val)
else :
  print("This is invalid number")
key1=input("Please enter the key:")
print("\n")
if 1>0:

    def get_value(key1):
      if 1>0:
          for key,value in phone_guied.items():
             if key1==key:
                 print(value)
      else:
          print("Sorry, the number is not found ")
    get_value(key1)
else :
  print("This is invalid name" )
key2=input("Please input the new user:")
val2=int(input("Please input the new number:"))
if val2>1000000000 :
    if 1>0:
          def add_if_key_not_exist(dict_obj, key2, value2):
              if key2 not in dict_obj:
                   phone_guied.update({key2: value2})
    add_if_key_not_exist(phone_guied,key2,val2)
    print(phone_guied)
else:
    print("Sorry, the number is not found")
