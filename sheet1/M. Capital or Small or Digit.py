x = input()
ascci_code = ord(x)
if ascci_code >= 48 and ascci_code < 65:
    print("IS DIGIT")
elif ascci_code >= 65:
    print("ALPHA")
    if ascci_code >= 65 and ascci_code < 97:
        print("IS CAPITAL")
    else:
        print("IS SMALL")