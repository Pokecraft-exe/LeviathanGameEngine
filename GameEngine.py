import tkinter as tk
import os
root = tk.Tk()
root.title("Leviathan Game Engine ~ no project loaded")
root.geometry("720x500")

rightframe = tk.Frame(root, bg='red')
rightframe.pack(side="right", fill='both')

projectsframe = tk.Frame(root, bg='red')
projectsframe.pack(side="right", fill='both')

root.mainloop()