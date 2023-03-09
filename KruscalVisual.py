import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Kruscal import kruskal

import networkx as nx
import matplotlib.pyplot as plt

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
def add():  # Los numeros ingresados deben ser convertidos a enteros para que el algoritmo los pueda usar
    node_a = int(node_a_entry.get())
    node_b = int(node_b_entry.get())
    weight = int(weight_entry.get())

    for n in nodes:
        # Verificar si la arista ya existe en la lista de nodos
        if (node_a == n[0] and node_b == n[1]) or (
                node_a == n[1] and node_b == n[0]):  # Compara las entradas con cada nodo ya ingresado
            messagebox.showerror("Error", "La arista ya existe en la tabla")
            return

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

    # Validar si hay al menos un elemento en la lista de nodos para habilitar el botón calcular arbol
    if len(nodes) > 0:
        calculate_button.config(state=tk.ACTIVE)


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


def calulate_tree():
    if len(nodes) == 0:
        print("La lista de nodos está vacía")
        return

    n = int(n_entry.get())
    tree = kruskal(n + 1, nodes)  # Necesitamos pasarle la cantidad de nodos +1 para que no se rompa el algoritmo
    print("Arbol mínimo:", tree)

    # Crear el grafo
    G = nx.Graph()
    for node in nodes:
        G.add_node(node[0])
        G.add_node(node[1])
        G.add_edge(node[0], node[1], weight=node[2])

    # Crear la figura y el plot
    fig, ax = plt.subplots(figsize=(8, 8))

    # Dibujar el grafo
    pos = nx.spring_layout(G, seed=42) # Obtener las posiciones de los nodos
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color='lightblue', node_size=1000)
    nx.draw_networkx_edges(G, pos, ax=ax, width=2, edge_color='grey')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'), ax=ax, font_size=14)

    # Dibujar los números de los nodos en rojo
    for node in G.nodes:
        nx.draw_networkx_labels(G, pos, labels={node: node}, font_color='red', font_size=14)

    # Mostrar la figura
    plt.show()


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

# Creacion del boton Calcular arbol mínimo
calculate_button = tk.Button(root, text="Calcular arbol mínimo", command=calulate_tree)
calculate_button.pack()
calculate_button.config(state=tk.DISABLED)

table.pack()
table_frame.pack()

# Ejecucion de la ventana
root.mainloop()
