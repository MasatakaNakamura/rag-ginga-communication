import faiss
import numpy as np

# 受け取ったベクトルを登録する関数
def register(index, vectors):
    
    # ベクトルを NumPy 配列に変換
    vector_list = np.array(vectors, dtype=np.float32)
    
    # ベクトルを登録
    index.add(vector_list)
    return index