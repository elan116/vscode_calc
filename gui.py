"""
Calculator GUI Application
A Windows-style graphical user interface for the calculator using tkinter.
"""

import tkinter as tk
from tkinter import font
from calculator import Calculator


class CalculatorGUI:
    """A graphical user interface for the calculator."""
    
    def __init__(self, root):
        """
        Initialize the Calculator GUI.
        
        Args:
            root: The tkinter root window
        """
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Set background color
        self.root.configure(bg="#f0f0f0")
        
        # Initialize calculator
        self.calc = Calculator()
        
        # Display variable
        self.display_var = tk.StringVar(value="0")
        self.current_input = ""
        self.operator = None
        self.first_number = None
        
        # Create UI
        self.create_widgets()
    
    def create_widgets(self):
        """Create and layout the calculator widgets."""
        # Display frame
        display_frame = tk.Frame(self.root, bg="#f0f0f0")
        display_frame.pack(pady=10, padx=10, fill=tk.BOTH)
        
        # Display label
        display_label = tk.Label(
            display_frame,
            text="Display",
            font=("Arial", 10),
            bg="#f0f0f0",
            fg="#666666"
        )
        display_label.pack(anchor="w")
        
        # Display entry (read-only)
        display = tk.Entry(
            display_frame,
            textvar=self.display_var,
            font=("Arial", 28, "bold"),
            justify="right",
            state="readonly",
            relief=tk.SUNKEN,
            bd=2,
            bg="white",
            fg="#333333"
        )
        display.pack(fill=tk.BOTH, ipady=15)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg="#f0f0f0")
        buttons_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Button layout
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["Clear", "History", "Delete", "Exit"]
        ]
        
        for row_idx, row in enumerate(buttons):
            for col_idx, btn_text in enumerate(row):
                self.create_button(buttons_frame, btn_text, row_idx, col_idx)
        
        # History frame
        self.create_history_frame()
    
    def create_button(self, parent, text, row, col):
        """
        Create a calculator button.
        
        Args:
            parent: Parent frame
            text: Button text
            row: Row position
            col: Column position
        """
        # Button colors
        if text in ["/", "*", "-", "+"]:
            bg_color = "#4CAF50"
            fg_color = "white"
        elif text == "=":
            bg_color = "#2196F3"
            fg_color = "white"
        elif text in ["Clear", "Delete", "History", "Exit"]:
            bg_color = "#f44336"
            fg_color = "white"
        else:
            bg_color = "#e8e8e8"
            fg_color = "#333333"
        
        button = tk.Button(
            parent,
            text=text,
            font=("Arial", 16, "bold"),
            bg=bg_color,
            fg=fg_color,
            relief=tk.RAISED,
            bd=1,
            height=3,
            width=8,
            activebackground="#ddd" if bg_color == "#e8e8e8" else "#45a049",
            command=lambda: self.on_button_click(text)
        )
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        
        # Configure grid weights for button spacing
        parent.grid_rowconfigure(row, weight=1)
        parent.grid_columnconfigure(col, weight=1)
    
    def create_history_frame(self):
        """Create a frame to display calculation history."""
        history_frame = tk.LabelFrame(
            self.root,
            text="History",
            font=("Arial", 10, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        history_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(history_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # History listbox
        self.history_listbox = tk.Listbox(
            history_frame,
            font=("Arial", 10),
            yscrollcommand=scrollbar.set,
            bg="white",
            fg="#333333",
            relief=tk.SUNKEN,
            bd=1,
            height=4
        )
        self.history_listbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.history_listbox.yview)
    
    def on_button_click(self, value):
        """
        Handle button clicks.
        
        Args:
            value: The button value clicked
        """
        if value.isdigit():
            self.handle_number(value)
        elif value == ".":
            self.handle_decimal()
        elif value in ["+", "-", "*", "/"]:
            self.handle_operator(value)
        elif value == "=":
            self.handle_equals()
        elif value == "Clear":
            self.handle_clear()
        elif value == "Delete":
            self.handle_delete()
        elif value == "History":
            self.show_history()
        elif value == "Exit":
            self.root.quit()
    
    def handle_number(self, num):
        """Handle number button clicks."""
        if self.current_input == "0":
            self.current_input = num
        else:
            self.current_input += num
        self.display_var.set(self.current_input)
    
    def handle_decimal(self):
        """Handle decimal point button."""
        if "." not in self.current_input:
            if self.current_input == "":
                self.current_input = "0"
            self.current_input += "."
            self.display_var.set(self.current_input)
    
    def handle_operator(self, op):
        """Handle operator button clicks."""
        if self.current_input == "":
            return
        
        if self.first_number is None:
            self.first_number = float(self.current_input)
        else:
            # Calculate if there's a pending operation
            self.handle_equals(op)
            return
        
        self.operator = op
        self.current_input = ""
    
    def handle_equals(self, next_op=None):
        """Handle equals button click."""
        if self.operator is None or self.current_input == "":
            return
        
        try:
            second_number = float(self.current_input)
            result = self.calc.calculate(self.first_number, second_number, self.operator)
            self.display_var.set(str(result))
            self.update_history()
            
            self.current_input = str(result)
            self.first_number = result if next_op else None
            self.operator = next_op
            
            if not next_op:
                self.current_input = ""
        
        except (ValueError, TypeError) as e:
            self.display_var.set(f"Error: {str(e)}")
            self.current_input = ""
            self.first_number = None
            self.operator = None
    
    def handle_clear(self):
        """Handle clear button click."""
        self.current_input = ""
        self.first_number = None
        self.operator = None
        self.display_var.set("0")
    
    def handle_delete(self):
        """Handle delete button (backspace)."""
        if self.current_input:
            self.current_input = self.current_input[:-1]
            self.display_var.set(self.current_input if self.current_input else "0")
    
    def show_history(self):
        """Display the calculation history."""
        self.history_listbox.delete(0, tk.END)
        
        history = self.calc.get_history()
        if not history:
            self.history_listbox.insert(tk.END, "No calculations yet")
        else:
            for i, entry in enumerate(history, 1):
                self.history_listbox.insert(
                    tk.END,
                    f"{i}. {entry['operation']} = {entry['result']}"
                )
    
    def update_history(self):
        """Update the history display."""
        self.show_history()


def main():
    """Main function to run the calculator GUI."""
    root = tk.Tk()
    gui = CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
