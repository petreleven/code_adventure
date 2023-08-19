import time

tick = time.time()
result = []
count = 500000
for i in range(count):
    result.append(i*i + i*7 +9)
tock = time.time()
print("Took seconds :"+str(tock-tick))

