import os
import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2


# Author: Kaan Nakipoğlu
file_paths_list = []


def merge_pdfs(pdf_list, output_filename):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        with open(pdf, 'rb') as pdf_file:
            pdf_merger.append(pdf_file)

    with open(output_filename, 'wb') as output_file:
        pdf_merger.write(output_file)
    messagebox.showinfo("Success", f"PDFs merged successfully into {output_filename}")


def select_files():
    global file_paths_list
    selected_paths = filedialog.askopenfilenames(
        title="Select PDF Files",
        filetypes=[("PDF files", "*.pdf")],
        defaultextension=".pdf"
    )
    if selected_paths:
        for path in selected_paths:
            file_paths_list.append(path)  # Store the full path
            file_listbox.insert(tk.END, os.path.basename(path))  # Show only the file name


def merge_files():
    global file_paths_list
    selected_indices = file_listbox.curselection()
    if not selected_indices:
        messagebox.showerror("Error", "No PDF files selected.")
        return

    pdfs_to_merge = [file_paths_list[i] for i in selected_indices]  # Get the full file paths

    output_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        title="Save Merged PDF As"
    )
    if not output_path:
        return

    merge_pdfs(pdfs_to_merge, output_path)


def remove_selected():
    global file_paths_list
    selected_files = file_listbox.curselection()
    for index in reversed(selected_files):
        file_listbox.delete(index)
        del file_paths_list[index]  # Remove the corresponding full path


def move_up():
    global file_paths_list
    selected_indices = file_listbox.curselection()
    if not selected_indices:
        return

    for index in selected_indices:
        if index == 0:  # If it's the first item, skip it
            continue
        file_listbox.delete(index)
        file_listbox.insert(index - 1, os.path.basename(file_paths_list[index]))
        file_listbox.selection_set(index - 1)

        # Move the corresponding path in file_paths_list
        file_paths_list[index], file_paths_list[index - 1] = file_paths_list[index - 1], file_paths_list[index]


def move_down():
    global file_paths_list
    selected_indices = file_listbox.curselection()
    if not selected_indices:
        return

    for index in reversed(selected_indices):
        if index == file_listbox.size() - 1:  # If it's the last item, skip it
            continue
        file_listbox.delete(index)
        file_listbox.insert(index + 1, os.path.basename(file_paths_list[index]))
        file_listbox.selection_set(index + 1)

        # Move the corresponding path in file_paths_list
        file_paths_list[index], file_paths_list[index + 1] = file_paths_list[index + 1], file_paths_list[index]


root = tk.Tk()
root.title("PDF Merger")
root.geometry("500x400")

listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=20)

file_listbox = tk.Listbox(listbox_frame, selectmode=tk.MULTIPLE, width=50, height=10)
file_listbox.pack(side=tk.LEFT, padx=10)

button_frame = tk.Frame(listbox_frame)
button_frame.pack(side=tk.RIGHT, padx=10)

move_up_button = tk.Button(button_frame, text="↑ Move Up", command=move_up)
move_up_button.pack(pady=5)

move_down_button = tk.Button(button_frame, text="↓ Move Down", command=move_down)
move_down_button.pack(pady=5)

add_button = tk.Button(root, text="Select PDFs", command=select_files)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Selected", command=remove_selected)
remove_button.pack(pady=5)

merge_button = tk.Button(root, text="Merge PDFs", command=merge_files)
merge_button.pack(pady=10)

root.mainloop()
