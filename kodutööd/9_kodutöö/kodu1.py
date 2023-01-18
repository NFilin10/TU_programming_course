
def erinevad_sümbolid(s):
    hulk = set()
    for symbol in s:
        if symbol in s:
            hulk.add(symbol)
    return hulk


def sümbolite_sagedus(s):
    letters_dict = {}
    
    for symbol in s:
        if symbol not in letters_dict:
            letters_dict[symbol] = 0
            
        letters_dict[symbol] += 1
    return letters_dict


def grupeeri(s):
    letters_dict = {}
    täishäälikud = ["e", "u", "i", "o", "a", "ü", "ä", "õ", "ö", "E", "U", "I", "O", "A", "Ü", "Ä","Õ","Ö"]
    märgid = [",", ".", "!", "?", ";", "-", ":", ' ', "'"]

    koik_tais = []
    koik_kaas = []
    koik_margid = []
    
    for symbol in s:
        if symbol in täishäälikud:
            koik_tais.append(symbol)
        elif symbol in märgid:
            koik_margid.append(symbol)
        else:
            koik_kaas.append(symbol)
        
    letters_dict['Täishäälikud'] = set()
    letters_dict['Kaashäälikud'] = set()
    letters_dict['Muud'] = set()
    
    for key, value in sümbolite_sagedus(koik_tais).items():
        letters_dict['Täishäälikud'].add((key, value))
        
    for key, value in sümbolite_sagedus(koik_kaas).items():
        letters_dict['Kaashäälikud'].add((key, value))
        
    for key, value in sümbolite_sagedus(koik_margid).items():
        letters_dict['Muud'].add((key, value))
    
    return letters_dict
    
    
print(grupeeri("äia õe oaõieaia õueaua ööAu"))
      