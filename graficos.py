import tkinter as tk

usuarios = (
        ("usuario1", "contrasenia1"),
        ("usuario2", "contrasenia2"),
        ("usuario3", "contrasenia3"),
    )



def login():

    usuario = entry_user.get()
    contrasenia = entry_contrasenia.get()

    for user, passw in usuarios:
            if user == usuario and passw == contrasenia:
                # Inicio de sesión exitoso
                print("¡Acceso exitoso!")
                print("-----------------------------------------------------------")
                abrir_nueva_ventana()
                return True

    print("Acceso denegado.")
    return False

def abrir_nueva_ventana():
    # Ocultar la ventana principal
    raiz.withdraw()
    
    # Crear una nueva ventana
    nueva_ventana = tk.Toplevel(raiz)
    nueva_ventana.geometry("400x400")
    nueva_ventana.configure(bg="#61afef")
    nueva_ventana.title("Nueva ventana")
    
    # Contenido de la nueva ventana
    label_bienvenida = tk.Label(nueva_ventana, text="¡Bienvenido!", font=("Arial", 16), bg="#61afef", fg="white")
    label_bienvenida.pack(pady=20)
    
    button_salir = tk.Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy, font=("Arial", 12))
    button_salir.pack(pady=20)
    
#Ventana principal
raiz = tk.Tk()
raiz.geometry("400x600")
raiz.configure(bg="#282c34")

label_user = tk.Label(raiz, text = "Ingresa tu usuario", bg="#282c20",fg="white",font=("Arial",12))
label_user.pack(pady=5)

entry_user = tk.Entry(raiz,font=("Arial",12))
entry_user.pack(pady=5)

label_user = tk.Label(raiz, text = "Ingresa tu contraseña", bg="#282c20",fg="white",font=("Arial",12))
label_user.pack(pady=5)

entry_contrasenia = tk.Entry(raiz,font=("Arial",12))
entry_contrasenia.pack(pady=5)

button_style = {
    "font" : ("Arial",12),
    "bg" : "#61afef",
    "fg" : "white",
 "activebackground" :"#98c379",
 "activeforeground" : "white",
 "width" : 20,
 "height" : 2,
 "relief" : "raised" 
}

button_login = tk.Button(raiz,text = "Iniciar sesion", command = login,**button_style)
button_login.pack(pady=5)

raiz.mainloop()
