import tkinter as tk
from LGE_IDE_assets.ListImageItemCollapsable import *
import json
import os

repo = ""
bgcolor = "#211111"
imageFile = []
imageFolder = None

def loadExplorer(winroot: tk.Tk, projectName):
    global repo, imageFile, imageFolder
    imageFile = [ImageTk.PhotoImage(Image.open("LGE_IDE_assets/file.png")), ImageTk.PhotoImage(Image.open("LGE_IDE_assets/json.png")), ImageTk.PhotoImage(Image.open("LGE_IDE_assets/cpp.png")), ImageTk.PhotoImage(Image.open("LGE_IDE_assets/obj.png")), ImageTk.PhotoImage(Image.open("LGE_IDE_assets/png.png"))]
    imageFolder = ImageTk.PhotoImage(Image.open("LGE_IDE_assets/folder.png"))
    solutionExplorer = tk.Frame(winroot)
    solutionExplorer.pack(side="left")
    filesList = ListImageItemCollapsable(solutionExplorer, projectName, imageFolder, bgcolor, "white", width=100, height=500)
    i=0
    for root, dirs, files in os.walk(repo):
        level = root.replace(repo, '').count(os.sep)
        indent = ' ' * 4 * (level)
        dir = filesList.insert('{}{}/'.format(indent, os.path.basename(root)), imageFolder, True)
        subindent = ' ' * 4 * (level + 1)
        i+=1
        for f in files:
            filename = os.path.basename(f)
            if os.path.splitext(filename)[1] == '.json':
                dir[0].insert('{}{}'.format(subindent, filename), imageFile[1], False)
            elif os.path.splitext(filename)[1] == '.cpp':
                dir[0].insert('{}{}'.format(subindent, filename), imageFile[2], False)
            elif os.path.splitext(filename)[1] == '.obj':
                dir[0].insert('{}{}'.format(subindent, filename), imageFile[3], False)
            elif os.path.splitext(filename)[1] == '.png':
                dir[0].insert('{}{}'.format(subindent, filename), imageFile[4], False)
            else:
                dir[0].insert('{}{}'.format(subindent, filename), imageFile[0], False)
            i+=1
    filesList.pack()

def loadFrames(root, projectName):
    bottomFrame = tk.Frame(root, bg=bgcolor, highlightthickness=1, borderwidth=1)
    bottomFrame.pack(side="bottom", fill='x')

    topframe = tk.Frame(root, bg=bgcolor, highlightthickness=1, borderwidth=1)
    topframe.pack(side="top", fill='x')

    rightframe = tk.Frame(topframe, bg=bgcolor, highlightthickness=1, borderwidth=1)
    rightframe.pack(side="right", fill='y')
    loadExplorer(rightframe, projectName.get())

def loadProject(projectName):
    global repo
    root = tk.Tk()
    root.geometry("%dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight()))
    root.state('zoomed')
    root.title("Leviathan Game Engine 2024 ~ " + projectName.get())
    repo = f"Projects/{projectName.get()}/"
    loadFrames(root, projectName)
    root.mainloop()

def loadNewProject(projectName):
    data = {
        "version": "2024",
        "language": "c++14",
        "engine": "SDLGameEngine"
    }
    with open("Projects/" + projectName.get() + "/project.json", "w") as f:
        json.dump(data, f)
    loadProject(projectName)
    return