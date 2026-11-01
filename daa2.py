
import heapq
from collections import Counter

def huffman_encoding(text):
    freq = Counter(text)
    heap = [[f, [ch, ""]] for ch, f in freq.items()]
    heapq.heapify(heap)

    if len(heap) == 1:
        return {heap[0][1][0]: "0"}

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        for item in left[1:]:
            item[1] = "0" + item[1]
        for item in right[1:]:
            item[1] = "1" + item[1]

        heapq.heappush(heap, [left[0] + right[0]] +
                       left[1:] + right[1:])

    return {ch: code for ch, code in heap[0][1:]}

text = input("Enter a string: ")
codes = huffman_encoding(text)

print("Huffman Codes:")
for ch, code in codes.items():
    print(repr(ch), ":", code)

encoded = "".join(codes[ch] for ch in text)
print("Encoded String:", encoded)
