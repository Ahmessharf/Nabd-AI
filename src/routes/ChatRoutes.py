import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from config import Config
from src.stores.vectordb.providers.VectorDBProviderFactory import VectorDBProviderFactory
from src.controllers.ChatController import ChatController

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/chat", tags=["Medical Chat"])

# We added session_id here!
class QuestionRequest(BaseModel):
    session_id: str = Field(default="user_123", description="Unique ID for the user's chat session.")
    query: str = Field(..., min_length=3, description="The medical question asked by the user.")

vector_factory = VectorDBProviderFactory(config=Config)
vector_db_provider = vector_factory.create(Config.CURRENT_VECTOR_DB)
chat_ctrl = ChatController()

@router.post("/ask")
def ask_medical_question(request: QuestionRequest):
    logger.info(f"Received question from session [{request.session_id}]: '{request.query}'")
    try:
        retrieved_chunks = vector_db_provider.search_by_text(
            collection_name="default", 
            query=request.query, 
            limit=3
        )
        
        # Pass the session_id to the controller!
        final_answer = chat_ctrl.generate_answer(
            query=request.query, 
            retrieved_chunks=retrieved_chunks,
            session_id=request.session_id
        )
        
        return {
            "session_id": request.session_id,
            "question": request.query,
            "answer": final_answer,
            "sources_retrieved": len(retrieved_chunks)
        }
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    
    