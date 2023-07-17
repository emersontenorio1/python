# import tkinter
#
# janela = tkinter.Tk()
# janela.geometry("500x300")
# def clique():
#     print("Fazer Login")
#
# texto = tkinter.Label(janela, text="Fazer Login")
# texto.pack(padx=10, pady=10)
#
# botao = tkinter.Button(janela, text="Login", command=clique)
# botao.pack(pady=10, padx=10)
#
#
# janela.mainloop()
#


import customtkinter


customtkinter.set_appearance_mode("dark")

janela = customtkinter.CTk()
janela.title("Tela de Login")
janela.geometry("500x300")
def clique():
     print("Fazer Login")


texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)
email = customtkinter.CTkEntry(janela, placeholder_text="Digite seu e-mail")
email.pack(pady=10, padx=10)
senha = customtkinter.CTkEntry(janela, placeholder_text="Digite sua senha", show="*")
senha.pack(pady=10, padx=10)
check = customtkinter.CTkCheckBox(janela, text="Lembrar login", hover_color="gray")
check.pack(pady=10, padx=10)
botao = customtkinter.CTkButton(janela, text="Login", command=clique, fg_color="black", hover_color="gray")
botao.pack(pady=10, padx=10)


janela.mainloop()



