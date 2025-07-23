from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = """
Experienced Full Stack Developer with strong background in Python, Django, React, REST APIs,
MySQL, Git, and cloud technologies like AWS and Docker. Passionate about building scalable web apps.
Familiar with Agile methodology and DevOps practices.
"""

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("🔍 Word Cloud of Resume Keywords", fontsize=16)
plt.show()
