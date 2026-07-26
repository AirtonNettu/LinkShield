# Etapa 12 — Organização das Camadas

## Objetivo

Organizar a estrutura interna do backend do LinkShield utilizando separação de responsabilidades.

Nesta etapa foi criada a base arquitetural para permitir crescimento do sistema sem concentrar regras de negócio, acesso a dados e integrações em um único local.

---

## Motivação

Durante as primeiras etapas o projeto possuía apenas a estrutura inicial da API:

```text
app/

├── main.py
└── api/
