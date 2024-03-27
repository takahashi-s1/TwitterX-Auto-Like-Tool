# TwitterX Auto IINE Tool
## 概要
X(twitter)の有料APIを使用せず、任意の検索キーワードを含むツイートに対して自動で「いいね」を送信するpythonスクリプトです。  
スクリプト実行後、自動でログインし、画像認識を用いた方法か、キーボードを用いた方法のどちらかで自動でいいねをしていきます。  
Xサーバーの過負荷にならないようルールの範囲内でXのアカウント運用を効率化するスクリプトです。

## 作成経緯
このプロジェクトを作成した理由は3つあります。

　1つ目は、私自身が、プログラミングスキルの向上を目的としたプロジェクトだけでなく、実在する世の中のニーズに応えるようなツールを作成したいと思ったからです。  
　プログラミングの学習を進める中で、ただ本やwebサイトに沿ったプロジェクトをこなすだけでなく、何か実社会、特にビジネス方面で必要とされる物、もしくはビジネスをより効率化させるツールを自身で作成したいと考えました。特に、昨今のビジネスや副業において、SNSを利用して集客や会社の認知度向上を図っている方々が増えていると感じ、それらの作業をより効率化できるようなツールとして自動いいねスクリプトを制作しました。

　2つ目は、実際に私自身がツイッターのアカウントを運用してみて、フォロワー数の増加（SNSでの集客や認知度拡大）を図るためには、他人のツイートに対して積極的に「いいね」する事が有効だと分かったからです。  
　企業や個人が、SNSを通して集客、認知度向上を図るためには、多くの人々に自身のツイートを見てもらい、インプレッション数を増やす必要があります。そのためには、まずはフォロワー数を増やす事が重要です。Xのアルゴリズムの仕組みにより、ある程度地盤が整った状態の方が、ツイートがおすすめに表示される事が多くなり、より多くの層にリーチさせる事ができるからです。

　実際に私自身でXのアカウントを運用してみて、アカウントの発信内容を工夫したり、他アカウントをフォローしたりする施策よりも、自身のアカウントの運営方針に合致した内容のツイートに対して積極的に「いいね」をした施策の方がフォロワーの増加幅が大きかったことが分かりました。今回は実験的にアカウント運用を行いましたが、実際にビジネスでSNSを活用されているアカウントにおいても、自ら「いいね」する事で認知度拡大を図っている方々は多いのではないでしょうか。  
　例えば、プログラミングスクールを運営していて、エンジニアに向けて情報発信している方は、#プログラミング学習　や　#駆け出しエンジニア　等のキーワードで検索し、当キーワードが含まれたツイートに「いいね」をする事で新たな層への認知を拡大させる事ができます。このような場合に、いいねという１つの業務を自動化するツールは有用です。

　3つ目は、Twitter APIの有料化によって、これまでの自動いいねツールが全て利用不可になってしまったからです。  
　長らく無料で利用可能だったAPIが有料化した事で、不便を感じている方々が少なからずいると思います。ルールや常識の範囲内でこのスクリプトを活用する事で、ビジネスでSNSを活用する方々の日々の業務がより効率化できると考えました。  
 
 上記３つの理由により今回X自動いいねスクリプトを製作しました。
## 機能
- 自動ログイン
- 任意のキーワードを検索し、自動で「いいね」する（※Xサーバーの過負荷にならないよう、（いいね回数15分当たり50回の上限に達しないよう）20秒毎に1回、最大190回いいねする（変更可能））
- いいねする際、mode = 0の場合は画像認識モードで、mode = 1の場合はキーボード操作モードで行う（キーボード操作推奨）
## 処理
- chromeをシークレットモードで開く
- Xを開く
- jsonファイルからアカウント情報を取得し、自動でログインする（ページソースを確かめてログインできているか確認する）
- 任意のキーワード、ハッシュタグでツイートを検索する（デモでは　＃プログラミング学習）
- 画像認識を用いた方法か、キーボード操作を利用した方法で自動で「いいね」する（キーボード操作推奨）
  - この際、いいね回数15分当たり50回の上限に達しないよう、20秒毎に1回いいねする。最大で190回（変更可能）。
- 終了したらchromeを閉じる

## デモ
[自動いいね](https://github.com/takahashi-s1/TwitterX-Auto-IINE-Tool/assets/149812365/b546d2c0-d35b-4dc0-9538-da1ec69df965)

## 使い方
- セキュリティ管理の為、jsonファイルにアカウント名、パスワードを保存する
<img width="242" alt="スクリーンショット 2024-03-27 154218" src="https://github.com/takahashi-s1/TwitterX-Auto-IINE-Tool/assets/149812365/a784a567-df96-4c04-ad47-2ad8b2d71a37">

  - この際、アカウントが複数ある場合は、pythonスクリプト-main関数(198)-＃アカウント選択-`account = data['accounts'][0]` にて、実行したいアカウントがjsonファイルの何番目にあるか記入する（例：jsonファイルの2番目にあれば、`account = data['accounts'][1]`）
<img width="629" alt="スクリーンショット 2024-03-27 145949" src="https://github.com/takahashi-s1/TwitterX-Auto-IINE-Tool/assets/149812365/5c7637b7-dedd-41f2-8c01-dba9ea2b25e2">  


- pythonスクリプト-main関数(198)-＃いいねしたいツイートの検索式- `search_text = ''`に検索したいキーワードを入力する（初期値は'プログラミング学習'）
<img width="358" alt="スクリーンショット 2024-03-27 145953" src="https://github.com/takahashi-s1/TwitterX-Auto-IINE-Tool/assets/149812365/55c159f2-4233-4de6-9952-57c49e87c5cf">  
    
- スクリプトを実行する

## 留意事項
- 実行環境：windows11 corei5 16GB での動作を確認しています。
- 現在Xでは自動化ルールを設けており過度な自動化を規制しています。(https://help.twitter.com/ja/rules-and-policies/x-automation)  
  また、アクション上限が設けられており、15分につき50回、1日に1000回いいねをすると凍結されると言われています。（各自で調べてご判断ください）そのため、当スクリプトのいいね最大数は190回になっています。
- Xサーバーに過負荷を掛けるような過度ないいねの自動化を実施した場合、アカウント凍結やBANされる危険性があります。利用する際は全て自己責任でご判断ください。

## 参照  
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
