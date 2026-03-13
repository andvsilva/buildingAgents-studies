
---

# Quantum Whale Optimization Algorithm (QWOA) — Code Explanation

## Overview

The **Quantum Whale Optimization Algorithm (QWOA)** is a **quantum-inspired metaheuristic optimization algorithm** derived from the classical **Whale Optimization Algorithm (WOA)** proposed by Seyedali Mirjalili.

The algorithm simulates the **bubble-net hunting behavior of humpback whales** while incorporating **quantum-inspired representations** of candidate solutions. Instead of representing solutions as deterministic vectors, the algorithm uses **probability amplitudes**, which are later transformed into classical values through a measurement process.

The Python implementation demonstrates how QWOA can be used to **minimize a mathematical objective function**.

---

# Structure of the Code

The program is composed of five main components:

1. Objective function
2. Population initialization
3. Quantum measurement
4. Optimization loop (QWOA dynamics)
5. Execution and result output

---

# 1. Objective Function

The algorithm optimizes a mathematical function called the **objective function**.

```python
def objective_function(x):
    return np.sum(x**2)
```

This example uses the **Sphere function**, a common benchmark in optimization problems:

$$
f(x) = \sum_{i=1}^{n} x_i^2
$$

The global minimum occurs at

$$
x = 0
$$

This function is used only to **demonstrate the optimization process**.

---

# 2. Population Initialization

The algorithm begins by generating an initial population of whales:

```python
def initialize_population(n_whales, dimension):
    population = np.random.rand(n_whales, dimension)
```

Each whale represents a **candidate solution** in the search space.

In QWOA, the population is stored as **quantum probability states**:

$$
q_i \in [0,1]^d
$$

where

* (n) = number of whales
* (d) = dimension of the problem

These probability values represent **quantum amplitudes** that will later be measured.

---

# 3. Quantum Measurement

Before evaluating the objective function, the quantum state must be converted into a classical solution:

```python
def quantum_measurement(q_state, lower_bound, upper_bound):
    return lower_bound + (upper_bound - lower_bound) * q_state
```

This operation simulates a **quantum measurement**.

Mathematically, the transformation is

$$
x = x_{min} + (x_{max}-x_{min})q
$$

where

* (q) is the probability amplitude
* (x) is the classical variable

This maps the quantum state into the **search space interval**.

---

# 4. Optimization Process

The main optimization routine is implemented in the function `QWOA`.

The algorithm iteratively updates whale positions using three main mechanisms.

---

## Encircling the Best Solution

When the algorithm identifies the best candidate solution, other whales move toward it:

$$
D = |C \cdot X^* - X|
$$

$$
X(t+1) = X^* - A \cdot D
$$

where

* (X^*) = best solution found so far
* (A) and (C) = random coefficient vectors

This mechanism represents whales **encircling their prey**.

---

## Exploration Phase

When

$$
|A| > 1
$$

the algorithm selects a **random whale** and moves toward it.

This increases **exploration** of the search space and helps avoid **local minima**.

---

## Spiral Bubble-Net Attack

The spiral model simulates the **bubble-net feeding strategy**:

$$
X(t+1) =
D e^{bl}\cos(2\pi l) + X^*
$$

where

* (b) controls the spiral shape
* (l) is a random number in ([-1,1])

This step balances **exploitation around the best solution**.

---

# 5. Quantum Update

After computing a new classical position, it is converted back into a **quantum probability state**:

```python
q_population[i] = (new_position - lower_bound) / (upper_bound - lower_bound)
```

The values are clipped to remain inside the interval:

```python
q_population[i] = np.clip(q_population[i], 0, 1)
```

This ensures the representation remains a valid **quantum-inspired state**.

---

# 6. Fitness Evaluation

Each whale's solution is evaluated using the objective function:

```python
fitness = np.array([objective(x) for x in population])
```

The algorithm then updates the **best solution found so far**.

---

# 7. Final Output

After the optimization loop finishes, the algorithm returns

* the **best solution vector**
* the **best objective value**

```python
print("Best solution found:")
print(best_solution)

print("Best objective value:")
print(best_score)
```

---

# Summary

The QWOA implementation follows these steps:

1. Initialize a quantum-inspired population
2. Convert quantum states into classical solutions
3. Evaluate the objective function
4. Update whale positions using encircling, exploration, and spiral strategies
5. Convert new solutions back into quantum states
6. Repeat until convergence

---

# Applications of QWOA

The Quantum Whale Optimization Algorithm can be applied to several optimization problems, including:

* combinatorial optimization
* feature selection in machine learning
* engineering design optimization
* hyperparameter tuning
* quantum circuit parameter optimization

---

If you'd like, I can also provide a **README.md version of this explanation** (clean and ready to place in a GitHub repository).
