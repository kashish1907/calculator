import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#2e2e2e")

        self.expression = ""

        self.display = tk.Entry(root, font=("Arial", 20), bd=10, insertwidth=2, width=15,
                                borderwidth=4, relief="ridge", bg="#f0f0f0", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, pady=10)

        btns = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)
        ]

        for btn in btns:
            text = btn[0]
            row = btn[1]
            col = btn[2]
            colspan = btn[3] if len(btn) == 4 else 1

            b = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14),
                          bg="#404040" if text not in ['C', '='] else "#d35400",
                          fg="white", bd=0, relief="raised",
                          command=lambda txt=text: self.on_button_click(txt))
            b.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)

        # Resize grid rows/cols
        for i in range(6):
            root.rowconfigure(i, weight=1)
        for j in range(4):
            root.columnconfigure(j, weight=1)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == "=":
            try:
                result = eval(self.expression)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.expression = str(result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)

# Launch calculator
if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
