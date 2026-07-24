# ADR-002 — Escolha do Uvicorn

## Status

Aceita

## Data

2026-07-24

## Contexto

O LinkShield utiliza FastAPI como framework HTTP.
Para executar uma aplicação FastAPI é necessário um servidor ASGI compatível.

## Decisão

O projeto utilizará o Uvicorn como servidor ASGI principal.

## Justificativa

O Uvicorn foi escolhido por:

- Compatibilidade nativa com FastAPI.
- Alto desempenho.
- Suporte ao padrão ASGI.
- Integração simples com ambientes Python modernos.

## Consequências

### Positivas

- Execução simples da API.
- Boa integração com FastAPI.
- Adequado para desenvolvimento e produção com configuração correta.

### Negativas

- Depende do ecossistema ASGI.
- Configurações de produção podem exigir componentes adicionais.

## Alternativas consideradas

- Hypercorn
- Gunicorn com workers ASGI