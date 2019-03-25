import pdb
import re, math
from collections import Counter
import json

WORD = re.compile(r'\w+')


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


fp = open('translatefr.en', "r")
translated_sentences = fp.readlines()
for i in range(len(translated_sentences)):
    translated_sentences[i] = translated_sentences[i].strip()
# translated_sentences = translated_sentences[:5]
ep = open("bucc2017/fr-en/fr-en.sample.en", "r")
original_sentences = ep.readlines()
for i in range(len(original_sentences)):
    original_sentences[i] = original_sentences[i].strip()
    x = original_sentences[i].split("\t", 1)
    original_sentences[i] = x[1]
fr_en_map = {}
for i in range(len(translated_sentences)):
    if i % 100 == 0:
        print i
    maxi = None
    maxi_index = None
    try:
        vec1 = text_to_vector(translated_sentences[i])
    except:
        continue
    for j in range(len(original_sentences)):
        try:
            vec2 = text_to_vector(original_sentences[j])
            score = get_cosine(vec1, vec2)
            if score > 0.7:
                if maxi == None:
                    maxi = score
                    maxi_index = j
                elif maxi < score:
                    maxi = score
                    maxi_index = j
        except:
            continue
    if maxi != None:
        fr_en_map[i + 1] = maxi_index + 1
fr_en_json = json.dumps(fr_en_map)
f = open("mapping.json", "w")
f.write(fr_en_json)
f.close()
