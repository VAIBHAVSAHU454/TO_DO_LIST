import tkinter as tk
from tkinter import messagebox

class TodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("TO-DO LIST")
        self.tasks = []

        # Create task entry field
        self.task_entry = tk.Entry(self.root, width=80)
        self.task_entry.pack(fill="both", padx=30, pady=30)

        # Create add task button
        self.add_button = tk.Button(self.root, text="ADD TASK", command=self.add_task)
        self.add_button.pack(fill="x", padx=30, pady=30)

        # Create task list box
        self.task_list = tk.Listbox(self.root, width=800)
        self.task_list.pack(fill="both", expand=True, padx=30, pady=30)

        # Create delete task button
        self.delete_button = tk.Button(self.root, text="DELETE TASK", command=self.delete_task)
        self.delete_button.pack(fill="x", padx=30, pady=30)

        # Create mark done button
        self.done_button = tk.Button(self.root, text="MARK AS DONE", command=self.mark_done)
        self.done_button.pack(fill="x", padx=30, pady=30)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "done": False})
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            del self.tasks[task_index]
        except IndexError:
            messagebox.showerror("ERROR!", "SELECT A TASK TO DELETE")

    def mark_done(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.tasks[task_index]["done"] = True
            self.task_list.itemconfig(task_index, fg="blue")
        except IndexError:
            messagebox.showerror("ERROR!", "SELECT A TASK MARK AS DONE")

if __name__ == "__main__":
    root = tk.Tk()
    todo = TodoList(root)
    root.mainloop()