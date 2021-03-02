import tkinter as tk

def mousefunction():
	print(algorithm.get(), progress.get())	
	#pass

def run():
	pass

def reset():
	pass

window = tk.Tk()
window.title("Setting Panel")
window.geometry('350x140')

mouseframe = tk.Frame(window)
mouselabel = tk.Label(mouseframe, text = 'mouse:')
mouselabel.grid(row = 0, column = 0, padx = 5, pady = 5)
mousebutton = tk.Button(mouseframe, text = 'Dijkstra', command = mousefunction)
mousebutton.grid(row = 0, column = 1, padx = 5)

menuframe = tk.Frame(window)
menulabel = tk.Label(menuframe, text = 'Algorithm: ')
menulabel.grid(row = 0, column = 0, padx = 5, pady = 5)
menuoptions = ['Dijkstra', 'A*']
algorithm = tk.StringVar(menuframe)
algorithm.set(menuoptions[0])
menuoptionmenu = tk.OptionMenu(menuframe, algorithm, *menuoptions)
menuoptionmenu.config(width = 8)
menuoptionmenu.grid(row = 0, column = 1, padx =5)

progress = tk.BooleanVar()
checkbutton = tk.Checkbutton(window, text ='Show Progression', variable = progress, onvalue = True, offvalue = False )

buttonsframe = tk.Frame(window)
runbutton = tk.Button(buttonsframe, text = 'Run', command = run)
runbutton.grid(row = 0, column = 0, padx = 5, pady = 5)
resetbutton = tk.Button(buttonsframe, text = 'Reset', command = reset)
resetbutton.grid(row = 0, column = 1, padx = 5, pady = 5)


mouseframe.pack()
menuframe.pack()
checkbutton.pack()
buttonsframe.pack()

window.mainloop()