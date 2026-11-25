import customtkinter as ctk


class JanelaPresenca(ctk.CTkToplevel):
    def __init__(self, master, atividade, usuario, inscricao_controller):
        super().__init__(master)
        self.title("Controle de presença")
        self.geometry("420x520")
        self.atividade = atividade
        self.usuario = usuario
        self.inscricao_controller = inscricao_controller
        self.transient(master.winfo_toplevel())
        self.after(150, self.prender)

        ctk.CTkLabel(self, text="Controle de presença",
                     font=("Small Fonts", 22, "bold")).pack(pady=(25, 5))
        ctk.CTkLabel(self, text=atividade['nome']).pack(pady=(0, 10))

        self.label_msg = ctk.CTkLabel(self, text="")
        self.label_msg.pack(pady=5)

        self.lista = ctk.CTkScrollableFrame(self)
        self.lista.pack(fill="both", expand=True, padx=20, pady=10)

        ctk.CTkButton(self, text="Fechar", command=self.destroy).pack(pady=(0, 20))

        self.carregar_inscritos()

    def prender(self):
        self.lift()
        self.focus()
        self.grab_set()

    def carregar_inscritos(self):
        sucesso, mensagem, inscritos = self.inscricao_controller.listar_inscritos(
            self.atividade['id'], self.usuario['id']
        )
        if not sucesso:
            self.label_msg.configure(text=mensagem, text_color="red")
            return

        if not inscritos:
            ctk.CTkLabel(self.lista, text="Nenhum inscrito nesta atividade.").pack(pady=20)
            return

        for inscrito in inscritos:
            caixa = ctk.CTkCheckBox(self.lista, text=inscrito['nome'])
            if inscrito['presente']:
                caixa.select()
            caixa.configure(command=lambda i=inscrito, c=caixa: self.alternar(i, c))
            caixa.pack(anchor="w", pady=8, padx=10)

    def alternar(self, inscrito, caixa):
        if caixa.get() == 1:
            marcado = True
        else:
            marcado = False

        sucesso, mensagem = self.inscricao_controller.marcar_presenca(
            self.atividade['id'], inscrito['usuario_id'], self.usuario['id'], marcado
        )
        if sucesso:
            self.label_msg.configure(text=mensagem, text_color="green")
        else:
            if marcado:
                caixa.deselect()
            else:
                caixa.select()
            self.label_msg.configure(text=mensagem, text_color="red")