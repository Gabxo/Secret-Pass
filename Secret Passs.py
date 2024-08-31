import secrets
import string

def generar_contrasena(longitud=12, mayusculas=True, minusculas=True, digitos=True, especiales=True):
    if longitud < 8:
        raise ValueError("La longitud mínima de la contraseña debe ser de 8 caracteres.")

    # Define los conjuntos de caracteres basados en las opciones seleccionadas
    caracteres = ''
    if mayusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if digitos:
        caracteres += string.digits
    if especiales:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Debe seleccionar al menos un tipo de carácter para la contraseña.")

    # Asegura que la contraseña contenga al menos un carácter de cada tipo seleccionado
    contrasena = []
    if mayusculas:
        contrasena.append(secrets.choice(string.ascii_uppercase))
    if minusculas:
        contrasena.append(secrets.choice(string.ascii_lowercase))
    if digitos:
        contrasena.append(secrets.choice(string.digits))
    if especiales:
        contrasena.append(secrets.choice(string.punctuation))

    # Completa el resto de la contraseña con caracteres aleatorios
    contrasena += [secrets.choice(caracteres) for _ in range(longitud - len(contrasena))]

    # Baraja la contraseña para evitar patrones predecibles
    secrets.SystemRandom().shuffle(contrasena)

    return ''.join(contrasena)

def obtener_opcion(menu_opciones):
    while True:
        opcion = input("Selecciona una opción: ").strip()
        if opcion in menu_opciones:
            return opcion
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu():
    while True:
        print("\nGenerador de Contraseñas Seguras")
        print("1. Generar una contraseña")
        print("2. Salir")

        opcion = obtener_opcion(['1', '2'])

        if opcion == '1':
            try:
                longitud = int(input("Introduce la longitud deseada de la contraseña (mínimo 8): ").strip())
                if longitud < 8:
                    print("La longitud mínima es de 8 caracteres. Inténtalo de nuevo.")
                    continue

                print("\nSelecciona los tipos de caracteres a incluir:")
                mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").strip().lower() == 's'
                minusculas = input("¿Incluir letras minúsculas? (s/n): ").strip().lower() == 's'
                digitos = input("¿Incluir dígitos? (s/n): ").strip().lower() == 's'
                especiales = input("¿Incluir caracteres especiales? (s/n): ").strip().lower() == 's'

                if not (mayusculas or minusculas or digitos or especiales):
                    print("Debes seleccionar al menos un tipo de carácter. Inténtalo de nuevo.")
                    continue

                contrasena = generar_contrasena(longitud, mayusculas, minusculas, digitos, especiales)
                print(f"Tu contraseña generada es: {contrasena}")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Se produjo un error inesperado: {e}")
        elif opcion == '2':
            print("Saliendo del programa. ¡Hasta luego!")
            break

if __name__ == "__main__":
    menu()
