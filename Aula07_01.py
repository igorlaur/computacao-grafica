def funcao (x, y=4, teste=True):
   print("x= "+str(x))
   print("y= "+str(y))
   if teste:
      print (x*y)

print("------funcao(1,2,False)")
funcao(1,2,False)
print("-------")

print("------funcao(5)")
funcao(5)
print("-------")

print("------funcao(teste=True, x=3)")
funcao(teste=True, x=3)
print("-------")

