import os
root = tk.Tk()
button = tk.Button(text="print",
                   fg="black",
                   command=lambda: print("test")
                   )
button.pack()
root.mainloop()