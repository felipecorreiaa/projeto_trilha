import customtkinter as ctk
from tkinter import messagebox
from controllers.organizacoes_controller import OrganizacoesController


class TelaMinhasOrganizacoes(ctk.CTkFrame):
    def __init__(self, master, usuario, ao_voltar):
        super().__init__(master, fg_color="transparent")
        self.usuario = usuario
        self.controller = OrganizacoesController()

        topo = ctk.CTkFrame(self, fg_color="transparent")
        topo.pack(fill="x", padx=20, pady=(20, 10))
        ctk.CTkButton(topo, text="Voltar", width=80, command=ao_voltar).pack(side="left")
        ctk.CTkLabel(topo, text="Minhas organizações",
                     font=("Small Fonts", 24, "bold")).pack(side="left", padx=20)

        cadastro = ctk.CTkFrame(self, fg_color="transparent")
        cadastro.pack(fill="x", padx=20, pady=10)
        self.entry_nome = ctk.CTkEntry(cadastro, placeholder_text="Nome da nova organização", width=400)
        self.entry_nome.pack(side="left", padx=(0, 10))
        self.entry_nome.bind("<Return>", lambda event: self.cadastrar())
        ctk.CTkButton(cadastro, text="Cadastrar", width=100, command=self.cadastrar).pack(side="left")

        self.label_msg = ctk.CTkLabel(self, text="")
        self.label_msg.pack(pady=5)

        self.lista = ctk.CTkScrollableFrame(self)
        self.lista.pack(fill="both", expand=True, padx=20, pady=10)

        self.carregar_organizacoes()

    def mostrar_mensagem(self, sucesso, mensagem):
        if sucesso:
            cor = "green"
        else:
            cor = "red"
        self.label_msg.configure(text=mensagem, text_color=cor)

    def carregar_organizacoes(self):
        for widget in self.lista.winfo_children():
            widget.destroy()

        organizacoes = self.controller.listar_organizacoes_por_gestor(self.usuario['id'])
        if not organizacoes:
            ctk.CTkLabel(self.lista, text="Você não possui organizações cadastradas.").pack(pady=20)
            return

        for organizacao in organizacoes:
            linha = ctk.CTkFrame(self.lista)
            linha.pack(fill="x", pady=4)
            ctk.CTkLabel(linha, text=organizacao['nome'],
                         font=("Small Fonts", 16)).pack(side="left", padx=15, pady=10)
            ctk.CTkButton(linha, text="Excluir", width=80, fg_color="#b00020",
                          hover_color="#800018",
                          command=lambda o=organizacao: self.excluir(o)).pack(side="right", padx=(0, 15))
            ctk.CTkButton(linha, text="Editar", width=80,
                          command=lambda o=organizacao: self.editar(o)).pack(side="right", padx=8)

    def cadastrar(self):
        sucesso, mensagem = self.controller.cadastrar(self.entry_nome.get(), self.usuario['id'])
        self.mostrar_mensagem(sucesso, mensagem)
        if sucesso:
            self.entry_nome.delete(0, "end")
            self.carregar_organizacoes()

    def editar(self, organizacao):
        dialogo = ctk.CTkInputDialog(
            text=f"Novo nome para '{organizacao['nome']}':",
            title="Editar organização"
        )
        novo_nome = dialogo.get_input()
        if novo_nome is None:        # o usuário cancelou
            return
        sucesso, mensagem = self.controller.atualizar(organizacao['id'], novo_nome)
        self.mostrar_mensagem(sucesso, mensagem)
        if sucesso:
            self.carregar_organizacoes()

    def excluir(self, organizacao):
        if messagebox.askyesno("Excluir organização", f"Deseja excluir '{organizacao['nome']}' mesmo?"):
            sucesso, mensagem = self.controller.excluir(organizacao['id'])
            self.mostrar_mensagem(sucesso, mensagem)
            self.carregar_organizacoes()