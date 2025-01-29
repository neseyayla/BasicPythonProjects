import tkinter as tk
from tkinter import filedialog, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 Notepad")
        self.root.geometry("600x500")

        # Menu
        menu = tk.Menu(root)
        root.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="🆕 New", command=self.new_note)
        file_menu.add_command(label="📂 Open", command=self.open_file)
        file_menu.add_command(label="💾 Save", command=self.save_file)
        file_menu.add_command(label="📄 Export PDF", command=self.save_as_pdf)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

        theme_menu = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="Theme", menu=theme_menu)
        theme_menu.add_command(label="☀ Light Mode", command=self.light_theme)
        theme_menu.add_command(label="🌙 Dark Mode", command=self.dark_theme)

        # Text area
        self.text_area = tk.Text(root, wrap="word", font=("Arial", 12))
        self.text_area.pack(expand=True, fill="both")

    def new_note(self):
        """Clears the text area for a new note."""
        self.text_area.delete(1.0, tk.END)

    def save_file(self):
        """Saves the note to a file."""
        file = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text Files", "*.txt")])
        if file:
            with open(file, "w", encoding="utf-8") as f:
                f.write(self.text_area.get(1.0, tk.END))
            messagebox.showinfo("Success", "Note saved successfully!")

    def open_file(self):
        """Opens an existing note from a file."""
        file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file:
            with open(file, "r", encoding="utf-8") as f:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, f.read())

    def light_theme(self):
        """Applies a light theme."""
        self.text_area.config(bg="white", fg="black")

    def dark_theme(self):
        """Applies a dark theme."""
        self.text_area.config(bg="black", fg="white")

    def save_as_pdf(self):
        """Converts the note to the PDF file."""
        file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files","*.pdf")])
        if file:
            pdf_canvas = canvas.Canvas(file, pagesize=letter)
            text = self.text_area.get(1.0,tk.END)
            text_pdf = pdf_canvas.beginText(30, 750)
            text_pdf.setFont("Helvetica", 12)
            for line in text.split("\n"):
                text_pdf.textLine(line)  # Writes each line properly
            pdf_canvas.drawText(text_pdf)

            pdf_canvas.save()
            messagebox.showinfo("Successfull converting", "Saved as a PDF File")