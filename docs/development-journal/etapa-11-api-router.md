# Etapa 11 - Organização inicial da API

## Objetivo

Separar os endpoints da aplicação utilizando APIRouter.

## Implementação

Foi criada a estrutura:

app/api/v1/routes

Criado o router de health check.

## Conceitos aprendidos

- módulos Python;
- pacotes;
- imports;
- APIRouter;
- separação de responsabilidades.

## Testes

Servidor iniciado com:

uvicorn app.main:app --reload

Endpoint validado:

GET /

Resposta:

{
    "message": "LinkShield API running"
}

Swagger validado em:

/docs