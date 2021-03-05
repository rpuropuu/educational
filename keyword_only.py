def total(initial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(initial)
    print(count)


total(13, 1, 2, 3, 4, extra_number=50)
total(20, 1, 2, 3, extra_number=30)
