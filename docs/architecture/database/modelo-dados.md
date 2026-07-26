---

# Relacionamentos

## Usuário → Análise

Um usuário pode realizar várias análises.

Relacionamento:

1:N

---

# URL Analisada → Análise

Uma URL pode possuir uma ou mais análises realizadas.

Relacionamento:

1:N

---

## Análise → Resultado

Cada análise gera um resultado.

Relacionamento:

1:1

---

## Análise → Relatório

Uma análise pode gerar um relatório consolidado.

Relacionamento:

1:1

---

## Sistema → Auditoria

Eventos importantes do sistema são registrados para rastreabilidade.

Relacionamento:

1:N

---

## Atributos das Entidades

## Usuário

- id
- nome
- email
- senha_hash
- ativo
- criado_em
- atualizado_em

## URL Analisada

- id
- usuario_id
- url
- dominio
- criada_em

## Análise de Segurança

- id
- url_id
- status
- tipo_analise
- iniciada_em
- finalizada_em

## Resultado

- id
- analise_id
- classificacao
- nivel_risco
- descricao
- criado_em

## Relatório

- id
- analise_id
- conteudo
- gerado_em

## Auditoria

- id
- usuario_id
- acao
- ip_origem
- criado_em

---

## Token de Acesso

- id
- usuario_id
- token_hash
- expiracao
- criado_em
- revogado_em
