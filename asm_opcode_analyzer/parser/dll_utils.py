def load_dll_dictionary(dll_file):
    with open(dll_file, 'r') as file:
        return file.read().split('\n')
