import math

def compute_cos_series(x, epsilon):
    series_sum = 0.0
    term = 1.0
    n = 0
    while abs(term) > epsilon:
        series_sum += term
        term = term * (-x * x) / ((2 * n + 1) * (2 * n + 2))
        n += 1
    return series_sum, n

def main():
    print("=== Вычисление cos(x) через ряд Тейлора ===\n")
    try:
        x = float(input("Введите значение аргумента x: "))
        epsilon = float(input("Введите точность вычислений ε (например, 0.0001): "))
    except ValueError:
        print("Ошибка: нужно вводить числа!")
        return

    if epsilon <= 0:
        print("Ошибка: точность должна быть положительным числом!")
        return

    exact_value = math.cos(x)
    series_value, iterations = compute_cos_series(x, epsilon)

    print(f"\n--- Результаты для x = {x}, ε = {epsilon} ---")
    print(f"Точное значение cos(x)  : {exact_value:.10f}")
    print(f"Значение через ряд      : {series_value:.10f}")
    print(f"Абсолютная погрешность  : {abs(exact_value - series_value):.2e}")
    print(f"Число итераций (n)      : {iterations}")

    print("\n=== Испытание на сходимость при разных x ===")
    print(f"{'x':>8} | {'cos(x) точное':>14} | {'через ряд':>14} | {'погрешность':>12} | {'итераций':>8}")
    print("-" * 70)

    test_values = [0.0, 0.5, 1.0, 2.0, 3.0, 5.0, 10.0]
    for test_x in test_values:
        val, iters = compute_cos_series(test_x, epsilon)
        exact = math.cos(test_x)
        error = abs(exact - val)
        print(f"{test_x:>8.2f} | {exact:>14.10f} | {val:>14.10f} | {error:>12.2e} | {iters:>8}")

if __name__ == "__main__":
    main()