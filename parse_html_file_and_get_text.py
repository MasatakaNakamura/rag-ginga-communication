from bs4 import BeautifulSoup

def get_text(file_path):
    """
    ローカルのHTMLファイルを読み込み、テキストを解析する関数。

    Parameters:
        file_path (str): HTMLファイルのパス。

    Returns:
        dict: テキスト情報を含む辞書。
    """
    try:
        # ファイルを開いてBeautiful Soupで解析
        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")

        # ページ内テキストを取得
        text = soup.get_text()
        t_all = []
        for t in text.split("\n"):
            if t.strip() != "":
                t_all.append(t.strip().replace("\u3000", ""))

        return {
            "text": "".join(t_all),
        }
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {file_path}")
        return None
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return None