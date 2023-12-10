import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

import dotenv

dotenv.load_dotenv(dotenv.find_dotenv("../.env"))

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

docs = "None"  # TODO: here goes the text

embeddings = OpenAIEmbeddings()
chroma = Chroma.from_document(embeddings, docs)
chroma.save("chroma")
