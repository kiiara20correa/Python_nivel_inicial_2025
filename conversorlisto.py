#Parte "visual"
from tkinter import Entry, messagebox, Label, Tk, StringVar, CENTER, ttk, Button
from PIL import Image, ImageTk  # para manejar imágenes

#Para generar la ventana 
ventana = Tk() 
ventana.configure(background= "light pink")
ventana.title("Conversor 𝓱𝓮𝓵𝓵𝓸 𝓴𝓲𝓽𝓽𝔂 ✿˖˚ ༘𐙚")
ventana.geometry("350x350")
ventana.resizable(False, False)

#Cargar imagen de fondo
imagen_fondo = Image.open("fondo.jpg")
imagen_fondo = imagen_fondo.resize((350, 350))# tamaño
fondo_tk = ImageTk.PhotoImage(imagen_fondo)

#Colocar imagen como fondo
label_fondo = Label(ventana, image=fondo_tk)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

#Texto dentro de la ventana
titulo = Label(ventana, text="♡ Conversor de Temperatura ♡", justify=CENTER, font=("Verdana", 15, "bold"), fg = "black", bg= "#fecee0")
titulo.grid(row=0, column=0, columnspan=2, pady=10)

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)

#MENÚ DESPLEGABLE 
opciones = ["Celsius", "Fahrenheit"]
#Menú izquierdo: ENTRADA
unidad_entrada = StringVar()
selector_entrada = ttk.Combobox(ventana, textvariable=unidad_entrada, values=opciones, state="readonly", width=10)
selector_entrada.grid(row=1, column=0, padx=10, pady=10)
selector_entrada.current(0)  # .current(): con él tomamos la poscion de la lista. Por defecto: Celsius
#Menú derecho: SALIDA
unidad_salida = StringVar()
selector_salida = ttk.Combobox(ventana, textvariable=unidad_salida, values=opciones, state="readonly", width=10)
selector_salida.grid(row=1, column=1, padx=10, pady=10)
selector_salida.current(1)  # Por defecto: Fahrenheit

#CAMPO DE ENTRADA para el usuario
entra = Entry(ventana)
entra.grid(row=2, column=0, ipadx=10, ipady=10, padx=10)

#CAMPO DE SALIDA
sale = Entry(ventana)
sale.grid(row=2, column=1, ipadx=10, ipady=10, padx=10)


#PARTE FUNCIONAL############################################################################################
def convertir_temperatura():
    valor_izq = entra.get().strip()
    valor_der = sale.get().strip()

    # Verificamos que no estén ambos llenos o vacíos
    if valor_izq and valor_der:
        messagebox.showwarning("Atención", "Ingresá el valor solo en uno de los campos")
        return
    if not valor_izq and not valor_der:
        messagebox.showwarning("Atención", "Ingresá algún valor para hacer la conversión")
        return
    
    # Determinar dirección: izquierda → derecha ...o derecha → izquierda
    if valor_izq:
        valor = valor_izq
        origen = unidad_entrada.get()
        destino = unidad_salida.get()
        campo_origen = entra
        campo_destino = sale
    else:
        valor = valor_der
        origen = unidad_salida.get()
        destino = unidad_entrada.get()
        campo_origen = sale
        campo_destino = entra

    # Verificar que sea un número válido
    #Pasar coma a punto solo si el usuario ingresa un número con coma:
    valor = valor.replace(",", ".")
    #Como se perimten números negativos, con coma o punto dejé de lado .isdigit()
    try:
        temperatura = float(valor)
    except ValueError:
        messagebox.showerror("ERROR", "Debe ingresar solo números")
        return
    # Conversión
    if origen == destino:
        messagebox.showinfo("Atención", "Seleccionaste la misma unidad en ambos campos.\nNo se realizará ninguna conversión.")
        resultado = temperatura
    elif origen == "Celsius" and destino == "Fahrenheit":
        resultado = temperatura * 9/5 + 32
    elif origen == "Fahrenheit" and destino == "Celsius":
        resultado = (temperatura - 32) * 5/9

    # Mostrar resultado
    campo_destino.delete(0, "end")
    campo_destino.insert(0, round(resultado, 2))

# Botón para hacer la conversión
boton = Button(ventana, text="Convertir", fg= "black", bg= "white", command= convertir_temperatura)
boton.grid(row=4, column=0, columnspan=2, pady= 10)

#COLOR
def actualizar_colores(event=None):
    for campo in (entra, sale):
        campo.configure(bg="#fe83af" if campo.get().strip() else "white")
entra.bind("<KeyRelease>", actualizar_colores)
sale.bind("<KeyRelease>", actualizar_colores)
  
#Al final de todas las lineas de configuración del entorno!!! 
ventana.mainloop() 
