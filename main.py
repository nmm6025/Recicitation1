def countWords(aString):
  countdictionary = {}
  splitString = aString.split()
  for i in splitString:
    if not i.isalpha():
      splitString[splitString.index(i)] = " "
  for i in splitString:
    if i.lower() not in countdictionary.keys():
      if i.isalpha():
        countdictionary[i] = 1
      else:
        countdictionary[i] = countdictionary[i] + 1
    continue
  return countdictionary

   