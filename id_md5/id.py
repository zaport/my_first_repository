import uuid
import itertools

def uid(id):
    seed = uuid.uuid4()
    if seed not in id:
        id.add(seed)
        return seed
    else:
        seed = uid(id)

def uniqueid():
    id = set()
    seed = uuid.uuid4()
    id.add(seed)
    while True:
        yield seed
        seed = uid(id)


unique_sequence = uniqueid()
id1 = next(unique_sequence)
id2 = next(unique_sequence)
id3 = next(unique_sequence)
print(id1, id2, id3)
ids = list(itertools.islice(unique_sequence, 1000))
print(ids)