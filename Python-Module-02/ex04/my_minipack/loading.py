import time

def ft_progress(lst):
    i = 1
    start = time.time()
    while i <= len(lst):
        yield i
        pourc = int(i * 100 / len (lst))
        nb = int(i * 20 / len(lst))
        arrow = ">".rjust(nb, "=")
        top = time.time() - start
        eta = (len(lst) * top / i) - top
        print(f"ETA: {eta:.2f}s [{pourc:3}%] [{arrow:<20}] {i}/{len(lst)} | elapsed time {top:.2f}s", end = '\r', flush=True)
        i += 1
