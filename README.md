# X(Twitter) Auto Like Tool
## 概要
X上で、任意の検索キーワードを含むツイートに対して自動で「いいね」を送信するpythonスクリプトです。  
スクリプト実行後、自動でログインし、画像認識を用いた方法か、キーボードを用いた方法のどちらかで自動でいいねをしていきます。  
Xサーバーの過負荷にならない範囲内でいいねを行います。  

https://github.com/takahashi-s1/TwitterX-Auto-IINE-Tool/assets/149812365/542a14f5-42d4-47c1-aef8-4230a86097bc

## 背景
pythonを用いて実際にどのようにビジネスにおける課題を解決しているか調べた際、企業によるSNSの広報活動を効率化する目的で、同様の機能を持つツールを有料で販売しているサイトを発見し、自分でも制作できるか興味を持った事がきっかけである。
 
## 機能
- jsonファイルにアカウント情報を保存する。その中の任意のアカウントで自動ログイン
- 任意のキーワードを検索し、自動で「いいね」する。※Xサーバーの過負荷にならないよう、（15分当たり50回のいいね数上限に達しないよう）20秒毎に1回、最大190回いいねする（変更可能）
- 自動でいいねする際、画像認識で判断するか、キーボード操作で行うか選べる（キーボード操作推奨）
  
## 工夫点
- セキュリティ面や複数アカウントでの運用を考慮して、アカウント名、パスワードをjsonファイルで管理するようにした（197行目）
- try/exceptブロックを使用して、エラーが出た際の原因を逐一分かるようにした（46、141、162、179）
- return codeを設定し、関数の処理やエラー適切に回収できるようにした（42、138）
- ユーザーのニーズに合わせて設定を柔軟に変更できるようにした
  - 検索キーワード(211)
  - いいね回数(28)
  - いいね間隔(18,173,186)
  - スクロール回数(27)
  - アカウント数
  - いいね方式（画像認識、キーボードショートカット）(26)
  - プライバシーモード(47)
- modeにより、いいねのハートマーク画像を認識してクリックする方法か、キーボードショートカットによる操作か選択できる（178）

## 処理の流れ
- chromeをシークレットモード（変更可能）で開く
- Xを開く
- ページソースを確認してログインチェックする
- jsonファイルからアカウント情報を取得し、自動でログインする（ページソースを確かめる）
- 任意のキーワード、ハッシュタグでツイートを検索する（デモでは　＃英語学習）
- 画像認識を用いた方法か、キーボード操作を利用した方法で自動で「いいね」する（デモではキーボード操作）
  - この際、いいね回数15分当たり50回の上限に達しないよう、20秒毎に1回いいねする。最大で190回（変更可能）。
- 処理が完了したらchromeを閉じる

## 使い方
- セキュリティ管理の為、accounts.jsonにアカウント名、パスワードを保存する
  - この際、アカウントが複数ある場合は、pythonスクリプト - main関数 - ＃アカウント選択 - `account = data['accounts'][0]` にて、実行したいアカウントがjsonファイルの何番目にあるか記入する（例：jsonファイルの2番目にあれば、`account = data['accounts'][1]`）  
  <img width="629" alt="スクリーンショット 2024-03-27 145949" src="https://github.com/takahashi-s1/TwitterX-Auto-IINE-Tool/assets/149812365/5c7637b7-dedd-41f2-8c01-dba9ea2b25e2">  


- pythonスクリプト - main関数 - ＃いいねしたいツイートの検索式 - `search_text = ''`に検索したいキーワードを入力する（初期値は'英語学習'  

   <img width="345" alt="スクリーンショット 2024-03-27 223820" src="https://github.com/takahashi-s1/TwitterX-Auto-IINE-Tool/assets/149812365/ff326357-7317-4a65-89de-6ed4d0c618bb">

- スクリプトを実行する

## テスト動画
[自動いいね](https://github.com/takahashi-s1/TwitterX-Auto-IINE-Tool/assets/149812365/03099bab-03c9-42ab-a124-3d862c57a325)  



## 留意事項
- 実行環境：windows11 corei5 16GB での動作を確認しています。
- 現在Xでは自動化ルールを設けており、Xサーバーに過負荷を掛けるような過度な自動化を規制しています。(https://help.twitter.com/ja/rules-and-policies/x-automation)  
  いいねにおけるアクション上限に関しては（手動であっても）15分につき50回、1日に1000回の基準があると言われております（各自でご判断ください）。当スクリプトではこの上限を元に過負荷を掛けない範囲で初期値を設定しています。しかし、いいねの自動化はアカウントの利用停止、凍結、BANの危険性がありますので、利用する際は各自の判断で行ってください。

## 参照  
- 退屈なことはpythonにやらせよう web  
https://automatetheboringstuff.com/
- subprocess  
https://jp-seemore.com/iot/python/10727/#toc2  
https://office54.net/python/python-subprocess-popen  
https://docs.python.org/ja/3/library/subprocess.html  
- pyautoマウス操作  
https://pyautogui.readthedocs.io/en/latest/mouse.html#mouse-clicks
- jsonファイル  
https://and-engineer.com/articles/YUrUYBAAACUA2zGd
- hotkey  
https://pyautogui.readthedocs.io/en/latest/keyboard.html#the-hotkey-function
- 例外処理  
  https://zenn.dev/tigrebiz/articles/python-try-exception
- pyautogui  
  http://kakedashi-xx.com:25214/index.php/2022/10/14/post-6886/  
  https://qiita.com/curry__30/items/95789faeb8715856ae9e  
  https://sasuwo.org/auto_good_for_twitter/  

