import tkinter as tk
import random

def mover_serpiente():
    global direccion, juego_activo
    if not juego_activo: return
    x, y = serpiente[0]
    if direccion == "arriba": y -= 10
    elif direccion == "abajo": y += 10
    elif direccion == "izquierda": x -= 10
    elif direccion == "derecha": x += 10
    nueva_cabeza = (x, y)
    if nueva_cabeza in serpiente[1:] or not (0 <= x < 400 and 0 <= y < 400):
        juego_activo = False
        resultado_label.config(text="¡Perdiste! Reinicia para jugar.")
        return
    if nueva_cabeza == comida:
        serpiente.append(serpiente[-1])
        generar_comida()
    serpiente.insert(0, nueva_cabeza)
    serpiente.pop()
    canvas.delete("all")
    dibujar_serpiente()
    dibujar_comida()
    ventana.after(100, mover_serpiente)

def dibujar_serpiente():
    for x, y in serpiente:
        canvas.create_rectangle(x, y, x + 10, y + 10, fill="blue")

def dibujar_comida():
    canvas.create_rectangle(comida[0], comida[1], comida[0] + 10, comida[1] + 10, fill="red")

def generar_comida():
    global comida
    comida = (random.randint(0, 39) * 10, random.randint(0, 39) * 10)

def cambiar_direccion(nueva_direccion):
    global direccion
    if (nueva_direccion == "arriba" and direccion != "abajo") or \
       (nueva_direccion == "abajo" and direccion != "arriba") or \
       (nueva_direccion == "izquierda" and direccion != "derecha") or \
       (nueva_direccion == "derecha" and direccion != "izquierda"):
        direccion = nueva_direccion

def reiniciar_juego():
    global serpiente, direccion, comida, juego_activo
    serpiente = [(200, 200), (190, 200), (180, 200)]
    direccion = "derecha"
    comida = (random.randint(0, 39) * 10, random.randint(0, 39) * 10)
    juego_activo = True
    resultado_label.config(text="¡Juega! Usa las flechas.")
    mover_serpiente()

ventana = tk.Tk()
ventana.title("Serpiente")
canvas = tk.Canvas(ventana, width=400, height=400, bg="black")
canvas.pack()

resultado_label = tk.Label(ventana, text="¡Juega! Usa las flechas.", font=("Arial", 14))
resultado_label.pack()

ventana.bind("<Up>", lambda event: cambiar_direccion("arriba"))
ventana.bind("<Down>", lambda event: cambiar_direccion("abajo"))
ventana.bind("<Left>", lambda event: cambiar_direccion("izquierda"))
ventana.bind("<Right>", lambda event: cambiar_direccion("derecha"))

boton_reiniciar = tk.Button(ventana, text="Reiniciar Juego", command=reiniciar_juego)
boton_reiniciar.pack()

reiniciar_juego()
ventana.mainloop()
