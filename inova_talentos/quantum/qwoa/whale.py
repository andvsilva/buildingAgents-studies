'''
Quantum Whale Optimization Algorithm (QWOA)

'''

import numpy as np

# ----------------------------------------
# Objective function (example: Sphere)
# ----------------------------------------
def objective_function(x):
    return np.sum(x**2)


# ----------------------------------------
# Initialize quantum population
# Each whale is represented by probability amplitudes
# ----------------------------------------
def initialize_population(n_whales, dimension):
    population = np.random.rand(n_whales, dimension)
    return population


# ----------------------------------------
# Quantum measurement
# Collapse quantum amplitudes into classical solution
# ----------------------------------------
def quantum_measurement(q_state, lower_bound, upper_bound):
    return lower_bound + (upper_bound - lower_bound) * q_state


# ----------------------------------------
# QWOA main algorithm
# ----------------------------------------
def QWOA(objective, dim, n_whales=20, max_iter=100, lower_bound=-10, upper_bound=10):

    # Initialize quantum population
    q_population = initialize_population(n_whales, dim)

    # Evaluate classical solutions
    population = np.array([
        quantum_measurement(q_population[i], lower_bound, upper_bound)
        for i in range(n_whales)
    ])

    fitness = np.array([objective(x) for x in population])

    best_idx = np.argmin(fitness)
    best_solution = population[best_idx]
    best_score = fitness[best_idx]

    for t in range(max_iter):

        a = 2 - t * (2 / max_iter)

        for i in range(n_whales):

            r1 = np.random.rand()
            r2 = np.random.rand()

            A = 2 * a * r1 - a
            C = 2 * r2
            p = np.random.rand()

            if p < 0.5:

                if abs(A) < 1:

                    # Encircling best solution
                    D = abs(C * best_solution - population[i])
                    new_position = best_solution - A * D

                else:

                    # Search random whale
                    rand_index = np.random.randint(n_whales)
                    X_rand = population[rand_index]
                    D = abs(C * X_rand - population[i])
                    new_position = X_rand - A * D

            else:

                # Spiral updating
                b = 1
                l = np.random.uniform(-1, 1)

                D = abs(best_solution - population[i])
                new_position = (
                    D * np.exp(b * l) * np.cos(2 * np.pi * l)
                    + best_solution
                )

            # Normalize back to quantum state
            q_population[i] = (new_position - lower_bound) / (upper_bound - lower_bound)

            q_population[i] = np.clip(q_population[i], 0, 1)

            population[i] = quantum_measurement(q_population[i], lower_bound, upper_bound)

        fitness = np.array([objective(x) for x in population])

        best_idx = np.argmin(fitness)

        if fitness[best_idx] < best_score:
            best_score = fitness[best_idx]
            best_solution = population[best_idx]

    return best_solution, best_score


# ----------------------------------------
# Run example
# ----------------------------------------

dimension = 5

best_solution, best_score = QWOA(
    objective_function,
    dim=dimension,
    n_whales=30,
    max_iter=200
)

print("Best solution found:")
print(best_solution)

print("\nBest objective value:")
print(best_score)