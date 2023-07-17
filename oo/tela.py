from tkinter import *
from tkinter import messagebox, ttk
import tkinter


def fazer_login():
    usurious = campo_usuario.get()
    senha = campo_senha.get()

    if usurious == "admin" and senha == "12345":
        messagebox.showinfo("Login", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos!")


janela = Tk()

janela.title("Tela de Login")

label_usuario = Label(janela, text="Usuário:")
label_usuario.pack()

campo_usuario = Entry(janela)
campo_usuario.pack()

label_senha = Label(janela, text="Senha:")
label_senha.pack()

campo_senha = Entry(janela, show="*")
campo_senha.pack()

botao_entrar = Button(janela, text="Entrar", command=fazer_login)
botao_entrar.pack()

janela.mainloop()
