import random

test_list = [120,68,-20,0,5,67,14,99]

sorted_list = sorted(test_list)

print(f"original list : {test_list}")
print(f"sorted list : {sorted_list}")

test_list.sort() #se modifico la estructura original
print(f"original list: {test_list}")

cards = ["2","3","4","6","7","q","s","g"]

shuffled_cards = random.sample(cards , k=len(cards))

print(f"shuffled cards : {shuffled_cards}")
print(f"original cards : {cards}")

random.shuffle(cards)
print(f"cards : {cards}")
