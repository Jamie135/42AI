import time


def ft_progress(lst):
    total = len(lst)
    start_time = time.time()
    # enumerate parcour lst tout en gardant une trace de l'index de chaque élément
    for i, item in enumerate(lst):
        # yield item sert à retourner chaque élément de la lst
        # un par un, à chaque itération de la boucle
        # lorsqu'on l'appel dans une boucle for, chaque itération de la boucle
        # récupère l'élément suivant de lst
        # tout comme si on utilisait return, mais sans interrompre la fonction
        # car elle reste "en pause" jusqu'à ce que la prochaine valeur soit demandée
        yield item
        progress = i / total
        elapsed_time = time.time() - start_time
        eta = elapsed_time / progress * (1 - progress) if progress > 0 else 0
        progress_bar = '[' + '=' * int(progress * 20) + '>' + ' ' * (19 - int(progress * 20)) + ']'
        print(f"ETA: {eta:.2f}s [{int(progress * 100)}%]{progress_bar} {i}/{total} | elapsed time {elapsed_time:.2f}s", end='\r')


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print("\n" + str(ret))

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print("\n" + str(ret))
