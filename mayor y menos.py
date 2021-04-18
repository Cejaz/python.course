A=int(input("INGRESE UN NUMERO \n"))
B=int(input("INGRESE UN NUMERO \n"))
C=int(input("INGRESE UN NUMERO \n"))
D=int(input("INGRESE UN NUMERO \n"))

if(A > B and A > C and A > D):
     X=A
else:
   if(B > A and B > C and B > D):
     X=B
   else:
     X=C
   if(B > A and B > C and B > D):
     X=B
   else:
     X=D    
     
if(A < B and A < C and A < D):
     Y=A
else:
   if(B < A and B < C and B < D):
     Y=B
   else:
     Y=C
   if(B < A and B < C and B < D):
     Y=B
   else:
     Y=D  
     
print("EL NUMERO MAYOR ES"+str(X)+"EL NUMERO MENOR ES"+str(Y))
