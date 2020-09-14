def changes(change):

    A500, A100, A50, A10, A5, A1 = 0, 0, 0, 0, 0, 0

    while change >= 500:
        change -= 500
        A500 += 1

    while change >= 100:
        change -= 100
        A100 += 1

    while change >= 50:
        change -= 50
        A50 += 1

    while change >= 10:
        change -= 10
        A10 += 1

    while change >= 5:
        change -= 5
        A10 += 1

    while change >= 1:
        change -= 1
        A1 += 1

    #print(A500, A100, A50, A10, A5, A1)
    qty_of_coin = A500 + A100 + A50 + A10 + A1
    return qty_of_coin

if __name__ == "__main__":

    change = int(input())
    change = 1000 - change
    print(changes(change))