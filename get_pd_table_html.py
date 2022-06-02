import pandas as pd

with open("result.md", 'w') as f:
    pd.read_csv("classify_results/result_40000.csv", sep=';', header=None).describe().round(4).to_html(f)