from collections import defaultdict

from .mnemonics import is_stop_word


def add_in_hash_table(key, hash_table):
    hash_value = hash(key)
    if hash_value in hash_table:
        hash_table[hash_value].append(key)
    else:
        hash_table[hash_value] = [key]


def list_to_gram(size, start, data_list):
    temp = []
    for itr in range(start, start + size):
        temp.append(data_list[itr])
    return ' '.join(temp)


def make_n_grams(size_of_gram, data_list, temp_hash_table=None, overlapping=True):
    if temp_hash_table is None:
        temp_hash_table = defaultdict(int)

    ngrams_list = []
    step = 1 if overlapping else size_of_gram

    for i in range(0, len(data_list) - size_of_gram + 1, step):
        ngram = list(data_list[i:i + size_of_gram])
        ngram_string = " ".join(ngram)
        ngrams_list.append(ngram_string)
        add_in_hash_table(ngram_string, temp_hash_table)

    return ngrams_list, temp_hash_table


def variable_length_n_grams(data_list):
    var_grams = []
    sequence = []

    for opcode in data_list:
        if is_stop_word(opcode):
            if sequence:
                string = ' '.join(sequence)
                var_grams.append(string)
                sequence.clear()
        else:
            sequence.append(opcode)

    if sequence:
        string = ' '.join(sequence)
        var_grams.append(string)

    return var_grams

