import tkinter as tk
from lexicalAnalysis import tokenize, TokenType
from parserAnalysis import Parser

class SyntaxAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Syntax Analyzer with Highlighting")

        self.text = tk.Text(root, height=18, width=80, font=("Consolas", 12))
        self.text.pack(padx=10, pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=5)

        self.text.bind("<KeyRelease>", self.schedule_analysis)
        self.analysis_job = None

        self.create_tags()

    def create_tags(self):
        self.text.tag_configure("TYPE", foreground="blue")
        self.text.tag_configure("ID", foreground="green")
        self.text.tag_configure("NUMBER", foreground="purple")
        self.text.tag_configure("OP", foreground="orange")
        self.text.tag_configure("SEMICOLON", foreground="#B8860B") #sarı çok göz yoruyor
        self.text.tag_configure("KEYWORD", foreground="red")
        self.text.tag_configure("COMPARISON", foreground="dark red")
        self.text.tag_configure("BRACE", foreground="gray")
        self.text.tag_configure("PAREN", foreground="gray")
        self.text.tag_configure("UNKNOWN", foreground="black")
        self.text.tag_configure("COMMENT", foreground="gray", font=("Consolas", 12, "italic"))

    def schedule_analysis(self, event=None):
        if self.analysis_job:
            self.root.after_cancel(self.analysis_job)
        self.analysis_job = self.root.after(300, self.analyze_syntax)

    def analyze_syntax(self):
        code = self.text.get("1.0", tk.END)
        tokens = tokenize(code)

        # Tüm tag’leri temizle
        for tag in self.text.tag_names():
            self.text.tag_remove(tag, "1.0", tk.END)

        # Token’ları vurgula
        current_index = 0
        for token in tokens:
            start_index = self.index_from_offset(current_index)
            end_index = self.index_from_offset(current_index + len(token.value))
            self.text.tag_add(token.type.name, start_index, end_index)
            current_index += len(token.value)

            while current_index < len(code) and code[current_index].isspace():
                current_index += 1

        # Syntax kontrolü
        parser = Parser(tokens)
        if parser.parse():
            self.result_label.config(text="✔ Syntax OK", fg="green")
        else:
            self.result_label.config(text="❌ Syntax Error", fg="red")

    def index_from_offset(self, offset):
        code = self.text.get("1.0", tk.END)
        line = 1
        col = 0
        count = 0
        for c in code:
            if count == offset:
                break
            if c == '\n':
                line += 1
                col = 0
            else:
                col += 1
            count += 1
        return f"{line}.{col}"

if __name__ == "__main__":
    root = tk.Tk()
    app = SyntaxAnalyzerGUI(root)
    root.mainloop()
