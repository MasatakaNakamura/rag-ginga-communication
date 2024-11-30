from bs4 import BeautifulSoup

def get_links(file_path):
    """
    ローカルのHTMLファイルを読み込み、リンクを解析する関数。

    Parameters:
        file_path (str): HTMLファイルのパス。

    Returns:
        dict: リンク情報を含む辞書。
    """
    try:
        # ファイルを開いてBeautiful Soupで解析
        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")

        # 全てのリンクを取得
        links = []
        for link in soup.find_all("a"):
            
            href = link.get("href")
            if href is not None and href.endswith(".pdf"):
                text = link.text.strip()
                links.append({"text": text, "url": href})

        return {
            "links": links
        }
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {file_path}")
        return None
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return None