# JupyTeX
LaTeXで実装したJupyter

## 使い方
* main.tex内でjuptex環境を使い，実行したいpythonのスクリプトを書く．
* 以下のコマンドでタイプセットする
``` bash
uplatex main.tex
pythontex main
uplatex main.tex
dvipdfmx main
```
## インタラクティブモードは実装中
main.texをlatexmkで監視し，以下のコマンドを実行すると対話モードに入ります．
``` bash
uplatex interactive_test.tex
```
そこで，pythonのコードを書くと，main.pdfに反映されます．
ただ，現段階でソースコードは表示されますが，実行結果は表示されません．

## 詳しい実装などについてはブログを見てください
[http://muscle-keisuke.hatenablog.com/entry/2017/12/16/173026](http://muscle-keisuke.hatenablog.com/entry/2017/12/16/173026)
