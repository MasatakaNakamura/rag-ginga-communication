# RAG Ginga Communication

## 概要
RAG Ginga Communicationは、RAGを使用して銀河通信内の情報を取得するプロジェクトです。

実行にはOPENAIのAPIキーが必要です。

APIキーは、プロジェクト内に.envファイルを作成し、

 * OPENAI_API_KEY=[your api key]

の形で記述してください。

## インストール
以下の手順に従ってインストールしてください。

```bash
git clone https://github.com/masae/rag-ginga-communication.git
cd rag-ginga-communication
pip install -r requirements.txt
```

## 使い方
以下のコマンドでプロジェクトを起動できます。

```bash
# Embedding後のVectorデータをFAISSに登録する
python register_main.py

# 質問をChatGPTに投げて応答を表示する
python chat_main.py
```
