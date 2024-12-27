import gensim
from gensim import models, corpora
from gensim.utils import simple_preprocess
import numpy as np
import time  # Импортируем модуль time

# Начинаем отсчет времени
start_time = time.time()

with open('result.txt', 'r', encoding='utf-8') as file:
    documents = file.readlines()

mydict = corpora.Dictionary([simple_preprocess(line) for line in documents])
corpus = [mydict.doc2bow(simple_preprocess(line)) for line in documents]

tfidf = models.TfidfModel(corpus)

tfidf_corpus = tfidf[corpus]

all_tfidf_weights = []
for doc in tfidf_corpus:
    all_tfidf_weights.extend([[mydict[id], freq] for id, freq in doc])

word_weights = {}
for word, weight in all_tfidf_weights:
    if word in word_weights:
        word_weights[word] += weight
    else:
        word_weights[word] = weight

sorted_word_weights = sorted(word_weights.items(), key=lambda x: x[1], reverse=True)[:30]

with open('output.txt', 'w') as f:
    for word, weight in sorted_word_weights:
        f.write(f"{word}: {np.around(weight, decimals=2)}\n")

# Завершаем отсчет времени
end_time = time.time()
execution_time = end_time - start_time

print(f"time: {execution_time:.10f} seconds")