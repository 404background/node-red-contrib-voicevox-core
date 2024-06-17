# examples

## sample-flow.json

このノードのサンプルフローです。

![sample-flow.png](./sample-flow.jpg)

http in/outノード、play audioノードなどと一緒に使えます。

## multiple-test.json

複数のノードを配置した場合のフローです。

![sample-flow.jpg](./sample-flow.jpg)

## msg-test.json

msgのプロパティで値を渡す場合のフローです。

![msg-test.png](./msg-test.png)

msg.voiceID、msg.voiceFolderで値を渡すことができます。

![msg.png](./msg.png)

## id-list.json

voicevox.htmlに記述されている、話者のIDのリストを出力するフローです。

![id-list.png](./id-list.png)

id_list.pyを実行したときに、id_list.jsonも生成されます。そのJSONファイルの中身を、injectノードのmsg.payloadに貼り付けてください。

![id-list-inject.png](./id-list-inject.png)

出力したファイルはNode-REDを起動しているディレクトリのvoicevox_id_list.textに保存されます。
