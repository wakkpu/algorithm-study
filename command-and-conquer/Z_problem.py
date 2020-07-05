result = 0

def Z(N, r, c):

    global result
    x_m = 2 ** (N-1)
    y_m = 2 ** (N-1)

    if N == 1: # base case
        if(c < x_m and r < y_m): # sector 1

            print(result)

        if(c >= x_m and r < y_m): # sector 2

            result += 1
            print(result)

        if(c < x_m and r >= y_m): # sector 3

            result += 2
            print(result)

        if(c >= x_m and r >= y_m): # sector 4

            result += 3
            print(result)

    else: # recursive cases
        if (c < x_m and r < y_m):  # sector 1

            Z(N-1, r//2, c//2)


        if (c >= x_m and r < y_m):  # sector 2

            result += (2 ** (N-1)) ** 2
            Z(N-1, r//2, c//2)

        if (c < x_m and r >= y_m):  # sector 3

            result += 2 * ((2 ** (N-1)) ** 2)
            Z(N-1, r//2, c//2)

        if (c >= x_m and r >= y_m):  # sector 4

            result += 3 * ((2 ** (N-1)) ** 2)
            Z(N-1, r//2, c//2)

if __name__ == "__main__":

    N, r, c = map(int, input().split())
    Z(N, r, c)