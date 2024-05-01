import subprocess

def createInputList(inputs):
    inputList=[]
    element = ""
    for input in inputs:
        if input == "\n":
            inputList.append(element)
            element = ""
        else:
            element += input
    
    if element != "":
        inputList.append(element+"\n")
        
    return inputList

def main():
    # 入力ファイルを読み込む カレントディレクトリからの相対パスか絶対パスで指定すること。大体はATCODERがカレントディレクトリである。
    with open("ABC345\\test\\A.txt", 'r') as file:
        inputs = file.readlines()
    
    inputList = createInputList(inputs)    
    # テストしたいPythonスクリプトのパス
    script_path = 'ABC345\A.py'
    
    # 各入力に対してスクリプトを実行
    for input in inputList:
        process = subprocess.Popen(['python', script_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # 入力を送信し、出力を取得
        
        output, errors = process.communicate(input.strip())
        # スクリプトの出力を表示
        print("Input:", input.strip())
        print("Output:", output)
        if errors:
            print("Errors:", errors)
            
if __name__ == '__main__':
    main()
