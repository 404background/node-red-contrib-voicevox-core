# node-red-contrib-voicevox-core

[voicevox_core](https://github.com/VOICEVOX/voicevox_core)を利用したNode-REDのノードです。  
文字列を受け取り、音声ファイルを出力します。  

▼voicevox_coreはこちら  
<https://github.com/VOICEVOX/voicevox_core>  

▼VOICEVOXはこちら  
<https://voicevox.hiroshiba.jp/>  

> [!CAUTION]
> **現状ではWindowsにしか対応していません。**  
> また**Pythonの環境が必要**で、パッケージがインストールされます。  
> 仮想環境にインストールできるようにする予定です。  
> >インストールされるもの：requests, voicevox_core  

## 動作確認環境

- Windows 10
- Python 3.8.3
- Node.js v20.10.0
- npm 9.1.3

voicevox_coreは0.15.0がインストールされます。  

## Node-RED関連

### ファイル構成

- .js: ノードの機能
- .html: エディタでの表示
- package.json: インストール時に使用、ノードのパスを指定

.jsの中のchild_processで、Pythonのプログラムを実行しています。  

### ローカルでの実行

▼インストールする場合  
```npm install ＜フォルダのパス＞```  
▼アンインストールする場合  
```npm uninstall ＜パッケージ名＞```  

## Python関連

### ファイル構成

- setup.py: 環境構築
- voicevox.py: 音声ファイルを出力（第一引数：文字列、第二引数：話者のID）
- id_list.py: 話者のリストを表示

話者のIDはデフォルトでは2です。  
voiceフォルダに音声ファイルが保存されます。  

## 検討事項

- 話者の指定
  - 現状はidを指定できます。
  - プルダウンで名前や感情を表示したいところです。
- ファイルパスの指定
  - npmでインストールされたvoiceフォルダに入るので、場所が分かりにくいです。
  - 現状ではmsg.payloadに音声ファイルの絶対パスを返すようにしています。
- Pythonプログラム実行中の表示
  - 音声ファイルを出力するのに少し時間がかかります。
  - 出力中にノードのステータスを表示して、分かりやすくしようと思っています。
- 何を出力するか
  - read fileノードで音声ファイルを開いてバイナリバッファで送ることもできますが、このノードでバイナリバッファを送るほうが使いやすいかも？
  - バイナリバッファで送るとファイルに保存しなくてもよくなりますが、出力に時間がかかります。
  - 選択できるようにしようかなと思っています。
- Pythonの仮想環境へのインストール
  - 仮想環境を作成して、そのpipにライブラリをインストールして実行するとエラーが出ます。
  - _rust.pydのファイル参照先が違うのかも？
  - コアライブラリのビルドを試そうと思っています。

## その他情報

▼Node-RED User Group Japan 「ノードの開発」  
<https://nodered.jp/docs/creating-nodes/>  
▼PythonでVOICEVOX COREを使ってみる（音声合成）  
<https://404background.com/program/voicevox-core/>  
▼Node-REDとVOICEVOX COREで音声合成（Python）  
<https://404background.com/program/node-red-voicevox/>  
