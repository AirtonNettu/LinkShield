from app.repositories.analysis_repository import AnalysisRepository
from app.repositories.url_repository import UrlRepository

from app.models.analise import Analise
from app.models.url_analisada import UrlAnalisada

class AnalysisService:
    """Coorderna o fluxo de análise de segurança."""
    def __init__(
            self,
            analysis_repository: AnalysisRepository, 
            url_repository: UrlRepository
        ):
        
        self.analysis_repository = analysis_repository
        self.url_repository = url_repository

    def scan_url(self, url: str) -> str:
        """Inicia o fluxo de análise de uma URL."""
        url_analisada = UrlAnalisada(
            usuario_id=1,
            url=url,
            dominio=url
        )
        self.url_repository.create_url(url_analisada)

        analysis = Analise(
            url_id=url_analisada.id,
            status="pendente",
            tipo_analise="url_scan"
        )

        self.analysis_repository.create_analysis(analysis)

        return url