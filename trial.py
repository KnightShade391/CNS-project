from threading import Thread

res = []

def func1(num, ind):
    for i in range(num):
        continue
    res.append(i)

threads = [None] * 2
args = [1000000, 5000000]
for i in range(2):
    threads[i] = Thread(target = func1, args = (args[i], i))
    threads[i].start()
    threads[i].join()
r1 = res[0]
r2 = res[1]
print(r1, r2, res)