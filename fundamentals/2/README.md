
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

--- 🚀
