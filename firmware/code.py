print("oh now u fuckin work")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

# macros = Macros()
# keyboard.modules.append(macros)

keyboard.col_pins = (board.GP5, board.GP6, board.GP7, board.GP8, board.GP9,
board.GP10, board.GP11, board.GP12, board.GP13, board.GP15,
board.GP14, board.GP16, board.GP17, board.GP18, board.GP19,
board.GP20, board.GP21)

keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4)

keyboard.keymap = [
   [KC.ESC]
]

keyboard.keymap = [
    [
    KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC,
    KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.DEL,
    KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT, KC.PGUP,
    KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLASH, KC.RSFT, KC.UP, KC.PGDN,
    KC.LCTRL, KC.LGUI, KC.LALT, KC.SPACE, KC.SPACE, KC.A, KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT
    ]
]

# replace kc.a with kc.fn or wtv it is

if __name__ == '__main__':
    keyboard.go()
    
    