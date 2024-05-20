


users = []

user1 = [70100100,"Pepito","Perez",3214567890,"pp@mail.com","M",29,"1234"]

user2 = [70200200,"Maria","Perez",3224567890,"jj@mail.com","F",29,"1234"]

user3 = [70300300,"Juan","Castro",3254567890,"jj@mail.com","F",29,"1234"]


users.append(user1)
users.append(user2)
users.append(user3)

print(users)

for item in users:
    print(item)

print(users[1][4])

#crear un inicio de sesion comparando el valor de correo y contraseña ingresado por el usuario vs el qe esta en la base de datos

i = int(input("Ingrese el index del usuario"))
mail = input("Ingrese email registrado")
password = input("Ingrese contraseña")

if mail == users[i][4] and password == users[i][7]:
 print(f"Bienvenido"(users[i][1]))

else:
    print("valide sus credenciales")

