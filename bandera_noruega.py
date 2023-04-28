#------------------------------
# Bandera España
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
ventana_principal.title("Bandera de Francia")

# tamaño de la ventana
ventana_principal.geometry("800x430")

# deshabilitar boton maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="black")

#------------------------------
# frame rojo
#------------------------------
frame_rojo= Frame(ventana_principal)
frame_rojo.config(bg="red", width=800, height=480)
frame_rojo.place(x=0, y=0)

#------------------------------
# frame blanco1
#------------------------------
frame_blanco1= Frame(ventana_principal)
frame_blanco1.config(bg="white", width=130, height=480)
frame_blanco1.place(x=150, y=0)

#------------------------------
# frame blanco2
#------------------------------
frame_blanco2= Frame(ventana_principal)
frame_blanco2.config(bg="white", width=800, height=130)
frame_blanco2.place(x=0, y=150)

#------------------------------
# frame azul1
#------------------------------
frame_azul1= Frame(ventana_principal)
frame_azul1.config(bg="midnight blue", width=800, height=65)
frame_azul1.place(x=0, y=180)

#------------------------------
# frame azul2
#------------------------------
frame_azul2= Frame(ventana_principal)
frame_azul2.config(bg="midnight blue", width=65, height=480)
frame_azul2.place(x=180, y=0)

# run
# se ejecuta el metodo mainlop() de la clase Tk () a través de la instancia ventana_principal. Este metodo despliega una ventana en la pantalla y queda a la espera de lo que el usuario haga (click en un botón, escrubir, etc). Cada acción del usuario se conoce como un evento. El método mainloop() es un bucle infinito.
ventana_principal.mainloop()