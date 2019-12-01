from settings import *

# Import Data
df = pd.read_csv("mpg_ggplot2.csv")

# Draw Plot
plt.figure(figsize=(13, 10), dpi=80)
sns.violinplot(x='class', y='hwy', data=df, scale='width', inner='quartile')

# Decoration
plt.title('Violin Plot of Highway Mileage by Vehicle Class', fontsize=22)
plt.show()
