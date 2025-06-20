from gtts import gTTS
import os
import hashlib

def md5_string(s: str) -> str:
    return hashlib.md5(s.encode('utf-8')).hexdigest()
# 你的单词列表
lesson = [
["MR. BLAKE : Good morning.","Good morning."],
["STUDENTS: Good morning, Mr. Blake.","Good morning, Mr. Blake."],
["MR. BLAKE :",""],
["    This is Miss Sophie Dupont.","This is Miss Sophie Dupont."],
["    Sophie is a new student.","Sophie is a new student."],
["    She is French.","She is French."],
["MR. BLAKE :",""],
["    Sophie, this is Hans.","Sophie, this is Hans."],
["    He is German.","He is German."],
["HANS : Nice to meet you.","Nice to meet you."],
["MR. BLAKE :",""],
["    And this is Naoko.","And this is Naoko."],
["    She's Japanese.","She's Japanese."],
["NAOKO : Nice to meet you.","Nice to meet you."],
["MR. BLAKE :",""],
["    And this is Chang-woo.","And this is Chang-woo."],
["    He's Korean.","    He's Korean."],
["CHANG-WOO : Nice to meet you.","Nice to meet you."],
["MR. BLAKE :",""],
["    And this is Luming.","And this is Luming."],
["    He's Chinese.","He's Chinese."],
["LUMING : Nice to meet you.","Nice to meet you."],
["MR. BLAKE :",""],
["    And this is Xiaohui.","And this is Xiaohui."],
["    She's Chinese, too.","She's Chinese, too."],
["XIAOHUI : Nice to meet you","Nice to meet you"],
]

# 输出目录，建议先创建
output_dir = "/Users/joy/Desktop/xuwei/work/git/guoguo/static/mp3"
os.makedirs(output_dir, exist_ok=True)

for item in lesson:
    word = item[1]
    text = item[0]
    if word != "" :
        tts = gTTS(text=word, lang='en', slow=True)  # 英文发音
        name = md5_string(word)
        filename = os.path.join(output_dir, f"{name}.mp3")
        # if not os.path.exists(filename):
        tts.save(filename)
        text = f"{text}<audiobutton id=\"{name}\" /></br>" 
    else:
        text = f"{text}</br>" 
    print(f"{text}")