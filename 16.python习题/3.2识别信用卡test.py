card_dict = {
    ((34, 37), (15,)): 'AMEX',
    ((6011), (16)): 'Discover',
    ((51, 52, 53, 54, 55), (16)): 'Mastercard',
    ((4), (13, 16)): 'VISA',
}

def get_issuer(card):
    for (start,len_v), type_v in card_dict.items():
        if str(card).startswith(tuple(map(str,start))) and len(card) in len_v:
            return type_v
        else:
            return 'Unknown'

