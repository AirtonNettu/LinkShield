from sqlalchemy.orm import Session

from app.models.url_analisada import UrlAnalisada


class UrlRepository:
    """Gerencia operações de persistência das URLs analisadas."""
    def __init__(self, session: Session):
        self.session = session


    def create_url(self, analyzed_url: UrlAnalisada) -> UrlAnalisada:
        """Persiste uma nova URL analisada no banco"""
        self.session.add(analyzed_url)
        self.session.commit()
        self.session.refresh(analyzed_url)
        
        return analyzed_url