from .VectorDBEnums import VectorDBEnums
from src.stores.vectordb.providers.FaissDBProvider import FaissDBProvider

class VectorDBProviderFactory:
    def __init__(self, config):
        # Inject the centralized configuration into the factory
        self.config = config

    def create(self, provider: str):
        # Dynamically route to the FAISS provider implementation
        if provider == VectorDBEnums.FAISS.value:
            return FaissDBProvider(config=self.config)

        # Return None if an unsupported database engine is requested
        return None
    
    