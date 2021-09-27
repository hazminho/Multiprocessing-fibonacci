import multiprocessing
import concurrent.futures
import time
import math


def matematika(x):
 n = int(math.sqrt(x))
 return n*n == x
def find_fibonacci(n):
 
 return matematika(5*n*n + 4) or matematika(5*n*n - 4)


def do_something(num):
  for i in range(100):
    if (find_fibonacci(i) == True):
      print(i,f"adalah sebuah angka fibonacci...{num}")
      time.sleep(1)
    else:
      print(i,f"BUKAN sebuah angka fibonacci....{num}")
      


start = time.perf_counter()

processes = []
for num in range(5):
  p = multiprocessing.Process(target=do_something, args=[num])
  p.start()

  processes.append(p)


for process in processes:
  process.join()

finish = time.perf_counter()

executed_time = round(finish - start, 2)
print(f"Finished in {executed_time} second(s)")