def reverse_numbers(start, end):
    for num in range(end, start - 1, -1):
        print(num)


start = 101
end = 10000
reverse_numbers(start, end)