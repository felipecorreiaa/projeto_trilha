import os
import customtkinter as ctk
from gui.tela_login import TelaLogin
from gui.tela_cadastro import TelaCadastro
from gui.tela_organizacoes import TelaOrganizacoes
from gui.tela_conta import TelaConta
from gui.tela_organizacao import TelaOrganizacao
from gui.tela_minhas_organizacoes import TelaMinhasOrganizacoes

ctk.set_appearance_mode("dark")
ctk.ThemeManager.theme["CTkFont"]["family"] = "Small Fonts"
ctk.ThemeManager.theme["CTkFont"]["size"] = 16
CAMINHO_ICONE = os.path.join(os.path.dirname(__file__), "..", "assets", "icone.ico")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Trilha")
        self.geometry("900x600")
        self.after(200, lambda: self.iconbitmap(CAMINHO_ICONE))
        self.usuario = None
        self.tela_atual = None
        self.mostrar_login()

    def trocar_tela(self, frame):
        if self.tela_atual is not None:
            self.tela_atual.destroy()
        self.tela_atual = frame
        self.tela_atual.pack(fill="both", expand=True)

    def mostrar_login(self):
        self.trocar_tela(TelaLogin(self, self.mostrar_cadastro, self.entrar))

    def mostrar_cadastro(self):
        self.trocar_tela(TelaCadastro(self, self.mostrar_login))

    def entrar(self, usuario):
        self.usuario = usuario
        self.mostrar_organizacoes()

    def mostrar_organizacoes(self):
        self.trocar_tela(TelaOrganizacoes(
            self, self.usuario, self.abrir_organizacao, self.mostrar_conta, self.sair
        ))

    def abrir_organizacao(self, organizacao):
        self.trocar_tela(TelaOrganizacao(
            self, self.usuario, organizacao, self.mostrar_organizacoes
        ))

    def sair(self):
        self.usuario = None
        self.mostrar_login()

    def mostrar_conta(self):
        self.trocar_tela(TelaConta(
            self, self.usuario, self.mostrar_organizacoes, self.atualizar_usuario, self.sair
        ))

    def atualizar_usuario(self, usuario):
        self.usuario = usuario

    def mostrar_organizacoes(self):
        self.trocar_tela(TelaOrganizacoes(
            self, self.usuario, self.abrir_organizacao, self.mostrar_conta,
            self.mostrar_minhas_organizacoes, self.sair
        ))

    def mostrar_minhas_organizacoes(self):
        self.trocar_tela(TelaMinhasOrganizacoes(
            self, self.usuario, self.mostrar_organizacoes
        ))