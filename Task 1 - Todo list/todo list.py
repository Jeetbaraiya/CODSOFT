import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("420x540")
        self.root.configure(bg="#232946")  

        # Color variables
        self.bg_color = "#232946"         
        self.card_color = "#393e6c"      
        self.accent_color = "#eebbc3"    
        self.entry_bg = "#f4f4f8"       
        self.entry_fg = "#232946"        
        self.button_color = "#b8c1ec"    
        self.button_fg = "#232946"       
        self.selected_color = "#eebbc3"  
        self.done_color = "#6bcB77"      

        self.tasks = []


        # Main frame (card)
        self.card = tk.Frame(root, bg=self.card_color, bd=0, relief="ridge")
        self.card.place(relx=0.5, rely=0.5, anchor="center", width=370, height=480)

        # Title
        tk.Label(self.card, text="📝 To-Do List", font=("Segoe UI", 20, "bold"),
                 bg=self.card_color, fg=self.accent_color).pack(pady=(18, 10))

        # Entry for new tasks
        self.task_entry = tk.Entry(self.card, width=26, font=("Segoe UI", 13),
                                   bg=self.entry_bg, fg=self.entry_fg, insertbackground=self.accent_color,
                                   relief="flat", highlightthickness=2, highlightbackground=self.accent_color)
        self.task_entry.pack(pady=(0, 12), ipady=6)

        # Button frame
        btn_frame = tk.Frame(self.card, bg=self.card_color)
        btn_frame.pack(pady=(0, 10))

        self.add_btn = tk.Button(btn_frame, text="Add Task", command=self.add_task,
                                 width=12, bg=self.button_color, fg=self.button_fg, font=("Segoe UI", 11, "bold"),
                                 activebackground="green", activeforeground=self.bg_color, bd=0, relief="flat", cursor="hand2")
        self.add_btn.grid(row=0, column=0, padx=5)
        self.add_btn.bind("<Enter>", lambda e: self.add_btn.config(bg="green", fg=self.bg_color))
        self.add_btn.bind("<Leave>", lambda e: self.add_btn.config(bg=self.button_color, fg=self.button_fg))

        self.done_btn = tk.Button(btn_frame, text="Mark as Done", command=self.mark_done,
                                  width=12, bg=self.button_color, fg=self.button_fg, font=("Segoe UI", 11, "bold"),
                                  activebackground="blue", activeforeground=self.bg_color, bd=0, relief="flat", cursor="hand2")
        self.done_btn.grid(row=0, column=1, padx=5)
        self.done_btn.bind("<Enter>", lambda e: self.done_btn.config(bg="blue", fg=self.bg_color))
        self.done_btn.bind("<Leave>", lambda e: self.done_btn.config(bg=self.button_color, fg=self.button_fg))

        self.delete_btn = tk.Button(btn_frame, text="Delete Task", command=self.delete_task,
                                    width=12, bg=self.button_color, fg=self.button_fg, font=("Segoe UI", 11, "bold"),
                                    activebackground="#f44336", activeforeground=self.bg_color, bd=0, relief="flat", cursor="hand2")
        self.delete_btn.grid(row=0, column=2, padx=5)
        self.delete_btn.bind("<Enter>", lambda e: self.delete_btn.config(bg="#f44336", fg=self.bg_color))
        self.delete_btn.bind("<Leave>", lambda e: self.delete_btn.config(bg=self.button_color, fg=self.button_fg))

        # Listbox for tasks
        self.listbox = tk.Listbox(self.card, width=32, height=13, font=("Segoe UI", 12),
                                  bg=self.entry_bg, fg=self.entry_fg, selectbackground=self.selected_color,
                                  selectforeground=self.bg_color, bd=0, relief="flat", highlightthickness=0)
        self.listbox.pack(pady=(0, 10))

        # Scrollbar for listbox
        scrollbar = tk.Scrollbar(self.card, orient="vertical", command=self.listbox.yview, bg=self.card_color)
        scrollbar.place(in_=self.listbox, relx=1.0, rely=0, relheight=1.0, bordermode="outside")
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Footer
        tk.Label(self.card, text="", font=("Segoe UI", 9, "italic"),
                 bg=self.card_color, fg="#b8c1ec").pack(side="bottom", pady=(0, 8))

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty")

    def mark_done(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            task = self.tasks[index]
            if not task.startswith("✔️"):
                self.tasks[index] = f"✔️ {task}"
                self.update_list()
                self.listbox.selection_set(index)
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete")

    def update_list(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            if task.startswith("✔️"):
                self.listbox.insert(tk.END, task)
                self.listbox.itemconfig(tk.END, fg=self.done_color)
            else:
                self.listbox.insert(tk.END, task)
                self.listbox.itemconfig(tk.END, fg=self.entry_fg)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
        