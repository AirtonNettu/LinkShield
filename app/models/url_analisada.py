from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base

from sqlalchemy import ForeignKey

from datetime import datetime

# Modelo ORM responsável por representar uma URL enviada
# pelo usuário para análise dentro do LinkShield.
#
# Essa entidade representa a ligação entre:
#
# Usuário
#    |
#    v
# URL analisada
#
# Responsabilidade:
# - Mapear os dados da URL no banco.
# - Manter a referência do usuário proprietário.
#
# Regras de análise de segurança ficam fora deste modelo,
# na camada de serviços.

class UrlAnalisada(Base):

    # Nome da tabela no banco PostgreSQL.
    __tablename__ = "urls_analisadas"

    # Identificador único da URL analisada.
    #
    # Permite que cada registro seja identificado
    # individualmente no banco de dados.

    id: Mapped[int] = mapped_column (
        primary_key=True,
    )

     # Identifica o usuário responsável pela URL analisada.
    #
    # Cria o relacionamento entre:
    #
    # usuarios.id
    #       |
    #       v
    # urls_analisadas.usuario_id
    #

    usuario_id: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id")
    )

        # Armazena a URL completa enviada pelo usuário.
    #
    # Mantém o valor original para auditoria
    # e análises futuras.

    url: Mapped[str]

     # Armazena o domínio extraído da URL.
    #
    # Será utilizado futuramente pelo motor
    # de análise de segurança.

    dominio: Mapped[str]

    # Registra quando a URL foi cadastrada no sistema.
    #
    # Utilizado para auditoria e rastreamento
    # do histórico de análises.

    criado_em: Mapped[datetime] = mapped_column(
        default=datetime.utcnow
    )

    