from dotenv import load_dotenv
from os import getenv
from langchain_oci.chat_models import ChatOCIGenAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

llm = ChatOCIGenAI(
    model_id=getenv("MODEL_ID"),
    service_endpoint=getenv("SERVICE_ENDPOINT"),
    compartment_id=getenv("COMPARTMENT_ID"),
    model_kwargs={"temperature": 0, "max_tokens": 500},
    auth_file_location="./config"
)

response = llm.invoke([HumanMessage(content="Tell me one fact about earth"), AIMessage(content="The Earth is the third planet from the Sun and is the only astronomical object known to harbor life."), ], temperature=0.7)
print(response)