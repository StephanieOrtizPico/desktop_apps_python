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
ventana_principal.geometry("800x480")

# deshabilitar boton maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="black")

#------------------------------
# frame rojo1
#------------------------------
frame_rojo1= Frame(ventana_principal)
frame_rojo1.config(bg="red", width=800, height=120)
frame_rojo1.place(x=0, y=0)

#------------------------------
# frame amarillo
#------------------------------
frame_amarillo= Frame(ventana_principal)
frame_amarillo.config(bg="yellow", width=800, height=240)
frame_amarillo.place(x=0, y=120)

#------------------------------
# frame rojo2
#------------------------------
frame_rojo2= Frame(ventana_principal)
frame_rojo2.config(bg="red", width=800, height=120)
frame_rojo2.place(x=0, y=360)

#------------------------------
# frame blanco
#------------------------------
frame_blanco= Frame(ventana_principal)
frame_blanco.config(bg="white", width=100, height=100)
frame_blanco.place(x=150, y=190)

# run
# se ejecuta el metodo mainlop() de la clase Tk () a través de la instancia ventana_principal. Este metodo despliega una ventana en la pantalla y queda a la espera de lo que el usuario haga (click en un botón, escrubir, etc). Cada acción del usuario se conoce como un evento. El método mainloop() es un bucle infinito.
ventana_principal.mainloop()