import customtkinter as ctk
from controllers.usuario_controller import UsuarioController


class TelaCadastro(ctk.CTkFrame):
    def __init__(self, master, ir_para_login):
        super().__init__(master)
        self.controller = UsuarioController()

        ctk.CTkLabel(self, text="CRIAR CONTA", font=("Small Fonts", 28, "bold"), text_color="white").pack(pady=(60, 20))

        self.entry_nome = ctk.CTkEntry(self, placeholder_text="Nome", width=300)
        self.entry_nome.pack(pady=8)

        self.entry_email = ctk.CTkEntry(self, placeholder_text="Email", width=300)
        self.entry_email.pack(pady=8)

        self.entry_senha = ctk.CTkEntry(self, placeholder_text="Senha", show="*", width=300)
        self.entry_senha.pack(pady=8)

        self.menu_tipo = ctk.CTkOptionMenu(self, values=["membro", "gestor"], width=300)
        self.menu_tipo.pack(pady=8)

        self.entry_nome.bind("<Return>", lambda event: self.entry_email.focus())

        self.entry_email.bind("<Return>", lambda event: self.entry_senha.focus())
        
        self.entry_senha.bind("<Return>", lambda event: self.cadastrar())

        self.label_msg = ctk.CTkLabel(self, text="")
        self.label_msg.pack(pady=8)

        ctk.CTkButton(self, text="Cadastrar", width=300, command=self.cadastrar).pack(pady=8)
        ctk.CTkButton(self, text="Voltar", width=300, fg_color="transparent",
                      border_width=1, command=ir_para_login).pack(pady=8)

    def cadastrar(self):
        sucesso, mensagem = self.controller.cadastrar(
            self.entry_nome.get(),
            self.entry_email.get(),
            self.entry_senha.get(),
            self.menu_tipo.get()
        )
        if sucesso:
            self.label_msg.configure(text=mensagem, text_color="green")
        else:
            self.label_msg.configure(text=mensagem, text_color="red")