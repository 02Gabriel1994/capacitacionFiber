import tkinter as tk
from tkinter import Canvas, Scrollbar

class CanvasWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas with Scrollbar")

        # Create a Canvas widget
        self.canvas = Canvas(root, bg="white")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a Scrollbar widget
        self.scrollbar = Scrollbar(root, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Connect the Scrollbar to the Canvas
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        # Create a frame to hold the content
        self.content_frame = tk.Frame(self.canvas, bg="white")
        self.canvas.create_window((0, 0), window=self.content_frame, anchor="nw")

        # Populate the content frame with widgets
        for i in range(50):
            label = tk.Label(self.content_frame, text=f"Item {i}", font=("Arial", 12))
            label.pack(pady=5)

        # Bind the canvas to scrollbar functionality
        self.content_frame.bind("<Configure>", self.update_scrollregion)

    def update_scrollregion(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    root = tk.Tk()
    app = CanvasWindow(root)
    root.mainloop()






