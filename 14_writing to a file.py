#write

text = 'Sample text to save \nNew line!'

saveFile = open('exampleFile.txt','w')
saveFile.write(text)
saveFile.close() #to save and closure of write operation


#append

appendMe = '\n new bit of append info'
appendFile = open('exampleFile.txt','a')
appendFile.write(appendMe)
appendFile.close()
