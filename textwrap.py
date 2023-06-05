import textwrap

def wrap(string, max_width):
    if len(string) > max_width:
        x = ""
        for i in range(max_width):
            x += string[i]
        string = string[max_width:]
        print(x)
        return wrap(string, max_width)
    else:
        return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)