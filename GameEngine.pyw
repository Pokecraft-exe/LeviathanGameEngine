import tkinter as tk
from projectSolution import loadProject, loadNewProject
import os

bgcolor = "#211111"

def openProject():
    global currentProjects, root, projectName
    selectedProject = currentProjects.curselection()
    if (selectedProject == ()):
        print("no projects selected")
    else:
        projectName.set(currentProjects.selection_get())
        root.destroy()
        loadProject(projectName)

def newProject():
    global projectName, root
    os.mkdir("Projects/" + projectName.get())
    root.destroy()
    loadNewProject(projectName)

root = tk.Tk()
root.configure(bg=bgcolor)
root.resizable(False, False)
root.title("Leviathan Game Engine 2024")
root.geometry("360x250")
root.iconbitmap(default="icon.ico")
projectName = tk.StringVar()

rightframe = tk.Frame(root, bg=bgcolor)
rightframe.pack(side="right", fill='both')

getStartedLabel = tk.Label(rightframe, text= "Get Started", bg=bgcolor, fg='white')
getStartedLabel.pack()

buttonNewProject = tk.Button(rightframe, text="New Project", bg='#332222', fg='white', command=newProject, highlightthickness=0, borderwidth=0)
buttonNewProject.pack(fill='x')

buttonOpenProject = tk.Button(rightframe, text="Open Project", bg='#332222', fg='white', command=openProject, highlightthickness=0, borderwidth=0)
buttonOpenProject.pack(fill='x')

projectNameLabel = tk.Label(rightframe, text= "New Project Name:", bg=bgcolor, fg='white')
projectNameLabel.pack()

textBoxNameProject = tk.Entry(rightframe, textvariable=projectName, bg='#332222', fg='white', highlightthickness=1, borderwidth=1)
textBoxNameProject.pack()

projectsframe = tk.Frame(root, bg=bgcolor)
projectsframe.pack(side="left", fill='both')

openRecentLabel = tk.Label(projectsframe, text="Open Recent", bg=bgcolor, fg='white')
openRecentLabel.pack(fill='y')

currentProjects = tk.Listbox(projectsframe, bg=bgcolor, fg='white', highlightthickness=0, borderwidth=0, selectbackground="#332222")
if ('Projects' in os.listdir('./')) :
    for i, dir in enumerate(os.listdir('./Projects')):
        currentProjects.insert(i, dir)
    currentProjects.pack()
else:
    currentProjects = tk.Label(projectsframe, text="No projects created", bg=bgcolor, fg='white')
    currentProjects.pack()
    os.mkdir('Projects')

root.mainloop()