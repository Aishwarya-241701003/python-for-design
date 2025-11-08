import tkinter as tk
from tkinter import colorchooser

class SimpleGraphicsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Graphics App")
        self.root.geometry("800x600")

    
        self.shape = "line"  
        self.color = "black"  
        self.start_x = None
        self.start_y = None

       
        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack(side=tk.TOP, padx=10, pady=10)

      
        control_frame = tk.Frame(root)
        control_frame.pack(side=tk.BOTTOM, pady=10)

  
        tk.Label(control_frame, text="Shape:").grid(row=0, column=0)
        tk.Button(control_frame, text="Line", command=lambda: self.set_shape("line")).grid(row=0, column=1)
        tk.Button(control_frame, text="Rectangle", command=lambda: self.set_shape("rectangle")).grid(row=0, column=2)
        tk.Button(control_frame, text="Circle", command=lambda: self.set_shape("circle")).grid(row=0, column=3)


        tk.Label(control_frame, text="Color:").grid(row=1, column=0)
        tk.Button(control_frame, text="Choose Color", command=self.choose_color).grid(row=1, column=1, columnspan=2)


        tk.Button(control_frame, text="Clear Canvas", command=self.clear_canvas).grid(row=2, column=0, columnspan=4)


        self.canvas.bind("<ButtonPress-1>", self.on_mouse_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_release)

    def set_shape(self, shape):
        self.shape = shape

    def choose_color(self):
        color = colorchooser.askcolor(title="Choose color")[1]  
        if color:
            self.color = color

    def clear_canvas(self):
        self.canvas.delete("all")

    def on_mouse_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_mouse_release(self, event):
        end_x = event.x
        end_y = event.y
        if self.shape == "line":
            self.canvas.create_line(self.start_x, self.start_y, end_x, end_y, fill=self.color, width=2)
        elif self.shape == "rectangle":
            self.canvas.create_rectangle(self.start_x, self.start_y, end_x, end_y, outline=self.color, width=2)
        elif self.shape == "circle":
         
            radius = ((end_x - self.start_x)**2 + (end_y - self.start_y)**2)**0.5
            self.canvas.create_oval(self.start_x - radius, self.start_y - radius, 
                                    self.start_x + radius, self.start_y + radius, 
                                    outline=self.color, width=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleGraphicsApp(root)
    root.mainloop()
