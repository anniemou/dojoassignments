1.
words = "It's thanksgiving day. It's my birthday,too!"
print words.index("day")
newwords = words.replace("day", "month")
print newwords

2.
x = [2,54,-2,7,12,98]
print(max(x))
print(min(x))

3.
x = ["hello",2,54,-2,7,12,98,"world"]
first = "hello"
last = "world"
print "My name is {} {}".format(first, last)


4.

x = [19,2,54,-2,7,12,98,32,10,-3,6]
# ta bazoume se seira opws leei, kanoume sort dld
x.sort()

# briskw to megethos tis listas
length = len(x)

# to split in half, shmainei na to spasw sthn mesh, ara thelw to miso tou oso megalo einai h lista
half = length / 2

# pairnw to prwto miso tis listas
firstHalf = x[:half]

# to deytero miso tis listas
secondHalf = x[half:]

# bazoume to prwto miso tis listas, sthn arxh tis deyteris. H arxh einai to 0.
secondHalf.insert(0, firstHalf)

print secondHalf
