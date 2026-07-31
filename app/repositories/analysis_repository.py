from sqlalchemy.orm import Session

from app.models.analise import Analise

class AnalysisRepository:
    """Gerencia operações de persistência das análises."""
    def __init__(self, session: Session):
        self.session = session
        
    def create_analysis(self, analysis: Analise) -> Analise:
        """Persiste uma nova análise no banco"""

        self.session.add(analysis)
        self.session.commit()
        self.session.refresh(analysis)
        return analysis