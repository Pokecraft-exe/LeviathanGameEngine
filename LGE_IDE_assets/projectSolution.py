import tkinter as tk
from LGE_IDE_assets.ListImageItemCollapsable import *
from LGE_IDE_assets.Terminal import *
import json
import os

repo = ""
bgcolor = "#211111"
imageFile = []
imageFolder = None
rightMenuShown = False
rightMenu = None

def loadRightClick(event, root, parent):
    global rightMenuShown, rightMenu
    unloadRightMenu()
    rightMenuShown = True
    x = root.winfo_pointerx()
    y = root.winfo_pointery()
    sizex = root.winfo_screenwidth()
    sizey = root.winfo_screenheight()
    if x + 110 < sizex:
        rightmenu = tk.Toplevel(root)
        rightmenu.geometry(f"100x200+{x}+{y}")    
        rightmenu.overrideredirect(1)
        rightMenu = rightmenu
    else:
        rightmenu = tk.Toplevel(root)
        rightmenu.geometry(f"100x200+{x-110}+{y}")    
        rightmenu.overrideredirect(1)
        rightMenu = rightmenu
    return

def unloadRightMenu():
    global rightMenuShown, rightMenu
    if rightMenuShown:
        rightMenuShown = False
        rightMenu.destroy()
    return

def walkDirs(folder):
    dirs = []
    files = []
    for f in os.listdir(folder):
        if os.path.splitext(f)[1] == '':
            dirs.append(f)
        else:
            files.append(f)
    print(dirs)
    return dirs

def walkFiles(folder):
    dirs = []
    files = []
    for f in os.listdir(folder):
        if os.path.splitext(f)[1] == '':
            dirs.append(f)
        else:
            files.append(f)
    return files

def insertSolutionExplorer(parent, src):
    for dir in walkDirs(src):
        inserted = parent.insert('{}/'.format(os.path.basename(dir)), imageFolder, True)
        for subdirs in walkDirs(src + '/' + dir):
            insertSolutionExplorer(inserted[0], src + '/' + dir)
        for f in walkFiles(src+'/'+dir):
            filename = os.path.basename(f)
            if os.path.splitext(filename)[1] == '.json':
                inserted[0].insert('{}'.format(filename), imageFile[1], False)
            elif os.path.splitext(filename)[1] == '.cpp':
                inserted[0].insert('{}'.format(filename), imageFile[2], False)
            elif os.path.splitext(filename)[1] == '.obj':
                inserted[0].insert('{}'.format(filename), imageFile[3], False)
            elif os.path.splitext(filename)[1] == '.png':
                inserted[0].insert('{}'.format(filename), imageFile[4], False)
            else:
                inserted[0].insert('{}'.format(filename), imageFile[0], False)
    for f in walkFiles(src):
        filename = os.path.basename(f)
        if os.path.splitext(filename)[1] == '.json':
            parent.insert('{}'.format(filename), imageFile[1], False)
        elif os.path.splitext(filename)[1] == '.cpp':
            parent.insert('{}'.format(filename), imageFile[2], False)
        elif os.path.splitext(filename)[1] == '.obj':
            parent.insert('{}'.format(filename), imageFile[3], False)
        elif os.path.splitext(filename)[1] == '.png':
            parent.insert('{}'.format(filename), imageFile[4], False)
        else:
            parent.insert('{}'.format(filename), imageFile[0], False)

def loadExplorer(winroot: tk.Tk, projectName):
    global repo, imageFile, imageFolder

    imageFile = [ImageTk.PhotoImage(Image.open("LGE_IDE_assets/file.png")), ImageTk.PhotoImage(Image.open("LGE_IDE_assets/json.png")), ImageTk.PhotoImage(Image.open("LGE_IDE_assets/cpp.png")), ImageTk.PhotoImage(Image.open("LGE_IDE_assets/obj.png")), ImageTk.PhotoImage(Image.open("LGE_IDE_assets/png.png"))]
    imageFolder = ImageTk.PhotoImage(Image.open("LGE_IDE_assets/folder.png"))

    solutionExplorer = tk.Frame(winroot)
    solutionExplorer.pack(side="left")

    filesList = ListImageItemCollapsable(solutionExplorer, "Solution Explorer", imageFolder, bgcolor, "white", width=100, height=500)

    print("repo:", repo)
    insertSolutionExplorer(filesList, repo[:-1])

    filesList.bind_cascade("<Button-3>", lambda e: loadRightClick(e, winroot, filesList))
    filesList.pack()

def loadTerminal(winroot : tk.Tk):
    terminalFrame = tk.Frame(winroot)
    terminalFrame.pack(side="bottom", fill="x")

    terminal = Terminal(terminalFrame, bg=bgcolor, fg="white")
    terminal.pack(fill='x')

    

def loadFrames(root, projectName):
    bottomFrame = tk.Frame(root, bg=bgcolor, highlightthickness=1, borderwidth=1)
    bottomFrame.pack(side="bottom", fill='x')

    topframe = tk.Frame(root, bg=bgcolor, highlightthickness=1, borderwidth=1)
    topframe.pack(side="top", fill='x')

    rightframe = tk.Frame(topframe, bg=bgcolor, highlightthickness=1, borderwidth=1)
    rightframe.pack(side="right", fill='y')

    loadTerminal(bottomFrame)
    loadExplorer(rightframe, projectName.get())

def loadProject(projectName):
    global repo
    root = tk.Tk()
    root.geometry("%dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight()))
    root.state('zoomed')
    root.title("Leviathan Game Engine 2024 ~ " + projectName.get())
    root.bind_all("<Button-1>", lambda e: unloadRightMenu())
    repo = f"Projects/{projectName.get()}/"

    menu = tk.Menu(root)

    FileMenu = tk.Menu(menu, tearoff=False)
    EditMenu = tk.Menu(menu, tearoff=False)
    ProjectMenu = tk.Menu(menu, tearoff=False)
    BuildMenu = tk.Menu(menu, tearoff=False)
    ToolsMenu = tk.Menu(menu, tearoff=False)
    ExtentionsMenu = tk.Menu(menu, tearoff=False)
    HelpMenu = tk.Menu(menu, tearoff=False)

    menu.add_cascade(label="File", menu=FileMenu)
    menu.add_cascade(label="Edit", menu=EditMenu)
    menu.add_cascade(label="Project", menu=ProjectMenu)
    menu.add_cascade(label="Build", menu=BuildMenu)
    menu.add_cascade(label="Tools", menu=ToolsMenu)
    menu.add_cascade(label="Extentions", menu=ExtentionsMenu)
    menu.add_cascade(label="Help", menu=HelpMenu)

    root.config(menu=menu)
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