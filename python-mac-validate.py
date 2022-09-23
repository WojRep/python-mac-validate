

def mac_validate(mac_address):
    pass

def mac_standardize(mac_address, standard=":", character="lower"):
    import re
    '''
        MM:MM:MM:SS:SS:SS
        MM-MM-MM-SS-SS-SS
        MMM.MMM.SSS.SSS
    '''

    mac_address = str(mac_address).strip(' :.-')

#    mac_address = ''.join(filter(str.isalnum, mac_address))
    mac_address = re.sub(r'[^a-fA-F0-9]', '', mac_address)

    if character == "lower":
        mac_address = mac_address.lower()
    elif character == "upper":
        mac_address = mac_address.upper()

    if standard == ":":
        pass
    elif standard == "-":
        pass
    elif standard == ".":
        pass

    return mac_address



print(mac_standardize("0a:eg:a0:34:33:9e"))