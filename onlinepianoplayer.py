import win32com.client, win32api, win32con
import time
from turtle import Turtle, Screen
import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
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

# Actuals Functions

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

# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

user32 = ctypes.WinDLL('user32', use_last_error=True)

music = '''QWERTYqwerty'''

# s = Screen()

# s.tracer(None)

# t = Turtle("circle", visible=False)
# t.pu()
# t.color("black")
# t.shapesize(3)

tempo = 200

# keyboard = Controller()

# shell = win32com.client.Dispatch("WScript.Shell")

# def rewrite():
#     s.clearscreen()
#     t.write(tempo, False, "center", ("MS Comic Sans", 30, "bold"))

# t.goto(0, 0)
# rewrite()

# s.update()

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
"LBRACKET":0x1A,
"RBRACKET":0x1B,
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
"SEMICOLON":0x27,
"APOSTROPHE":0x28,
"GRAVE":0x29,
"LSHIFT":0x2A,
"BACKSLASH":0x2B,
"Z":0x2C,
"X":0x2D,
"C":0x2E,
"V":0x2F,
"B":0x30,
"N":0x31,
"M":0x32,
"COMMA":0x33,
"PERIOD":0x34,
"SLASH":0x35,
"RSHIFT":0x36,
"MULTIPLY":0x37,   
"LMENU":0x38 ,  
"SPACE":0x39,
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
"0":0x0B
}

def up():
    s.onkeypress(up, None)
    tempo += 1
    rewrite()
    s.onkeypress(up, "Up")

def down():
    s.onkeypress(down, None)
    temp -= 1
    rewrite()
    s.onkeypress(down, "Down")

def play():
    delay = 1 / tempo * 60
    print(delay)
    for b in music:
        mult = 1
        # print(b)
        if b != " ":
            bd = keydict.get(b.upper(), 0x2C)
            if b.isupper():
                PressKey(keydict.get("LSHIFT"))
            PressKey(bd)
            ReleaseKey(bd)
            if b.isupper():
                ReleaseKey(keydict.get("LSHIFT"))

        else:
            mult = 1/2

        time.sleep(delay * mult)

# s.listen()
# s.onkeypress(up, "Up")
# s.onkeypress(down, "Down")

time.sleep(5)

play()

# s.mainloop()