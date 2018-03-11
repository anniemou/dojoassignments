def list_compare(list_one, list_two):
    if len(list_one) != len(list_two):
        print "The lists are not the same" 
        return
    for i in range(0, len(list_one)):
        item1 = list_one[i]
        item2 = list_two[i]
        if item1 != item2:
            print "The lists are not the same" 
            return
    print "The lists are the same"


list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5]
    
list_compare(list_one, list_two)