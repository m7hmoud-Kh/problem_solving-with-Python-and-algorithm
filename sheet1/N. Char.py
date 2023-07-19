x = input()
assci_code = ord(x)
if assci_code >= 65 and assci_code < 97:
        assci_code += 32
else:
        assci_code -= 32
print(chr(assci_code))