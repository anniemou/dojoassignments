#!name, age, country of birth, favorite language.
# #My name is Anna
# #My age is 101
#My country of birth is The United States
#My favorite language is Python
###############################################################
info2 = {"name": "Anna", "age": 101, "country of birth": "The United States", "favorite language": "Python"}
def iterateDict(dic):
    for key,data in dic.iteritems():
        print "My {} is {}".format(key, data)

iterateDict(info2)




