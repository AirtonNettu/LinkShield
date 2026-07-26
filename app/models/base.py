# Importa a classe DeclarativeBase do SQLAlchemy ORM.
# Ela será usada como base para criação dos modelos do banco.
# Todas as entidades do sistema irão herdar dessa classe.

from sqlalchemy.orm import DeclarativeBase


# Classe base do ORM do LinkShield.
# Responsabilidade:
# - Centralizer a configuração dos modelos SQLAlchemy.
# - Permitir que todas as enfilades compartilhem a mesma metadata.
#
# Futuramente:
# Usuario, Analise, Resultado, Auditoria etc.
# irão herdar dessa classe.

class Base(DeclarativeBase):
    pass