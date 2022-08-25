import random, copy

def bogo(items):
    # Kopier den liste, vi har modtaget som parameter, så vi ikke ændrer den originale
    items = items.copy()
    isSorted = None # Boolean til markering af, om listen er sorteret
    attempts = 0 # Tællevariabel til at holde styr på antal af forsøg
    while not isSorted:
        attempts += 1
        if attempts > len(items) * 5000: # Check for at stoppe tendensen mod uendeligt
            print('Giver op på grund af for mange forsøg ({}) og bruger TimSort'.format(attempts))
            items.sort()
            return items
        random.shuffle(items) # Bland alle elementer helt tilfældigt
        isSorted = True # Vi går ud fra at listen tilfældigvis er sorteret,
        # ...og prøver i denne løkke at bevise det modsatte
        for index in range(len(items)-1):
            if items[index] > items[index+1]:
                isSorted = False
                break # Bryd løkken hvis et eneste element er forkert sorteret
    print('Sorteret efter {} forsøg'.format(attempts))
    return items

def bubbleSort(items):
    for x in range(len(items)-1):
        for y in range(len(items)-1-x):
            if items[y] > items[y+1]:
                items[y], items[y+1] = items[y+1], items[y]
    return items

def gnomeSort(items):
    for x in range(len(items)-1):
        for y in range(len(items)-1):
            if items[y] > items[y+1]:
                items[y], items[y+1] = items[y+1], items[y]
    return items

def selectionSort(items):
    for ind in range(len(items)):
        min_index = ind

        for j in range(ind, len(items)):
            if items[j] < items[min_index]:
                min_index= j

        (items[ind],items[min_index])= (items[min_index], items[ind])
        print(items)

    return items


def insertionSort(items):
    for i in range(1, len(items)):
        key=items[i]

        j=i-1
        while j >= 0 and key< items[j]:
           items[j+1]=items[j]
           j-=1
        items[j+1]=key
    return items

def mergeSort(items):
    for i in range


if __name__ == '__main__':
    l = list(range(0, 5))
    lb = l.copy()
    for i in range(1):
        random.shuffle(lb)
        ## Kald den funktion, du vil teste
        ls = insertionSort(l)
        ## Kald den funktion, du vil teste
        if ls != l:
            print('Fejl! Algoritmen kan ikke sortere.')
            break
    print('Succes! Algoritmen sorterer korrekt.')
    print('blandet: ', lb)
    print('sorteret:', ls)
