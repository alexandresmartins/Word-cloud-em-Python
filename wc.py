import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

# Carregando o texto
texto = "A engenharia de dados é uma área essencial para o sucesso de projetos de análise de dados. Ela se concentra na coleta, armazenamento e processamento de dados de forma eficiente e segura. Com habilidades em programação, banco de dados e Big Data, engenheiros de dados criam soluções escaláveis e eficazes para lidar com grandes volumes de dados, permitindo a análise e insights que podem melhorar os negócios."

# Pré-processando o texto
stopwords = set(STOPWORDS)
wordcloud = WordCloud(background_color="white", max_words=200, stopwords=stopwords)

# Criando a word cloud
wordcloud.generate(texto)

# Configurando a imagem
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad=0)

# Mostrando a imagem
plt.show()

# Salvando a imagem
wordcloud.to_file("wordcloud.png")
