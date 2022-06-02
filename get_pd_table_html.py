import pandas as pd

with open("result.md", 'w') as f:
    pd.read_csv("classify_results/result_5000.csv", sep=';', header=None).describe().round(2).to_html(f)