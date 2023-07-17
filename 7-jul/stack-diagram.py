from diagrams import Diagram
from diagrams.generic.blank import Blank

with Diagram("Architecture Diagram", show=False):
    user = Blank("User")
    
    with Diagram("Next.js App"):
        nextjs = Blank("Application Logic")
        auth = Blank("Clerk Auth")
        user >> nextjs >> auth
    
    with Diagram("Models"):
        replicate = Blank("Replicate (Image Model)")
        openai = Blank("OpenAI (Text Model)")
        nextjs >> replicate
        nextjs >> openai
    
    langchain = Blank("Langchain.js (LLM Orchestration)")
    ai_sdk = Blank("AI SDK (Text Streaming)")
    nextjs >> langchain >> ai_sdk
    
    database = Blank("Pinecone/Supabase pgvector (VectorDB)")
    nextjs >> database
    
    deployment = Blank("Fly (Deployment)")
    nextjs >> deployment
