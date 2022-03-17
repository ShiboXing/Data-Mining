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

step = 1
TPR, FPR = [], []
for i in range(10):
    tp, fn, tn, fp = 0, 0, 0, 0
    for j in range(len(scores1)):
        if scores1[j][0] >= i:
            if scores1[j][1]:
                tp += 1
            else:
                fp += 1
        else:
            if scores1[j][1]:
                fn += 1
            else:
                tn += 1
    tpr = float(tp) / (tp + fn)
    fpr = float(fp) / (fp + tn)
    # print(tp, fn, tn, fp)
    # print(tpr, fpr)
    TPR.append(tpr)
    FPR.append(fpr)
plt.plot(FPR, TPR)
plt.ylabel("TPR")
plt.xlabel("FPR")
plt.rc('font', size=15)
plt.show()
