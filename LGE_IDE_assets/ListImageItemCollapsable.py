import tkinter as tk
from PIL import ImageTk, Image

class ListImageItemCollapsable(tk.Frame):
    def __init__(self, root, label : str, image: tk.PhotoImage, bg="White", fg="black", **kwargs):
        super().__init__(root, bg = bg, **kwargs)
        self.bgcolor = bg
        self.fgcolor = fg
        self.items = []
        self.collapsed = False
        self.selected = None
        self.parent = root

        self.imageCollapse = ImageTk.PhotoImage(Image.open("LGE_IDE_assets/collapse.png"))
        self.imageCollapsed = ImageTk.PhotoImage(Image.open("LGE_IDE_assets/collapsed.png"))
        
        newItem = tk.Frame(self, bg=self.bgcolor)
        newItem.bind("<Button-1>", lambda e, i=0: self.select(i))
        newItemImage = tk.Label(newItem, image=image, bg=self.bgcolor)
        newItemCollapseImage = tk.Label(newItem, image=self.imageCollapse, bg=self.bgcolor)
        newItemLabel = tk.Label(newItem, text=label, bg=self.bgcolor, fg=self.fgcolor)
        newItemLabel.bind("<Button-1>", lambda e, i=len(self.items): self.select(i))
        newItemCollapseImage.bind("<Button-1>", lambda e: self.collapse())
        
        self.items.append([newItem, newItemCollapseImage, newItemImage, newItemLabel, False])
    def collapse(self):
        if (self.collapsed == True):
            # uncollapse
            self.collapsed = False
            self.items[0][4] = False
            self.items[0][1].configure(image=self.imageCollapse)
            self.renderItems()
        else:
            # collapse
            self.collapsed = True
            self.items[0][4] = True
            self.items[0][1].configure(image=self.imageCollapsed)
            for i in range(1, len(self.items)):
                for j in self.items[i]:
                    j.pack_forget()
    def renderItems(self):
        for i in self.items:
            if (len(i) == 3):
                # frame item (non collapsable)
                i[0].pack(fill='x') # the frame
                i[1].pack(side='left') # the image
                i[2].pack(side='left') # the label
            elif (len(i) == 1):
                # frame item (non collapsable)
                i[0].pack()
            else:
                i[0].pack(fill='x')
                i[1].pack(side="left")
                i[2].pack(side="left")
                if (i[4] == True):
                    i[1].configure(image=self.imageCollapsed)
                else:
                    i[1].configure(image=self.imageCollapse)
                i[3].pack(side="left")
        return
    def deselect(self, noparent = False):
        if (self.selected != None):
            for i in self.items:
                if (len(i) == 3):
                    i[0].configure(bg=self.bgcolor)
                    i[1].configure(bg=self.bgcolor)
                    i[2].configure(bg=self.bgcolor)
                elif (len(i) == 5):
                    i[0].configure(bg=self.bgcolor)
                    i[1].configure(bg=self.bgcolor)
                    i[2].configure(bg=self.bgcolor)
                    i[3].configure(bg=self.bgcolor)
                else:
                    i[0].deselect(True)
        self.selected = None
        if (noparent == False):
            if (type(self.parent) == ListImageItemCollapsable):
                self.parent.deselect()
    def select(self, index : int):
        self.deselect()
        self.selected=index
        if (self.selected != None):
            if (len(self.items[self.selected]) == 3):
                self.items[self.selected][0].configure(bg='#332222')
                self.items[self.selected][1].configure(bg='#332222')
                self.items[self.selected][2].configure(bg='#332222')
            if (len(self.items[self.selected]) == 5):
                self.items[self.selected][0].configure(bg='#332222')
                self.items[self.selected][1].configure(bg='#332222')
                self.items[self.selected][2].configure(bg='#332222')
                self.items[self.selected][3].configure(bg='#332222')
        return
    def pack(self, side = None, fill = None):
        super().pack()
        self.renderItems()
    def insert(self, label : str, image : tk.PhotoImage, collapsable : bool = False):
        if (image == None):
            raise ValueError("image cannot be None")
        newItem = None
        if (collapsable == False):
            newItem = tk.Frame(self, bg=self.bgcolor)
            currentIndex = len(self.items)
            newItem.bind("<Button-1>", lambda e, i=len(self.items): self.select(i))
            newItemImage = tk.Label(newItem, image=image, bg=self.bgcolor)
            newItemLabel = tk.Label(newItem, text=label, bg=self.bgcolor, fg=self.fgcolor)
            newItemLabel.bind("<Button-1>", lambda e, i=len(self.items): self.select(i))
            self.items.append([newItem, newItemImage, newItemLabel])
        else:
            newItem = ListImageItemCollapsable(self, label, image, bg=self.bgcolor, fg=self.fgcolor)
            self.items.append([newItem])
        return self.items[len(self.items) - 1]
