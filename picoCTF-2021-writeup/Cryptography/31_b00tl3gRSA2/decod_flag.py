from Crypto.Util.number import long_to_bytes

c = 24671005237524713926353346277545930647178352298559668385932896012579109894122520377187768313208226992229285992848317140202626178774598340031249145139938679896088874021463220309428952912854564728583959962723694799495582232782493043171087707842755629255194315973794606626971669114495890354071890436563936897704
n = 105760530531025436955612311481084551141712020584860702340597133164102847123167169739434833136258478502812722552456582440826441500952079159122249429274963951295547928034458140096705407288335588156103842304787508857709281789494304255771075252823696091203106367301825364517994008390006948115589455754694509545101
d = 65537

print(long_to_bytes(pow(c, d, n)).decode())

