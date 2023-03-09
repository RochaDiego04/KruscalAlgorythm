import tkinter as tk
from tkinter import ttk

# Crear ventana
root = tk.Tk()
root.title("Algoritmo de Kruskal")
root.geometry("400x400")

# Crear label superior
n_label = tk.Label(root, text="Introduzca el número de nodos:")
n_label.pack()

n_entry = tk.Entry(root)
n_entry.pack()

table_frame = tk.Frame(root)

# Creacion de la tabla
table = ttk.Treeview(table_frame, columns=("start_node", "end_node", "weight"), show="headings")
table.heading("start_node", text="Nodo de inicio")
table.heading("end_node", text="Nodo de destino")
table.heading("weight", text="Peso")

# Lista para almacenar los nodos
nodes = []

# Funcion para agregar fila a la tabla
def add():
    node_a = node_a_entry.get()
    node_b = node_b_entry.get()
    weight = weight_entry.get()

    # Crear un tuple con los datos y agregarlo a la lista de nodos
    node = (node_a, node_b, weight)
    nodes.append(node)
    print("Lista de nodos:", nodes)

    # Agregar la fila a la tabla
    table.insert("", tk.END, values=node)

    # Limpiar formulario
    node_a_entry.delete(0, tk.END)
    node_b_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)


# Creacion del formulario
node_a_label = tk.Label(root, text="Nodo de inicio:")
node_a_entry = tk.Entry(root)
node_b_label = tk.Label(root, text="Nodo de destino:")
node_b_entry = tk.Entry(root)
weight_label = tk.Label(root, text="Peso:")
weight_entry = tk.Entry(root)

add_button = tk.Button(root, text="Agregar", command=add)


# Funcion del boton
def on_confirm_n():
    try:
        n = int(n_entry.get())
        print(f"El usuario introdujo {n} nodos")

        # Mostrar la tabla
        table_frame.pack()

        # Mostrar formulario
        node_a_label.pack()
        node_a_entry.pack()
        node_b_label.pack()
        node_b_entry.pack()
        weight_label.pack()
        weight_entry.pack()
        add_button.pack()
        confirm_button.config(state=tk.DISABLED)
    except ValueError:
        print("Introduzca un número entero válido")


# Ocultar el formulario
node_a_label.pack_forget()
node_a_entry.pack_forget()
node_b_label.pack_forget()
node_b_entry.pack_forget()
weight_label.pack_forget()
weight_entry.pack_forget()
add_button.pack_forget()

# Ocultar la tabla
table_frame.pack_forget()

# Creacion del boton Confirmar
confirm_button = tk.Button(root, text="Confirmar", command=on_confirm_n)
confirm_button.pack()

table.pack()
table_frame.pack()

root.mainloop()
