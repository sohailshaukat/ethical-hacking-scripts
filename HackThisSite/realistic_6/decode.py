#! python3

def sum_triplet(text):
    stream = text.split(".")
    if not stream[0]:
        del stream[0]
    triplets = []
    while stream:
        i = 3
        triplet = []
        while i:
            triplet.append(stream.pop())
            i -= 1
        triplets.append(sum(map(int,triplet)))
    return(triplets)


sum_triplet_result = sum_triplet(".26.58.13.28.22.48")

print("sum: ", sum_triplet_result)

print("".join(list(map(chr, sum_triplet_result))[::-1]))