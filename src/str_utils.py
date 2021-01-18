def keep_only_numbers(inp:str) -> str:
    return ''.join([x for x in inp if x.isnumeric() or x == ' '])
