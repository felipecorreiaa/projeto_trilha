import customtkinter as ctk


class FormularioAtividade(ctk.CTkToplevel):
    def __init__(self, master, titulo, valores, ao_salvar):
        super().__init__(master)
        self.title(titulo)
        self.geometry("420x480")
        self.ao_salvar = ao_salvar
        self.transient(master.winfo_toplevel())
        self.after(150, self.prender)

        ctk.CTkLabel(self, text=titulo, font=("Small Fonts", 22, "bold")).pack(pady=(25, 15))

        self.entry_nome = self.criar_campo("Nome da atividade", valores.get("nome", ""))
        self.entry_dia = self.criar_campo("Dia (dd/mm/aaaa)", valores.get("dia", ""))
        self.entry_horario = self.criar_campo("Horário (HH:MM)", valores.get("horario", ""))
        self.entry_descricao = self.criar_campo("Descrição", valores.get("descricao", ""))
        self.entry_link = self.criar_campo("Link de inscrição (opcional)", valores.get("link", ""))

        # Enter pula para o próximo campo; no último, salva
        campos = [self.entry_nome, self.entry_dia, self.entry_horario,
                  self.entry_descricao, self.entry_link]
        for atual, proximo in zip(campos, campos[1:]):
            atual.bind("<Return>", lambda event, p=proximo: p.focus())
        self.entry_link.bind("<Return>", lambda event: self.salvar())

        self.label_msg = ctk.CTkLabel(self, text="")
        self.label_msg.pack(pady=8)

        ctk.CTkButton(self, text="Salvar", width=340, command=self.salvar).pack(pady=6)
        ctk.CTkButton(self, text="Cancelar", width=340, fg_color="transparent",
                      border_width=1, command=self.destroy).pack(pady=6)

    def prender(self):
        self.lift()
        self.focus()
        self.grab_set()

    def criar_campo(self, placeholder, valor=""):
        entry = ctk.CTkEntry(self, placeholder_text=placeholder, width=340)
        entry.pack(pady=8)
        if valor:
            entry.insert(0, valor)
        return entry

    def salvar(self):
        sucesso, mensagem = self.ao_salvar(
            self.entry_nome.get(),
            self.entry_dia.get(),
            self.entry_horario.get(),
            self.entry_descricao.get(),
            self.entry_link.get()
        )
        if sucesso:
            self.destroy()
        else:
            self.label_msg.configure(text=mensagem, text_color="red")