while True:
    bok_kwadratu = input("Podaj bok kwadratu a ja policze jego pole: ")

    try:
        bok_kwadratu = int(bok_kwadratu)
        if bok_kwadratu > 0:
            pole_kwadratu = bok_kwadratu ** 2
            print(f"Pole kwadratu wynosi {pole_kwadratu}.")
            break

        else:
            print('Podałeś liczbę mniejsza od zera. Bok nie może być liczbą ujemną!')

    except ValueError:
        print("Podaj prawdidłową liczbę!")

