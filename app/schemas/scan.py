from pydantic import BaseModel

class ScanRequest(BaseModel):
    """Dados necessários para iniciar uma analise de Url"""
    url: str

class ScanResponse(BaseModel):
    """Dados retornados após a analise de Url"""
    id: str
    classification: str
    risk_level: str
    description: str