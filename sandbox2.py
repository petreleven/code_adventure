import time
def iterate(n):
    tick = time.time()
    result = []
    for i in range(n):
        result.append(n*n + n*7 +9)
    tock = time.time()
    print("Took seconds :"+str(tock-tick))