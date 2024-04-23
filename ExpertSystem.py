import tkinter as tk
from tkinter import ttk
import numpy as np
from aima.utils import *
from aima.logic import *

#KB
kb = FolKB()
kb.tell(expr('Target(x)'))
kb.tell(expr('Leisure(x)'))
kb.tell(expr('Preference(x)'))
kb.tell(expr('Cost(x)'))
kb.tell(expr('Leisure(Beach)'))
kb.tell(expr('Leisure(Historical)'))
kb.tell(expr('Leisure(Nature)'))
kb.tell(expr('Leisure(City)'))
kb.tell(expr('Preference(Secluded)'))
kb.tell(expr('Preference(Crowded)'))
kb.tell(expr('Cost(Cheap)'))
kb.tell(expr('Cost(Luxurious)'))
kb.tell(expr('Leisure(x) & Preference(y) & Cost(z) ==> Target(k)'))
kb.tell(expr('Leisure(Beach) & Preference(Secluded) & Cost(Cheap) ==> Target(Beach,Secluded,Cheap,Tichy_Beach)'))
kb.tell(expr('Leisure(Beach) & Preference(Secluded) & Cost(Luxurious) ==> Target(Beach,Secluded,Luxurious,Thais_Beach)'))
kb.tell(expr('Leisure(Beach) & Preference(Crowded) & Cost(Cheap) ==> Target(Beach,Crowded,Cheap,Les_Aiguades_Beach)'))
kb.tell(expr('Leisure(Beach) & Preference(Crowded) & Cost(Luxurious) ==> Target(Beach,Crowded,Luxurious,Atlantis_Beach)'))
kb.tell(expr('Leisure(Historical) & Preference(Secluded) & Cost(Cheap) ==> Target(Historical,Secluded,Cheap,Bourdj_Moussa_Museum)'))
kb.tell(expr('Leisure(Historical) & Preference(Secluded) & Cost(Luxurious) ==> Target(Historical,Secluded,Luxurious,Enchanted_cave)'))
kb.tell(expr('Leisure(Historical) & Preference(Crowded) & Cost(Cheap) ==> Target(Historical,Crowded,Cheap,Casbah_of_Béjaïa)'))
kb.tell(expr('Leisure(Historical) & Preference(Crowded) & Cost(Luxurious) ==> Target(Historical,Crowded,Luxurious,Water_Museum)'))
kb.tell(expr('Leisure(Nature) & Preference(Secluded) & Cost(Cheap) ==> Target(Nature,Secluded,Cheap,Kafrida_Waterfalls)'))
kb.tell(expr('Leisure(Nature) & Preference(Secluded) & Cost(Luxurious) ==> Target(Nature,Secluded,Luxurious,Dark_Lake)'))
kb.tell(expr('Leisure(Nature) & Preference(Crowded) & Cost(Cheap) ==> Target(Nature,Crowded,Cheap,Cap_Carbon)'))
kb.tell(expr('Leisure(Nature) & Preference(Crowded) & Cost(Luxurious) ==> Target(Nature,Crowded,Luxurious,Tizi_Nberbar)'))
kb.tell(expr('Leisure(City) & Preference(Secluded) & Cost(Cheap) ==> Target(City,Secluded,Cheap,Medina)'))
kb.tell(expr('Leisure(City) & Preference(Secluded) & Cost(Luxurious) ==> Target(City,Secluded,Luxurious,Taos_Amrouche_Culture_House)'))
kb.tell(expr('Leisure(City) & Preference(Crowded) & Cost(Cheap) ==> Target(City,Crowded,Cheap,Place_Gueydon)'))
kb.tell(expr('Leisure(City) & Preference(Crowded) & Cost(Luxurious) ==> Target(City,Crowded,Luxurious,Souk_El_Djemaa)'))

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