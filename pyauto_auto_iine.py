import sys
import os
path = os.path.join(os.path.dirname(__file__), '../')
sys.path.append(path)
import pyautogui as pag
import time
import subprocess
import pyperclip
import urllib.parse
import json

class TwitterGui:
  #　共通定数
  wait_time = 3
  chrome_path = r'chrome.exe'
  
  # ログイン変数
  twitter_login_url = 'https://twitter.com/i/flow/login'
  twitter_url = 'https://twitter.com/'
  twitter_username = ''
  twitter_password = ''
  is_login_check_text = '"screen_name":"'
  
  #いいね変数
  twitter_search_url = 'https://twitter.com/search?q='
  twitter_like_button = 'twitter_auto_like/data/like_button.jpg'
  
  scroll_num = 5 #スクロール回数
  mode = 1 #0の時は画像認識モード、1の時はキーボード操作モード
  next_post_keyboard_com = 'j'
  do_like_keyboard_com = 'l'
  
  #コンストラクタ
  def __init__(self, wait_time, twitter_username, twitter_password):
    self.wait_time = wait_time
    self.twitter_username = twitter_username
    self.twitter_password = twitter_password
    self.twitter_url += self.twitter_username
    
  # ログイン処理
  def login_twitter(self):
    return_code = 0
    is_opened_chrome = False
    
    # Chrome起動
    try:
      chrome_path = self.chrome_path
      subprocess.Popen(['start', self.chrome_path, '--incognito'], shell=True)      
      time.sleep(self.wait_time)
      is_opened_chrome = True
      
      ## ログインチェック
      ## twitterを開く
      pag.hotkey('ctrl', "l")
      time.sleep(self.wait_time)

      pag.hotkey('ctrl', "a")
      time.sleep(self.wait_time)

      pyperclip.copy(self.twitter_url)
      pag.hotkey("ctrl", "v")
      time.sleep(self.wait_time)

      pag.press("enter")
      time.sleep(self.wait_time)  
      
      # ページのソースを取得
      pag.hotkey("ctrl", "u")
      time.sleep(self.wait_time)
      pag.hotkey("ctrl", "a")
      time.sleep(self.wait_time)
      pag.hotkey("ctrl", "c")
      time.sleep(self.wait_time)
      html_src_text = pyperclip.paste()
      time.sleep(self.wait_time)            

        # ログインチェック
      if self.is_login_check_text not in html_src_text:
        ## ログイン画面を表示
        pag.hotkey('ctrl', "l")
        time.sleep(self.wait_time)

        pyperclip.copy(self.twitter_login_url)
        pag.hotkey("ctrl", "v")
        time.sleep(self.wait_time)
        pag.press("enter")
        time.sleep(self.wait_time)
          
          ## アカウント名の入力欄に移動
        for i in range(0,3):
            pag.hotkey("tab")
            time.sleep(self.wait_time)

        ## アカウント名を入力
        pyperclip.copy(self.twitter_username)
        pag.hotkey("ctrl", "v")
        time.sleep(self.wait_time)
        pag.press("enter")
        time.sleep(self.wait_time)

        ## パスワードを入力
        pag.hotkey("ctrl", "a")
        time.sleep(self.wait_time)
        pyperclip.copy(self.twitter_password)
        pag.hotkey("ctrl", "v")
        time.sleep(self.wait_time)
        pag.press("enter")
        time.sleep(self.wait_time)

        ## プロフィール画面へ移動
        pag.hotkey('ctrl', "l")
        time.sleep(self.wait_time)

        pag.hotkey('ctrl', "a")
        time.sleep(self.wait_time)

        pyperclip.copy(self.twitter_url)
        pag.hotkey("ctrl", "v")
        time.sleep(self.wait_time)

        pag.press("enter")
        time.sleep(self.wait_time)
      else:
        pag.hotkey('ctrl', "w")
    except Exception as e:
      print(e)
      return_code = 1
      # Chromeを起動した後のエラーの場合は閉じる
      if is_opened_chrome == True:
        pag.FAILSAFE = False
        pag.moveTo(0,0)
        pag.hotkey('ctrl', 'shift', "w")
    return return_code        
  
  # locateonscreenで画像認識
  def wait_detecting_image(self, image_file_path, cofidence_param):
    if cofidence_param is None:
      cofidence_param = 0.7
    for tryCount in range(60):
      try: 
        if pag.locateOnScreen(image_file_path, confidence=cofidence_param):
          break
      except Exception as e: 
        time.sleep(self.wait_time)   

  # いいね処理
  def fav_tweet(self, search_condition):
    return_code = 0 # 0の場合は正常終了　1の場合は異常終了

    # Twitterの画面を開く
    return_code = self.login_twitter()
    
    if return_code == 0:
      # アドレスバーにフォーカスしツイートを検索
      pag.hotkey('ctrl', "l")
      time.sleep(self.wait_time)

      pag.hotkey('ctrl', "a")
      time.sleep(self.wait_time)

      access_url = self.twitter_search_url + urllib.parse.quote(search_condition) + '&src=typed_query&f=live'
      pyperclip.copy(access_url)
      pag.hotkey("ctrl", "v")
      time.sleep(self.wait_time)

      pag.press("enter")
      time.sleep(self.wait_time)

      # 任意の回数だけ画面をスクロールさせ自動いいねをする
      for num in range(0, self.scroll_num):
        # mode == 0、画像認識を用いていいね
        if self.mode == 0:
          # 画面をスクロール
          pag.press('pagedown')
          time.sleep(self.wait_time)

          # 画面内にいいねの画像を探しクリック
          p= pag.locateOnScreen(self.twitter_like_button, confidence=0.8)
          if p is not None:
              x, y = pag.center(p)
              pag.click(x, y)
              time.sleep(20)
            
        # キーボードを用いていいね      
        elif self.mode == 1:
          # 次のポストをフォーカス  
          pag.press(self.next_post_keyboard_com) 
          time.sleep(self.wait_time)
                
          # いいね
          pag.press(self.do_like_keyboard_com) 
          time.sleep(20)  
      ## Chromeを閉じる
      pag.hotkey('ctrl', 'shift', "w")
    return return_code

if __name__ == "__main__":
  
  #jsonファイルからアカウント情報を取得
  accounts_json_path = 'twitter_auto_like/data/accounts.json' 

  with open(accounts_json_path) as f:
      data = json.load(f)
      
      #アカウント選択
      account = data['accounts'][0] #何番目のアカウントかここで選択
      account_username = account['username']
      account_password = account['password']
      
    # オブジェクト作成
  twitter_obj = TwitterGui(3, account_username, account_password)

    # いいねしたいツイートの検索式
  search_text = '#プログラミング学習'

  # ある単語を含むツイートに対して自動いいねをする
  twitter_obj.fav_tweet(search_text)
