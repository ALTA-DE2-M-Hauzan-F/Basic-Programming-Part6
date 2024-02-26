def caesar(offset, input_str):
    pattern = ""
    for s in input_str:
        # get unicode (97-122)
        newcode=ord(s)+offset%26
        if s==" ":
            pattern +=" "
        # return unicode to alphabet
        elif newcode >122:
            pattern +=chr(newcode-26)
        else: pattern +=chr(newcode)
    return pattern

if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl