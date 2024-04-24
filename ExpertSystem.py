import tkinter as tk
from tkinter import ttk
from aima.utils import expr
from aima.logic import FolKB, fol_fc_ask
from ttkthemes import ThemedTk

# Knowledge Base
kb = FolKB()
kb.tell(expr('Beach(x)'))
kb.tell(expr('Historical(x)'))
kb.tell(expr('Nature(x)'))
kb.tell(expr('City(x)'))
kb.tell(expr('Secluded(x)'))
kb.tell(expr('Crowded(x)'))
kb.tell(expr('Luxurious(x)'))
kb.tell(expr('Cheap(x)'))
kb.tell(expr('Beach(x) & Secluded(x) & Cheap(x) ==> TichyBeach(x)'))
kb.tell(expr('Beach(x) & Crowded(x) & Cheap(x) ==> AiguadesBeach(x)'))
kb.tell(expr('Beach(x) & Secluded(x) & Luxurious(x) ==> ThaisBeach(x)'))
kb.tell(expr('Beach(x) & Crowded(x) & Luxurious(x) ==> AtlantisBeach(x)'))
kb.tell(expr('Historical(x) & Secluded(x) & Cheap(x) ==> BourdjMoussaMuseum(x)'))
kb.tell(expr('Historical(x) & Secluded(x)  & Luxurious(x) ==> EnchantedCave(x)'))
kb.tell(expr('Historical(x) & Crowded(x) & Cheap(x) ==> CasbahofBejaia(x)'))
kb.tell(expr('Historical(x) & Crowded(x) & Luxurious(x) ==> WaterMuseum(x)'))
kb.tell(expr('Nature(x) & Secluded(x) & Cheap(x) ==> KafridaWaterfalls(x)'))
kb.tell(expr('Nature(x) & Secluded(x) & Luxurious(x) ==> DarkLake(x)'))
kb.tell(expr('Nature(x) & Crowded(x) & Cheap(x) ==> CapCarbon(x)'))
kb.tell(expr('Nature(x) & Crowded(x) & Luxurious(x) ==> TiziNberbar(x)'))
kb.tell(expr('City(x) & Secluded(x) & Cheap(x) ==> Medina(x)'))
kb.tell(expr('City(x) & Secluded(x) & Luxurious(x) ==> TaosAmroucheCultureHouse(x)'))
kb.tell(expr('City(x) & Crowded(x) & Cheap(x) ==> PlaceGueydon(x)'))
kb.tell(expr('City(x) & Crowded(x) & Luxurious(x) ==> SoukElDjemaa(x)'))

# Agenda
agenda = []


def button_func():
    destinations = [var_1.get(), var_2.get(), var_3.get()]
    user = expr('Bejaia')
    agenda = [expr(destination + '(Bejaia)') for destination in destinations]

    memory = {}
    result = []

    for p in agenda:
        if fol_fc_ask(kb, expr(p)):
            memory[p] = True
        else:
            memory[p] = False

    if memory.get(expr('Beach(Bejaia)'), False) and memory.get(expr('Secluded(Bejaia)'), False) and memory.get(expr('Cheap(Bejaia)'), False):
        result.append(expr('TichyBeach(Bejaia)'))
    if memory.get(expr('Beach(Bejaia)'), False) and memory.get(expr('Crowded(Bejaia)'), False) and memory.get(expr('Cheap(Bejaia)'), False):
        result.append(expr('AiguadesBeach(Bejaia)'))
    if memory.get(expr('Beach(Bejaia)'), False) and memory.get(expr('Secluded(Bejaia)'), False) and memory.get(expr('Luxurious(Bejaia)'), False):
        result.append(expr('ThaisBeach(Bejaia)'))
    if memory.get(expr('Beach(Bejaia)'), False) and memory.get(expr('Crowded(Bejaia)'), False) and memory.get(expr('Luxurious(Bejaia)'), False):
        result.append(expr('AtlantisBeach(Bejaia)'))
    if memory.get(expr('Historical(Bejaia)'), False) and memory.get(expr('Secluded(Bejaia)'), False) and memory.get(expr('Cheap(Bejaia)'), False):
        result.append(expr('BourdjMoussaMuseum(Bejaia)'))
    if memory.get(expr('Historical(Bejaia)'), False) and memory.get(expr('Secluded(Bejaia)'), False) and memory.get(expr('Luxurious(Bejaia)'), False):
        result.append(expr('EnchantedCave(Bejaia)'))
    if memory.get(expr('Historical(Bejaia)'), False) and memory.get(expr('Crowded(Bejaia)'), False) and memory.get(expr('Cheap(Bejaia)'), False):
        result.append(expr('CasbahofBejaia(Bejaia)'))
    if memory.get(expr('Historical(Bejaia)'), False) and memory.get(expr('Crowded(Bejaia)'), False) and memory.get(expr('Luxurious(Bejaia)'), False):
        result.append(expr('WaterMuseum(Bejaia)'))
    if memory.get(expr('Nature(Bejaia)'), False) and memory.get(expr('Secluded(Bejaia)'), False) and memory.get(expr('Cheap(Bejaia)'), False):
        result.append(expr('KafridaWaterfalls(Bejaia)'))
    if memory.get(expr('Nature(Bejaia)'), False) and memory.get(expr('Secluded(Bejaia)'), False) and memory.get(expr('Luxurious(Bejaia)'), False):
        result.append(expr('DarkLake(Bejaia)'))
    if memory.get(expr('Nature(Bejaia)'), False) and memory.get(expr('Crowded(Bejaia)'), False) and memory.get(expr('Cheap(Bejaia)'), False):
        result.append(expr('CapCarbon(Bejaia)'))
    if memory.get(expr('Nature(Bejaia)'), False) and memory.get(expr('Crowded(Bejaia)'), False) and memory.get(expr('Luxurious(Bejaia)'), False):
        result.append(expr('TiziNberbar(Bejaia)'))
    if memory.get(expr('City(Bejaia)'), False) and memory.get(expr('Secluded(Bejaia)'), False) and memory.get(expr('Cheap(Bejaia)'), False):
        result.append(expr('Medina(Bejaia)'))
    if memory.get(expr('City(Bejaia)'), False) and memory.get(expr('Secluded(Bejaia)'), False) and memory.get(expr('Luxurious(Bejaia)'), False):
        result.append(expr('TaosAmroucheCultureHouse(Bejaia)'))
    if memory.get(expr('City(Bejaia)'), False) and memory.get(expr('Crowded(Bejaia)'), False) and memory.get(expr('Cheap(Bejaia)'), False):
        result.append(expr('PlaceGueydon(Bejaia)'))
    if memory.get(expr('City(Bejaia)'), False) and memory.get(expr('Crowded(Bejaia)'), False) and memory.get(expr('Luxurious(Bejaia)'), False):
        result.append(expr('SoukElDjemaa(Bejaia)'))

    

    # Clear any existing result labels
    for label in window.winfo_children():
        if isinstance(label, ttk.Label) and "Recommended destinations" in label.cget("text"):
            label.pack_forget()

    # Update the result label with the recommended destinations
    if result:
        result_str = ', '.join(str(expr) for expr in result)
        print(f"Recommended destinations: {result_str}")
        result_label = ttk.Label(window, text=f"Recommended destinations: {result_str}")
        result_label.pack(pady=10)
    else:
        print("No matching destinations found.")
        result_label = ttk.Label(window, text="No matching destinations found.")
        result_label.pack(pady=10)
# Create ThemedTk window
window = ThemedTk(theme="arc")
window.geometry('800x400')
window.title('Trip Recommender')

# Create frames and widgets
frame_1 = ttk.Frame(window)
l_intro = ttk.Label(frame_1, text='A personalised travel recommender. Answer the following questions:')
frame_1.pack()
l_intro.pack()

var_1 = tk.StringVar(value='Beach')
frame_2 = ttk.Frame(window)
label_1 = ttk.Label(frame_2, text='Preferred leisure activity:')
entry_1 = ttk.Combobox(frame_2, values=('Beach', 'Historical', 'Nature', 'City'), textvariable=var_1)
frame_2.pack(pady=10)
label_1.pack(side='left')
entry_1.pack(side='left')

var_2 = tk.StringVar(value='Secluded')
frame_3 = ttk.Frame(window)
label_2 = ttk.Label(frame_3, text='Preference for crowds:')
entry_2 = ttk.Combobox(frame_3, values=('Secluded', 'Crowded'), textvariable=var_2)
frame_3.pack(pady=10)
label_2.pack(side='left')
entry_2.pack(side='left')

var_3 = tk.StringVar(value='Cheap')
frame_4 = ttk.Frame(window)
label_3 = ttk.Label(frame_4, text='Budget preference:')
entry_3 = ttk.Combobox(frame_4, values=('Cheap', 'Luxurious'), textvariable=var_3)
frame_4.pack(pady=10)
label_3.pack(side='left')
entry_3.pack(side='left')

button = ttk.Button(window, text='See results', command=button_func)
button.config(style='Accent.TButton')
button.pack(pady=10)

window.mainloop()
