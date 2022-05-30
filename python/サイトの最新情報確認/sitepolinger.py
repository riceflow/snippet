#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' See. I/O 2019年10月号 P100 JUPYTER NOTEBOOK レシピ '''

import codecs, csv, difflib, hashlib, os, sys, requests

CACHEDIR = './cache' # 前回受信データを保存するフォルダ
if not os.path.exists(CACHEDIR):
    os.mkdir(CACHEDIR)

# タイトル<tab>URLの書式のURLリストを読み込む
# with open("urllist.txt", 'r', 'utf-8') as f: #元コード
with codecs.open("urllist.txt", 'r', 'utf-8') as f: #置換コード(codecsを追加)
    tsv = csv.reader(f, delimiter = '\t')
    for row in tsv:
        print(row[0] + 'に接続...')

        # 接続して情報を取得
        url = row[1]
        info = requests.get(url)

        # 本文をバイナリで取得
        content = info.content

        # キャッシュするファイル名
        h = hashlib.sha1(url.encode('utf-8')).hexdigest()
        fullpath = os.path.join(CACHEDIR, h)

        # キャッシュを取得して比較
        oldcontent = b''
        if os.path.exists(fullpath):
            with open(fullpath, 'rb') as r:
                oldcontent = r.read()
        if content != oldcontent:
            print(row[0] + '(' + row[1] + ')は更新されています')
            diff = difflib.unified_diff(
                oldcontent.decode(
                    info.apparent_encoding, 'ignore').splitlines(keepends=True),
                content.decode(
                    info.apparent_encoding, 'ignore').splitlines(keepends=True),
                '旧', '新')
            sys.stdout.writelines(diff)
        else:
            print(row[0] + '(' + row[1] + ')は更新されていません')

        # キャッシュに書き込む
        with open(fullpath, 'wb') as w:
            w.write(content)
