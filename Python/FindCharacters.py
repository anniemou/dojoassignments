def findInChar(words,character):
    for word in words:
        if(word.find(character) >= 0):
            print word
findInChar(['hello','world','my','name','is','Anna'],'o')     



