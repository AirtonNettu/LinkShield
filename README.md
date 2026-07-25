# 🛡️ LinkShield

<p align="center">
  Plataforma backend para análise e proteção de URLs utilizando Python, FastAPI e boas práticas de Engenharia de Software.
</p>

---

# 📌 Sobre o projeto

O **LinkShield** é uma plataforma em desenvolvimento para análise de links, identificação de riscos e integração com serviços de inteligência de ameaças.

O projeto está sendo construído seguindo uma abordagem profissional de Engenharia de Software, priorizando:

- arquitetura organizada;
- separação de responsabilidades;
- documentação contínua;
- versionamento de código;
- desenvolvimento incremental;
- qualidade e manutenção do software.

O objetivo é evoluir o LinkShield como uma solução real, preparada para receber recursos como:

- análise de URLs;
- classificação de risco;
- histórico de consultas;
- relatórios;
- autenticação;
- integrações com APIs de segurança.

---

# 🎯 Objetivos do projeto

Os principais objetivos do LinkShield são:

- construir uma API backend escalável;
- aplicar boas práticas de desenvolvimento Python;
- desenvolver uma arquitetura preparada para crescimento;
- implementar recursos de segurança;
- integrar serviços externos;
- aplicar conceitos de Engenharia de Software na prática.

---

# 🏗️ Arquitetura do sistema

O LinkShield está sendo desenvolvido utilizando uma arquitetura modular, permitindo evolução gradual do sistema.

## Visão arquitetural planejada

A implementação atual encontra-se na fase inicial da API backend. A arquitetura abaixo representa a evolução planejada do sistema.

```text
Usuário
   |
   v
Interface Web
   |
   v
API REST (FastAPI)
   |
   v
Camada de Aplicação
   |
   v
Serviços de Análise
   |
   +----------------+
   |                |
   v                v
Banco de Dados   APIs Externas
                 Segurança
```

A arquitetura foi planejada para permitir crescimento sem comprometer a organização do sistema.

---

# 🚀 Status atual

O projeto encontra-se na fase inicial de construção da API backend.

## Funcionalidades implementadas:

✅ Estrutura inicial do projeto  
✅ Ambiente Python configurado  
✅ Gerenciamento de dependências com uv  
✅ Aplicação FastAPI funcionando  
✅ Servidor Uvicorn configurado  
✅ Documentação automática Swagger  
✅ Estrutura de rotas utilizando APIRouter  
✅ Versionamento inicial da API  
✅ Controle de código utilizando Git  
✅ Documentação arquitetural inicial  

---

# 📂 Estrutura do projeto

A estrutura do LinkShield segue uma arquitetura modular organizada para permitir evolução gradual do backend.

```text
LinkShield/
│
├── .github/
│
├── app/
│   │
│   ├── api/
│   │   │
│   │   └── v1/
│   │       │
│   │       └── routes/
│   │           │
│   │           ├── __init__.py
│   │           └── health.py
│   │
│   ├── core/
│   │
│   ├── integrations/
│   │   └── providers/
│   │
│   ├── models/
│   │
│   ├── repositories/
│   │
│   ├── schemas/
│   │
│   ├── services/
│   │
│   ├── __init__.py
│   │
│   └── main.py
│
├── docs/
│   │
│   ├── architecture/
│   │   │
│   │   ├── ADR-001-fastapi.md
│   │   └── ADR-002-uvicorn.md
│   │
│   └── development-journal/
│       │
│       ├── etapa-01-inicializacao.md
│       ├── etapa-02-07-fundacao-backend.md
│       ├── etapa-08-fastapi.md
│       ├── etapa-09-10-ambiente-servidor.md
│       └── etapa-11-api-router.md
│
├── .gitignore
│
├── pyproject.toml
│
├── README.md
│
└── uv.lock
```
# 🧩 Organização das camadas

As camadas abaixo representam a arquitetura planejada do backend.

Algumas estruturas já existem no projeto atualmente, enquanto outras serão implementadas conforme a evolução das próximas etapas.

---

## app/api

Camada responsável pela exposição dos endpoints HTTP.

Exemplo:

```text
api/

└── v1/

    └── routes/

        └── health.py
```

Responsável por receber requisições e encaminhar para a aplicação.

---

# app/services

Camada responsável pelas regras de negócio.

Exemplos futuros:

- análise de URL;
- cálculo de risco;
- processamento dos resultados;
- regras de segurança.

---

# app/repositories

Camada responsável pelo acesso aos dados.

Futuramente será responsável pela comunicação com:

- PostgreSQL;
- mecanismos de armazenamento;
- consultas;
- persistência de dados.

---

# app/models

Representação das entidades do sistema.

Exemplos:

- usuário;
- link analisado;
- histórico;
- relatório.

---

# app/schemas

Responsável pela validação dos dados de entrada e saída utilizando modelos Pydantic.

Fluxo:

```text
JSON recebido
      |
      v
Schema
      |
      v
Validação
```

---

# app/integrations/providers

Camada responsável pelas integrações externas.

Exemplos:

- APIs de segurança;
- serviços de threat intelligence;
- provedores externos.

---

# app/core

Configurações centrais da aplicação.

Responsável por:

- configurações globais;
- variáveis de ambiente;
- segurança;
- parâmetros do sistema.

---

# docs

Central de documentação técnica.

Contém:

- arquitetura;
- decisões arquiteturais (ADR);
- diário de desenvolvimento;
- evolução das etapas.

---

# 🧠 Responsabilidade dos arquivos principais

## app/main.py

Arquivo responsável pela inicialização da aplicação FastAPI.

Responsabilidades:

- criar aplicação;
- registrar routers;
- configurar entrada principal da API.

Exemplo:

```python
from fastapi import FastAPI

app = FastAPI()
```

---

# 🔀 Versionamento da API

O projeto utiliza versionamento de API.

Estrutura:

```text
/api/v1
```

O versionamento permite evolução futura sem quebrar clientes existentes.

Exemplo:

```text
/api/v1

/api/v2
```

---

# ❤️ Health Check

Endpoint utilizado para verificar se a API está funcionando.

Endpoint atual:

```http
GET /
```

Resposta:

```json
{
    "message": "LinkShield API running"
}
```

---

# 🛠️ Tecnologias utilizadas

## Backend

- Python 3.12
- FastAPI
- Uvicorn

## Gerenciamento

- uv
- Git
- GitHub

## Documentação

- Markdown
- Swagger OpenAPI

## Planejado

- PostgreSQL
- Docker
- Docker Compose
- Redis
- Autenticação JWT
- APIs de Threat Intelligence
- Frontend Web

---

# ⚙️ Como executar o projeto

## Pré-requisitos

Instalar:

- Python 3.12+
- uv

---

## Instalar dependências

Na raiz do projeto:

```bash
uv sync
```

---

## Ativar ambiente virtual

Linux:

```bash
source .venv/bin/activate
```

---

## Executar servidor

```bash
uvicorn app.main:app --reload
```

Servidor:

```text
http://127.0.0.1:8000
```

---

# 📚 Documentação da API

O FastAPI gera documentação automática utilizando Swagger UI.

Acesse:

```text
http://127.0.0.1:8000/docs
```

---

# 🧪 Teste rápido

Executar:

```bash
curl http://127.0.0.1:8000/
```

Resposta esperada:

```json
{
    "message": "LinkShield API running"
}
```

---

# 📝 Desenvolvimento

O desenvolvimento do LinkShield segue uma abordagem incremental.

Cada etapa possui:

- objetivo;
- estudo dos conceitos;
- implementação;
- testes;
- revisão;
- documentação;
- commit versionado.

---

# 🗺️ Roadmap

## Fundação Backend

✅ Estrutura inicial  
✅ FastAPI configurado  
✅ Uvicorn configurado  
✅ Rotas organizadas  
✅ Documentação inicial  

## Próximas evoluções

⏳ Organização completa das camadas internas  
⏳ Banco de dados PostgreSQL  
⏳ Modelagem das entidades  
⏳ Autenticação e autorização  
⏳ Análise de URLs  
⏳ Integração com APIs de segurança  
⏳ Histórico de consultas  
⏳ Geração de relatórios  
⏳ Dockerização  
⏳ Pipeline CI/CD  
⏳ Deploy em ambiente Cloud  

---

# 🤝 Contribuição

O projeto segue boas práticas de desenvolvimento:

- commits semânticos;
- documentação contínua;
- revisão de alterações;
- evolução incremental;
- organização arquitetural.

---

# 📌 Licença

Projeto em desenvolvimento, criado inicialmente como estudo prático de Engenharia de Software, com objetivo de evolução para uma solução real.

---

# 👨‍💻 Autor

Desenvolvido por **José Airton (Airton Neto)**.

GitHub:https://github.com/AirtonNettu
Linkedin:https://www.linkedin.com/in/jose-airton-cloud


---

Projeto criado com foco em:

- Desenvolvimento Backend;
- Python;
- FastAPI;
- Segurança;
- Arquitetura de Sistemas;
- Cloud Computing.

O LinkShield está sendo desenvolvido seguindo boas práticas profissionais de:

- arquitetura de software;
- documentação técnica;
- versionamento de código;
- organização modular;
- desenvolvimento incremental.

O objetivo é evoluir o LinkShield como uma solução real, com possibilidade futura de disponibilização como produto ou serviço.