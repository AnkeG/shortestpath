import tkinter as tk


	#print(algorithm.get(), progress.get())
	#pass

class controlpanel:

	def __init__(self):
		self.window = tk.Tk()
		self.window.title("Setting Panel")
		self.window.geometry('350x140')

		self.mouseframe = tk.Frame(self.window)
		self.mouselabel = tk.Label(self.mouseframe, text = 'Mouse:')
		self.mouselabel.grid(row = 0, column = 0, padx = 5, pady = 5)
		self.mousebutton = tk.Button(self.mouseframe, text = 'endpoints', command = self.toggle_mouse)
		self.mousebutton.grid(row = 0, column = 1, padx = 5)

		self.menuframe = tk.Frame(self.window)
		self.menulabel = tk.Label(self.menuframe, text = 'Algorithm:')
		self.menulabel.grid(row = 0, column = 0, padx = 5, pady = 5)
		self.menuoptions = ['dijkstra', 'a_star']
		self.algorithm = tk.StringVar(self.menuframe)
		self.algorithm.set(self.menuoptions[0])
		self.menuoptionmenu = tk.OptionMenu(self.menuframe, self.algorithm, *self.menuoptions) 
		self.menuoptionmenu.config(width = 8)
		self.menuoptionmenu.grid(row = 0, column = 1, padx =5)

		self.progress = tk.BooleanVar()
		self.checkbutton = tk.Checkbutton(self.window, text ='Show Progression', variable = self.progress, onvalue = True, offvalue = False )

		self.buttonsframe = tk.Frame(self.window)
		self.runbutton = tk.Button(self.buttonsframe, text = 'Run', command = self.run)
		self.runbutton.grid(row = 0, column = 0, padx = 5, pady = 5)
		self.resetbutton = tk.Button(self.buttonsframe, text = 'Reset', command = self.reset)
		self.resetbutton.grid(row = 0, column = 1, padx = 5, pady = 5)


		self.mouseframe.pack()
		self.menuframe.pack()
		self.checkbutton.pack()
		self.buttonsframe.pack()

		#window.mainloop()

	def toggle_mouse(self):
		if self.mousebutton['text'] == 'endpoints':
			self.mousebutton.configure(text = 'barriers')
		else:
			self.mousebutton.configure(text = 'endpoints')

	def run():
		pass

	def reset():
		pass

	def update(self):
		self.window.update_idletasks()
		self.window.update()

	def getsetting(self, setting):
		setting.algorithm = self.algorithm.get()
		setting.animation = self.progress.get()
		setting.mousefunction = self.mousebutton['text']
		return setting

if __name__ == "__main__":
	controlpanel = controlpanel()
	controlpanel.window.mainloop()