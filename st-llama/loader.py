from typing import List

from langchain.document_loaders import TextLoader
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter

from langchain.embeddings import LlamaCppEmbeddings


def get_embeddings(model_path: str, text_path: str, n_gpu_layers: int = None):
    """
    create embeddings for documents and query using LlamaCppEmbeddings
    # params using google style docstring
    Args:
        model_path (str): path to llama model
        text_path (str): path to text file
        query (str): query string
        n_gpu_layers (int): number of layers offloaded to gpu

    Returns:
        texts (List[Document]): list of documents
        embedded_texts (List[List[float]]): list of embedded documents
    """
    # load doc
    loader = TextLoader(text_path)
    doc = loader.load()

    # split doc
    splitter = CharacterTextSplitter(chunk_size=10, chunk_overlap=0)
    texts = splitter.split_documents(doc)

    embeddings_model = LlamaCppEmbeddings(model_path=model_path, n_gpu_layers=n_gpu_layers)

    return texts, embeddings_model
