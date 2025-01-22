import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim.models import Phrases
from gensim.models.phrases import Phraser
import pymorphy2

# Загрузка необходимых ресурсов NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Лемматизация текста для русского языка
def lemmatize_text(text):
    morph = pymorphy2.MorphAnalyzer()
    words = word_tokenize(text, language='russian')
    stop_words = set(stopwords.words('russian'))

    # Лемматизация и удаление стоп-слов
    lemmatized_words = [morph.parse(word)[0].normal_form for word in words if word.isalnum() and word.lower() not in stop_words]
    return lemmatized_words


# Функция для загрузки текста из файла
def load_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Функция для записи лемматизированных слов в файл
def save_lemmatized_text(lemmatized_words, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(' '.join(lemmatized_words))

# Пример: загрузка текста из файла
file_path = 'resultCOOL.txt'  # Укажите путь к вашему текстовому файлу
text = load_text_from_file(file_path)

# Лемматизация текста
lemmatized_words = lemmatize_text(text)

# Сохранение лемматизированных слов в новый файл
output_file_path = 'lemmatized_text.txt'  # Укажите путь к файлу, в который хотите сохранить результат
save_lemmatized_text(lemmatized_words, output_file_path)

# Разделяем текст на список слов (как в первом коде)
texts = [lemmatized_words]

# Создание биграмм
bigram = Phrases(texts, min_count=3, threshold=3)
bigram_model = Phraser(bigram)

# Получаем биграммы
words_with_underscore = []
for word in bigram_model[texts[0]]:
    if '_' in word:
        words_with_underscore.append(word)

# Убираем дубликаты
un_list_bigram = list(set(words_with_underscore))
print("Биграммы:", un_list_bigram)

# Создание триграмм
trigram = Phrases(bigram_model[texts], threshold=2)
trigram_model = Phraser(trigram)

# Получаем триграммы
words_with_underscore = []
for word in trigram_model[bigram_model[texts[0]]]:
    if word.count('_') == 2:
        words_with_underscore.append(word)

# Убираем дубликаты
un_list_trigram = list(set(words_with_underscore))
print("Триграммы:", un_list_trigram)
