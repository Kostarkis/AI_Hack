import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

os.environ["OPENAI_API_KEY"] = "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"

docs = None  # TODO: here goes the text

embeddings = OpenAIEmbeddings()
chroma = Chroma.from_embeddings(embeddings, docs)
chroma.save("chroma")
