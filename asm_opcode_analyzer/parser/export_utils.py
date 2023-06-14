def export_data_to_csv(data, export_file):
    with open(export_file, 'w+') as file:
        for key, value in data.items():
            file.write(f"{key},{value}\n")
    print("Data Exported Successfully")


def export_list_to_csv(data_list, export_file):
    with open(export_file, 'w+') as file:
        for item in data_list:
            file.write(f"{item}\n")
    print("Data Exported Successfully")


def export_list_to_txt(data_list, export_file):
    with open(export_file, 'w+') as file:
        for item in data_list:
            file.write(f"{item}\n")
    print("Data Exported Successfully")
