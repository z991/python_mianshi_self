ISSUERS = {
    ((34, 37), (15,)): 'AMEX',
    ((6011,), (16,)): 'Discover',
    ((51, 52, 53, 54, 55), (16,)): 'Mastercard',
    ((4,), (13, 16)): 'VISA',
}


# def get_issuer(number):
#     return next((issuer for (starts, lengths), issuer in ISSUERS.items() if
#                  str(number).startswith(tuple(map(str, starts))) and len(str(number)) in lengths), 'Unknown')

def get_issuer(number):
    for (starts, lenghs), issuer in ISSUERS.items():
        if str(number).startswith(tuple(map(str, starts))) and len(str(number)) in lenghs:
            return issuer
    return 'Unknown'




if __name__ == '__main__':
    re = get_issuer(378282246310005)
    print(re)
