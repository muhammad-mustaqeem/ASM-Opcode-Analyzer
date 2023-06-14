import re

from .mnemonics import is_valid_opcode


def is_not_excluded(opcode):
    exclusion_list = [
        'unicode', 'off', 'unk', 'asc', 'dword', 'public', 'word', 'near', 'proc', 'byte',
        'endp', 'align', 'db', 'dw', 'dd', 'dt', 'offset'
    ]
    return opcode not in exclusion_list


def import_opcodes_to_list(file_name, mnemonics):
    regex = r"(.\w+:[\d\w]+\s([0-9A-F]+\s)+)?\s+([a-zA-Z0-9]+)(\s?.*)"
    opcode_list = []

    with open(file_name, 'r', encoding='latin1') as file:
        for line in file:
            line = line.rstrip('\n')
            match = re.match(regex, line)
            if match:
                opcode = match.group(3)

                if is_not_excluded(opcode) and is_valid_opcode(opcode, mnemonics):
                    opcode_list.append(opcode)

    return opcode_list


def import_hex_dump_to_list(file_name):
    hex_dump = []
    with open(file_name, 'r+', encoding='latin1') as file:
        for line in file:
            line = line.replace('\n', '')
            dump = line.split(' ')
            dump.pop(0)
            dump = list(filter(('??').__ne__, dump))
            hex_dump += dump
    return hex_dump
