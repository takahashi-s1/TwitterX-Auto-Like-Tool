# TwitterX Auto IINE Tool
## 概要
任意の検索キーワードを含むツイートに対して自動で「いいね」を送信するpythonスクリプトです。  
スクリプト実行後、自動でログインし、画像認識を用いた方法か、キーボードを用いた方法のどちらかで自動でいいねをしていきます。  
Xサーバーの過負荷にならないよう常識の範囲内でXのアカウント運用を効率化します。

## 機能
- jsonファイルに保存したアカウント情報を取得し、その中の任意のアカウントで自動ログイン
- 任意のキーワードを検索し、自動で「いいね」する。※Xサーバーの過負荷にならないよう、（いいね回数15分当たり50回の上限に達しないよう）20秒毎に1回、最大190回いいねする（変更可能）。
- 自動でいいねする際、画像認識で判断するか、キーボード操作で行うか選べる（キーボード操作推奨）
## 処理
- chromeをシークレットモード（変更可能）で開く
- Xを開く
- ページソースを確認してログインチェックする
- jsonファイルからアカウント情報を取得し、自動でログインする（ページソースを確かめる）
- 任意のキーワード、ハッシュタグでツイートを検索する（デモでは　＃英語学習）
- 画像認識を用いた方法か、キーボード操作を利用した方法で自動で「いいね」する（デモではキーボード操作）
  - この際、いいね回数15分当たり50回の上限に達しないよう、20秒毎に1回いいねする。最大で190回（変更可能）。
- 終了したらchromeを閉じる

## 使い方
- セキュリティ管理の為、accounts.jsonにアカウント名、パスワードを保存する
  - この際、アカウントが複数ある場合は、main関数内の、＃アカウント選択-`account = data['accounts'][0]` にて、実行したいアカウントがjsonファイルの何番目にあるか記入する（例：jsonファイルの2番目にあれば、`account = data['accounts'][1]`）
　<img width="629" alt="スクリーンショット 2024-03-27 145949" src="https://github.com/takahashi-s1/TwitterX-Auto-IINE-Tool/assets/149812365/5c7637b7-dedd-41f2-8c01-dba9ea2b25e2">  


- main関数内の、＃いいねしたいツイートの検索式- `search_text = ''`に検索したいキーワードを入力する（初期値は'英語学習'）
  <img width="345" alt="スクリーンショット 2024-03-27 223820" src="https://github.com/takahashi-s1/TwitterX-Auto-IINE-Tool/assets/149812365/ff326357-7317-4a65-89de-6ed4d0c618bb">

- スクリプトを実行する

## デモ
[自動いいね](https://github.com/takahashi-s1/TwitterX-Auto-IINE-Tool/assets/149812365/03099bab-03c9-42ab-a124-3d862c57a325)  

## 制作に至った背景
　私がこのプロジェクトを作成した理由は3つあります。
  
  
　1つ目は、私自身が、プログラミングスキルの向上を目的としたプロジェクトだけでなく、実在する世の中のニーズに応えるようなツールを作成したいと思ったからです。  
　プログラミングの学習を進める中で、ただ本やwebサイトに沿ったプロジェクトをこなすだけでなく、実社会、特にビジネス方面で必要とされる物、もしくはビジネスをより効率化させる物を自身で作成したいと考えました。特に、昨今のビジネスや副業において、SNSを利用して集客や会社の認知度向上を図っている方々が増えていると感じ、それらの業務をより効率化するツールを制作する事を目標に定めました。

　2つ目は、実際に私自身がXのアカウントを運用してみて、インプレッション数の増加（認知度拡大）を図る上で「いいね作業」が最も有効である一方で、多大な労力と時間を要する業務だと実感したからです。  
　まず私は、企業や個人がSNSを通してどのように集客・認知度向上を図っているか知るため、実際に0からXアカウントの運用を始めました。その結果、インプレッション数を大幅に増加させるには、フォロワー数という地盤を整え、Xのアルゴリズムに優遇される事が重要だと分かりました。また、そのフォロワー数を増やす為には、発信内容の工夫や、他アカウントのフォローよりも、自身のアカウントの運営方針に合致した内容のツイートに、積極的に「いいね」をして回る事が最も有効だと分かりました。しかし、これらの「いいね回り」は非常に地道で時間のかかる作業で、私と同じようにこれらの業務を効率化したいと思う方々がいるのではないかと思い、自動いいね機能の制作に至りました。  
  
  
 <img width="636" alt="スクリーンショット 2024-03-27 160542" src="https://github.com/takahashi-s1/TwitterX-Auto-IINE-Tool/assets/149812365/cb6e8e1e-b93e-46f9-b0c0-239e6504d9e8">  

[引用：X API 料金表](https://developer.twitter.com/en/products/twitter-api)  
 
 　3つ目は、Twitter APIの有料化によって、これまでの自動いいねツールが全て利用不可になってしまったからです。
　twitterが買収されて以降、長らく無料だったtwitter APIが有料化されました。basicプランで100ドル、proプランで5000ドルという料金に躊躇し、現在のアカウント運用に不便を感じている方々が多くいると考えました。このようなニーズを満たし、ビジネスでSNSを活用する方々に向けて、ルールや常識の範囲内でより業務を効率化する「いいね自動スクリプト」制作を決意しました。
 
 上記３つの理由により今回X自動いいねスクリプトを制作しました。
 
## 頑張った点
- 当初はアカウントのユーザー名とパスワードを直接pythonコード内に記入する形をとっていたが、セキュリティ面や複数アカウントでの運用を考慮してjsonファイルで管理するようにした（197行目）。
- クラスや関数を定義して処理を抽象化した事で可読性や再利用性を高めた（12行目）。
- try/exceptブロックを使用して、エラーが出た際にその箇所や原因が分かるようにした（46、141、162、179行目）。
- return codeを設定し、関数の処理やエラー適切に回収できるようにした。
- 当初はpyautoGUIのlocateonscreenでいいねのハートマークを認識してクリックする形をとっていたが、処理の正確性を考慮してキーボードショートカットによる操作を追加した（178行目）。また、前のコードを消さずにmodeで操作方法を変更できるようにした（26行目）。
- ユーザーのニーズに合わせて設定を柔軟に変更できるようにした。
  - 検索キーワード
  - いいね回数
  - いいね間隔
  - スクロール回数
  - アカウント数
  - いいね方式（画像認識、キーボードショートカット）
  - プライバシーモード




## 留意事項
- 実行環境：windows11 corei5 16GB での動作を確認しています。
- 現在Xでは自動化ルールを設けており、Xサーバーに過負荷を掛けるような過度な自動化を規制しています。(https://help.twitter.com/ja/rules-and-policies/x-automation)  
  いいねにおけるアクション上限に関しては（手動であっても）15分につき50回、1日に1000回の基準があると言われております（各自でご判断ください）。当スクリプトではこの上限を元に過負荷を掛けない範囲で初期値を設定しています。しかし、いいねの自動化はアカウントの利用停止、凍結、BANの危険性がありますので、もし利用する際は自己責任で各自の判断で行ってください。

## 参照  
- 退屈なことはpythonにやらせよう web版  
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
