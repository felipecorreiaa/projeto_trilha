import customtkinter as ctk
from controllers.organizacoes_controller import OrganizacoesController


class TelaOrganizacoes(ctk.CTkFrame):
    def __init__(self, master, usuario, ao_abrir, ao_conta, ao_minhas, ao_sair):
        super().__init__(master, fg_color="transparent")
        self.controller = OrganizacoesController()
        self.ao_abrir = ao_abrir

        topo = ctk.CTkFrame(self, fg_color="transparent")
        topo.pack(fill="x", padx=20, pady=(20, 10))
        ctk.CTkLabel(topo, text=f"Olá, {usuario['nome']}",
                     font=("Small Fonts", 20, "bold")).pack(side="left")
        ctk.CTkButton(topo, text="Sair", width=80, command=ao_sair).pack(side="right")
        ctk.CTkButton(topo, text="Minha conta", width=120, command=ao_conta).pack(side="right", padx=(0, 10))
        if usuario['tipo'] == "gestor":
            ctk.CTkButton(topo, text="Minhas organizações", width=160,
                          command=ao_minhas).pack(side="right", padx=(0, 10))

        busca = ctk.CTkFrame(self, fg_color="transparent")
        busca.pack(fill="x", padx=20, pady=10)
        self.entry_busca = ctk.CTkEntry(busca, placeholder_text="Buscar organização por nome", width=400)
        self.entry_busca.pack(side="left", padx=(0, 10))
        self.entry_busca.bind("<Return>", lambda event: self.buscar())
        ctk.CTkButton(busca, text="Buscar", width=100, command=self.buscar).pack(side="left")

        self.lista = ctk.CTkScrollableFrame(self)
        self.lista.pack(fill="both", expand=True, padx=20, pady=10)

        self.mostrar_organizacoes(self.controller.listar_organizacoes())

    def buscar(self):
        palavra = self.entry_busca.get().strip()
        if palavra:
            organizacoes = self.controller.buscar_por_palavra_chave(palavra)
        else:
            organizacoes = self.controller.listar_organizacoes()
        self.mostrar_organizacoes(organizacoes)

    def mostrar_organizacoes(self, organizacoes):
        for widget in self.lista.winfo_children():
            widget.destroy()

        if not organizacoes:
            ctk.CTkLabel(self.lista, text="Nenhuma organização encontrada.").pack(pady=20)
            return

        for organizacao in organizacoes:
            linha = ctk.CTkFrame(self.lista)
            linha.pack(fill="x", pady=4)
            ctk.CTkLabel(linha, text=organizacao['nome'],
                         font=("Small Fonts", 16)).pack(side="left", padx=15, pady=10)
            ctk.CTkButton(linha, text="Abrir", width=80,
                          command=lambda o=organizacao: self.ao_abrir(o)).pack(side="right", padx=15)