def asc_des():
  y=[]
  for i in range(5):
      x=int(input("Enter your numbers by order:  "))
      y.append(x)
      ascending_order=sorted(y)
      discending_order=sorted(y, reverse=True)


  print(f'"main list = "{y}')
  print(f'"ascending_order = "{ascending_order}')
  print(f'"discending_order = "{discending_order}')


# asc_des()



