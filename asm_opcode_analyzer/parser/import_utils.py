import re

from .mnemonics import is_valid_opcode


def import_opcodes_to_list(file_name, mnemonics):
    regex = "(.\w+:[\d\w]+\s([0-9|A-F]+\s)+)?\s+([a-z|A-Z|0-9]+)(\s?.*)"
    opcode_list = []
    with open(file_name, 'r+', encoding='latin1') as file:
        for line in file:
            line = line.replace('\n', '')
            if bool(re.search(regex, line)):
                m0 = re.match(regex, line)
                try:
                    opcode = m0.group(3)
                    if opcode not in [
                        'unicode', 'off', 'unk', 'asc', 'dword', 'public', 'word', 'near', 'proc', 'byte',
                        'endp', 'align', 'db', 'dw', 'dd', 'dt', 'offset'
                    ]:
                        if is_valid_opcode(opcode, mnemonics):
                            opcode_list.append(opcode)
                except:
                    continue
            else:
                continue
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


def import_api_to_list(file_name, valid_api):
    api_regex = "(.*)(__stdcall\s(\w+))"
    api_list = []
    with open(file_name, 'r', encoding='latin1') as file_data:
        for line in file_data:
            if "__stdcall" in line:
                if bool(re.search(api_regex, line)):
                    matched_data = re.match(api_regex, line)
                    api_extracted = matched_data.group(3)
                    if api_extracted in valid_api:
                        api_list.append(api_extracted)
    return api_list


def import_dll_to_list(file_name, valid_dll):
    dll_list = []
    dll_regex = "(?:.*?)(?:'?)(\w+(?:(?:\.|\-|\_)*\w*))(?:\.DLL|\.dll)(?:'?)"
    dll_extensions = [".DLL", ".dll", "_DLL"]
    with open(file_name, 'r', encoding='latin1') as file_data:
        for line in file_data:
            for dll_extension in dll_extensions:
                if dll_extension in line:
                    if bool(re.search(dll_regex, line)):
                        matched_data = re.match(dll_regex, line)
                        dll_extracted = matched_data.group(1).lower()
                        if dll_extracted in valid_dll:
                            dll_list.append(dll_extracted)
    return dll_list
