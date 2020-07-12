from math import log

def counting_sort(A, k):
    # A: input list
    # k: maximum value of A

    # B: output list init with 0
    B = [0] * len(A)

    # C: counting list init with 0
    C = [0] * (k+1)

    # count occurences
    for a in A:
        C[a] += 1

    print(C)

    # update C as cumulative
    for i in range(k):
        C[i+1] += C[i]

    print(C)

    # update B
    for j in reversed(range(len(A))):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1

    return B

def get_digit(number, d, base):
  return (number // base ** d) % base

def counting_sort_with_digit(A, d, base):
    # k : ex) 10진수의 최대값 = 9
    k = base - 1
    B = [-1] * len(A)
    C = [0] * (k + 1)
    # 현재 자릿수를 기준으로 빈도수 세기
    for a in A:
        C[get_digit(a, d, base)] += 1
    # C 업데이트
    for i in range(k):
        C[i + 1] += C[i]
    # 현재 자릿수를 기준으로 정렬
    for j in reversed(range(len(A))):
        B[C[get_digit(A[j], d, base)] - 1] = A[j]
        C[get_digit(A[j], d, base)] -= 1
    return B

def radix_sort(A, base=10):

    digit = int(log(max(A), base)+1)

    for d in range(digit):
        A = counting_sort_with_digit(A, d, base)

    return A

if __name__ == "__main__":

    A = [2,0,2,0,4,1,5,5,2,0,2,4,0,4,0,3]
    D = [15, 27, 64, 25, 50, 17, 39, 28]

    print(counting_sort(A, 5))
    print()
    print(radix_sort(D))