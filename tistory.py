import feedparser  
with open("README.md", "r", encoding='utf-8') as f:
    content = f.read()
rss = feedparser.parse("http://bysxx.tistory.com/rss" )

post = ""
for i, feed in reversed(list(enumerate(rss['entries']))): 
    date = feed['published_parsed'] 
    check = f"- [{feed['title']}]({feed['link']})"
    if(content.find(check)) == -1:
        post = f"\n- [{feed['title']}]({feed['link']})" + post
print('post:', post)
text = f"{content}{post}" 
with open("README.md", 'w', encoding='utf-8') as f:
    f.write(text)
