from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


# Representa a entidade Usuário no banco de dados.
#
# Responsável apenas pelo mapeamento ORM.
#
# Conecta:
# API → Services → Repository → ORM → Banco
#
# Regras de negócio são tratadas fora deste modelo.

class Usuario(Base):

    # Nome da tabela no banco PostgreSQL.
    __tablename__ = "usuarios"

    # Identificador único do usuário.
    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    # Nome de exibição do usuário.
    nome: Mapped[str]

    # Email utilizado para identificação/login.
    email: Mapped[str]

    # Armazena apenas o hash da senha.
    # Senhas nunca devem ser armazenadas em texto puro.
    senha_hash: Mapped[str]

    # Define se a conta do usuário está ativa.
    #
    # Utilizado para controle de acesso e gerenciamento
    # do Ciclo de vida da conta.
    ativo: Mapped[bool]

    # Registra quando o usuário foi criado
    #
    # Utilizado para auditoria e rastreamento
    # do clico de vida da conta.
    criado_em: Mapped[datetime] = mapped_column(
        default=datetime.utcnow
    )

    # Registra a última atualização do usuário.
    #
    # Permite acompanhar alterações realizadas
    # no Cadastro.
    atualizado_em: Mapped[datetime] = mapped_column(

        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )