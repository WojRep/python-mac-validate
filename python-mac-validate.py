

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
        mac_address == mac_address[0-2] + ":" + mac_address[2-4] + ":" + mac_address[4-6] + ":" + mac_address[6-8] + ":" + mac_address[8-10] + ":" + mac_address[10-12]
    elif standard == "-":
        mac_address == mac_address[0-2] + "-" + mac_address[2-4] + "-" + mac_address[4-6] + "-" + mac_address[6-8] + "-" + mac_address[8-10] + "-" + mac_address[10-12]
    elif standard == ".":
        mac_address == mac_address[0-3] + "." + mac_address[3-6] + "." + mac_address[6-9] + "." + mac_address[9-12]

    return mac_address



print(mac_standardize("0a:eg:a0:34:33:9e"))