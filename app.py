from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import Listbox, Button, END, messagebox
from PyPDF2 import PdfMerger
import os

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        self.root.geometry("400x300")

        # Create the Listbox to show dragged files
        self.file_listbox = Listbox(self.root, selectmode="extended")
        self.file_listbox.pack(fill="both", expand=True, padx=10, pady=10)

        # Enable drag-and-drop for the Listbox
        self.root.drop_target_register(DND_FILES)
        self.root.dnd_bind('<<Drop>>', self.add_dragged_files)

        # Button to merge PDFs
        self.merge_button = Button(root, text="Merge PDFs", command=self.merge_pdfs)
        self.merge_button.pack(pady=5)

    def add_dragged_files(self, event):
        # Get the list of dragged files
        files = self.root.tk.splitlist(event.data)
        for file in files:
            if file.endswith(".pdf"):
                self.file_listbox.insert(END, file)  # Add valid PDF files to the Listbox
            else:
                messagebox.showwarning("Invalid File", f"{file} is not a PDF file!")

    def merge_pdfs(self):
        files = self.file_listbox.get(0, END)
        if not files:
            messagebox.showerror("Error", "No files selected.")
            return

        try:
            merger = PdfMerger()
            for file in files:
                merger.append(file)
            output_path = os.path.join(os.getcwd(), "combined.pdf")
            merger.write(output_path)
            merger.close()
            messagebox.showinfo("Success", f"Merged file saved as:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to merge PDFs:\n{str(e)}")

        # Clear the Listbox after merging
        self.file_listbox.delete(0, END)


if __name__ == "__main__":
    root = TkinterDnD.Tk()  # Use TkinterDnD's Tk class
    app = PDFMergerApp(root)
    root.mainloop()
