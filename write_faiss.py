import faiss
    
# FAISSに追加したベクトルを保存する関数
def write(index, file_path):
    # ファイルに書き込む
    faiss.write_index(index, file_path)