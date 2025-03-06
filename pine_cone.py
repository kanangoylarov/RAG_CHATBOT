import os
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec


api_key = "pcsk_5Dz2Tk_Kxg582JxMNoNAJKKK6QaZjH6UH7zUwtZ97oCq4akVak78hFDcoYG81KCiC4Fpaq"
pc = Pinecone(api_key=api_key)


index_name = "cocktail-index"


if index_name not in [i["name"] for i in pc.list_indexes()]:
    pc.create_index(
        name=index_name,
        dimension=384, 
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )


index = pc.Index(index_name)


csv_file = "final_cocktails.csv"
df = pd.read_csv(csv_file)


model = SentenceTransformer("all-MiniLM-L6-v2")


texts = df["text"].tolist()
embeddings = model.encode(texts, convert_to_numpy=True)  


vectors = [{"id": str(df.iloc[i]["id"]), "values": embeddings[i].tolist()} for i in range(len(df))]


index.upsert(vectors)


def query_pinecone(query: str):
    """
    Kullanıcıdan gelen sorguyu Pinecone içinde arayıp en alakalı sonuçları döndürür.
    """

    query_embedding = model.encode(query, convert_to_numpy=True).tolist()


    results = index.query(vector=query_embedding, top_k=3, include_metadata=True)


    cocktails = []
    for match in results["matches"]:
        cocktail_id = int(match["id"])
        cocktail_text = df.loc[df["id"] == cocktail_id, "text"].values[0]
        cocktails.append({"id": cocktail_id, "text": cocktail_text, "score": match["score"]})

    return cocktails