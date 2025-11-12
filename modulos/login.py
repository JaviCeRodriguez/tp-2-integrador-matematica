def credenciales():
    return { "email": "javier@mate.com", "contrasena": "12345abc" }


def iniciar_sesion():
    print("=== Sistema de Inicio de Sesión ===")
    usuario = credenciales()

    email = input("Ingrese su email: ")
    contrasena = input("Ingrese su contraseña: ")

    if email == usuario["email"] and contrasena == usuario["contrasena"]:
        print(f"\n✅ Bienvenido {email.split('@')[0]}!")
        print("➡️  Acceso concedido a los datos del sistema")
        return True
    else:
        print("\n🚨 Error: Credenciales inválidas. Verifique su email y contraseña.")
        return False


if __name__ == "__main__":
    iniciar_sesion()