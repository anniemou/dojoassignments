#input
#l = ['magical unicorns',19,'hello',98.98,'world']
#output
#"The list you entered is of mixed type"
#"String: magical unicorns hello world"
#"Sum: 117.98"
##############################################################
#input
#l = [2,3,1,7,4,12]
#output
#"The list you entered is of integer type"
#"Sum: 29"
##################################################################
#input
#l = ['magical','unicorns']
#output
#"The list you entered is of string type"
#"String: magical unicorns"

lista1 = ['magical unicorns',19,'hello',98.98,'world']

def type_list(userList):
    newstring = "String:"
    sum = 0
    processed_string = False
    processed_number = False
    processed_type = "mixed"

    for item in userList:
        if isinstance(item, basestring):
            processed_string = True
            newstring += " " + item
        
        if isinstance(item, int) or isinstance(item, float):
            processed_number = True
            sum += item

    if processed_number and not processed_string:
        processed_type = "integer"
    elif processed_string and not processed_number:
        processed_type = "string"

    print "The list you entered is of {} type".format(processed_type)
    print sum

type_list(lista1)