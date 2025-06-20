from gtts import gTTS
import os

# 你的单词列表
words = [
    "morning", "Miss", "new", "student", "French",
    "German", "nice", "meet", "Japanese", "Korean",
    "Chinese", "too", "Mr"
]

# 输出目录，建议先创建
output_dir = "/Users/joy/Desktop/xuwei/work/git/guoguo/static/mp3"
os.makedirs(output_dir, exist_ok=True)

for word in words:
    tts = gTTS(text=word, lang='en', slow=False)  # 英文发音
    filename = os.path.join(output_dir, f"{word}.mp3")
    tts.save(filename)
    print(f"Saved {filename}")