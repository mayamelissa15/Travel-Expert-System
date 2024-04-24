import tkinter as tk
from tkinter import ttk
from aima.utils import expr
from aima.logic import FolKB, fol_fc_ask
from ttkthemes import ThemedTk

# Base de connaissances
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

# Initialisation de l'agenda
agenda = []

# Fonction de traitement du bouton
def button_func():
    destinations = [var_1.get(), var_2.get(), var_3.get()]
    user = expr('Bejaia')
    agenda = [expr(destination + '(Bejaia)') for destination in destinations]

    memory = {}
    result = []

    # Analyse de chaque destination
    for p in agenda:
        if fol_fc_ask(kb, expr(p)):
            memory[p] = True
        else:
            memory[p] = False

    # Recherche des destinations recommandées en fonction des préférences
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

    # Effacer les labels de résultat existants
    for label in window.winfo_children():
        if isinstance(label, ttk.Label) and "Recommended destinations" in label.cget("text"):
            label.pack_forget()

    # Mise à jour du label de résultat avec les destinations recommandées
    if result:
        result_str = ', '.join(str(expr) for expr in result)
        print(f"Destinations recommandées : {result_str}")
        explanation = generate_explanation(result)  # Générer l'explication
        result_label = ttk.Label(window, text=f"Destinations recommandées : {result_str}\n{explanation}")
        result_label.pack(pady=10)
    else:
        print("Aucune destination correspondante trouvée.")
        result_label = ttk.Label(window, text="Aucune destination correspondante trouvée.")
        result_label.pack(pady=10)

# Générer l'explication pour les destinations recommandées
def generate_explanation(destinations):
    explanation = ""
    for destination in destinations:
        if destination == expr('TichyBeach(Bejaia)'):
            explanation += "TichyBeach a été recommandé en raison de sa plage isolée et bon marché.\n"
        elif destination == expr('AiguadesBeach(Bejaia)'):
            explanation += "AiguadesBeach a été recommandé en raison de sa plage bondée et bon marché.\n"
        elif destination == expr('ThaisBeach(Bejaia)'):
            explanation += "ThaisBeach a été recommandé en raison de sa plage isolée et luxueuse.\n"
        elif destination == expr('AtlantisBeach(Bejaia)'):
            explanation += "AtlantisBeach a été recommandé en raison de sa plage bondée et luxueuse.\n"
        elif destination == expr('BourdjMoussaMuseum(Bejaia)'):
            explanation += "BourdjMoussaMuseum a été recommandé pour son caractère historique, sa tranquillité et son prix abordable.\n"
        elif destination == expr('EnchantedCave(Bejaia)'):
            explanation += "EnchantedCave a été recommandé pour son caractère historique, sa tranquillité et son luxe.\n"
        elif destination == expr('CasbahofBejaia(Bejaia)'):
            explanation += "CasbahofBejaia a été recommandé pour son caractère historique, sa foule et son prix abordable.\n"
        elif destination == expr('WaterMuseum(Bejaia)'):
            explanation += "WaterMuseum a été recommandé pour son caractère historique, sa foule et son luxe.\n"
        elif destination == expr('KafridaWaterfalls(Bejaia)'):
            explanation += "KafridaWaterfalls a été recommandé pour son aspect naturel, sa tranquillité et son prix abordable.\n"
        elif destination == expr('DarkLake(Bejaia)'):
            explanation += "DarkLake a été recommandé pour son aspect naturel, sa tranquillité et son luxe.\n"
        elif destination == expr('CapCarbon(Bejaia)'):
            explanation += "CapCarbon a été recommandé pour son aspect naturel, sa foule et son prix abordable.\n"
        elif destination == expr('TiziNberbar(Bejaia)'):
            explanation += "TiziNberbar a été recommandé pour son aspect naturel, sa foule et son luxe.\n"
        elif destination == expr('Medina(Bejaia)'):
            explanation += "Medina a été recommandé pour son aspect urbain, sa tranquillité et son prix abordable.\n"
        elif destination == expr('TaosAmroucheCultureHouse(Bejaia)'):
            explanation += "TaosAmroucheCultureHouse a été recommandé pour son aspect urbain, sa tranquillité et son luxe.\n"
        elif destination == expr('PlaceGueydon(Bejaia)'):
            explanation += "PlaceGueydon a été recommandé pour son aspect urbain, sa foule et son prix abordable.\n"
        elif destination == expr('SoukElDjemaa(Bejaia)'):
            explanation += "SoukElDjemaa a été recommandé pour son aspect urbain, sa foule et son luxe.\n"
        # Ajouter d'autres explications pour les autres destinations ici
    return explanation

# Créer la fenêtre ThemedTk
window = ThemedTk(theme="arc")
window.geometry('800x400')
window.title('Recommandateur de voyages')

# Créer les cadres et les widgets
frame_1 = ttk.Frame(window)
l_intro = ttk.Label(frame_1, text='Un recommandateur de voyages personnalisé. Répondez aux questions suivantes :')
frame_1.pack()
l_intro.pack()

var_1 = tk.StringVar(value='Beach')
frame_2 = ttk.Frame(window)
label_1 = ttk.Label(frame_2, text='Activité de loisir préférée :')
entry_1 = ttk.Combobox(frame_2, values=('Beach', 'Historical', 'Nature', 'City'), textvariable=var_1)
frame_2.pack(pady=10)
label_1.pack(side='left')
entry_1.pack(side='left')

var_2 = tk.StringVar(value='Secluded')
frame_3 = ttk.Frame(window)
label_2 = ttk.Label(frame_3, text='Préférence pour les foules :')
entry_2 = ttk.Combobox(frame_3, values=('Secluded', 'Crowded'), textvariable=var_2)
frame_3.pack(pady=10)
label_2.pack(side='left')
entry_2.pack(side='left')

var_3 = tk.StringVar(value='Cheap')
frame_4 = ttk.Frame(window)
label_3 = ttk.Label(frame_4, text='Préférence budgétaire :')
entry_3 = ttk.Combobox(frame_4, values=('Cheap', 'Luxurious'), textvariable=var_3)
frame_4.pack(pady=10)
label_3.pack(side='left')
entry_3.pack(side='left')

button = ttk.Button(window, text='Voir les résultats', command=button_func)
button.config(style='Accent.TButton')
button.pack(pady=10)

window.mainloop()
