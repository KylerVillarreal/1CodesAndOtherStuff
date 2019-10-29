# Transposition Cipher

# original: This_is_a_Secret_message_I_want_to_transit
#encrypted: hsi_ertmsaeta_att_rnmtti_sasce_esg_htiwn_otasi

def scramble2Encrypt(plainText):
    evenChars = ""
    odd Chars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText