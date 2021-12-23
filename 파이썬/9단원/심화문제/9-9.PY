
from wordcloud import WordCloud, STOPWORDS

s_words = STOPWORDS.union({'south','north','korean','world','country'})
wordcloud = WordCloud(width = 2000,height=1500, 
                      stopwords= s_words).generate()