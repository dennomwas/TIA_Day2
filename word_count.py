def wordcount(string):
  mylist = string.split()
  words_dict = {}

  for word in mylist:
    if word.isdigit(): 
      word = int(word)

    if word in words_dict:
      words_dict[word] +=  1
      
    else:
      words_dict[word] = 1
  return words_dict

string = "olly olly in come come free"
print (wordcount(string))