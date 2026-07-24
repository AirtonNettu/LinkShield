# Etapa 08 — Instalação do FastAPI

## Objetivo

Adicionar o framework FastAPI como primeira dependência oficial do backend.

## O que foi feito

- Definido o uso do uv como gerenciador de dependências.
- Instalado o FastAPI usando `uv add fastapi`.
- Atualizado o pyproject.toml.
- Criado o arquivo uv.lock.

## Conceitos aprendidos

- Gerenciamento moderno de dependências Python.
- Diferença entre dependências diretas e indiretas.
- Papel do pyproject.toml e uv.lock.

## Impacto na arquitetura

O backend do LinkShield agora possui a base tecnológica para criação da API REST.

## Arquivos alterados

- pyproject.toml
- uv.lock
- docs/development-journal/etapa-08-fastapi.md

## Próxima etapa

Adicionar o servidor ASGI Uvicorn e criar a primeira execução da aplicação.