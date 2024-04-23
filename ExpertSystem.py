import tkinter as tk
from tkinter import ttk
import numpy as np
from aima3.utils import *
from aima3.logic import *

#KB
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
kb.tell(expr('Historical(x) & Crowded(x) & Cheap(x) ==> CasbahofBéjaïa(x)'))
kb.tell(expr('Historical(x) & Crowded(x) & Luxurious(x) ==> WaterMuseum(x)'))
kb.tell(expr('Nature(x) & Secluded(x) & Cheap(x) ==> KafridaWaterfalls(x)'))
kb.tell(expr('Nature(x) & Secluded(x) & Luxurious(x) ==> DarkLake(x)'))
kb.tell(expr('Nature(x) & Crowded(x) & Cheap(x) ==> CapCarbon(x)'))
kb.tell(expr('Nature(x) & Crowded(x) & Luxurious(x) ==> TiziNberbar(x)'))
kb.tell(expr('City(x) & Secluded(x) & Cheap(x) ==> Medina(x)'))
kb.tell(expr('City(x) & Secluded(x) & Luxurious(x) ==> TaosAmroucheCultureHouse(x)'))
kb.tell(expr('City(x) & Crowded(x) & Cheap(x) ==> PlaceGueydon(x)'))
kb.tell(expr('City(x) & Crowded(x) & Luxurious(x) ==> SoukElDjemaa(x)'))


def button_func():
    query = expr(f'Target({var_1.get()},{var_2.get()},{var_3.get()},k)')
    r = fol_fc_ask(kb, query)
    result = list(r)
    value = list(result[0].values())
    frame_5 = ttk.Frame(window)
    label_r = ttk.Label(frame_5, text=f'The recommended destination is:')
    frame_5.pack()
    label_r.pack()
    frame_6 = ttk.Frame(window)
    a = ttk.Label(frame_6, text=f'{value}')
    frame_6.pack()
    a.pack()
    



window = tk.Tk()
window.geometry('800x400')
window.title('Trip recommender')
frame_1 = ttk.Frame(window)
l_intro = ttk.Label(frame_1, text='A personalised travel recommender, all you gotta do is answer on the three questions bellow :')
frame_1.pack()
l_intro.pack()

var_1 = tk.StringVar(value='x')
frame_2 = ttk.Frame(window)
label_1 = ttk.Label(frame_2, text='How do you prefer spending time during your vacations?')
entry_1 = ttk.Combobox(frame_2, values=('Beach','Historical','Nature','City'), textvariable= var_1)
frame_2.pack(pady=2)
label_1.pack(side='left')
entry_1.pack(side='left')

var_2 = tk.StringVar(value='y')
frame_3 = ttk.Frame(window)
label_2 = ttk.Label(frame_3, text='Do you prefer secluded spots or places with more tourist amenities?')
entry_2 = ttk.Combobox(frame_3, values=('Secluded','Crowded'), textvariable= var_2)
frame_3.pack(pady=2)
label_2.pack(side='left')
entry_2.pack(side='left')

var_3 = tk.StringVar(value='z')
frame_4 = ttk.Frame(window)
label_3 = ttk.Label(frame_4, text='Do you prefer budget-friendly options or are you willing to splurge for a unique experience?')
entry_3 = ttk.Combobox(frame_4, values=('Cheap','Luxurious'), textvariable= var_3)
frame_4.pack(pady=2)
label_3.pack(side='left')
entry_3.pack(side='left')

button = ttk.Button(window, text='See results', command= button_func)
button.pack()

window.mainloop()