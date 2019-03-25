import mtranslate

fp = open("bucc2017/fr-en/fr-en.sample.fr", "r")
wp = open("translatefr.en", "w")
france_sentences = fp.readlines()
for i in range(len(france_sentences)):
    france_sentences[i] = france_sentences[i].strip()
    x = france_sentences[i].split("\t", 1)
    france_sentences[i] = x[1]
# france_sentences = france_sentences[:5]
cou = 0
translations = []
x = mtranslate.translate(france_sentences[0], "en", "auto")
for sentence in france_sentences:
    cou += 1
    try:
        x = mtranslate.translate(sentence, "en", "auto")
        translations.append(x)
    except:
        translations.append("no-valid-translation")
    if cou % 100 == 0:
        print cou
for translation in translations:
    try:
        wp.write(translation.encode("utf-8"))
        wp.write('\n'.encode("utf-8"))
    except:
        wp.write('No-translation'.encode("utf-8"))
        wp.write('\n'.encode("utf-8"))
wp.close()
