import zipfile

# ZIPファイルを読み込み
zip_file = zipfile.ZipFile('./logs_1.zip')

# ZIPの中身を取得
file_list = zip_file.filelist

# リストから取り出す
for file in file_list:
    # ファイル名を取得
    filename = file.filename
    # ファイルサイズを取得
    filesize = file.file_size
    # ファイルの中身を取得
    file_content = zip_file.read(filename)
    # ファイルの先頭から10バイトを取得
    file_head = file_content[:10]
    # ファイルの先頭を表示
    print(filename, filesize, file_head)
    print('------------------------------')

# ZIPファイルをクローズ
zip_file.close()
