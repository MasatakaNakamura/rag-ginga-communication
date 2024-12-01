
def chunk_str(str, chunk_size, orver_lap=0):
    """
    文字列を指定したサイズで分割する関数。

    Parameters:
        str (str): 分割する文字列。
        chunk_size (int): 分割するサイズ。
        orver_lap (int): オーバーラップするサイズ。

    Returns:
        list: 分割した文字列のリスト。
    """
    
    return [str[i:i + chunk_size] for i in range(0, len(str), chunk_size - orver_lap)]
