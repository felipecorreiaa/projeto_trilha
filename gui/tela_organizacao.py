import customtkinter as ctk
import webbrowser
from datetime import datetime
from tkinter import messagebox
from controllers.usuario_controller import UsuarioController
from controllers.atividades_controller import AtividadesController
from controllers.inscricao_controller import InscricaoController
from gui.formulario_atividade import FormularioAtividade
from gui.janela_presenca import JanelaPresenca


def formatar_dia(dia_iso):
    return datetime.strptime(dia_iso, "%Y-%m-%d").strftime("%d/%m/%Y")

def abrir_link(link):
    if not link.startswith(("http://", "https://")):
        link = "https://" + link
    webbrowser.open(link)


class TelaOrganizacao(ctk.CTkFrame):
    def __init__(self, master, usuario, organizacao, ao_voltar):
        super().__init__(master, fg_color="transparent")
        self.usuario = usuario
        self.organizacao = organizacao
        self.dono = organizacao['gestor_id'] == usuario['id']
        self.atividades_controller = AtividadesController()
        self.inscricao_controller = InscricaoController()

        gestor = UsuarioController().buscar_por_id(organizacao['gestor_id'])
        if gestor:
            nome_gestor = gestor['nome']
        else:
            nome_gestor = "Gestor não encontrado"

        topo = ctk.CTkFrame(self, fg_color="transparent")
        topo.pack(fill="x", padx=20, pady=(20, 5))
        ctk.CTkButton(topo, text="Voltar", width=80, command=ao_voltar).pack(side="left")
        ctk.CTkLabel(topo, text=organizacao['nome'],
                     font=("Small Fonts", 24, "bold")).pack(side="left", padx=20)
        if self.dono:
            ctk.CTkButton(topo, text="Adicionar atividade", width=160,
                          command=self.adicionar).pack(side="right")
        ctk.CTkLabel(self, text=f"Gestor: {nome_gestor}").pack(anchor="w", padx=20)

        self.label_msg = ctk.CTkLabel(self, text="")
        self.label_msg.pack(pady=5)

        self.lista = ctk.CTkScrollableFrame(self)
        self.lista.pack(fill="both", expand=True, padx=20, pady=10)

        self.carregar_atividades()

    def carregar_atividades(self):
        for widget in self.lista.winfo_children():
            widget.destroy()

        atividades = self.atividades_controller.listar_por_organizacao(self.organizacao['id'])
        if not atividades:
            ctk.CTkLabel(self.lista, text="Nenhuma atividade cadastrada.").pack(pady=20)
            return

        inscritas = set()
        for atividade in self.inscricao_controller.listar_por_usuario(self.usuario['id']):
            inscritas.add(atividade['id'])

        for atividade in atividades:
            self.criar_cartao(atividade, atividade['id'] in inscritas)

    def criar_cartao(self, atividade, inscrito):
        cartao = ctk.CTkFrame(self.lista)
        cartao.pack(fill="x", pady=5)

        info = ctk.CTkFrame(cartao, fg_color="transparent")
        info.pack(side="left", fill="x", expand=True, padx=15, pady=10)
        titulo = f"{formatar_dia(atividade['dia'])} {atividade['horario']} - {atividade['nome']}"
        ctk.CTkLabel(info, text=titulo, font=("Small Fonts", 16, "bold"), anchor="w").pack(fill="x")
        ctk.CTkLabel(info, text=atividade['descricao'], anchor="w",
                     justify="left", wraplength=450).pack(fill="x")
        if atividade['link_inscricao']:
            link = atividade['link_inscricao']
            linha_link = ctk.CTkFrame(info, fg_color="transparent")
            linha_link.pack(fill="x", anchor="w")

            ctk.CTkButton(linha_link, text=link, anchor="w", width=0,
                          fg_color="transparent", hover_color=("gray80", "gray25"),
                          text_color=("#1a73e8", "#6ea8fe"),
                          command=lambda l=link: abrir_link(l)).pack(side="left")
            ctk.CTkButton(linha_link, text="Copiar", width=60,
                          command=lambda l=link: self.copiar_link(l)).pack(side="left", padx=8)

        botoes = ctk.CTkFrame(cartao, fg_color="transparent")
        botoes.pack(side="right", padx=15)

        if self.dono:
            ctk.CTkButton(botoes, text="Presença", width=100,
                          command=lambda a=atividade: self.abrir_presenca(a)).pack(pady=2)
            ctk.CTkButton(botoes, text="Editar", width=100,
                          command=lambda a=atividade: self.editar(a)).pack(pady=2)
            ctk.CTkButton(botoes, text="Excluir", width=100, fg_color="#b00020",
                          hover_color="#800018",
                          command=lambda a=atividade: self.excluir(a)).pack(pady=2)
        else:
            if inscrito:
                ctk.CTkButton(botoes, text="Cancelar inscrição", width=140,
                              command=lambda a=atividade: self.cancelar(a)).pack()
            else:
                ctk.CTkButton(botoes, text="Inscrever-se", width=140,
                              command=lambda a=atividade: self.inscrever(a)).pack()

    def mostrar_mensagem(self, sucesso, mensagem):
        if sucesso:
            cor = "green"
        else:
            cor = "red"
        self.label_msg.configure(text=mensagem, text_color=cor)

    def inscrever(self, atividade):
        sucesso, mensagem = self.inscricao_controller.inscrever(atividade['id'], self.usuario['id'])
        self.mostrar_mensagem(sucesso, mensagem)
        self.carregar_atividades()

    def cancelar(self, atividade):
        sucesso, mensagem = self.inscricao_controller.cancelar(atividade['id'], self.usuario['id'])
        self.mostrar_mensagem(sucesso, mensagem)
        self.carregar_atividades()

    def excluir(self, atividade):
        if messagebox.askyesno("Excluir atividade", f"Deseja excluir '{atividade['nome']}' mesmo?"):
            sucesso, mensagem = self.atividades_controller.excluir(atividade['id'], self.usuario['id'])
            self.mostrar_mensagem(sucesso, mensagem)
            self.carregar_atividades()

    def adicionar(self):
        def salvar(nome, dia, horario, descricao, link):
            sucesso, mensagem = self.atividades_controller.cadastrar(
                self.organizacao['id'], self.usuario['id'],
                nome, dia, horario, descricao, link
            )
            if sucesso:
                self.mostrar_mensagem(True, mensagem)
                self.carregar_atividades()
            return sucesso, mensagem

        FormularioAtividade(self, "Adicionar atividade", {}, salvar)

    def editar(self, atividade):
        valores = {
            "nome": atividade['nome'],
            "dia": formatar_dia(atividade['dia']),
            "horario": atividade['horario'],
            "descricao": atividade['descricao'],
            "link": atividade['link_inscricao'] or "",
        }

        def salvar(nome, dia, horario, descricao, link):
            sucesso, mensagem = self.atividades_controller.atualizar(
                atividade['id'], self.usuario['id'],
                nome, dia, horario, descricao, link
            )
            if sucesso:
                self.mostrar_mensagem(True, mensagem)
                self.carregar_atividades()
            return sucesso, mensagem

        FormularioAtividade(self, "Editar atividade", valores, salvar)

    def copiar_link(self, link):
        self.clipboard_clear()
        self.clipboard_append(link)
        self.update()
        self.mostrar_mensagem(True, "Link copiado.")

    def abrir_presenca(self, atividade):
        JanelaPresenca(self, atividade, self.usuario, self.inscricao_controller)