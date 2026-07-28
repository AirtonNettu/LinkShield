from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Resultado(Base):
    """Representa o resultado consolidado de uma análise."""

    __tablename__ = "resultados"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    analise_id: Mapped[int] = mapped_column(
        ForeignKey("analises.id")
    )

    classificacao: Mapped[str]

    nivel_risco: Mapped[str]

    descricao: Mapped[str]

    criado_em: Mapped[datetime] = mapped_column(
        default=datetime.utcnow
    )