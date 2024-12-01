from openai import OpenAI
import numpy as np
import os
from dotenv import load_dotenv

def embeddings(texts):
    """
    文章のベクトル化を行う関数。

    Parameters:
        texts (list): ベクトル化する文章のリスト。

    Returns:
        list: ベクトル化された文章のリスト。
    """
    
    # 環境変数を読み込む
    load_dotenv()
    
    # OpenAIのクライアントを作成
    client = OpenAI()
    
    # OpenAIのモデルを使って文章のベクトル化を行う
    response = client.embeddings.create(
        input=texts,
        model="text-embedding-3-small"
    )
    
    # ベクトル化された文章のリストを返す
    return response.data[0].embedding
