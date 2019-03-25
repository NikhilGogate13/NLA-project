import json
Tp = 0
Fp = 0
Tn = 0
Fn = 0

Total = 21497

with open('mapping.json', 'r') as f:
    results = json.load(f)

f_amap = open('bucc2017/fr-en/fr-en.sample.gold', 'r').read().split('\n')

ac_dic = {}

for mapping in f_amap:
    if mapping != '':
        x = mapping.split('\t')
        key = x[0][3:]
        value = x[1][3:]
        key = int(key)
        value = int(value)
        ac_dic[key] = value

for key in results:
    value = results[key]
    key = int(key)
    if key not in ac_dic:
        Fp += 1
    else:
        if ac_dic[key] == value:
            Tp += 1
        else:
            Fn += 1
Tn = Total - Tp - Fp - Fn
print('True positive :', Tp)
print('False positive :', Fp)
print('True negative :', Tn)
print('False negative :', Fn)

Precision = float(Tp) / (float(Tp) + float(Fp))
Recall = float(Tp) / (float(Tp) + float(Fn))

F1score = (2 * Precision * Recall) / (Precision + Recall)

print('Precision :', Precision)
print('Recall :', Recall)
print('F1-score :', F1score)
