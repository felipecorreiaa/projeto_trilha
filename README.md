# 🧭 Trilha

Trilha é um sistema desktop de gestão de organizações estudantis (como ligas acadêmicas, diretórios acadêmicos, atléticas e grupos de estudos), desenvolvido como projeto interdisciplinar do 1º período do curso de Sistemas de Informação da Universidade Federal Rural de Pernambuco (UFRPE).

Hoje, essa gestão costuma ser manual e fragmentada, espalhada entre Discord, grupos de WhatsApp e planilhas. A proposta do Trilha é centralizar atividades, materiais e participação em um único lugar

## 🎯 Público-alvo

Gestores e membros de organizações estudantis em ambiente universitário.

## 🛠️ Funcionalidades 

🔐 Cadastro e login de usuários (gestor e membro)

🔑 Níveis de acesso diferentes para gestores e membros

🏛️ Lista e busca de organizações cadastradas

📅 Calendário de atividades da organização: cadastro, edição e exclusão pelo gestor

📝 Inscrição e cancelamento de inscrição em atividades

✅ Controle de presença dos inscritos pelo gestor

👤 Minha conta: alteração dos dados e exclusão da conta

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
| Organizações (Membro) |	O membro visualiza as organizações cadastradas. |
| Organizações (Gestor) |	O gestor visualiza, cadastra, edita e exclui organizações, com validação de nome inválido e de nome já existente. |
| Busca de organização por palavra-chave |	O usuário visualiza as organizações cadastradas e pode fazer uma busca usando apenas palavras para encontrar a organização desejada. |

## 🚀 Release 2.0

| Funcionalidade | Descrição |
|---|---|
| Cadastro de Atividade | O gestor adiciona uma atividade à agenda da organização (nome, dia, horário, descrição e link de inscrição opcional), exibida para todos os usuários. Valida campos em branco, dia, horário e se o usuário é o gestor da organização. |
| Leitura e Edição de Atividade | Qualquer usuário vê as atividades da organização, ordenadas por data e horário. O gestor edita uma atividade, mantendo os valores atuais dos campos deixados em branco. |
| Exclusão de Atividade | O gestor exclui uma atividade (e as inscrições ligadas a ela) após confirmar a exclusão. |
| Inscrição na Atividade | O usuário se inscreve em uma atividade da organização ou cancela a inscrição. Não permite inscrição em atividade que já aconteceu nem inscrição duplicada. |
| Controle de Presença | O gestor escolhe uma atividade, vê os inscritos e marca ou desmarca a presença de cada um. |

## 🎓 Projeto acadêmico

Projeto em desenvolvimento durante o 1º período do curso de Sistemas de Informação da Universidade Federal Rural de Pernambuco (UFRPE) pelo estudante Felipe Albuquerque Correia.
