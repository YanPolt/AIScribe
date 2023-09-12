from fastapi import FastAPI
import httpx
import redis
from api.ai import llm, embeddings
import os
from langchain.prompts import ChatPromptTemplate
from langchain import PromptTemplate, LLMChain
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.chains import RetrievalQA
from langchain.indexes import VectorstoreIndexCreator

app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# REDIS_HOST = os.getenv("REDIS_HOST", "redis")
# REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# Crea un cliente de Redis
# redis_client = redis.StrictRedis(
#    host=REDIS_HOST, port=REDIS_PORT, decode_responses=True
# )
# Instrucciones generales para el prompt
aiscribe_prompt = "A partir de este momento eres AIScribe, un motor de inteligencia artificial que se encarga de ayudar a desarolladores a documentar sus proyectos.\
    Recibirás diferentes tareas que debes llevar a cabo utilizando todos tus conocimientos de programación y evaluación de código, sé tan exhaustivo como sientas que sea necesario para que las ideas sean claras y completas.\
    Recuerda que tu público pueden ser desde otros desarrolladores del mismo proyecto hasta usuarios con habilidades no tan técnicas, por lo que debes mantener un lengaje formal pero sencillo y evitar tecnicismos en la medida de lo posible.\
    Todo lo que describas debe estar en formato markdown, ya que se utilizará para generar la documentación de un proyecto."


@app.get("/")
async def read_root(prompt: str):
    """Recibe un prompt y lo envía a la API de OpenAI para obtener una respuesta"""
    #    cached_result = redis_client.get(prompt)
    #    if cached_result:
    #        return {"response": cached_result, "source": "redis"}
    # Crea un template para el prompt
    template_string = (
        aiscribe_prompt
        + """\n Tarea: Te enviaré un texto con la descripción de un proyecto de tecnología; el cual puede incluir o \
        no los objetivos, los requisitos, snippets de codigo, el alcance, la fase actual, la arquitectura, etc. Quiero que en base a esa \
        descripción, generes una documentación tecnica que incluya la información ya suministrada y la complementes. El texto se encuentra delimitado \
        por comillas triples (```). \
        texto: ```{text}```"""
    )
    promtp_template = ChatPromptTemplate.from_template(template_string)
    prompt = promtp_template.format_messages(text=prompt)
    # Check if the prompt is cached

    result = llm(prompt)  # Use the llm instance from ai.py
    return {"response": result, "source": "openai"}


@app.get("/translate")
async def translate(text: str):
    """Resume y traduce un texto que ingresa por parámetro a un lenguaje apto para un público no técnico"""

    # Crea un template para el prompt
    template_string = (
        aiscribe_prompt
        + """Te enviaré un texto en formato markdown que hace parte de la documentación técnica de un producto digital. \
        Quiero que resumas el texto, que se encuentra delimitado por triple comillas(```), en un estilo que sea fácil de entender para \
        un público no técnico y lo retornes en formato markdown con al menos un titulo (h1). \
        texto: ```{text}```"""
    )
    promtp_template = ChatPromptTemplate.from_template(template_string)
    prompt = promtp_template.format_messages(text=text)

    # Genera la respuesta
    response = llm(prompt)

    return {"response": response}


@app.get("/resume")
async def resume(file_path: str):
    """Resume varios textos que ingresan por parámetro"""
    loader = UnstructuredMarkdownLoader(file_path)
    docs = loader.load()
    db = DocArrayInMemorySearch.from_documents(docs, embeddings)
    retriever = db.as_retriever()
    # Acá la idea no es pasar todos los documentos sino solo las partes que nos interesan para el resumen pero toca evaluar
    # si se va a pasar junto a un prompt los documentos o unicamente el path
    qdocs = "".join([docs[i].page_content for i in range(len(docs))])
    response1 = llm.call_as_llm(
        f"Tarea: Por favor resume en un lenguaje sencillo un texto que agrupa varios archivos \
                                de documentación de un proyecto tecnologico. La respuesta debe encontrarse en formato markdown \
                                y debe contener por lo menos un titulo(h1). El texto se encuentra delimitado por triple comillas(```). \
                                Texto: ```{qdocs}``` "
    )

    qa_stuff = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=retriever, verbose=True
    )
    query = f"Tarea: Por favor resume en un lenguaje sencillo un texto que agrupa varios archivos \
                de documentación de un proyecto tecnologico. La respuesta debe encontrarse en formato markdown \
                y debe contener por lo menos un titulo(h1). El texto se encuentra delimitado por triple comillas(```). \
                Texto: ```{qdocs}``` "
    response2 = qa_stuff.run(query)
    db.delete()
    return {"response1": response1, "response2": response2}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
