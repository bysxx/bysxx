import feedparser  
with open("README.md", "r", encoding='utf-8') as f:
    content = f.read()
rss = feedparser.parse("http://bysxx.tistory.com/rss" )

post = ""
check = f"### Latest Posts 📰"
content = content.split(check)[0]
for i, feed in reversed(list(enumerate(rss['entries']))): 
    date = feed['published_parsed'] 
    post = f"\n- [{feed['title']}]({feed['link']})" + post
text = f"{content}{check}{post}" 
with open("README.md", 'w', encoding='utf-8') as f:
    f.write(text)
