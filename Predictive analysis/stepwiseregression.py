y = [78.5,74.3,104.3,87.6,95.9,109.2,102.7,72.5,93.1,115.9,83.8,113.3,109.4]
x1 = [7,1,11,11,7,11,3,1,2,21,1,11,10]

x2 = [26,29,56,31,52,55,71,31,54,47,40,66,68]
x3 = [6,15,8,8,6,9,17,22,18,4,23,9,8]
x4 = [66,52,20,47,33,22,6,44,22,26,34,12,12]
n = len(y)
# 
def mean(arr):
    return sum(arr) / len(arr)

def sos(arr):
    mv = mean(arr)
    return sum((i - mv) ** 2 for i in arr)

def socp(arr1, arr2):
    m1 = mean(arr1)
    m2 = mean(arr2)
    return sum((arr1[i] - m1) * (arr2[i] - m2) for i in range(n))

def re(x, y):
    b1 = socp(x, y) / sos(x)
    b0 = mean(y) - b1 * mean(x)
    return b0, b1

def sr():
    v3 = [x1, x2, x3, x4]
    cv = []
    rv = v3.copy()
    while rv:
        bv = None
        brs = -float('inf')
        for var in rv:
            cov = cv + [var]
            y_m = mean(y)
            ss_t = sos(y)
            ss_r = 0
            for i in range(n):
                y_pred = mean(y)
                for c_v in cov:
                    b0, b1 = re(c_v, y)
                    y_pred += b1 * (c_v[i] - mean(c_v))
                ss_r += (y_pred - y_m) ** 2
            rs = ss_r / ss_t
            if rs > brs:
                brs = rs
                bv = var
        if bv:
            cv.append(bv)
            rv.remove(bv)
            print("chosen variables:", cv)
            print("p_squared:", brs)

sr()