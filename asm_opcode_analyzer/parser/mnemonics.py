from collections import defaultdict


def load_mnemonics(mnemonics_file):
    mnemonics = []
    mnemonic_indexer = defaultdict(int)
    with open(mnemonics_file, 'r') as file:
        itr = 0
        for line in file:
            line = line.strip('\n').lower()
            mnemonics.append(line)
            if line[0] not in mnemonic_indexer:
                mnemonic_indexer[line[0]] = itr
            itr += 1
    return mnemonics, mnemonic_indexer


def is_valid_opcode(opcode, mnemonics):
    opcode = opcode.lower()
    start = mnemonics[1][opcode[0]]
    for count in range(start, len(mnemonics)):
        if opcode == mnemonics[count]:
            return True
        if opcode[0] < mnemonics[count][0] or opcode[1] < mnemonics[count][1]:
            return False
    return False


def is_stop_word(opcode):
    stop_words = [
        'call', 'jmp', 'ret', 'iret', 'iretd', 'iretw', 'int', 'into', 'leave', 'retf', 'retn', 'je', 'jz',
        'jcxz', 'jp', 'jpe', 'jne', 'jnz', 'jecxz', 'jnp', 'jpo', 'ja', 'jae', 'jb', 'jbe', 'jna', 'jnae',
        'jnbe', 'jc', 'jnc', 'jg', 'jge', 'jl', 'jle', 'jng', 'jnge', 'jnl', 'jnle', 'jo', 'jno', 'js', 'jns'
    ]
    return opcode in stop_words
