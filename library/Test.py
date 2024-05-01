import subprocess

# 入力ファイルを読み込む カレントディレクトリからの相対パスか絶対パスで指定すること。大体はATCODERがカレントディレクトリである。
with open("ABC345\\test\\input.txt", 'r') as file:
    inputs = file.readlines()

# テストしたいPythonスクリプトのパス
script_path = 'ABC345\A.py'

# 各入力に対してスクリプトを実行
for input in inputs:
    process = subprocess.Popen(['python', script_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # 入力を送信し、出力を取得
    output, errors = process.communicate(input.strip())
    # スクリプトの出力を表示
    print("Input:", input.strip())
    print("Output:", output)
    if errors:
        print("Errors:", errors)
