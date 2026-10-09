# Task 5 – Exploratory Data Analysis (EDA)

## Internship Task
**Task 5: Exploratory Data Analysis (EDA)**

The objective of this task is to explore a dataset using statistical summaries and visualizations, identify patterns, trends, relationships, missing values, and anomalies, and summarize the findings.

## Dataset
**Titanic passenger dataset** (`train.csv`)

- Rows: 891
- Columns: 12
- Target variable: `Survived`
- 0 = Did not survive
- 1 = Survived

## Tools Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## EDA Performed
1. Dataset shape and information using `info()`
2. Statistical summary using `describe()`
3. Frequency analysis using `value_counts()`
4. Missing-value analysis
5. Univariate analysis
6. Bivariate analysis
7. Histograms
8. Boxplots
9. Scatterplots
10. Correlation heatmap
11. Pairplot
12. Skewness and outlier discussion
13. Multicollinearity discussion
14. Key findings and conclusion
15. Interview questions and answers

## Main Findings
- Overall survival rate: **38.38%**
- Female survival rate: **74.2%**
- Male survival rate: **18.9%**
- First-class survival rate: **63.0%**
- Second-class survival rate: **47.3%**
- Third-class survival rate: **24.2%**
- `Pclass` has a correlation of approximately **-0.34** with survival.
- `Fare` has a correlation of approximately **0.26** with survival.
- `Fare` is strongly right-skewed.
- Missing values are mainly present in `Cabin` and `Age`.

## Files
- `Task_5_EDA_Titanic.ipynb` – complete Jupyter Notebook
- `Task_5_EDA_Report.pdf` – PDF report of findings
- `train.csv` – dataset used for the analysis
- `plots/` – generated visualizations

## How to Run
1. Open `Task_5_EDA_Titanic.ipynb` in Jupyter Notebook, JupyterLab, Google Colab, or VS Code.
2. Keep `train.csv` in the same folder as the notebook.
3. Run the cells from top to bottom.

## Conclusion
The EDA shows clear differences in survival across sex and passenger class. It also highlights skewed fare values, outliers, and missing data that should be considered in further analysis or predictive modeling.
