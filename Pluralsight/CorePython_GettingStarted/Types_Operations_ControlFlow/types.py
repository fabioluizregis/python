# Int
print("============= INT =============")
print (10)
print (0b10) # 10 em binário
print (0o10) #10 em octal
print (0x10) #10 em hexadecimal

print (int(3.5))
print (int(-3.5))
print (int("496"))
print (int("10000", 3)) #10000 em base 3

#########################################################
# Float
print ("============= FLOAT =============")
print (3.124)
print (3e8) # 3 seguidos de 8 zeros (velocidade da luz)
print (1.616e-35) # 1.616 vezes 10 elevado -35 (Constante de Planck)
print (float("1.618"))
print (float("inf")) # infinito
print (float("-inf")) # -infinito
print (float(3.0 + 1))

#########################################################
# None
print ("============= None =============")
print (None)

a = None
print (a is None)

#########################################################
# Bool
print ("============= Bool =============")
print (True) # True
print (False) # False
print (bool(0)) # False
print (bool(42)) # True
print (bool(-1)) # True
print (bool(0.0)) # False
print (bool(0.207)) # True
print (bool(-1.117)) # True
print (bool([])) # False
print (bool([1, 5, 9])) # True
print (bool("")) # False
print (bool("Spam")) # True
print (bool("False")) # True
print (bool("True")) # True
