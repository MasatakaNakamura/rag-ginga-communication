from embedding import embeddings as embedding
import faiss
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv

# chunk_contents.txtの内容を取得する関数
def load_chunk_contents(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        chunk_contents = f.readlines()
    # 各行の末尾の改行文字を削除
    chunk_contents = [content.strip() for content in chunk_contents]
    return chunk_contents

if __name__ == "__main__":

    # 環境変数を読み込む
    load_dotenv()
    
    # FASSに登録されているベクトルを読み込む
    index = faiss.read_index("vectors/faiss.index")
    
    # 質問をベクトル化
    question = "2024年12月の勤務表提出期限と猶予期限は？"
    vector = embedding(question)
    questin_vectors = np.array([vector], dtype=np.float32)
    print("Question is embedding finished.")
    
    # k個の近似ベクトルを検索
    k = 3
    distances, indices = index.search(questin_vectors, k)
    
    print("検索結果:")
    print("距離:", distances)
    print("インデックス:", indices)
    
    chunk = load_chunk_contents("vectors/chunk_contents.txt")
    print("Loaded chunk contents")

    # OpenAIのクライアントを作成
    client = OpenAI()
    prompt = f'''以下の質問に以下の情報をベースに回答してください。
    [ユーザの質問]
    {question}
    
    [情報]
    {chunk[indices[0][0]], chunk[indices[0][1]], chunk[indices[0][2]]}
    '''
    response = client.completions.create(
        model = "gpt-3.5-turbo-instruct",
        prompt = prompt,
        max_tokens = 200
    )
    
    print(response.choices[0].text)
    
