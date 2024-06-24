A_1 = float(input("Subject 1 (Grade): "))
A_2 = float(input("Subject 1 (Unit/s): "))
B_1 = float(input("Subject 2 (Grade): "))
B_2 = float(input("Subject 2 (Unit/s): "))
C_1 = float(input("Subject 3 (Grade): "))
C_2 = float(input("Subject 3 (Unit/s): "))
D_1 = float(input("Subject 4 (Grade): "))
D_2 = float(input("Subject 4 (Unit/s): "))
E_1 = float(input("Subject 5 (Grade): "))
E_2 = float(input("Subject 5 (Unit/s): "))

GWA = (((A_1*A_2)+(B_1*B_2)+(C_1*C_2)+(D_1*D_2)+(E_1*E_2))/(A_2 + B_2 + C_2 + D_2 + E_2))

print("Your GWA for the first semester is ", GWA)
