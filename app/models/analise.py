from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base

# Representa uma análise de segurança realizada pelo LinkShield.
#
# Responsável apenas pelo mapeamento ORM da entidade.
#
# Conecta:
# API → Services → Repository → ORM → Banco
#
# Uma análise pertence a uma URL analisada.
#
# Regras de análise de segurança, classificação de risco
# e processamento ficam fora deste modelo.

class Analise(Base):
    __tablename__ = "analises"

    # Identificador único da análise realizada.
    #
    # Permite diferenciar cada execução de análise
    # armazenada no sistema.

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

     # Identifica a URL analisada que originou esta execução.
    #
    # Relacionamento:
    #
    # urls_analisadas.id
    #          |
    #          v
    # analises.url_id
    #
    url_id: Mapped[int] = mapped_column(
        ForeignKey("urls_analisadas.id")
    )

      # Estado atual do processamento da análise.
    #
    # Representa o ciclo de execução:
    #
    # pendente
    # processando
    # concluida
    # falhou
    #

    status: Mapped[str]

     # Define qual tipo de análise foi executada.
    #
    # Permite identificar o módulo de segurança
    # responsável pela análise.

    tipo_analise: Mapped[str]

    # Registra o momento em que a análise foi iniciada.
    #
    # Utilizado para controle de processamento,
    # métricas e auditoria.

    iniciada_em: Mapped[datetime] = mapped_column(
        default=datetime.utcnow
    )

    # Registra o momento em que a análise foi concluída.
    #
    # Pode permanecer vazio enquanto a análise
    # ainda estiver em processamento.

    finalizada_em: Mapped[datetime | None] = mapped_column(
        nullable=True
    )
