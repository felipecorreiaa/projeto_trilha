# projeto_trilha
## 🧭 Trilha

Trilha é um sistema desktop de gestão de organizações estudantis (como ligas acadêmicas, diretórios acadêmicos, atléticas e grupos de estudos), desenvolvido como projeto interdisciplinar do 1º período do curso de Sistemas de Informação da Universidade Federal Rural de Pernambuco (UFRPE).

Hoje, essa gestão costuma ser manual e fragmentada, espalhada entre Discord, grupos de WhatsApp e planilhas. A proposta do Trilha é centralizar atividades, materiais e participação em um único lugar

## 🎯 Público-alvo

Gestores e membros de organizações estudantis em ambiente universitário.

## 🛠️ Funcionalidades 

👥 Cadastro de membro e gestor 
🏛️ Lista de organizações cadastradas
📁 Repositório de arquivos da organização (envio e download)
📅 Calendário de atividades
📄 Emissão automática de certificado em PDF 
📢 Mural de avisos
🔑 Diferentes níveis de acesso para gestores e membros

## 🛠️ Tecnologias

Python

CustomTkinter

SQLite

## 🚀 Como executar

Clone o repositório:
git clone https://github.com/felipecorreiaa/projeto_trilha.git
cd projeto_trilha

Instale as dependências:
pip install -r requirements.txt

Execute o sistema:
python main.py

## 🚀 Release 1.0
|Funcionalidade	| Descrição |
|---|---|
| Menu Inicial | Menu principal do sistema. Se o usuário digitar uma opção inexistente, é notificado e solicitado a digitar novamente. |
| Cadastro de Conta |	Cadastro de usuário (gestor ou membro) com e-mail, senha e tipo de cadastro. |
| Organizações (Membro) |	O membro visualiza as organizações cadastradas e acessa a área de uma organização específica para ver suas informações. |
| Organizações (Gestor) |	O gestor visualiza, cadastra, edita e exclui organizações, com validação de nome inválido e de nome já existente. |
| Adicionar Atividade |	O gestor adiciona uma atividade à agenda da organização (dia, horário e breve descrição/link de inscrição), exibida para todos os membros na aba de calendário. Valida dia, horário e descrição. |


## 🎓 Projeto acadêmico

Projeto em desenvolvimento durante o 1º período do curso de Sistemas de Informação da Universidade Federal Rural de Pernambuco (UFRPE) pelo estudante Felipe Correia.
