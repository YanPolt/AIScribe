import os
import openai
import markdown
from langchain.chat_models import AzureChatOpenAI, ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings


#Se remueven las credenciales de Azure por seguridad

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_BASE"] = ""
os.environ["OPENAI_API_KEY"] = ""
os.environ["OPENAI_API_VERSION"] = "2023-05-15"

llm = AzureChatOpenAI(deployment_name="Test1", model_name="gpt-35-turbo")
embeddings = OpenAIEmbeddings(deployment="Embedding")