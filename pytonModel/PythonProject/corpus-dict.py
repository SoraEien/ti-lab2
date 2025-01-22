import spacy
from gensim import corpora, models
from collections import Counter
import numpy as np
from pprint import pprint

# Загрузка модели spacy для русского языка
nlp = spacy.load('ru_core_news_sm')

# Чтение текста из файла
with open('lemmatized_text.txt', 'r', encoding='utf-8') as file:
    TEXT2 = file.read()

# Лемматизация токенов
tokens = nlp(TEXT2)
lemmatized_tokens = [token.lemma_ for token in tokens if not token.is_stop and not token.is_punct]

# Вывод лемматизированных токенов
pprint(lemmatized_tokens)

# Подсчет частоты лемматизированных токенов
word_freq = Counter(lemmatized_tokens)

# Создание корпуса: список кортежей (слово, частота)
corpus = [(word, freq) for word, freq in word_freq.items()]

# Вывод корпуса
pprint(corpus)

# Создание словаря
dictionary = corpora.Dictionary([lemmatized_tokens])

# Создание корпуса в формате bag-of-words
corpus_bow = [dictionary.doc2bow(lemmatized_tokens)]

# Печать BOW
for doc in corpus_bow:
    print([[dictionary[id], freq] for id, freq in doc])

# Создание модели TF-IDF
tfidf = models.TfidfModel(corpus_bow, smartirs='ntc')

# Получение TF-IDF для документа
doc_tfidf = tfidf[corpus_bow[0]]

# Сортировка по весу
sorted_tfidf = sorted(doc_tfidf, key=lambda x: x[1], reverse=True)

# Вывод первых 30 слов и их весов
for word_id, weight in sorted_tfidf[:30]:
    print(dictionary[word_id], np.around(weight, decimals=2))
