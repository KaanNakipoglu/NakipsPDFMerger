import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2


# Author: Kaan Nakipoğlu
def merge_pdfs(pdf_list, output_filename):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        with open(pdf, 'rb') as pdf_file:
            pdf_merger.append(pdf_file)

    with open(output_filename, 'wb') as output_file:
        pdf_merger.write(output_file)
    messagebox.showinfo("Success", f"PDFs merged successfully into {output_filename}")


def select_files():
    file_paths = filedialog.askopenfilenames(
        title="Select PDF Files",
        filetypes=[("PDF files", "*.pdf")],
        defaultextension=".pdf"
    )
    if file_paths:
        for path in file_paths:
            file_listbox.insert(tk.END, path)


def merge_files():
    pdfs_to_merge = file_listbox.get(0, tk.END)
    if not pdfs_to_merge:
        messagebox.showerror("Error", "No PDF files selected.")
        return

    output_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        title="Save Merged PDF As"
    )
    if not output_path:
        return

    merge_pdfs(list(pdfs_to_merge), output_path)


def remove_selected():
    """Remove selected files from the listbox."""
    selected_files = file_listbox.curselection()
    for index in reversed(selected_files):
        file_listbox.delete(index)


root = tk.Tk()
root.title("PDF Merger")
root.geometry("400x400")

file_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50, height=10)
file_listbox.pack(pady=20)

add_button = tk.Button(root, text="Select PDFs", command=select_files)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Selected", command=remove_selected)
remove_button.pack(pady=5)

merge_button = tk.Button(root, text="Merge PDFs", command=merge_files)
merge_button.pack(pady=10)

root.mainloop()
