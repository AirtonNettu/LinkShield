# Etapas 02-07 — Fundação do Backend

## Objetivo

Construir a base técnica do backend do LinkShield, preparando o projeto para executar uma aplicação FastAPI de forma organizada e reproduzível.

## Decisões tomadas

Durante esta fase foram definidas as bases do projeto:

- utilização do Python como linguagem principal do backend;
- utilização do gerenciador de dependências uv;
- criação de ambiente virtual isolado;
- organização inicial seguindo uma estrutura profissional de projeto.

## Ambiente Python

Foi criado um ambiente virtual próprio do projeto:

.venv/

O objetivo é evitar conflitos entre dependências globais da máquina e as dependências específicas do LinkShield.

O ambiente contém:

- interpretador Python;
- bibliotecas instaladas;
- executáveis utilizados pelo projeto.

## Gerenciamento de dependências

O projeto passou a utilizar:

- pyproject.toml;
- uv.lock.

O arquivo `pyproject.toml` define as dependências principais.

O arquivo `uv.lock` registra versões exatas para garantir instalações reproduzíveis.

## Introdução ao FastAPI

O FastAPI foi escolhido como framework backend.

A primeira aplicação foi criada utilizando:

```python
from fastapi import FastAPI

app = FastAPI()

Neste momento o projeto passou a possuir uma aplicação web executável.