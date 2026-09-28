import regex as re
from collections import defaultdict
import pickle
from tqdm import tqdm

def pretokenize(text):
    pattern = r"""'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""
    return re.findall(pattern, text)

def count_pairs(ids):
    counts = defaultdict(int)
    for pair in zip(ids, ids[1:]):
        counts[pair] += 1
    return counts


def merge(ids, pair, new_id):
    merged_ids = []
    i = 0

    while i < len(ids):
        if i < len(ids) - 1 and (ids[i], ids[i+1]) == pair:
            merged_ids.append(new_id)
            i += 2
        else:
            merged_ids.append(ids[i])
            i += 1

    return merged_ids

def train_bpe(text, vocab_size):
    
    ids = list(text.encode("utf-8"))

    num_merges = vocab_size - 256  
    merge_rules = {}

    for step in range(num_merges):

        counts = count_pairs(ids)

        if not counts:
            break

        best_pair = max(counts, key=counts.get)
       
        new_id = 256 + step
        merge_rules[best_pair] = new_id

        ids = merge(ids, best_pair, new_id)

    return merge_rules

class BPETokenizer:
    def __init__(self, merge_rules):
        self.merge_rules = merge_rules

        self.id_to_bytes = {i: bytes([i]) for i in range(256)}

        for (id1, id2), new_id in merge_rules.items():
            self.id_to_bytes[new_id] = self.id_to_bytes[id1] + self.id_to_bytes[id2]

        self.vocab_size = len(self.id_to_bytes)

    @staticmethod
    def load_from(filepath):
        with open(filepath, 'rb') as f:
            merge_rules = pickle.load(f)
        return BPETokenizer(merge_rules)

    def _encode_text(self, text):
        ids = list(text.encode("utf-8"))
        for merge_pair, new_id in self.merge_rules.items():
            ids = merge(ids, merge_pair, new_id)
        return ids


    def encode(self, input_text, show_progress=False):
        ids = list(input_text.encode("utf-8"))
        merge_items = self.merge_rules.items()
        if show_progress:
            merge_items = tqdm(merge_items, total=len(self.merge_rules), desc="Encoding")

        for merge_pair, new_id in merge_items:
            ids = merge(ids, merge_pair, new_id)

        return ids

    def decode(self, ids):
        byte_list = [self.id_to_bytes[i] for i in ids]
        text_bytes = b"".join(byte_list)
        text = text_bytes.decode("utf-8", errors="replace")
        return text
