import gensim

def read_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        texts = [line.strip().split() for line in file.readlines()]
    return texts

file_path = 'result.txt'
texts = read_from_file(file_path)

bigr = gensim.models.phrases.Phrases(texts, min_count=3, threshold=3)
words_underscore = []
for word in bigr[texts[0]]:
    if '_' in word:
        words_underscore.append(word)
res = list(set(words_underscore))

# ��������� ���� ��� ������
with open('outputBI.txt', 'w') as f:
    f.write("Bigramms:\n")  # ����� "Bigramms" � ��������� �� ����� ������
    f.write(" ".join(res))   # ����� �������� res ����� ������


trigr = gensim.models.phrases.Phrases(bigr[texts], threshold=2)
words_underscore = []
for word in trigr[bigr[texts[0]]]:
    if word.count('_') == 2:
        words_underscore.append(word)
res = list(set(words_underscore))

# ��������� ���� ��� ������
with open('outputTRI.txt', 'w') as f:
    f.write("Trigramms:\n")  # ����� "Bigramms" � ��������� �� ����� ������
    f.write(" ".join(res))   # ����� �������� res ����� ������