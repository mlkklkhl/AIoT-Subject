import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("human detection.csv")

group1 = df['Light'][df['Label'] == 'human - light']
group2 = df['Light'][df['Label'] == 'human - dark']

Lmeans, Dmeans = group1.mean(), group2.mean()
ttest = stats.ttest_ind(group1, group2)

sns.histplot(group1, color="skyblue", label="human - light's Light", kde=True)
sns.histplot(group2, color="orchid", label="human - dark's Light", kde=True)
plt.text(x=4000, y=300, s="human - light's mean: %.2f" % Lmeans, color='skyblue')
plt.text(x=4000, y=250, s="human - dark's mean: %.2f" % Dmeans, color='orchid')
plt.text(x=4000, y=200, s="ttest.pvalue: %.2f" % ttest.pvalue, color='red')
plt.title("T-Test between Light distribution by Label")
plt.legend()
plt.show()

print(ttest.pvalue)
