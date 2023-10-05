def table(num):
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")

for num in range(51, 61):
    print(f"Table for {num}:")
    table(num)
    print()
