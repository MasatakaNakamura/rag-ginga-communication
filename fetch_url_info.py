import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup


def login_and_fetch_content(login_url, data_url, login_payload):
    """
    ログインして次のページに遷移し、情報を取得する関数。

    Parameters:
        login_url (str): ログインページのURL。
        data_url (str): 遷移後にデータを取得するURL。
        login_payload (dict): ログイン時に送信するデータ（例: ユーザー名とパスワード）。

    Returns:
        dict: ページのタイトルとリンク情報を含む辞書。
    """
    with requests.Session() as session:
        
        # ログインページにアクセス
        try:
            response = session.get(login_url)
            
            # basic認証
            response = session.post(data_url, data=login_payload)
            
            # ログインが成功したか確認
            if response.status_code == 200:
                print("ログイン成功")
                
                # 次のページにアクセス
                response = session.post(login_url, data=login_payload)
                
                # ページのタイトルとリンク情報を取得
                soup = BeautifulSoup(response.content, "html.parser")
                title = soup.title.string
                links = [{"text": link.text, "url": link.get("href")} for link in soup.find_all("a")]
                
                return {"title": title, "links": links}
            
            else:
                print(f"ログインに失敗しました。ステータスコード: {response.status_code}")
        except Exception as e:
            print(f"エラーが発生しました: {e}")
            return None

# 使用例
if __name__ == "__main__":
    # ログインページのURL
    login_url = "https://system.ginga.info/ohana/"

    # 遷移後のページのURL
    top_url = "https://system.ginga.info/ohana/information.xhtml"

    load_dotenv()
    userId = os.getenv("OHANA_ID")
    password = os.getenv("OHANA_PASS")
    
    # ログインに必要なデータ（ユーザー名やパスワードなど）
    login_payload = {
        "login-form:loginId": userId,
        "login-form:password": password,
        "login-form:j_idt23": "ログイン"
    }

    result = login_and_fetch_content(login_url, top_url, login_payload)

    if result:
        print(f"タイトル: {result['title']}\n")
        print("リンク一覧:")
        for link in result['links']:
            print(f"- テキスト: {link['text']}, URL: {link['url']}")
