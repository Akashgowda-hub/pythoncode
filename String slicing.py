# learning String Slicing

string = "Public Repo is open to all"
Length = len(string)
print (Length)

print (string[0:26])  # this will print values from includes 0 charcater to exceluding 26th character
print (string[:26])     # this will be same as above line 5
print (string[-2:-1])  
#  logic works as len(string) -2: len(string) -1
#  26-2:26-1
#  24:25  # this will print values from includes 24th charcater to exceluding 25th character