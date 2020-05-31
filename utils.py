
def is_int(int_str):
    try:
        int(int_str)
        return True
    except ValueError:
        return False