def main():
    print("=== Сумма целых чисел от A до B ===\n")
    a = int(input("Введите целое число A: "))
    b = int(input("Введите целое число B (должно быть больше A): "))

    if a >= b:
        print("Ошибка: число A должно быть строго меньше числа B!")
        return

    total_sum = 0
    for number in range(a, b + 1):
        total_sum += number

    print(f"\nСумма всех целых чисел от {a} до {b} включительно = {total_sum}")

if __name__ == "__main__":
    main()