print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitSide, SplitType

keyboard = KMKKeyboard()
keyboard.row_pins = (board.GP2, board.GP9, board.GP11,board.GP12,board.GP13, )
keyboard.col_pins = (board.GP8, board.GP7, board.GP6, board.GP5, board.GP4, board.GP3, board.GP10, )
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ----- MODULES -----

keyboard.modules.append(Layers())
keyboard.modules.append(MediaKeys())
keyboard.modules.append(MouseKeys())
keyboard.modules.append(Split(
    split_type=SplitType.UART,  # Defaults to UART
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.GP1,  # The primary data pin to talk to the secondary device with
    data_pin2=board.GP0,  # Second uart pin to allow 2 way communication
    uart_flip=True,  # Reverses the RX and TX pins if both are provided
    use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
))



# ----- USER KEYS -----
_____ = KC.TRNS
FN = KC.MO(1)

# ----- KEYMAP -----
keyboard.keymap = [
    [ # DEFAULT QWERTY
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,  _____,        _____,   KC.N6,  KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.EQL,
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,   _____,        _____,   KC.Y,   KC.U,    KC.I,    KC.O,    KC.P,    KC.MINS,
        KC.ESC,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,   KC.VOLU,      KC.PGUP, KC.H,   KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,
        KC.BSPC, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,   KC.VOLD,      KC.PGDN, KC.N,   KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.BSLS,
        FN,      KC.LALT, KC.LBRC, KC.RBRC, KC.LCTL, KC.SPC, KC.LSFT,      KC.ENT,  KC.SPC, KC.RGUI, KC.MPRV, KC.MNXT, KC.RCTL, KC.DEL,
    ],
    [ # FUNCTION LAYER
        KC.F12,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,  _____,        _____,   KC.F6,  KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,
        _____,   _____,   _____,   KC.UP,   _____,   _____,  _____,        _____,   _____,  _____,   _____,   _____,   _____,   _____,
        _____,   _____,   KC.LEFT, KC.DOWN, KC.RIGHT,_____,  _____,        _____,   _____,  _____,   _____,   _____,   _____,   _____,
        _____,   _____,   _____,   _____,   _____,   _____,  _____,        _____,   _____,  _____,   _____,   _____,   _____,   _____,
        KC.DEL,  _____,   _____,   _____,   _____,   _____,  _____,        _____,   _____,  _____,   _____,   _____,   _____,   _____,
    ],
]



if __name__ == '__main__':
    keyboard.go()
