import os
import tkinter as tk
from tkinter import messagebox, filedialog

path = "D:\doc\pythonprojects\Files\FilesforPrograms"
z = os.listdir(path)

def open_and_create_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt")
    if filepath:
        with open(filepath, 'w') as file:
            pass

def edit_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filepath:
        hide_all_frames()
        edit_frame.pack()

        def save_content():
            content = input_text.get("1.0", tk.END)
            with open(filepath, 'w') as file:
                file.write(content)
            messagebox.showinfo("File Update", "Content saved successfully.")
            show_all_frames()

        with open(filepath, 'r') as file:
            content = file.read()

        input_label = tk.Label(edit_frame, text="Edit content:")
        input_label.pack()

        input_text = tk.Text(edit_frame, height=10, width=50)
        input_text.insert(tk.END, content)
        input_text.pack()

        save_button = tk.Button(edit_frame, text="Save", width=20, command=save_content)
        save_button.pack()

def read_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filepath:
        hide_all_frames()
        read_frame.pack()

        with open(filepath, 'r') as file:
            content = file.read()

        text_widget = tk.Text(read_frame, height=10, width=50)
        text_widget.insert(tk.END, content)
        text_widget.config(state=tk.DISABLED)
        text_widget.pack()

        close_button = tk.Button(read_frame, text="Close", width=20, command=show_all_frames)
        close_button.pack()

def delete_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filepath:
        confirm = messagebox.askquestion("Confirm Deletion", "Are you sure you want to delete this file?")
        if confirm == 'yes':
            os.remove(filepath)
            messagebox.showinfo("File Deletion", "File removed successfully.")

def delete_content():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filepath:
        confirm = messagebox.askquestion("Confirm Deletion", "Are you sure you want to delete the contents of this file?")
        if confirm == 'yes':
            with open(filepath, 'w') as file:
                pass
            messagebox.showinfo("File Content is deleted.", "File content deleted successfully.")

def exit_program():
    messagebox.showinfo("Exit", "Exiting the program.")
    exit()

def hide_all_frames():
    create_frame.pack_forget()
    edit_frame.pack_forget()
    read_frame.pack_forget()
    delete_frame.pack_forget()
    delete_content_frame.pack_forget()

def show_all_frames():
    create_frame.pack()
    edit_frame.pack()
    read_frame.pack()
    delete_frame.pack()
    delete_content_frame.pack()

root = tk.Tk()

create_frame = tk.Frame(root)
edit_frame = tk.Frame(root)
read_frame = tk.Frame(root)
delete_frame = tk.Frame(root)
delete_content_frame = tk.Frame(root)

def main():
    def create_command_window():
        hide_all_frames()
        create_frame.pack()

    command_label = tk.Label(root, text="What operation would you like to perform?")
    command_label.pack()

    command1 = tk.Button(root, text="1. Read a file", width=20, command=read_file)
    command1.pack()

    command2 = tk.Button(root, text="2. Edit a file", width=20, command=edit_file)
    command2.pack()

    command3 = tk.Button(root, text="3. Create a file", width=20, command=open_and_create_file)
    command3.pack()

    command4 = tk.Button(root, text="4. Delete a file", width=20, command=delete_file)
    command4.pack()

    command5 = tk.Button(root, text="5. Delete contents of a file", width=20, command=delete_content)
    command5.pack()

    command6 = tk.Button(root, text="6. Exit", width=20, command=exit_program)
    command6.pack()

    root.mainloop()

if __name__ == '__main__':
    main()
