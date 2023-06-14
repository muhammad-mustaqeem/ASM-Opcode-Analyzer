def load_api_dictionary(api_file):
    with open(api_file, 'r+') as file:
        return file.read().split('\n')
