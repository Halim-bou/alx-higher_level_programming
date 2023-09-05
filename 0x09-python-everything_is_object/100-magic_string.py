#1/usr/bin/python3
def magic_string():
    magic_string.lenth = getattr(magic_string, 'lenth', 0) + 1
    return (', '.join(["BestSchool" for i in range(magic_string.lenth)]))
