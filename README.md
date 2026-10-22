
# 💇‍♀️ Salão Bella Beleza

### Sistema Web de Gestão para Salão de Beleza

![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Framework-000000?logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Banco_de_Dados-003B57?logo=sqlite&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Testes-2088FF?logo=githubactions&logoColor=white)
![Status](https://img.shields.io/badge/Status-MVP_Publicado-brightgreen)

> Projeto acadêmico desenvolvido na disciplina de **Projeto de Software**, contemplando as Experiências Práticas I, II, III e IV.

## 🌐 Acesse o sistema

**[Clique aqui para acessar o Salão Bella Beleza](https://leticiaferraz.pythonanywhere.com/)**

A aplicação está hospedada na plataforma PythonAnywhere.

> **Atenção:** o sistema é um MVP acadêmico. Não utilize dados pessoais reais, pois ainda não possui autenticação e controle de acesso.

---

## 📖 Sobre o projeto

O **Salão Bella Beleza** é uma aplicação web desenvolvida para auxiliar na organização administrativa de um salão de beleza.

O projeto surgiu da necessidade de centralizar informações sobre clientes e serviços, reduzindo a dependência de anotações manuais e facilitando a consulta dos registros.

A proposta inicial também incluía um sistema completo de agendamentos. Entretanto, durante o desenvolvimento, o escopo foi reduzido para priorizar a entrega de funcionalidades básicas, testadas e funcionais.

O MVP foi desenvolvido utilizando **Python, Flask e SQLite**, com interface construída em HTML, CSS e JavaScript.

## 🎯 Objetivos

- Facilitar o cadastro de clientes.
- Organizar os serviços oferecidos pelo salão.
- Centralizar as informações em um banco de dados.
- Oferecer uma interface simples e acessível.
- Aplicar boas práticas de desenvolvimento e versionamento.
- Disponibilizar o MVP em um ambiente de nuvem pública.

## ✨ Funcionalidades implementadas

| Funcionalidade | Descrição | Situação |
|---|---|---|
| Página inicial | Navegação entre as funcionalidades | ✅ Concluída |
| Cadastro de clientes | Registro de informações de clientes | ✅ Concluída |
| Consulta de clientes | Visualização dos clientes cadastrados | ✅ Concluída |
| Cadastro de serviços | Registro de serviços, preços e durações | ✅ Concluída |
| Consulta de serviços | Visualização dos serviços cadastrados | ✅ Concluída |
| Validação de serviços | Verificação de valores informados | ✅ Concluída |
| Mensagens de confirmação | Feedback visual após os cadastros | ✅ Concluída |
| Modo de alto contraste | Recurso para facilitar a leitura | ✅ Concluída |
| Gerenciamento de agendamentos | Cadastro e controle de horários | ⏳ Planejado |
| Edição e exclusão de registros | Atualização e remoção de informações | ⏳ Planejado |
| Autenticação | Controle de acesso aos dados | ⏳ Planejado |

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem principal |
| Flask | Framework web |
| SQLite | Banco de dados relacional |
| HTML5 | Estrutura das páginas |
| CSS3 | Estilização e acessibilidade |
| JavaScript | Interatividade e alto contraste |
| Jinja2 | Renderização de templates |
| pytest | Testes automatizados |
| Git | Controle de versões |
| GitHub | Hospedagem do código-fonte |
| GitHub Actions | Integração contínua |
| PythonAnywhere | Hospedagem da aplicação |
| UptimeRobot | Monitoramento de disponibilidade |

---

## 📁 Estrutura do projeto

```text
salao-bella-beleza/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── templates/
│   ├── index.html
│   ├── clientes.html
│   └── servicos.html
│
├── tests/
│   ├── test_database.py
│   └── test_integracao.py
│
├── app.py
├── database.py
├── README.md
└── .gitignore
```

### Principais arquivos

- **app.py:** contém as rotas e a lógica principal da aplicação Flask.
- **database.py:** gerencia a conexão com o SQLite e a criação das tabelas.
- **templates/:** contém as páginas HTML da aplicação.
- **tests/:** contém os testes automatizados.
- **tests.yml:** configura a execução dos testes no GitHub Actions.

## 🚀 Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/LeticiaFerraz00/salao-bella-beleza.git
```

### 2. Entre na pasta

```bash
cd salao-bella-beleza
```

### 3. Crie o ambiente virtual

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 5. Instale as dependências

```bash
python -m pip install Flask pytest pytest-cov
```

### 6. Prepare o banco de dados

```bash
python -c "from database import criar_tabelas; criar_tabelas()"
```

### 7. Execute a aplicação

```bash
python app.py
```

Acesse no navegador:

```text
http://127.0.0.1:5000
```

> As instruções acima são destinadas ao ambiente de desenvolvimento local. Em produção, utilize um servidor WSGI e configure uma chave secreta de sessão segura.

---

## 🧪 Testes automatizados

O projeto utiliza **pytest** para verificar funcionalidades importantes.

Os testes incluem:

- Verificação da conexão com o banco SQLite.
- Teste de integração do cadastro de clientes.

Para executar:

```bash
python -m pytest tests/ -v
```

Para verificar a cobertura:

```bash
python -m pytest tests/ --cov=app --cov=database --cov-report=term-missing
```

### Integração contínua

O repositório possui um workflow do **GitHub Actions** que executa verificações automatizadas após atualizações nas branches configuradas.

Isso ajuda a identificar possíveis problemas e manter a qualidade do código.

---

## ♿ Acessibilidade

O sistema possui um modo de alto contraste implementado com CSS e JavaScript.

Quando ativado, a interface utiliza:

- Fundo preto.
- Textos brancos.
- Botões e elementos de destaque amarelos.

A preferência é armazenada no `localStorage`, permitindo que seja mantida durante a navegação.

As mensagens de confirmação também utilizam o atributo `role="status"` para melhorar a comunicação com tecnologias assistivas.

Esses recursos representam melhorias iniciais de acessibilidade, não uma certificação de conformidade integral com as WCAG.

## ☁️ Publicação na nuvem

A aplicação foi publicada no **PythonAnywhere**, utilizando:

- Python 3.13.
- Ambiente virtual.
- Configuração WSGI.
- Banco SQLite.
- Chave de sessão armazenada fora do repositório público.

**Endereço:** https://leticiaferraz.pythonanywhere.com/

## 📊 Monitoramento

A disponibilidade da aplicação é acompanhada pelo **UptimeRobot**, por meio de verificações HTTP(s) a cada cinco minutos.

A ferramenta permite identificar interrupções de disponibilidade e acompanhar o histórico de funcionamento.

> A hospedagem gratuita pode possuir limitações de recursos, disponibilidade e necessidade de renovação periódica.

---

## 🔐 Segurança e limitações

O projeto utiliza consultas SQL parametrizadas e validações básicas para reduzir problemas de entrada de dados.

Durante a publicação, a chave secreta de sessão foi armazenada separadamente do código-fonte.

Entretanto, o MVP ainda não possui:

- Autenticação e autorização de usuários.
- Controle de acesso aos registros.
- Gerenciamento completo de agendamentos.
- Edição e exclusão de cadastros.
- Proteções completas para uso com dados pessoais reais.

Por isso, a versão publicada é destinada à demonstração acadêmica e deve utilizar somente dados fictícios.

## 🔮 Melhorias futuras

As próximas versões poderão incluir:

1. **Cadastro integrado de atendimentos:** reunir cliente, telefone, serviço, horário, profissional e preço.
2. **Agenda diária:** visualizar os atendimentos programados.
3. **Prevenção de conflitos:** impedir agendamentos em horários incompatíveis.
4. **Edição e exclusão:** atualizar ou remover registros com segurança.
5. **Autenticação:** restringir o acesso às informações.
6. **Melhorias de usabilidade:** simplificar os fluxos conforme o feedback dos usuários.
7. **Ampliação dos testes:** aumentar a cobertura das funcionalidades.

## 🌱 Objetivo de Desenvolvimento Sustentável

O projeto está relacionado ao:

**ODS 8 — Trabalho Decente e Crescimento Econômico**

A iniciativa busca contribuir para a modernização dos processos administrativos de pequenos empreendimentos.

Embora o MVP tenha demonstrado potencial para facilitar a organização dos registros, ainda são necessárias novas funcionalidades e medições para comprovar ganhos de produtividade e redução de conflitos de agendamento.

---

## 👩‍💻 Autoria

**Leticia Ferraz**

Curso de graduação — Disciplina de Projeto de Software

Experiências Práticas I, II, III e IV.

**GitHub:** [LeticiaFerraz00](https://github.com/LeticiaFerraz00)

---

### 💗 Salão Bella Beleza

*Um projeto acadêmico que transformou planejamento, programação, testes e implantação em uma aplicação web funcional.*
