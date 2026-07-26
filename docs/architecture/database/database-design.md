# Database Design - LinkShield

## Banco de Dados

O LinkShield utilizará PostgreSQL como banco de dados principal.

## Motivo da escolha

O PostgreSQL foi escolhido pelos seguintes motivos:

- estabilidade;
- suporte a relacionamentos complexos;
- recursos avançados de segurança;
- excelente integração com Python;
- suporte a índices e consultas avançadas.

## Padrão de Nomenclatura

As tabelas utilizarão:

- nomes em snake_case;
- nomes no plural;
- chaves primárias usando id;
- chaves estrangeiras usando entidade_id.

Exemplo:

usuarios

usuario_id

analises

analise_id
