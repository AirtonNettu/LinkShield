# ADR-001 — Escolha do FastAPI

## Status

Aceita

## Data

2026-07-24

## Contexto

O LinkShield necessita de uma API REST moderna, com alto desempenho, validação de dados, documentação automática e boa integração com o ecossistema Python.

## Decisão

O projeto utilizará o FastAPI como framework principal para a camada HTTP.

## Justificativa

A escolha foi baseada nos seguintes fatores:

- Alto desempenho baseado em ASGI.
- Integração nativa com Pydantic.
- Documentação automática (OpenAPI/Swagger).
- Tipagem forte utilizando recursos modernos do Python.
- Grande adoção pela comunidade.

## Consequências

### Positivas

- Desenvolvimento rápido.
- Código fortemente tipado.
- Excelente documentação da API.
- Facilidade para testes.

### Negativas

- Curva de aprendizado maior que frameworks mais simples.
- Dependência do ecossistema ASGI.

## Alternativas consideradas

- Flask
- Django REST Framework