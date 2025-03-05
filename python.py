import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk 
class TiendaHotWheels:
    def __init__(self, root):
        self.root = root
        self.root.title(" Tienda de Hot Wheels")
        self.root.geometry("600x500")
        self.root.configure(bg="#222")  

        self.inventario = {
        }

        self.titulo = tk.Label(root, text=" Tienda de Hot Wheels", font=("Arial", 18, "bold"), fg="white", bg="#222")
        self.titulo.pack(pady=10)

        self.frame = tk.Frame(root, bg="#222")
        self.frame.pack()

        self.mostrar_inventario()

        self.boton_agregar = tk.Button(root, text=" Agregar Modelo", command=self.agregar_modelo, bg="green", fg="white", font=("Arial", 12))
        self.boton_agregar.pack(pady=5)

        self.boton_vender = tk.Button(root, text=" Vender Modelo", command=self.vender_modelo, bg="red", fg="white", font=("Arial", 12))
        self.boton_vender.pack(pady=5)

    def mostrar_inventario(self):
        
        for widget in self.frame.winfo_children():
            widget.destroy()  

        for modelo, datos in self.inventario.items():
            frame_modelo = tk.Frame(self.frame, bg="#333", padx=10, pady=5)
            frame_modelo.pack(pady=5, fill="x")

           
            try:
                imagen = Image.open(datos["imagen"])
                imagen = imagen.resize((80, 50))
                img = ImageTk.PhotoImage(imagen)
                label_imagen = tk.Label(frame_modelo, image=img, bg="#333")
                label_imagen.image = img  
                label_imagen.pack(side="left", padx=10)
            except:
                label_imagen = tk.Label(frame_modelo, text=" ", font=("Arial", 24), bg="#333", fg="white")
                label_imagen.pack(side="left", padx=10)

            info = f"{modelo} | ${datos['precio']} | Stock: {datos['cantidad']}"
            label_texto = tk.Label(frame_modelo, text=info, font=("Arial", 12), fg="white", bg="#333")
            label_texto.pack(side="left")

    def agregar_modelo(self):
      
        nombre = simpledialog.askstring("Agregar Modelo", "Nombre del modelo:")
        if not nombre:
            return

        precio = simpledialog.askfloat("Agregar Modelo", "Precio del modelo:")
        cantidad = simpledialog.askinteger("Agregar Modelo", "Cantidad disponible:")

        if nombre in self.inventario:
            self.inventario[nombre]["cantidad"] += cantidad
        else:
            self.inventario[nombre] = {"precio": precio, "cantidad": cantidad, "imagen": "default.png"}

        messagebox.showinfo("✅ Éxito", f"{cantidad} unidades de '{nombre}' agregadas.")
        self.mostrar_inventario()

    def vender_modelo(self):
       
        nombre = simpledialog.askstring("Vender Modelo", "Nombre del modelo:")
        if not nombre or nombre not in self.inventario:
            messagebox.showerror(" Error", "Modelo no encontrado.")
            return

        cantidad = simpledialog.askinteger("Vender Modelo", "Cantidad a vender:")
        if cantidad > self.inventario[nombre]["cantidad"]:
            messagebox.showerror(" Error", f"Sólo hay {self.inventario[nombre]['cantidad']} disponibles.")
            return

        self.inventario[nombre]["cantidad"] -= cantidad
        if self.inventario[nombre]["cantidad"] == 0:
            del self.inventario[nombre]

        messagebox.showinfo("Venta Exitosa", f"Se vendieron {cantidad} unidades de '{nombre}'.")
        self.mostrar_inventario()


root = tk.Tk()
app = TiendaHotWheels(root)
root.mainloop()
