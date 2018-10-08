import multiprocessing
import random

words = ['I', 'can', 'see', 'the', 'mountains']

def write_word_to_file(f):
    w = random.choice(words)
    f.write("{}\n".format(w))

def run(fl, n):
    for _ in range(n):
        write_word_to_file(fl)

q = multiprocessing.Pool()
f = open('out.txt', 'a')

procs = [ multiprocessing.Process(target=run, args=(f,5)) for _ in range(5) ]
for p in procs: p.start()
for p in procs: p.join()

f.close()
