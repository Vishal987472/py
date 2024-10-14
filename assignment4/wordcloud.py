from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "this is vishal."
wordcloud = WordCloud(width=200, height=100, background_color='white').generate(text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off') 
plt.show()