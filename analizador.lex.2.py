import ply.lex as lex
import tkinter as tk

# Definir tokens
tokens = (
    'TIPODATO',
    'CORCHETEAPERTURA',
    'CORCHETECIERRE',
    'PARENTESISAPERTURA',
    'PARENTESISCIERRE',
    'LLAVEAPERTURA',
    'LLAVECIERRE',
    'RESERVADO ',
    'PUNTOCOMA',
    'OPERADOR',
)

# Definir reglas de expresiones regulares para los tokens
t_IDENTIFICADOR = r'static|void|burbuja|arrego|¡'
t_PARENTISISAPERTURA = r'('
t_PARENTESISCIERRE = r')'
t_PUNTOCOMA = r';'
t_OPERADOR = r'++'
t_TIPODATO = r'int'
t_CORCHETEAPERTURA = r'['
t_CORCHETECIERRE = r'['
t_LLAVEAPERTURA = r'{'
t_LLAVECIERRE = r'}'

# Definir una regla para identificadores (ID)
def t_RESERVADO(t):
     r'while|for'
     return t

# Definir una regla para números (NUMBER)
def t_OPERADOR(t):
     r'++'
     t.value = int(t.value)
     return t

# Ignorar caracteres de espacio en blanco
t_ignore = ' \t'

# Manejar saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejar errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

# Función para analizar el texto de entrada
def analizar():
    input_text = text_entry.get("1.0", tk.END)
    lexer.input(input_text)
    tokens_output.config(state=tk.NORMAL)
    tokens_output.delete("1.0", tk.END)
    token_count = 0
    for tok in lexer:
        token_count += 1
        tokens_output.insert(tk.END, f"Token: {tok.type}, Lexema: {tok.value}, Línea: {tok.lineno}\n")
    tokens_output.insert(tk.END, f"\nTotal de Tokens: {token_count}\n")
    tokens_output.config(state=tk.DISABLED)

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Analizador Léxico")

# Entrada de texto
text_entry = tk.Text(root, wrap=tk.WORD, height=10, width=40)
text_entry.pack()

# Botón de análisis
analyze_button = tk.Button(root, text="Analizar", command=analizar)
analyze_button.pack()

# Salida de tokens
tokens_output = tk.Text(root, wrap=tk.WORD, height=10, width=40)
tokens_output.config(state=tk.DISABLED)
tokens_output.pack()

root.mainloop()