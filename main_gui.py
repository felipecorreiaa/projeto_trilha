from database.criar_banco import criar_tabelas
from gui.app import App

if __name__ == "__main__":
    criar_tabelas()
    App().mainloop()