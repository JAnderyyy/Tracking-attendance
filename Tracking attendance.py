from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Отслеживание посещаемости")
        self.root.geometry("600x400")

        self.people = []
        self.attendance_vars = []

        self.setup_ui()

    def setup_ui(self):
        columns = ("name", "last_name")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings", selectmode="none")
        self.tree.heading("name", text="Имя")
        self.tree.heading("last_name", text="Фамилия")
        self.tree.column("name", width=150)
        self.tree.column("last_name", width=150)
        self.tree.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)

        scrollbar = ttk.Scrollbar(self.root, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=3, sticky='ns')

        self.name_entry = Entry(self.root)
        self.name_entry.grid(row=1, column=0, padx=5, pady=5)
        self.name_entry.insert(0, "Имя")
        self.name_entry.bind("<FocusIn>", self.clear_name_entry)
        self.name_entry.bind("<FocusOut>", self.restore_name_entry)

        self.last_name_entry = Entry(self.root)
        self.last_name_entry.grid(row=1, column=1, padx=5, pady=5)
        self.last_name_entry.insert(0, "Фамилия")
        self.last_name_entry.bind("<FocusIn>", self.clear_last_name_entry)
        self.last_name_entry.bind("<FocusOut>", self.restore_last_name_entry)

        add_button = Button(self.root, text="Добавить", command=self.add_person)
        add_button.grid(row=1, column=2, padx=5, pady=5)

        mark_attendance_button = Button(self.root, text="Отметить присутствие", command=self.mark_attendance)
        mark_attendance_button.grid(row=2, column=0, padx=5, pady=10)

        report_button = Button(self.root, text="Показать отчет", command=self.show_report)
        report_button.grid(row=2, column=1, padx=5, pady=10)

        reset_button = Button(self.root, text="Сбросить посещение", command=self.reset_attendance)
        reset_button.grid(row=2, column=2, padx=5, pady=10)

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure([0, 1, 2], weight=1)

    def clear_name_entry(self, event):
        if self.name_entry.get() == "Имя":
            self.name_entry.delete(0, END)
            self.name_entry.config(fg='black')

    def restore_name_entry(self, event):
        if not self.name_entry.get():
            self.name_entry.insert(0, "Имя")
            self.name_entry.config(fg='grey')

    def clear_last_name_entry(self, event):
        if self.last_name_entry.get() == "Фамилия":
            self.last_name_entry.delete(0, END)
            self.last_name_entry.config(fg='black')

    def restore_last_name_entry(self, event):
        if not self.last_name_entry.get():
            self.last_name_entry.insert(0, "Фамилия")
            self.last_name_entry.config(fg='grey')

    def add_person(self):
        name = self.name_entry.get().strip()
        last_name = self.last_name_entry.get().strip()
        if name and last_name:
            self.people.append({'name': name, 'last_name': last_name, 'attended': False})
            self.tree.insert("", END, values=(name, last_name))
            self.name_entry.delete(0, END)
            self.last_name_entry.delete(0, END)
        else:
            messagebox.showwarning("Внимание", "Пожалуйста, введите имя и фамилию.")

    def mark_attendance(self):
        for person in self.people:
            person['attended'] = True
        messagebox.showinfo("Отметка", "Посещение отмечено для всех присутствующих.")

    def show_report(self):
        total_people = len(self.people)
        attended_people = sum(1 for p in self.people if p['attended'])
        absent_people = total_people - attended_people

        report_message = (
            f"Общее число человек: {total_people}\n"
            f"Присутствовали: {attended_people}\n"
            f"Отсутствовали: {absent_people}"
        )
        messagebox.showinfo("Отчет посещаемости", report_message)

    def reset_attendance(self):
        for person in self.people:
            person['attended'] = False
        messagebox.showinfo("Обновление", "Статус посещения сброшен.")

root = Tk()
app = AttendanceApp(root)
root.mainloop()
