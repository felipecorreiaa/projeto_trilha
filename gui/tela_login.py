import os
import customtkinter as ctk
from controllers.usuario_controller import UsuarioController
from PIL import Image

CAMINHO_LOGO = os.path.join(os.path.dirname(__file__), "..", "assets", "trilha-logo-claro.png")

class TelaLogin(ctk.CTkFrame):
    def __init__(self, master, ir_para_cadastro, ao_logar):
        super().__init__(master)
        self.controller = UsuarioController()
        self.ao_logar = ao_logar

        imagem = Image.open(CAMINHO_LOGO)
        self.logo = ctk.CTkImage(light_image=imagem, dark_image=imagem, size=(140, 78))

        ctk.CTkLabel(
            self, text="TRILHA", image=self.logo, compound="right",
            font=("Small Fonts", 40, "bold")
            ).pack(pady=(80, 20))

        self.entry_email = ctk.CTkEntry(self, placeholder_text="Email", width=300)
        self.entry_email.pack(pady=8)

        self.entry_senha = ctk.CTkEntry(self, placeholder_text="Senha", show="*", width=300)
        self.entry_senha.pack(pady=8)

        self.entry_email.bind("<Return>", lambda event: self.entry_senha.focus())

        self.entry_senha.bind("<Return>", lambda event: self.entrar())

        self.label_msg = ctk.CTkLabel(self, text="")
        self.label_msg.pack(pady=8)

        ctk.CTkButton(self, text="Entrar", width=300, command=self.entrar).pack(pady=8)
        ctk.CTkButton(self, text="Criar conta", width=300, fg_color="transparent",
                      border_width=1, command=ir_para_cadastro).pack(pady=8)

    def entrar(self):
        sucesso, mensagem, usuario = self.controller.login(
            self.entry_email.get(), self.entry_senha.get()
        )
        if sucesso:
            self.ao_logar(usuario)
        else:
            self.label_msg.configure(text=mensagem, text_color="red")