import time


def progress(lst):
    total = len(lst)
    start_time = time.time()
    # enumerate parcour lst tout en gardant une trace de l'index de chaque élément
    for i, val in enumerate(lst):
        # val represente l'element actuel de lst
        # yield val sert à retourner l'élément de lst sans terminer la fonction
        # elle renvoie un résultat au générateur appelant et conserve l'état de la fonction 
        # pour que l'exécution puisse reprendre là où elle s'est arrêtée lors du prochain appel 
        yield val

        # proportion de la barre parcourue
        progress = i / total

        # le temps écoulé depuis le début de l'itération
        elapsed_time = time.time() - start_time

        # calcul pour l'estimation du temps restant
        if progress > 0:
            eta = elapsed_time / progress * (1 - progress)
        else:
            eta = 0

        # '=' * int(progress * 20) calcule le nombre de symboles '='
        # ' ' * (19 - int(progress * 20)) calcule le nombre d'espaces nécessaires pour compléter la barre
        progress_bar = '[' + '=' * int(progress * 20) + '>' + ' ' * (19 - int(progress * 20)) + ']'

        # affiche la progression de la barre formatté comme dans le sujet
        #'\r' permet de overwrite la ligne recente de la progression
        print(f"ETA: {eta:.2f}s [{int(progress * 100)}%]{progress_bar} {i}/{total} | elapsed time {elapsed_time:.2f}s", end='\r')
