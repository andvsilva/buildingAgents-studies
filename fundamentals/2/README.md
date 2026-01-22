
---

## Pandas: Filtering, Merging, and Reshaping Datasets

This guide provides practical examples of **filtering**, **merging**, and **reshaping** datasets using **Pandas**. It is designed as a quick reference for data analysis and data preparation workflows.

---

### Filtering Data

#### Filter rows with conditions

```python
df[df["age"] > 30]
```

```python
df[(df["age"] > 25) & (df["salary"] < 8000)]
```

```python
df[(df["age"] < 25) | (df["salary"] > 8000)]
```

#### Filter columns

```python
df[["name", "salary"]]
```

#### Using `query()` (recommended for readability)

```python
df.query("age > 25 and salary < 8000")
```

---

### Merging DataFrames

#### Example datasets

```python
employees = pd.DataFrame({
    "emp_id": [1, 2, 3],
    "name": ["Ana", "Bruno", "Carlos"]
})

salaries = pd.DataFrame({
    "emp_id": [1, 2, 4],
    "salary": [3000, 7000, 5000]
})
```

#### Inner Join

```python
pd.merge(employees, salaries, on="emp_id")
```

#### Left Join

```python
pd.merge(employees, salaries, on="emp_id", how="left")
```

#### Right Join

```python
pd.merge(employees, salaries, on="emp_id", how="right")
```

#### Outer Join

```python
pd.merge(employees, salaries, on="emp_id", how="outer")
```

---

### Concatenating DataFrames

#### Stack rows (vertical)

```python
pd.concat([df1, df2], axis=0)
```

#### Combine columns (horizontal)

```python
pd.concat([df1, df2], axis=1)
```

---

### Reshaping Data

#### Wide to Long (`melt`)

```python
pd.melt(
    sales,
    id_vars="product",
    var_name="month",
    value_name="sales"
)
```

#### Long to Wide (`pivot`)

```python
long_df.pivot(index="product", columns="month", values="sales")
```

#### Aggregated reshape (`pivot_table`)

```python
pd.pivot_table(
    long_df,
    index="product",
    columns="month",
    values="sales",
    aggfunc="mean"
)
```

---

### Useful Patterns

#### Filter + Merge pipeline

```python
result = (
    employees
    .query("emp_id != 3")
    .merge(salaries, on="emp_id", how="left")
)
```

#### Handle missing values after merge

```python
df["salary"].fillna(0, inplace=True)
```

---

### Quick Reference

| Task         | Pandas Function            |
| ------------ | -------------------------- |
| Filter rows  | `df[condition]`, `query()` |
| Merge tables | `merge()`                  |
| Concatenate  | `concat()`                 |
| Wide → Long  | `melt()`                   |
| Long → Wide  | `pivot()`, `pivot_table()` |

 🚀


---

## Data Cleaning and Missing Value Imputation

This section covers common techniques for **cleaning datasets** and **handling missing values** using **Pandas**, which are essential steps in any data analysis or machine learning pipeline.

---

### Identifying Missing Data

```python
df.isna()
```

```python
df.isna().sum()
```

```python
df.info()
```

---

### Dropping Missing Values

#### Drop rows with any missing values

```python
df.dropna()
```

#### Drop rows where all values are missing

```python
df.dropna(how="all")
```

#### Drop columns with missing values

```python
df.dropna(axis=1)
```

#### Drop rows based on specific columns

```python
df.dropna(subset=["salary", "age"])
```

---

### Filling Missing Values (Imputation)

#### Fill with a constant value

```python
df.fillna(0)
```

```python
df["salary"].fillna("Unknown", inplace=True)
```

---

#### Fill with mean, median, or mode

```python
df["age"].fillna(df["age"].mean(), inplace=True)
```

```python
df["salary"].fillna(df["salary"].median(), inplace=True)
```

```python
df["department"].fillna(df["department"].mode()[0], inplace=True)
```

---

### Forward and Backward Fill

#### Forward fill

```python
df.fillna(method="ffill")
```

#### Backward fill

```python
df.fillna(method="bfill")
```

---

### Conditional Imputation

```python
df.loc[df["salary"].isna(), "salary"] = df["salary"].median()
```

---

### Cleaning Data Types

#### Convert data types

```python
df["age"] = df["age"].astype(int)
```

```python
df["date"] = pd.to_datetime(df["date"])
```

---

### Removing Duplicates

```python
df.duplicated()
```

```python
df.drop_duplicates()
```

```python
df.drop_duplicates(subset=["emp_id"])
```

---

### Handling Invalid or Inconsistent Values

#### Replace invalid values

```python
df["salary"].replace(-1, pd.NA, inplace=True)
```

```python
df.replace("N/A", pd.NA, inplace=True)
```

---

### Common Cleaning Pipeline

```python
clean_df = (
    df
    .replace("N/A", pd.NA)
    .drop_duplicates()
    .assign(
        age=lambda x: x["age"].fillna(x["age"].median()),
        salary=lambda x: x["salary"].fillna(x["salary"].mean())
    )
)
```

---

### Best Practices

* Always **inspect missing values** before dropping data
* Prefer **imputation** over deletion when data is scarce
* Use **median** for skewed numerical distributions
* Use **mode** for categorical features
* Document cleaning decisions clearly

---

### Quick Reference

| Task              | Pandas Function             |
| ----------------- | --------------------------- |
| Detect missing    | `isna()`, `info()`          |
| Remove missing    | `dropna()`                  |
| Fill missing      | `fillna()`                  |
| Replace values    | `replace()`                 |
| Remove duplicates | `drop_duplicates()`         |
| Convert types     | `astype()`, `to_datetime()` |

---


# **Feature Engineering**

Feature engineering is the process of transforming raw data into meaningful features that improve the predictive power of machine learning models. Good features can reveal patterns that the model otherwise wouldn’t detect.

---

**Creating New Features**

You have a dataset of people with **height (in meters)** and **weight (in kg)**, and you want to predict if someone is overweight.

* Raw features: `height`, `weight`
* New feature: **BMI (Body Mass Index)**

[
\text{BMI} = \frac{\text{weight}}{\text{height}^2}
]

**Python example:**

```python
import pandas as pd

df = pd.DataFrame({'height':[1.7, 1.8, 1.6], 'weight':[70, 80, 50]})
df['BMI'] = df['weight'] / df['height']**2
print(df)
```

Output:

| height | weight | BMI   |
| ------ | ------ | ----- |
| 1.7    | 70     | 24.22 |
| 1.8    | 80     | 24.69 |
| 1.6    | 50     | 19.53 |

> **Why it helps:** BMI is more informative for predicting overweight than using height or weight separately.

---

**Transforming Features**

* **Scaling:** Some models (like KNN or SVM) are sensitive to feature magnitude.
* **Log transformation:** Reduces skewness in features like income or price.

**Example:**

```python
import numpy as np
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame({'income':[2000, 5000, 100000]})
df['log_income'] = np.log(df['income'])
scaler = StandardScaler()
df['income_scaled'] = scaler.fit_transform(df[['income']])
print(df)
```

---

**Handling Missing Values**

Missing data can reduce model accuracy.

Strategies include filling with **mean** (numerical), **mode** (categorical), or predicting missing values using other features.

**Example:**

```python
df = pd.DataFrame({'age':[25, np.nan, 30]})
df['age'].fillna(df['age'].mean(), inplace=True)
print(df)
```

---

**Feature Interactions**

Sometimes, combining two features captures relationships better.

**Example:** Predicting house price

```python
df = pd.DataFrame({'area':[50, 100, 80], 'rooms':[2,4,3]})
df['area_per_room'] = df['area'] / df['rooms']
print(df)
```

---

# **Encoding Techniques**

**Theory:** Many ML models cannot handle categorical (non-numerical) features. Encoding converts them into numbers.

---

**Label Encoding**

* Assign each category an integer
* Good for **ordinal data**

```python
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({'size':['Small','Medium','Large']})
le = LabelEncoder()
df['size_encoded'] = le.fit_transform(df['size'])
print(df)
```

Output:

| size   | size_encoded |
| ------ | ------------ |
| Small  | 2            |
| Medium | 1            |
| Large  | 0            |

> Integers imply order; suitable for "Low < Medium < High".

---

**One-Hot Encoding**

* Creates a **binary column for each category**
* Good for **nominal data**

```python
df = pd.DataFrame({'color':['Red','Green','Blue']})
df_onehot = pd.get_dummies(df, columns=['color'])
print(df_onehot)
```

Output:

| color_Red | color_Green | color_Blue |
| --------- | ----------- | ---------- |
| 1         | 0           | 0          |
| 0         | 1           | 0          |
| 0         | 0           | 1          |

---

**Target / Mean Encoding**

* Replace category with **average target value**

**Example:** Predict if a person buys a product based on city:

```python
df = pd.DataFrame({'city':['A','B','A','C'], 'buy':[1,0,1,0]})
mean_encode = df.groupby('city')['buy'].mean()
df['city_encoded'] = df['city'].map(mean_encode)
print(df)
```

Output:

| city | buy | city_encoded |
| ---- | --- | ------------ |
| A    | 1   | 1.0          |
| B    | 0   | 0.0          |
| A    | 1   | 1.0          |
| C    | 0   | 0.0          |

> Captures relationship between **city** and **buying tendency**.

---

**Encoding Cyclical Features**

* Hours, months, weekdays are cyclical
* Use sine & cosine to capture circularity

```python
df = pd.DataFrame({'hour':[0,6,12,18]})
df['hour_sin'] = np.sin(2*np.pi*df['hour']/24)
df['hour_cos'] = np.cos(2*np.pi*df['hour']/24)
print(df)
```

---

**Key Takeaways**

* Feature engineering creates meaningful features that improve model performance.
* Scaling, transforming, and handling missing values are essential preprocessing steps.
* Encoding converts categorical or cyclical features into numerical forms suitable for machine learning models.
* The choice of encoding depends on **data type** (numerical, categorical, ordinal, cyclical) and the **model used**.

---

# Feature Scaling and Normalization

Feature scaling and normalization are **data preprocessing techniques** used to transform numerical features so they are on comparable scales. This is important because many machine learning algorithms are sensitive to the magnitude of feature values.

---

## Why Feature Scaling Is Important

Many algorithms rely on:

* Distance calculations (e.g., KNN, K-Means)
* Gradient descent (e.g., Linear Regression, Neural Networks)

If features have very different ranges, larger-valued features can dominate the model.

**Example:**

* Age: 20–60
* Salary: 30,000–120,000

Without scaling, salary will dominate model behavior.

---

## Normalization (Min–Max Scaling)

### What It Does

Rescales features to a fixed range, usually **[0, 1]**.

### Formula

[
x' = \frac{x - x_{min}}{x_{max} - x_{min}}
]

### When to Use

* Distance-based algorithms (KNN, K-Means)
* Neural networks
* When data has **no significant outliers**

### Python Example

```python
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Sample dataset: [Age, Salary]
X = np.array([
    [25, 30000],
    [35, 50000],
    [45, 80000]
])

scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)

print("Normalized data:")
print(X_normalized)
```

### Output (approx.)

```text
[[0.   0.  ]
 [0.5  0.4 ]
 [1.   1.  ]]
```

---

## Standardization (Z-Score Scaling)

### What It Does

Transforms features so that:

* Mean = 0
* Standard deviation = 1

### Formula

[
x' = \frac{x - \mu}{\sigma}
]

### When to Use

* Linear Regression
* Logistic Regression
* Support Vector Machines (SVM)
* Principal Component Analysis (PCA)

### Python Example

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)

print("Standardized data:")
print(X_standardized)
```

### Output (approx.)

```text
[[-1.22 -1.14]
 [ 0.00 -0.27]
 [ 1.22  1.41]]
```

---

## Robust Scaling (Handling Outliers)

### What It Does

Uses:

* Median
* Interquartile Range (IQR)

This makes it robust to outliers.

### When to Use

* Data with significant outliers

### Python Example

```python
from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
X_robust = scaler.fit_transform(X)

print("Robust scaled data:")
print(X_robust)
```

---

## Important Rule: Avoid Data Leakage ⚠️

Always fit the scaler **only on training data**.

```python
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

❌ Never fit on test data.

---

## Summary Table

| Method         | Output Range | Handles Outliers | Typical Use        |
| -------------- | ------------ | ---------------- | ------------------ |
| MinMaxScaler   | 0–1          | ❌ No             | KNN, K-Means       |
| StandardScaler | Unbounded    | ⚠️ Moderate      | Most ML models     |
| RobustScaler   | Unbounded    | ✔ Yes            | Data with outliers |

---

## Conclusion

* **Normalization** scales data to a fixed range
* **Standardization** centers data with unit variance
* Proper scaling improves model accuracy and convergence

---

Below is a **clear explanation with Python examples**, formatted so you can **directly paste it into a `README.md`**.

---

# Handling Outliers and Skewed Distributions

Real-world data often contains **outliers** and **skewed distributions**. If not handled properly, they can negatively affect machine learning models, especially those based on distance or statistical assumptions.

---

## 1. What Are Outliers?

**Outliers** are extreme values that differ significantly from most observations.

### Example

* Salaries: `[30k, 35k, 40k, 45k, 1,000k]`
* `1,000k` is an outlier

### Why Outliers Are a Problem

* Distort mean and standard deviation
* Hurt performance of Linear Regression, K-Means, PCA
* Slow or destabilize gradient descent

---

## 2. Detecting Outliers

### A. Interquartile Range (IQR)

[
IQR = Q3 - Q1
]

Outliers are values:

* `< Q1 - 1.5 × IQR`
* `> Q3 + 1.5 × IQR`

### Python Example

```python
import numpy as np

data = np.array([30, 32, 35, 36, 38, 40, 120])

q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = data[(data < lower_bound) | (data > upper_bound)]
print("Outliers:", outliers)
```

---

## 3. Handling Outliers

### A. Remove Outliers (Use Carefully)

✔ When outliers are **errors or noise**

```python
filtered_data = data[(data >= lower_bound) & (data <= upper_bound)]
```

❌ Avoid if outliers are meaningful (e.g., high-income customers)

---

### B. Capping / Winsorization

Limits extreme values to a threshold.

```python
data_capped = np.clip(data, lower_bound, upper_bound)
```

✔ Preserves dataset size
✔ Reduces extreme influence

---

### C. Robust Scaling (Recommended)

Uses **median** and **IQR** instead of mean and standard deviation.

```python
from sklearn.preprocessing import RobustScaler

X = data.reshape(-1, 1)
scaler = RobustScaler()
X_robust = scaler.fit_transform(X)

print(X_robust)
```

✔ Very effective for outliers
✔ Safe for most ML models

---

## 4. Skewed Distributions

A **skewed distribution** is not symmetric.

* **Right-skewed** (positive skew): income, sales
* **Left-skewed** (negative skew): exam scores (easy exam)

### Why Skewness Is a Problem

* Violates assumptions of linear models
* Reduces model performance
* Makes scaling less effective

---

## 5. Handling Skewed Data

### A. Log Transformation (Most Common)

✔ For right-skewed data
❌ Cannot handle zero or negative values

```python
import numpy as np

income = np.array([2000, 3000, 4000, 10000, 50000])
log_income = np.log(income)

print(log_income)
```

---

### B. Log1p Transformation (Safer)

Handles zeros.

```python
log_income = np.log1p(income)
```

---

### C. Square Root Transformation

✔ For moderate skew

```python
sqrt_income = np.sqrt(income)
```

---

### D. Power Transforms (Best for ML)

#### Box-Cox (positive values only)

```python
from sklearn.preprocessing import PowerTransformer

pt = PowerTransformer(method="box-cox")
X_bc = pt.fit_transform(income.reshape(-1, 1))
```

#### Yeo-Johnson (allows zero & negatives)

```python
pt = PowerTransformer(method="yeo-johnson")
X_yj = pt.fit_transform(income.reshape(-1, 1))
```

✔ Makes data more Gaussian
✔ Excellent for linear models and PCA

---

## 6. Recommended Pipeline (Best Practice)

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PowerTransformer, RobustScaler

pipeline = Pipeline([
    ("power", PowerTransformer(method="yeo-johnson")),
    ("scaler", RobustScaler())
])

X_processed = pipeline.fit_transform(X)
```

---

## 7. Summary Table

| Problem          | Solution        | Tool               |
| ---------------- | --------------- | ------------------ |
| Extreme outliers | Robust scaling  | `RobustScaler`     |
| Right skew       | Log / Log1p     | `np.log1p`         |
| Any skew         | Power transform | `PowerTransformer` |
| Outliers + skew  | Power + Robust  | Pipeline           |

---

## 8. Key Takeaways

* **Do not blindly remove outliers**
* Use **RobustScaler** instead of StandardScaler when outliers exist
* Apply **log or power transforms** for skewed data
* Always fit transformations on **training data only**

---

# Text Preprocessing: Tokenization, Stemming, and Lemmatization

Text preprocessing is a crucial step in **Natural Language Processing (NLP)**. Raw text is unstructured and noisy, so we transform it into a clean, standardized format before feeding it into machine learning or deep learning models.

---

## 1. Why Text Preprocessing Is Important

Text data may contain:

* Upper/lowercase inconsistencies
* Punctuation and symbols
* Different word forms (`running`, `ran`, `runs`)
* Stopwords (`is`, `the`, `and`)

Preprocessing helps to:

* Reduce noise
* Reduce vocabulary size
* Improve model accuracy and efficiency

---

## 2. Tokenization

### What Is Tokenization?

**Tokenization** is the process of breaking text into smaller units called **tokens**.

* Tokens can be **words**, **subwords**, or **sentences**

### Example

Sentence:

```
"Text preprocessing is very important!"
```

Tokens:

```
["Text", "preprocessing", "is", "very", "important"]
```

---

### Python Example (Word Tokenization)

```python
import nltk
nltk.download("punkt")

from nltk.tokenize import word_tokenize

text = "Text preprocessing is very important!"
tokens = word_tokenize(text)

print(tokens)
```

**Output**

```text
['Text', 'preprocessing', 'is', 'very', 'important', '!']
```

---

### Sentence Tokenization

```python
from nltk.tokenize import sent_tokenize

text = "NLP is powerful. It is widely used."
sentences = sent_tokenize(text)

print(sentences)
```

**Output**

```text
['NLP is powerful.', 'It is widely used.']
```

---

## 3. Stemming

### What Is Stemming?

**Stemming** reduces words to their **root form** by removing suffixes.

* The result may **not be a real word**
* It is a **rule-based** approach

### Example

| Original | Stem   |
| -------- | ------ |
| running  | run    |
| studies  | studi  |
| better   | better |

---

### Python Example (Porter Stemmer)

```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["running", "runs", "ran", "studies"]
stems = [stemmer.stem(word) for word in words]

print(stems)
```

**Output**

```text
['run', 'run', 'ran', 'studi']
```

---

### Pros and Cons of Stemming

**Pros**

* Fast
* Reduces vocabulary size

**Cons**

* Can produce incorrect or unnatural words
* Loses semantic meaning

---

## 4. Lemmatization

### What Is Lemmatization?

**Lemmatization** reduces words to their **dictionary base form (lemma)**.

* Produces **real words**
* Uses vocabulary and grammar rules
* Slower but more accurate than stemming

### Example

| Original | Lemma |
| -------- | ----- |
| running  | run   |
| better   | good  |
| studies  | study |

---

### Python Example (WordNet Lemmatizer)

```python
import nltk
nltk.download("wordnet")
nltk.download("omw-1.4")

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = ["running", "better", "studies"]
lemmas = [lemmatizer.lemmatize(word) for word in words]

print(lemmas)
```

**Output**

```text
['running', 'better', 'study']
```

> ⚠️ Notice that `"running"` did not change — this is because **lemmatization needs part-of-speech (POS) information**.

---

### Lemmatization with POS Tags (Recommended)

```python
from nltk.corpus import wordnet
from nltk import pos_tag

nltk.download("averaged_perceptron_tagger")

def get_wordnet_pos(tag):
    if tag.startswith("J"):
        return wordnet.ADJ
    elif tag.startswith("V"):
        return wordnet.VERB
    elif tag.startswith("N"):
        return wordnet.NOUN
    elif tag.startswith("R"):
        return wordnet.ADV
    return wordnet.NOUN

sentence = "The children are running faster"
tokens = word_tokenize(sentence)
pos_tags = pos_tag(tokens)

lemmas = [
    lemmatizer.lemmatize(word, get_wordnet_pos(tag))
    for word, tag in pos_tags
]

print(lemmas)
```

**Output**

```text
['The', 'child', 'be', 'run', 'fast']
```

---

## 5. Stemming vs Lemmatization

| Aspect       | Stemming             | Lemmatization    |
| ------------ | -------------------- | ---------------- |
| Speed        | Fast                 | Slower           |
| Output       | May not be real word | Always real word |
| Accuracy     | Lower                | Higher           |
| Uses grammar | ❌ No                 | ✔ Yes            |

---

## 6. Typical NLP Preprocessing Pipeline

```python
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

text = "NLP techniques are improving rapidly!"

# Lowercase
text = text.lower()

# Remove punctuation
text = re.sub(r"[^a-z\s]", "", text)

# Tokenize
tokens = word_tokenize(text)

# Lemmatize
lemmatizer = WordNetLemmatizer()
tokens = [lemmatizer.lemmatize(word) for word in tokens]

print(tokens)
```

**Output**

```text
['nlp', 'technique', 'are', 'improving', 'rapidly']
```

---

## 7. Key Takeaways

* **Tokenization** splits text into meaningful units
* **Stemming** is fast but less accurate
* **Lemmatization** is slower but linguistically correct
* Lemmatization with POS tagging gives the **best results**
* Choose based on **speed vs accuracy requirements**

---

## 8. When to Use What?

* **Search engines** → Stemming
* **Chatbots / NLP understanding** → Lemmatization
* **Deep learning models** → Tokenization + embeddings

---

# Working with Time Series Data

Time series data is a sequence of observations collected **over time**, usually at regular intervals (hourly, daily, monthly, etc.). Examples include stock prices, weather data, website traffic, and sensor readings.

---

## 1. What Is Time Series Data?

A dataset is considered a **time series** when:

* Observations are **time-ordered**
* Time dependency matters
* Past values influence future values

### Example

| Date       | Sales |
| ---------- | ----- |
| 2024-01-01 | 120   |
| 2024-01-02 | 135   |
| 2024-01-03 | 128   |

---

## 2. Key Characteristics of Time Series

### A. Trend

Long-term increase or decrease.

📈 Example: steadily increasing sales

---

### B. Seasonality

Repeating patterns at fixed intervals.

📅 Example: higher sales every December

---

### C. Cyclic Patterns

Irregular fluctuations over long periods.

📉 Example: economic cycles

---

### D. Noise

Random variation not explained by the model.

---

## 3. Loading and Preparing Time Series Data

### Python Example (Using Pandas)

```python
import pandas as pd

# Create a time series dataset
data = {
    "date": pd.date_range(start="2024-01-01", periods=7, freq="D"),
    "sales": [120, 135, 128, 140, 150, 160, 155]
}

df = pd.DataFrame(data)
df.set_index("date", inplace=True)

print(df)
```

---

## 4. DateTime Handling

### Converting to DateTime

```python
df.index = pd.to_datetime(df.index)
```

### Extracting Time Features

```python
df["day"] = df.index.day
df["month"] = df.index.month
df["weekday"] = df.index.weekday
```

✔ Useful for ML models that don’t natively handle time

---

## 5. Resampling Time Series

Change the frequency of data.

### Downsampling (Daily → Monthly)

```python
monthly_sales = df.resample("M").mean()
```

### Upsampling (Daily → Hourly)

```python
hourly_sales = df.resample("H").ffill()
```

---

## 6. Rolling Statistics (Smoothing)

Used to reduce noise and reveal trends.

### Moving Average

```python
df["rolling_mean"] = df["sales"].rolling(window=3).mean()
```

### Rolling Standard Deviation

```python
df["rolling_std"] = df["sales"].rolling(window=3).std()
```

---

## 7. Handling Missing Values

### Detect Missing Data

```python
df.isna().sum()
```

### Fill Missing Values

```python
df["sales"].fillna(method="ffill", inplace=True)
df["sales"].fillna(method="bfill", inplace=True)
```

---

## 8. Time Series Decomposition

Break a series into:

* Trend
* Seasonality
* Residuals

```python
from statsmodels.tsa.seasonal import seasonal_decompose

decomposition = seasonal_decompose(df["sales"], model="additive", period=3)
```

---

## 9. Stationarity (Very Important)

Many time series models require **stationary data**:

* Mean is constant
* Variance is constant
* No trend or seasonality

### Augmented Dickey-Fuller (ADF) Test

```python
from statsmodels.tsa.stattools import adfuller

result = adfuller(df["sales"])
print("ADF Statistic:", result[0])
print("p-value:", result[1])
```

✔ p-value < 0.05 → stationary
❌ p-value ≥ 0.05 → non-stationary

---

## 10. Making a Series Stationary

### Differencing

```python
df["sales_diff"] = df["sales"].diff()
```

### Log Transformation

```python
import numpy as np
df["sales_log"] = np.log(df["sales"])
```

---

## 11. Train-Test Split for Time Series

❌ Never shuffle time series data

### Correct Way

```python
train = df.iloc[:-2]
test = df.iloc[-2:]
```

---

## 12. Simple Forecasting Models

### A. Naive Forecast

```python
df["naive_forecast"] = df["sales"].shift(1)
```

---

### B. ARIMA Model

```python
from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(train["sales"], order=(1, 1, 1))
model_fit = model.fit()

forecast = model_fit.forecast(steps=len(test))
print(forecast)
```

---

## 13. Feature Engineering for ML Models

```python
df["lag_1"] = df["sales"].shift(1)
df["lag_7"] = df["sales"].shift(7)
```

✔ Enables use of regression & ML models

---

## 14. Common Time Series Models

| Model                 | Use Case                       |
| --------------------- | ------------------------------ |
| ARIMA                 | Trend-based forecasting        |
| SARIMA                | Seasonal data                  |
| Exponential Smoothing | Short-term forecasting         |
| Prophet               | Business time series           |
| LSTM                  | Complex long-term dependencies |

---

## 15. Best Practices

✔ Keep data time-ordered
✔ Handle missing timestamps
✔ Check stationarity
✔ Use rolling statistics
✔ Avoid data leakage

---

## 16. Summary

* Time series data depends on time order
* Trends and seasonality must be handled explicitly
* Stationarity is key for classical models
* Feature engineering enables ML models
* Never shuffle time series data

---