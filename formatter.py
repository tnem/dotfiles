sample_string = "KC_EQUAL,KC_1,KC_2,KC_3,KC_4,KC_5,KC_ESCAPE,KC_BSLASH,KC_Q,KC_W,KC_E,KC_R,KC_T,TG(2),KC_TAB,KC_A,KC_S,KC_D,KC_F,KC_G,KC_LSPO,CTL_T(KC_Z),KC_X,KC_C,KC_V,KC_B,KC_LCTL,KC_LGUI,KC_GRAVE,KC_BSLASH,KC_LEFT,MO(3),KC_LALT,MO(1),KC_HOME,KC_BSPACE,KC_DELETE,KC_END,TG(2),KC_6,KC_7,KC_8,KC_9,KC_0,KC_MINUS,KC_LBRACKET,KC_Y,KC_U,KC_I,KC_O,KC_P,KC_RBRACKET,KC_H,KC_J,KC_K,KC_L,LT(2,KC_SCOLON),GUI_T(KC_QUOTE),KC_LCTL,KC_N,KC_M,KC_COMMA,KC_DOT,CTL_T(KC_SLASH),KC_RSPC,MO(3),KC_DOWN,KC_UP,KC_RIGHT,KC_LGUI,MO(1),KC_LALT,KC_PGUP,KC_PGDOWN,KC_ENTER,KC_SPACE"

box_len = 12

def printn(strsegments):
    tempstr = ""
    
    for i in range(len(strsegments)):
        bstr = "|{:^" + str(box_len) + "}"
        tempstr += bstr.format(strsegments[i])

    tempstr += "|"

    return tempstr

def printllen(llen):
    print "-" * (llen * (box_len + 1) + 1)

def reformat(s):
    entries = s.split(",")

    printllen(7)
    print printn(entries[0:7])
    printllen(7)
    print printn(entries[7:14])
    printllen(6)
    print printn(entries[14:20] + [""])
    printllen(7)
    print printn(entries[20:27])
    printllen(7)
    print printn(entries[27:33])
    printllen(6)

print reformat(sample_string)
