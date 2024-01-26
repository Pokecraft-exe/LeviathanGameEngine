import tkinter as tk
import os
root = tk.Tk()
root.title("Leviathan Game Engine ~ no project loaded")
root.geometry("720x500")

rightframe = tk.Frame(root, bg='red')
rightframe.pack(side="right", fill='both')

buttonNewProject = tk.Button(rightframe, text="New Project")
buttonNewProject.pack(side='bottom', fill='x')

buttonNewProject = tk.Button(rightframe, text="Open Project")
buttonNewProject.pack(side='top')

projectsframe = tk.Frame(root, bg='green')
projectsframe.pack(side="left", fill='both')



root.mainloop()