import customtkinter as ctk
from tkinter import messagebox
from controllers.usuario_controller import UsuarioController


class TelaConta(ctk.CTkFrame):
    def __init__(self, master, usuario, ao_voltar, ao_atualizar, ao_excluir):
        super().__init__(master, fg_color="transparent")
        self.controller = UsuarioController()
        self.usuario = usuario
        self.ao_atualizar = ao_atualizar
        self.ao_excluir = ao_excluir

        ctk.CTkLabel(self, text="MINHA CONTA", font=("Small Fonts", 28, "bold")).pack(pady=(40, 5))
        ctk.CTkLabel(self, text=f"Tipo de conta: {usuario['tipo']}").pack(pady=(0, 20))

        self.entry_nome = ctk.CTkEntry(self, width=300)
        self.entry_nome.insert(0, usuario['nome'])
        self.entry_nome.pack(pady=8)

        self.entry_email = ctk.CTkEntry(self, width=300)
        self.entry_email.insert(0, usuario['email'])
        self.entry_email.pack(pady=8)

        self.entry_senha = ctk.CTkEntry(self, placeholder_text="Nova senha", show="*", width=300)
        self.entry_senha.pack(pady=8)

        self.label_msg = ctk.CTkLabel(self, text="")
        self.label_msg.pack(pady=8)

        ctk.CTkButton(self, text="Salvar alterações", width=300, command=self.salvar).pack(pady=8)
        ctk.CTkButton(self, text="Excluir conta", width=300, fg_color="#b00020",
                      hover_color="#800018", command=self.excluir).pack(pady=8)
        ctk.CTkButton(self, text="Voltar", width=300, fg_color="transparent",
                      border_width=1, command=ao_voltar).pack(pady=8)

    def salvar(self):
        sucesso, mensagem = self.controller.editar_usuario(
            self.usuario['id'],
            self.entry_nome.get(),
            self.entry_email.get(),
            self.entry_senha.get()
        )
        if sucesso:
            self.usuario = self.controller.buscar_por_id(self.usuario['id'])
            self.ao_atualizar(self.usuario)
            self.entry_senha.delete(0, "end")
            self.label_msg.configure(text=mensagem, text_color="green")
        else:
            self.label_msg.configure(text=mensagem, text_color="red")

    def excluir(self):
        if messagebox.askyesno("Excluir conta", "Deseja excluir a conta mesmo? Essa ação não pode ser desfeita."):
            sucesso, mensagem = self.controller.excluir_conta(self.usuario['id'])
            if sucesso:
                self.ao_excluir()
            else:
                self.label_msg.configure(text=mensagem, text_color="red")