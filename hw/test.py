from re import L
import matplotlib.pyplot as plt
from bisect import bisect, bisect_left

labels = [True, True, False, False, False, True, False, True, True, True, True, False, False, True, False, False]
with open("scores") as f:
    scores1 = f.readline().strip().split(' ')
    scores2 = f.readline().strip().split(' ')
    scores1 = sorted([(float(scores1[i]), labels[i]) for i in range(len(labels))])
    scores2 = sorted([(float(scores2[i]), labels[i]) for i in range(len(labels))])

print(scores1)
print(scores2)

scores = []
for s, l in scores2:
    if l:
        scores += [(s, l)] * 10
    else:
        scores.append((s, l))

step = 1
TPR, FPR = [], []
PRECISION = []
for i in range(10):
    tp, fn, tn, fp = 0, 0, 0, 0
    for j in range(len(scores)):
        if scores[j][0] >= i:
            if scores[j][1]:
                tp += 1
            else:
                fp += 1
        else:
            if scores[j][1]:
                fn += 1
            else:
                tn += 1
    tpr = float(tp) / (tp + fn)
    fpr = float(fp) / (fp + tn)
    precision = float(tp) / (tp+fp) if tp+fp else 0
    TPR.append(tpr)
    FPR.append(fpr)
    PRECISION.append(precision)
    if i==3 or i==5 or i==7:
        print(tp, fn, tn, fp)
        print(tpr, fpr)
        print('precision: ', precision)
        print('f-measure: ', 2.0/(1/precision + 1/tpr), 2*tp/(2*tp + fp + fn))

fig, ax = plt.subplots()
ax.plot(FPR, TPR)
plt.ylabel("TPR")
plt.xlabel("FPR")
for i in [3, 5, 7]:
    # ax.scatter(FPR[i], TPR[i])
    ax.scatter(PRECISION[i], TPR[i])
    ax.annotate(f"threshold: {i}", (FPR[i], TPR[i]))
plt.rc('font', size=15)
plt.show()
