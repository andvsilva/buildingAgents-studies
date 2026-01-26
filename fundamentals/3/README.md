# Machine Learning

**Machine Learning (ML)** is a field of Artificial Intelligence focused on building systems that **learn patterns from data** and make **predictions or decisions** without being explicitly programmed for every rule.

## Core idea
> Instead of writing rules → you provide **data + an objective**, and the algorithm learns by itself.

---

## Main Types of Machine Learning

### 1️⃣ Supervised Learning
Uses **labeled data** (input + correct output).

**Examples:**
- Classification: spam vs. not spam  
- Regression: predicting house prices  

**Common algorithms:**
- Linear / Logistic Regression  
- Decision Trees  
- Random Forest  
- SVM  
- k-NN  
- Neural Networks  

---

### 2️⃣ Unsupervised Learning
Works with **unlabeled data**, discovering hidden patterns.

**Examples:**
- Customer segmentation  
- Product clustering  

**Common algorithms:**
- K-Means  
- Hierarchical Clustering  
- DBSCAN  
- PCA (dimensionality reduction)

---

### 3️⃣ Semi-Supervised Learning
Combines a small amount of labeled data with a large amount of unlabeled data.  
Useful when labeling data is expensive.

---

### 4️⃣ Reinforcement Learning
An agent learns through **trial and error**, receiving rewards from the environment.

**Examples:**
- Games (AlphaGo)  
- Robotics  
- Dynamic recommendation systems  

**Key concepts:**
- Agent  
- Environment  
- Action  
- Reward  

---

## Typical Machine Learning Pipeline

1. Data collection  
2. Data cleaning & preprocessing  
   - Normalization  
   - Outlier handling  
   - Feature engineering  
3. Data splitting  
   - Training / Validation / Test  
4. Model training  
5. Evaluation  
   - Accuracy, Precision, Recall, F1-score, RMSE, etc.  
6. Deployment & monitoring  

---

## Simple Python Example (scikit-learn)

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data
X, y = load_iris(return_X_y=True)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
```

## Where Machine Learning Is Used

📊 Data & Analytics

💳 Fraud detection

🛒 Recommendation systems (Netflix, Amazon)

🏥 Healthcare (diagnostics)

🧠 NLP (chatbots, LLMs)

👁️ Computer Vision

## Supervised vs. Unsupervised Learning

Machine Learning algorithms can be broadly categorized into **Supervised** and **Unsupervised** learning, depending on whether labeled data is available during training.

---

### Supervised Learning

**Supervised learning** uses **labeled datasets**, where each data point includes:
- Input features (**X**)
- A known target or label (**y**)

The model learns a direct relationship between inputs and outputs.

#### Common tasks
- **Classification**: Predicting categories
- **Regression**: Predicting continuous values

#### Examples
- Spam detection (spam / not spam)
- Credit risk assessment
- House price prediction
- Medical diagnosis

#### Common algorithms
- Linear Regression  
- Logistic Regression  
- Decision Trees  
- Random Forest  
- Support Vector Machines (SVM)  
- k-Nearest Neighbors (k-NN)  
- Neural Networks  

#### Key characteristics
- Requires labeled data
- Easier to evaluate with metrics (Accuracy, Precision, RMSE, etc.)
- High performance when quality labels are available

---

### Unsupervised Learning

**Unsupervised learning** works with **unlabeled data** and focuses on discovering hidden patterns or structures without predefined outputs.

#### Common tasks
- **Clustering**: Grouping similar data points
- **Dimensionality Reduction**: Reducing feature space
- **Anomaly Detection**: Identifying unusual behavior

#### Examples
- Customer segmentation
- Product grouping
- Fraud or anomaly detection
- Topic modeling in text data

#### Common algorithms
- K-Means  
- Hierarchical Clustering  
- DBSCAN  
- Gaussian Mixture Models (GMM)  
- Principal Component Analysis (PCA)  
- Autoencoders  

#### Key characteristics
- No labeled data required
- Harder to evaluate quantitatively
- Excellent for exploratory data analysis

---

### Comparison Summary

| Aspect | Supervised Learning | Unsupervised Learning |
|------|-------------------|----------------------|
| Data | Labeled | Unlabeled |
| Objective | Predict outcomes | Discover patterns |
| Output | Known targets | Clusters or structures |
| Evaluation | Straightforward | Often subjective |
| Use cases | Prediction & classification | Exploration & segmentation |

---

### When to Use Each Approach

- **Supervised Learning**:  
  Use when labeled data is available and prediction accuracy is important.

- **Unsupervised Learning**:  
  Use when labels are unavailable and the goal is to explore or understand data structure.


✔ Same unit as target variable.

---

#### R² Score (Coefficient of Determination)

Measures how much variance is explained by the model.

✔ Higher is better (max = 1).

---

### Clustering Metrics (Unsupervised)

- **Silhouette Score**
- **Davies–Bouldin Index**
- **Calinski–Harabasz Index**

✔ Used when no labels are available.

---

## Choosing the Right Metric

- **Imbalanced classification** → Precision, Recall, F1, ROC-AUC
- **Regression problems** → MAE, RMSE, R²
- **Business-critical decisions** → Align metric with cost of errors
- **Exploratory analysis** → Clustering scores + domain interpretation

---

## Best Practices

- Always evaluate on **unseen data**
- Use **cross-validation** when data is limited
- Compare models using **multiple metrics**
- Monitor performance after deployment (data drift, concept drift)



## Cross-Validation and Hyperparameter Tuning

To build robust machine learning models that generalize well to unseen data, it is essential to use **cross-validation** and **hyperparameter tuning**.

---

## Cross-Validation

**Cross-validation (CV)** is a technique used to evaluate a model’s performance by splitting the dataset into multiple training and validation subsets.

### Why use cross-validation?

- Reduces overfitting
- Provides a more reliable performance estimate
- Makes better use of limited data
- Helps compare models fairly

---

### k-Fold Cross-Validation

The most common approach is **k-fold cross-validation**:

1. Split the dataset into *k* equal folds
2. Train the model on *k − 1* folds
3. Validate it on the remaining fold
4. Repeat the process *k* times
5. Average the results

✔ Typical values: `k = 5` or `k = 10`

---

### Cross-Validation Variants

- **Stratified k-Fold**  
  Preserves class distribution (recommended for classification)

- **Time Series Cross-Validation**  
  Respects temporal order (used for time series data)

- **Leave-One-Out (LOOCV)**  
  Uses one sample for validation at a time (computationally expensive)

---

### Example: Cross-Validation in Python

```python
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

model = RandomForestClassifier(random_state=42)

scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")

print("CV Accuracy:", scores.mean())
````

---

## Hyperparameter Tuning

**Hyperparameters** are configuration values set *before* training (e.g., learning rate, number of trees).
They are not learned from data but strongly affect model performance.

### Examples of hyperparameters

* Number of estimators (`n_estimators`)
* Maximum tree depth (`max_depth`)
* Learning rate (`learning_rate`)
* Regularization strength (`C`, `alpha`)

---

## Hyperparameter Tuning Techniques

### Grid Search

Tries **all possible combinations** of hyperparameters.

✔ Exhaustive but computationally expensive.

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 5, 10]
}

grid = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring="accuracy"
)

grid.fit(X, y)

print("Best params:", grid.best_params_)
print("Best score:", grid.best_score_)
```

---

### Random Search

Samples **random combinations** of hyperparameters.

✔ Faster and often nearly as effective as grid search.

---

### Bayesian Optimization

Uses previous results to choose the next best set of hyperparameters.

✔ More efficient for large search spaces.

Popular libraries:

* Optuna
* Hyperopt
* scikit-optimize

---

## Cross-Validation + Hyperparameter Tuning

Hyperparameter tuning should **always be combined with cross-validation** to avoid overfitting to a single validation set.

✔ Best practice:

* Use cross-validation inside GridSearch / RandomSearch
* Evaluate final performance on a **separate test set**

---

## Best Practices

* Start with simple models and defaults
* Tune only the most impactful hyperparameters
* Use stratified CV for classification
* Avoid data leakage at all costs
* Balance performance gains vs. computational cost

---

## Summary

| Concept               | Purpose                         |
| --------------------- | ------------------------------- |
| Cross-Validation      | Reliable performance estimation |
| Hyperparameter Tuning | Optimize model configuration    |
| Grid Search           | Exhaustive tuning               |
| Random Search         | Efficient tuning                |
| Bayesian Optimization | Intelligent tuning              |


🚀

## Regression, Classification, and Clustering Models

Machine learning models can be grouped by the type of problem they are designed to solve. The three most common categories are **Regression**, **Classification**, and **Clustering**.

---

## Regression Models

**Regression** models are used to predict **continuous numerical values**.

### Typical use cases
- House price prediction
- Sales forecasting
- Demand estimation
- Financial risk modeling

### Common regression algorithms
- Linear Regression  
- Ridge Regression  
- Lasso Regression  
- Elastic Net  
- Decision Tree Regressor  
- Random Forest Regressor  
- Gradient Boosting Regressor  
- Support Vector Regression (SVR)

### Example targets
- Price
- Revenue
- Temperature
- Time-to-event

### Common evaluation metrics
- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

## Classification Models

**Classification** models predict **discrete class labels**.

### Typical use cases
- Spam detection
- Fraud detection
- Customer churn prediction
- Medical diagnosis

### Common classification algorithms
- Logistic Regression  
- Decision Trees  
- Random Forest  
- Gradient Boosting (XGBoost, LightGBM)  
- Support Vector Machines (SVM)  
- k-Nearest Neighbors (k-NN)  
- Naive Bayes  
- Neural Networks  

### Classification types
- **Binary classification** (e.g., yes / no)
- **Multiclass classification** (e.g., categories)
- **Multilabel classification** (e.g., multiple tags)

### Common evaluation metrics
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

---

## Clustering Models

**Clustering** is an **unsupervised learning** technique that groups similar data points without labeled outputs.

### Typical use cases
- Customer segmentation
- Market basket analysis
- Anomaly detection
- Document and topic grouping

### Common clustering algorithms
- K-Means  
- Hierarchical Clustering  
- DBSCAN  
- Gaussian Mixture Models (GMM)  
- Mean Shift  

### Key characteristics
- No labeled data required
- Results depend on distance metrics and data scaling
- Often used for exploratory data analysis

### Common evaluation metrics
- Silhouette Score
- Davies–Bouldin Index
- Calinski–Harabasz Index

---

## Comparison Summary

| Model Type | Learning Type | Output | Typical Use |
|----------|--------------|--------|-------------|
| Regression | Supervised | Continuous values | Prediction |
| Classification | Supervised | Discrete classes | Decision making |
| Clustering | Unsupervised | Groups / clusters | Pattern discovery |

---

## Choosing the Right Model

- Use **regression** when predicting numerical values
- Use **classification** when predicting categories or labels
- Use **clustering** when exploring data without labels

🚀
---

## 1. Decision Trees 🌳

**What it is**
A tree-structured model that splits data using feature-based rules until it reaches a prediction.

**How it works**
At each node, the algorithm chooses a feature and a threshold that best separates the data (using metrics like **Gini impurity** or **Entropy**).

**Pros**

* Very easy to understand and interpret
* Works with numerical and categorical data
* No need for feature scaling

**Cons**

* Prone to **overfitting**
* Small data changes can drastically change the tree

**Best used when**

* Interpretability matters
* You want quick baseline models

**Example**

```text
if age < 30:
    predict "No Loan"
else:
    predict "Loan"
```

---

## 2. Support Vector Machines (SVM) ⚖️

**What it is**
A powerful classifier that finds the **optimal separating hyperplane** between classes.

**How it works**
Maximizes the **margin** between classes. With **kernels**, it can model nonlinear boundaries.

**Pros**

* Excellent performance on high-dimensional data
* Effective when classes are well-separated

**Cons**

* Computationally expensive for large datasets
* Sensitive to kernel and hyperparameter choice

**Best used when**

* Dataset is medium-sized
* Clear class separation exists

**Common kernels**

* Linear
* Polynomial
* RBF (Gaussian)

---

## 3. K-Nearest Neighbors (KNN) 📍

**What it is**
A **lazy learning** algorithm that predicts based on the closest data points.

**How it works**
Looks at the *k* nearest neighbors (using distance metrics like Euclidean) and uses majority voting (classification) or averaging (regression).

**Pros**

* Simple and intuitive
* No training phase

**Cons**

* Slow at prediction time
* Sensitive to noise and feature scaling

**Best used when**

* Dataset is small
* Decision boundaries are irregular

**Key hyperparameter**

* `k` (number of neighbors)

---

## 4. Random Forests 🌲🌲🌲

**What it is**
An **ensemble** of decision trees trained on random subsets of data and features.

**How it works**
Each tree votes, and the final prediction is the majority vote (classification) or average (regression).

**Pros**

* Reduces overfitting
* High accuracy
* Handles missing values and noise well

**Cons**

* Less interpretable than a single tree
* Larger models, more memory usage

**Best used when**

* You want strong performance with minimal tuning
* Data is noisy or complex

---

## Quick Comparison ⚡

| Model         | Interpretable | Needs Scaling | Handles Nonlinearity | Speed             |
| ------------- | ------------- | ------------- | -------------------- | ----------------- |
| Decision Tree | ✅ High        | ❌ No          | ✅ Yes                | Fast              |
| SVM           | ❌ Low         | ✅ Yes         | ✅ Yes (kernels)      | Medium            |
| KNN           | ⚠️ Medium     | ✅ Yes         | ✅ Yes                | Slow (prediction) |
| Random Forest | ⚠️ Medium     | ❌ No          | ✅ Yes                | Fast              |

---


# Bias–Variance Tradeoff and Overfitting

## 1. Theory

### Bias

**Bias** measures how far the *average prediction* of a model is from the true underlying function.

* Caused by **over-simplifying assumptions**
* High bias → model is **too simple**
* Leads to **underfitting**

---

### Variance

**Variance** measures how sensitive a model is to changes in the training data.

* Caused by **high model complexity**
* High variance → model is **too flexible**
* Leads to **overfitting**

---

### Bias–Variance Tradeoff

Model complexity controls bias and variance in opposite directions:

* Increasing complexity → **bias decreases**, **variance increases**
* Decreasing complexity → **bias increases**, **variance decreases**

The objective is to find a model that **generalizes well** by balancing both.

---

## 2. Error Decomposition

For a regression problem, the expected prediction error at a point ( x ) can be decomposed as:

$$
\mathbb{E}\big[(y - \hat{f}(x))^2\big]
= $$
$$
\underbrace{\text{Bias}^2}_{\text{systematic error}}
+
\underbrace{\text{Variance}}_{\text{model sensitivity}}
+
\underbrace{\sigma^2}_{\text{irreducible noise}}
$$


Where:

* **Bias²**: error due to incorrect assumptions
* **Variance**: error due to fluctuations in training data
* **Noise** ( \sigma^2 ): inherent randomness in the data

---

## 3. Overfitting and Underfitting

### Overfitting

A model is **overfitting** when:

* Training error is **very low**
* Test/validation error is **high**

This indicates **low bias and high variance**.

---

### Underfitting

A model is **underfitting** when:

* Training error is **high**
* Test/validation error is **high**

This indicates **high bias and low variance**.

---

## 4. Example: Polynomial Regression

### True Data-Generating Process

Assume the true relationship is:

$$
y = x^2 + \epsilon,
\quad \epsilon \sim \mathcal{N}(0, \sigma^2)
$$

A small dataset is sampled from this process.

---

### Case 1: Linear Model (Underfitting)

$$
\hat{y} = ax + b
$$


* Cannot represent curvature
* Strong model assumption

**Analysis**

* Bias: **high**
* Variance: **low**
* Training error: high
* Test error: high

---

### Case 2: Quadratic Model (Good Fit)

$$
\hat{y} = ax^2 + bx + c
$$


* Matches the true structure
* Captures signal without noise

**Analysis**

* Bias: low
* Variance: moderate
* Training error: low
* Test error: low

---

### Case 3: High-Degree Polynomial (Overfitting)

$$
\hat{y} = a_7 x^7 + a_6 x^6 + \cdots + a_0
$$


* Fits almost all training points exactly
* Learns noise

**Analysis**

* Bias: very low
* Variance: **high**
* Training error: (\approx 0)
* Test error: high

---

## 5. Learning Curves

### High Bias Model

* Training error: high
* Validation error: high
* Gap between errors: small

### High Variance Model

* Training error: very low
* Validation error: high
* Gap between errors: large

---

## 6. Role of Regularization

Regularization penalizes model complexity:

$$
\mathcal{L}(\theta) = \text{Loss}(\theta) + \lambda \lVert \theta \rVert^2
$$

* Reduces variance
* Slightly increases bias
* Improves generalization

---

## 7. Summary

* **Bias** → error from oversimplification
* **Variance** → error from over-complexity
* **Overfitting** → low bias, high variance
* **Underfitting** → high bias, low variance
* **Best model** → minimizes **generalization error**, not training error

---

# Scikit-learn Pipelines and Model Evaluation

## 1. Motivation

In a typical machine learning workflow, we apply multiple steps:

* Data preprocessing (scaling, encoding, imputation)
* Feature engineering
* Model training
* Model evaluation

If these steps are not handled carefully, we risk:

* **Data leakage**
* Inconsistent preprocessing between train and test data
* Hard-to-reproduce experiments

**Scikit-learn Pipelines** solve these problems by chaining steps into a single, unified object.

---

## 2. What Is a Pipeline?

A **Pipeline** is a sequence of transformations ending with an estimator.

[
X \xrightarrow{\text{Transform}_1} X_1 \xrightarrow{\text{Transform}_2} X_2 \xrightarrow{\text{Model}} \hat{y}
]

In scikit-learn:

```python
from sklearn.pipeline import Pipeline
```

Each step must be:

* A **transformer** (`fit`, `transform`)
* Except the last step, which is an **estimator** (`fit`, `predict`)

---

## 3. Example: Classification Pipeline

### Problem

Binary classification with features on different scales.

### Steps

1. Standardize features
2. Train a logistic regression model

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline(steps=[
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])
```

### Training

```python
pipeline.fit(X_train, y_train)
```

### Prediction

```python
y_pred = pipeline.predict(X_test)
```

**Key point:**
The scaler is fitted **only on the training data**, preventing data leakage.

---

## 4. Pipelines and Cross-Validation

### Why This Matters

Without a pipeline, scaling might be applied **before** cross-validation, leaking information from validation folds.

With a pipeline:

[
\text{CV Error} = \frac{1}{k} \sum_{i=1}^{k} \mathcal{L}
\big(y^{(i)}, \hat{y}^{(i)}\big)
]

Each fold:

* Fits preprocessing **only on its training split**
* Evaluates on unseen validation data

### Example

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(
    pipeline,
    X,
    y,
    cv=5,
    scoring="accuracy"
)

scores.mean()
```

---

## 5. Model Evaluation Metrics

### Classification Metrics

| Metric    | Formula                | When to Use            |
| --------- | ---------------------- | ---------------------- |
| Accuracy  | ( \frac{TP + TN}{N} )  | Balanced classes       |
| Precision | ( \frac{TP}{TP + FP} ) | Costly false positives |
| Recall    | ( \frac{TP}{TP + FN} ) | Costly false negatives |
| F1-score  | ( 2\frac{PR}{P+R} )    | Imbalanced data        |

---

### Regression Metrics

| Metric | Formula                           | Interpretation         |   |                    |
| ------ | --------------------------------- | ---------------------- | - | ------------------ |
| MSE    | ( \frac{1}{n}\sum (y-\hat{y})^2 ) | Penalizes large errors |   |                    |
| RMSE   | ( \sqrt{\text{MSE}} )             | Same units as target   |   |                    |
| MAE    | ( \frac{1}{n}\sum                 | y-\hat{y}              | ) | Robust to outliers |
| (R^2)  | (1 - \frac{SS_{res}}{SS_{tot}})   | Variance explained     |   |                    |

---

## 6. Example: Regression Pipeline with Evaluation

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", Ridge(alpha=1.0))
])

scores = cross_val_score(
    pipeline,
    X,
    y,
    cv=5,
    scoring="neg_mean_squared_error"
)

rmse = (-scores.mean()) ** 0.5
rmse
```

---

## 7. Pipelines + Hyperparameter Tuning

Hyperparameters are accessed using:

```
<step_name>__<parameter_name>
```

### Example: Grid Search

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    "model__alpha": [0.01, 0.1, 1, 10]
}

grid = GridSearchCV(
    pipeline,
    param_grid,
    cv=5,
    scoring="neg_mean_squared_error"
)

grid.fit(X_train, y_train)

grid.best_params_
```

**All preprocessing is safely included inside cross-validation.**

---

## 8. ColumnTransformer (Mixed Data Types)

For datasets with numerical and categorical features:

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), num_features),
        ("cat", OneHotEncoder(), cat_features)
    ]
)

pipeline = Pipeline([
    ("preprocess", preprocessor),
    ("model", LogisticRegression())
])
```

---

## 9. Common Evaluation Pitfalls

* Evaluating on training data
* Preprocessing outside cross-validation
* Using accuracy on imbalanced datasets
* Ignoring variance across folds

---

## 10. Summary

* **Pipelines** ensure correctness, reproducibility, and safety
* They prevent **data leakage**
* They integrate seamlessly with:

  * Cross-validation
  * Grid search
  * Model evaluation
* Proper evaluation focuses on **generalization**, not training performance

---