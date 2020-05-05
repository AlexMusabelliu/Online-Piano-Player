import time
import ctypes
import sys

SendInput = ctypes.windll.user32.SendInput

PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
    ("wScan", ctypes.c_ushort),
    ("dwFlags", ctypes.c_ulong),
    ("time", ctypes.c_ulong),
    ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
    ("wParamL", ctypes.c_short),
    ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
    ("dy", ctypes.c_long),
    ("mouseData", ctypes.c_ulong),
    ("dwFlags", ctypes.c_ulong),
    ("time",ctypes.c_ulong),
    ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
     ("mi", MouseInput),
     ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
    ("ii", Input_I)]

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

user32 = ctypes.WinDLL('user32', use_last_error=True)

#dict. of key scancodes
keydict = {"Q":0x10,
"W":0x11,
"E":0x12,
"R":0x13,
"T":0x14,
"Y":0x15,
"U":0x16,
"I":0x17,
"O":0x18,
"P":0x19,
"[":0x1A,
"]":0x1B,
"RETURN":0x1C,
"LCONTROL":0x1D,
"A":0x1E,
"S":0x1F,
"D":0x20,
"F":0x21,
"G":0x22,
"H":0x23,
"J":0x24,
"K":0x25,
"L":0x26,
";":0x27,
"'":0x28,
"`":0x29,
"LSHIFT":0x2A,
"\\":0x2B,
"Z":0x2C,
"X":0x2D,
"C":0x2E,
"V":0x2F,
"B":0x30,
"N":0x31,
"M":0x32,
",":0x33,
".":0x34,
"/":0x35,
"RSHIFT":0x36,
"*":0x37,   
"LMENU":0x38,  
" ":0x39,
"CAPITAL":0x3A,
"1":0x02,
"2":0x03,
"3":0x04,
"4":0x05,
"5":0x06,
"6":0x07,
"7":0x08,
"8":0x09,
"9":0x0A,
"0":0x0B,
"!":0x02,
"@":0x03,
"#":0x04,
"$":0x05,
"%":0x06,
"^":0x07,
"&":0x08,
"*":0x09,
"(":0x0A,
")":0x0B
}

MUSIC = '''^qEtTiPiTtEq8(etYtpYpsps*EiPiPgPgJgJ[c9]JgJgPgPiPiE@^qQEQYEQiEQ4(eTeTITeiTe[i$]EiPiEiEiPiE[Y4]EYPYEpYe[YG]pY[^g]qEtTiPiTtEq8(e[ts]Yt[pS]Yp[sD]ps[*D]Ei[PS]iP[is]Ei[PS]iP[9dg]PiPiEiEQ[EH]q^[@G]^(QEQYEQiEQ4(e[Tg]eT[ID]TWiT[WS][i$s]EiPiEiEiPiE[Y4]EYPYEpYeYpY[^g]qEtTi[PJ]iTtEq[8j](et[YJ]t[pl]Yps[pG]s[*g]EiPiPgPgJgJ[c9]JgJgPgPiPiE[@G]^qQEQ[YL]EQiEQ[4l](eT[eJ]T[Ij]Te[il]Te[i$J]EiPiEiEiPiE[Y4]EYPYEpYeYpY[^g]qEtTi[PJ]iTtEq[8j](et[YJ]t[pl]Yps[pG]s[*g]EiPiPgPgJgJ[c9]JgJgPgPiPiE[@G]^qQEQ[YL]EQiEQ[4l](eT[eJ]T[Ij]Te[il]Te[i$J]EiPiEiEiPiE[Y4]EYPYEpYeYpY^qEtTiPiTtEq8(etYtpYpsps*EiPiPgPgJgJ[c9]JgJgPgPiPiE@^qQEQYEQiEQ4(eTeTITeiTe[i$]EiPiEiEiPiE[Y4]EYPYEpYeYpY ||| [^EPSJ]'''
MUSIC = MUSIC.replace("\n", "").replace("{", "[").replace("}", "]").replace("|", " ")

TEMPO = 90

def play(v=False):
    '''
    Plays out the string listed in music by sending out keystrokes.

    Chords can be played with placing keys in brackets - i.e. [keys].
    | are converted to " " for compatibility with some sheet music.
    Curly braces are interpreted as brackets: remove those if not supposed to be chords.

    Args:
        v (optional): default false, sets the verbose flag to true
        
    Returns:
        N/A
    '''
    delay = 1 / TEMPO * 60
    
    if v:
        print(f"Time between each note: {delay}")
    
    building = False
    mult = 1/4
    pDelay = delay
    pMult = mult

    specials = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

    for b in MUSIC:
        if b == "]":
            delay = pDelay
            mult = pMult

        elif b == "[":
            pDelay = delay
            delay = 0.005
            pMult = mult
            mult = 1

        elif b != " ":
            bd = keydict.get(b.upper(), 0x2C)

            use_shift = b.isupper() or b in specials

            if use_shift:
                PressKey(keydict.get("LSHIFT"))

            PressKey(bd)
            ReleaseKey(bd)

            if use_shift:
                ReleaseKey(keydict.get("LSHIFT"))

        time.sleep(delay * mult)

if __name__ == "__main__":
    time.sleep(5)
    play(v=True)