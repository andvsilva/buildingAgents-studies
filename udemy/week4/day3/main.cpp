#include <cstdio>
#include <chrono>

int main() {
    using namespace std;

    const unsigned int iterations = 200000000;
    const double param1 = 4.0;
    const double param2 = 1.0;

    auto t_start = chrono::high_resolution_clock::now();

    double result = 1.0;
    double ip = param1; // i = 1 -> i*param1

    for (unsigned int i = 1; i <= iterations; ++i) {
        double j = ip - param2;
        result -= 1.0 / j;
        j = ip + param2;
        result += 1.0 / j;
        ip += param1;
    }

    result *= 4.0;

    auto t_end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = t_end - t_start;

    printf("Result: %.12f\n", result);
    printf("Execution Time: %.6f seconds\n", elapsed.count());

    return 0;
}