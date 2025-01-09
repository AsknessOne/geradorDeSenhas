import string
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def gerar_senha():
    """
    Gera uma senha aleatória e embaralhada que contém caracteres especiais, letras e números.

    Args: 
        int: Resposta numérica que é inserida pelo o usuário.
    
    Returns:
        string: Senha gerada.
    
    Raises:
        ValueError: Se nenhuma entrada for inserida
    
    """

    '''Obtém e valida o tamanho da senha, gerando mensagens de erro caso seja incompatível.'''
    try:
        tamanho = int(entry_tamanho.get())
        if tamanho < 4:
            messagebox.showwarning("Erro", "Por favor, o tamanho precisa ser de no mínimo 4 caracteres.")
            return
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")
        return
    
    
    # Garantindo que tenha ao menos um de cada caractere desejado.
    senha = [
        random.choice(string.ascii_letters),
        random.choice(string.digits),
        random.choice(string.punctuation),
        ]
    possibilidades = "".join([string.ascii_letters, string.digits, string.punctuation])
    senha.extend(random.choices(possibilidades, k=tamanho -3))

    random.shuffle(senha)

    # Exibindo a senha gerada
    senha_final = ''.join(senha)
    saida.delete(0,tk.END)
    saida.insert(0, senha_final)


def copiar_senha():
    """
    Limpa a área de transferência do usuário e adiciona a senha gerada à saída.

    Raises:
        ValueError: Se nenhuma senha estiver presente no campo de saída.
    """
    senha = saida.get()
    if not senha:
        messagebox.showerror("Erro", "Nenhuma senha foi gerada para copiar.")
        return
 
    janela.clipboard_clear() 
    janela.clipboard_append(saida.get())  
    messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência!")

# Cria a janela para visualização.
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry('550x330')
janela.configure(bg='#CDC1FF') 

# Estilo para melhorar o aspecto da janela.
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 10), padding=5)
style.configure('TEntry', padding=5)


# Textos
tk.Label(janela, text='Gerador de Senhas', 
                         font=('Helvetica', 16, 'bold'), bg='#CDC1FF', fg='#001F3F', anchor='w', justify='left').pack(pady=10, fill='x')

tk.Label(janela, text='Seja bem vindo!', 
                         font=('Helvetica', 13, 'bold'), bg='#CDC1FF', fg='#0B192C', anchor='w', justify='left').pack(pady=1, fill='x')

tk.Label(janela, text='Digite o número de caracteres desejado e clique em "Gerar Senha".', 
                         font=('Helvetica', 11), bg='#CDC1FF', fg='#0B192C').pack(pady=5)

# Campo de entrada do usuário.
entry_tamanho =ttk.Entry(janela)
entry_tamanho.pack(pady=10)

# Botão Enviar.
ttk.Button(
    janela, text='Gerar Senha', command=gerar_senha,).pack(pady=10)

# Campo de saída da senha que é gerada.
saida = ttk.Entry(janela)
saida.pack(pady=5)

# Botão Copiar
ttk.Button(janela, text='Copiar', command=copiar_senha).pack(pady=5)

janela.mainloop()