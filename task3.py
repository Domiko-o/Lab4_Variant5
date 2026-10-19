def minutes_to_time(total_minutes):
    """Переводит общее количество минут в формат ЧЧ:ММ"""
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"{hours:02d}:{minutes:02d}"


def time_to_minutes(time_str):
    """Переводит строку времени 'ЧЧ:ММ' в общее количество минут"""
    parts = time_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    return hours * 60 + minutes


def main():
    print("=== Составление расписания автобусного маршрута ===\n")

    start_time_str = input("Время начала работы маршрута: ")
    end_time_str = input("Время окончания работы маршрута: ")
    route_time = int(input("Протяжённость маршрута в минутах (в один конец): "))
    rest_time = int(input("Время отдыха на конечных остановках (в минутах): "))

    start_time = time_to_minutes(start_time_str)
    end_time = time_to_minutes(end_time_str)

    print("\n--- Суточное расписание отправления ---")

    current_time = start_time
    trip_number = 1

    while current_time < end_time:
        print(f"Рейс {trip_number}: Отправление от пункта А в {minutes_to_time(current_time)}")

        departure_B = current_time + route_time + rest_time

        print(f"         -> Отправление от пункта В в {minutes_to_time(departure_B)}")

        current_time = departure_B + route_time + rest_time
        trip_number += 1

    print("\nРасписание составлено.")


if __name__ == "__main__":
    main()