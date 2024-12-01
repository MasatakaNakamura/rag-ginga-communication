from parse_html_file_and_get_text import get_text
from parse_html_file_and_get_links import get_links
from chunk_string import chunk_str

if __name__ == "__main__":
    # 読み込みたいHTMLファイルのパス
    file_path = "html/お知らせ.html"

    # 指定したHTMLファイルのテキストを取得
    result_text = get_text(file_path)
    
    # 指定したHTMLファイルのリンクを取得
    result_links = get_links(file_path)

    if result_text:
        print(f"{result_text['text']}")
        print(len(result_text['text']))

    if result_links:
        for link in result_links['links']:
            print(f"- リンクファイル: {link['text']}, URL: {link['url']}")
            
    # テキストを500文字ごとに分割
    chunk = chunk_str(
        result_text['text'],
        500,
        50
    )
