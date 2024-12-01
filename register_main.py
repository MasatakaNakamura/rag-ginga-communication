from parse_html_file_and_get_text import get_text
from parse_html_file_and_get_links import get_links
from chunk_string import chunk_str
from embedding import embeddings as embedding
import faiss
from register_faiss import register
from write_faiss import write

if __name__ == "__main__":
    # 読み込みたいHTMLファイルのパス
    file_path = "html/お知らせ.html"

    # 指定したHTMLファイルのテキストを取得
    result_text = get_text(file_path)
    
    # 指定したHTMLファイルのリンクを取得
    result_links = get_links(file_path)

    # テキストを500文字ごとに分割
    chunk = chunk_str(
        result_text['text'],
        500,
        50
    )
    print("Chunk is finished.")
    
    # 分割したテキストをembedding.pyのembeddings関数に渡す
    vectors = [ embedding(chunkText) for chunkText in chunk]
    print("Embedding is finished.")

    # 元のChunkの内容を保存するリスト
    chunk_contents = chunk.copy()

    # データの次元数（ベクトルの要素数）
    dimension = len(vectors[0])
    print("Dimension is finished.", dimension)
    
    # L2距離（ユークリッド距離）でのインデックスを作成
    index = faiss.IndexFlatL2(dimension)
    print("Index is finished.", index)

    # このインデックスを関数に渡して登録
    register(index, vectors)
    print("Register is finished.")
    
    # 登録したベクトルをファイルに保存
    write(index, "vectors/faiss.index")
    print("Write is finished.")
    
    # 元のChunkの内容をファイルに保存
    with open("vectors/chunk_contents.txt", "w", encoding="utf-8") as f:
        for content in chunk_contents:
            f.write(content + "\n")
    print("Chunk contents are saved.")

    print("Registration is completed.")