#------------------------------
# Suma Enteros 1.0
#------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *

#------------------------------
# funciones de la app
#------------------------------

#------------------------------
# ventana principal de la app
#------------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Suma Enteros 1.0")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="thistle")

#------------------------------
# frame entrada datos
#------------------------------
frame_entrada= Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x=10, y=10)

# logo app
logo = PhotoImage(file="img/escudo_colegio.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=70,y=40)

# titulo de la app
titulo = Label(frame_entrada, text="Suma Enteros 1.0")
titulo.config(bg="thistle", fg="white", font=("Arial", 16))
titulo.place(x=240, y=10)

#------------------------------
# frame operaciones
#------------------------------
frame_operaciones= Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)

#------------------------------
# frame resultados
#------------------------------
frame_rojo= Frame(ventana_principal)
frame_rojo.config(bg="white", width=480, height=180)
frame_rojo.place(x=10, y=310)

# run
# se ejecuta el metodo mainlop() de la clase Tk () a través de la instancia ventana_principal. Este metodo despliega una ventana en la pantalla y queda a la espera de lo que el usuario haga (click en un botón, escrubir, etc). Cada acción del usuario se conoce como un evento. El método mainloop() es un bucle infinito.
ventana_principal.mainloop()