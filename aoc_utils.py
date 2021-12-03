def read_input(file_path: str) -> list[str]:
    """Read in from file, pass back as an array of strings representing each line"""
    input_as_list = []
    with open(file_path) as f:
        for each in f.read().splitlines():
            input_as_list.append(each)
    return input_as_list
