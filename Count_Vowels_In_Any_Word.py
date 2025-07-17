def Count_Vowels (x):
  x=x.lower()
  vowels="aeiou"
  y=0
  for i in x:
    if (i in vowels):
      y+=1
  print(y)

x=input('enter a string')
Count_Vowels(x)
