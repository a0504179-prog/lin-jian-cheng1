# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 10:18:07 2026

@author: USER
"""

# import requests
# from bs4 import BeautifulSoup

# # 目標網址
# url = "https://www.lccnet.com.tw/lccnet/student-stories/details/321"

# # 模擬瀏覽器的 User-Agent，避免被網站當作機器人封鎖
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#                   "AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/115.0.0.0 Safari/537.36"
# }

# try:
#     # 發送 GET 請求
#     response = requests.get(url, headers=headers)
    
#     # 檢查請求是否成功 (狀態碼 200 代表成功)
#     if response.status_code == 200:
#         # 設定編碼（避免中文亂碼）
#         response.encoding = response.apparent_encoding
        
#         # 使用 BeautifulSoup 解析 HTML
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         # 印出整頁的 HTML 原始碼（或你可以根據需求用 soup.find() 抓取特定標籤）
#         print(soup.prettify())
        
#         # 範例：如果想把原始碼存成文字檔
#         with open("lccnet_page.html", "w", encoding="utf-8") as file:
#             file.write(response.text)
#         print("網頁原始碼已成功儲存為 lccnet_page.html")
        
#     else:
#         print(f"網頁請求失敗，狀態碼：{response.status_code}")

# except Exception as e:
#     print(f"發生錯誤：{e}")


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import time

# # 設定網址
# url = "https://www.lccnet.com.tw/lccnet/student-stories/details/321"

# # 初始化 Chrome 瀏覽器選項
# options = webdriver.ChromeOptions()
# # options.add_argument("--headless")  # 如果不想跳出瀏覽器視窗，可以取消這行的註解

# # 啟動瀏覽器
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# try:
#     # 打開網頁
#     driver.get(url)
    
#     # 等待 3 秒讓網頁 JavaScript 載入完成
#     time.sleep(3)
    
#     # 取得完整的網頁 HTML 原始碼
#     page_source = driver.page_source
    
#     # 印出前 1000 個字元的原始碼（避免印太多洗版）
#     print(page_source[:1000])
    
#     # 儲存為 HTML 檔案
#     with open("lccnet_selenium.html", "w", encoding="utf-8") as file:
#         file.write(page_source)
#     print("動態網頁原始碼已成功儲存為 lccnet_selenium.html")

# finally:
#     # 關閉瀏覽器
#     driver.quit()


# from bs4 import BeautifulSoup

# # 讀取你剛剛爬下來並儲存的 HTML 檔案
# # (如果是用 Selenium 存的，可以把檔名改成 "lccnet_selenium.html")
# html_filename = "lccnet_page.html"

# try:
#     with open(html_filename, "r", encoding="utf-8") as file:
#         html_content = file.read()

#     # 使用 BeautifulSoup 解析
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # 【注意】以下標籤與 class 名稱需根據聯成電腦網頁實際的 HTML 結構做微調
#     # 通常文章標題會放在 h1 或特定標題區塊
#     title = soup.find('h1')
#     title_text = title.get_text(strip=True) if title else "未找到標題"

#     # 假設文章內容通常包在特定的 article、main 或特定的 class 中
#     # 這裡以常見的文章內文容器為例（實際結構可用瀏覽器按 F12 檢查）
#     # 如果不確定，可以嘗試抓取整段 article 或特定的文字區塊
#     article_content = soup.find('article') # 或者 soup.find('div', class_='story-content') 等
    
#     if not article_content:
#         # 如果找不到 <article>，嘗試抓取包含主要內文的區塊（可依實際網頁調整）
#         article_content = soup.find('div', class_='content') or soup.find('main')

#     print(f"=== 文章標題 ===\n{title_text}\n")
#     print("=== 文章內文 ===")

#     if article_content:
#         # 萃取所有段落文字 (<p> 標籤)
#         paragraphs = article_content.find_all('p')
#         for p in paragraphs:
#             print(p.get_text(strip=True))
            
#         # 如果內文沒有用 <p> 包起來，也可以直接印出整個文字
#         # print(article_content.get_text(separator='\n', strip=True))
#     else:
#         print("無法自動定位內文區塊，印出網頁所有文字：")
#         print(soup.get_text(separator='\n', strip=True))

# except FileNotFoundError:
#     print(f"找不到檔案 {html_filename}，請先確認是否已成功執行爬蟲並儲存檔案。")
# except Exception as e:
#     print(f"發生錯誤：{e}")

# import jieba
# import jieba.analyse
# from collections import Counter

# # 假設 article_text 是你從網頁中萃取出來的完整文章內文字串
# # 這裡先用範例文字代替
# article_text = "聯成電腦學員心得分享，透過專業的課程訓練，順利轉職成為軟體工程師，學習過程雖然辛苦但非常充實。"

# # 1. 基本斷詞 (精確模式)
# # cut_all=False 代表精確模式，適合文本分析
# seg_list = jieba.cut(article_text, cut_all=False)

# # 將切出來的詞彙用斜線隔開並印出
# print("=== 基本斷詞結果 ===")
# print(" / ".join(seg_list))

# # --------------------------------------------------

# # 2. 進階：過濾停用詞與標點符號，並計算詞頻
# # 定義常見的標點符號或無意義的停用詞
# stop_words = {"，", "。", "、", "的", "了", "在", "是", "我", "有", "和", "就", "不", "人", "都", "一", "個", "上", "也", "很", "到", "說", "要", "去", "你", "會", "著", "沒有", "看", "好", "自己", "這"}

# # 重新執行斷詞並過濾
# words = jieba.cut(article_text)
# filtered_words = []
# for w in words:
#     w = w.strip()
#     # 過濾掉空白以及停用詞、單字長度過短的詞
#     if w and w not in stop_words and len(w) > 1:
#         filtered_words.append(w)

# # 計算詞頻（找出文章中最常出現的關鍵字）
# word_counts = Counter(filtered_words)

# print("\n=== 出現頻率最高的前 5 個關鍵字 ===")
# for word, frequency in word_counts.most_common(5):
#     print(f"詞彙: {word} | 次數: {frequency}")

# # --------------------------------------------------

# # 3. 自動提取關鍵字 (使用 jieba 的 TF-IDF 演算法)
# print("\n=== 自動萃取文章關鍵字 (TF-IDF) ===")
# keywords = jieba.analyse.extract_tags(article_text, topK=5, withWeight=False)
# print(" / ".join(keywords))

# import jieba
# from collections import Counter
# import re

# # 假設這是你從網頁抓下來並萃取出的文章內文
# # (你也可以直接把前面爬蟲抓到的文字變數帶入這裡)
# article_text = """
# 聯成電腦學員心得分享，透過專業的課程訓練，學員順利轉職成為軟體工程師。
# 學習過程雖然辛苦但非常充實，老師教得很好，上課內容也很實用，對未來的軟體職涯非常有幫助。
# """

# # 1. 資料清洗：使用正規表達式（re）過濾掉標點符號與特殊字元
# cleaned_text = re.sub(r'[^\w\s]', '', article_text)

# # 2. 執行 jieba 斷詞
# words = jieba.cut(cleaned_text)

# # 3. 定義停用詞（Stop Words）與過濾條件
# # 這些是常見的無意義助詞或代名詞，可以根據需求自行新增
# stop_words = {"的", "了", "在", "是", "我", "有", "和", "就", "不", "人", "都", "一", "個", "上", "也", "很", "到", "說", "要", "去", "你", "會", "著", "沒有", "看", "好", "自己", "這", "學員"}

# filtered_words = []
# for w in words:
#     w = w.strip()
#     # 篩選條件：排除空白、排除停用詞、且詞彙長度需大於 1 個字
#     if w and w not in stop_words and len(w) > 1:
#         filtered_words.append(w)

# # 4. 使用 Counter 計算詞頻
# word_counts = Counter(filtered_words)

# # 5. 格式化輸出結果（列出出現頻率最高的前 10 個詞）
# print("=== 文章詞頻統計分析 (Top 10) ===")
# print(f"{'詞彙':<10} | {'出現次數':<10}")
# print("-" * 25)

# for word, count in word_counts.most_common(10):
#     print(f"{word:<10} | {count:<10}")

import streamlit as st
import requests
from bs4 import BeautifulSoup
import jieba
from collections import Counter
import re

# 網頁標題與設定
st.set_page_config(page_title="網頁文章爬蟲與詞頻分析工具", page_icon="📊", layout="centered")

st.title("📊 網頁文章爬蟲與詞頻分析工具")
st.write("輸入聯成電腦學員心得或其他網址，自動幫你抓取文章內文並進行中文詞頻統計！")

# 1. 使用者輸入網址
url = st.text_input("請輸入目標網址 (URL)：", value="https://www.lccnet.com.tw/lccnet/student-stories/details/321")

# 自訂停用詞輸入框
default_stops = "的, 了, 在, 是, 我, 有, 和, 就, 不, 人, 都, 一, 個, 上, 也, 很, 到, 說, 要, 去, 你, 會, 著, 沒有, 看, 好, 自己, 這, 學員"
stop_words_input = st.text_area("自訂停用詞（用逗號分隔）：", value=default_stops)

# 執行按鈕
if st.button("開始抓取與分析", type="primary"):
    if not url:
        st.warning("請先輸入網址！")
    else:
        with st.spinner("正在爬取網頁並進行詞頻分析，請稍候..."):
            try:
                # 模擬瀏覽器 Header 避免被擋
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                                  "Chrome/115.0.0.0 Safari/537.36"
                }
                
                # 發送請求
                response = requests.get(url, headers=headers, timeout=10)
                response.encoding = response.apparent_encoding
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    # 抓取標題
                    title = soup.find('h1')
                    title_text = title.get_text(strip=True) if title else "未找到標題"
                    
                    # 抓取內文區塊 (可依網站結構調整)
                    article_content = soup.find('article') or soup.find('div', class_='content') or soup.find('main')
                    
                    if article_content:
                        paragraphs = article_content.find_all('p')
                        article_text = "\n".join([p.get_text(strip=True) for p in paragraphs])
                    else:
                        article_text = soup.get_text(separator='\n', strip=True)
                    
                    # 顯示抓取結果
                    st.success("網頁爬取成功！")
                    
                    with st.expander("📌 檢視文章標題與內文"):
                        st.subheader(title_text)
                        st.text_area("內文預覽", article_text, height=200)
                    
                    # 2. 進行詞頻分析
                    # 資料清洗 (去除標點符號)
                    cleaned_text = re.sub(r'[^\w\s]', '', article_text)
                    
                    # 執行斷詞
                    words = jieba.cut(cleaned_text)
                    
                    # 處理停用詞集合
                    stop_words = {w.strip() for w in stop_words_input.split(",")}
                    
                    filtered_words = []
                    for w in words:
                        w = w.strip()
                        # 過濾條件：非空白、非停用詞、長度大於 1
                        if w and w not in stop_words and len(w) > 1:
                            filtered_words.append(w)
                    
                    # 計算詞頻
                    word_counts = Counter(filtered_words)
                    top_n = st.slider("顯示詞頻前幾名的詞彙：", min_value=5, max_value=30, value=10)
                    
                    # 3. 呈現結果
                    st.subheader(f"📈 文章詞頻統計 (Top {top_n})")
                    
                    # 轉成表格呈現
                    chart_data = {
                        "詞彙": [item[0] for item in word_counts.most_common(top_n)],
                        "出現次數": [item[1] for item in word_counts.most_common(top_n)]
                    }
                    
                    # 左右分欄：左邊顯示表格，右邊顯示長條圖
                    col1, col2 = st.columns(2)
                    with col1:
                        st.dataframe(chart_data, use_container_width=True)
                    with col2:
                        st.bar_chart(data=chart_data, x="詞彙", y="出現次數")
                        
                else:
                    st.error(f"網頁請求失敗，狀態碼：{response.status_code}")

            except Exception as e:
                st.error(f"發生錯誤：{e}")