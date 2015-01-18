# -*- coding: utf-8 -*-
from __future__ import division
from evdev import ecodes as e, UInput, uinput

_alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'

def scrolldown():
    capabilities = {
        e.EV_REL : (e.REL_X, e.REL_Y, e.REL_WHEEL), 
        e.EV_KEY : (e.BTN_LEFT, e.KEY_ENTER, e.BTN_RIGHT, e.KEY_SCROLLDOWN),
    }
    with UInput(capabilities) as ui:
        ui.write(e.EV_REL, e.REL_WHEEL, -100000)
        ui.syn()

def press_key(KEY='KEY_ENTER'):
    capabilities = {
        e.EV_REL : (e.REL_X, e.REL_Y, e.REL_WHEEL), 
        e.EV_KEY : (e.BTN_LEFT, e.KEY_ENTER, e.BTN_RIGHT, e.KEY_SCROLLDOWN),
    }

    with uinput.UInput() as ui:
        ui.write(e.EV_KEY, e.ecodes[KEY], 1)
        ui.syn()

def press_ctrl_plus(KEY='KEY_S'):
    capabilities = {
        e.EV_REL : (e.REL_X, e.REL_Y, e.REL_WHEEL), 
        e.EV_KEY : (e.BTN_LEFT, e.KEY_ENTER, e.KEY_S, e.KEY_V, e.BTN_RIGHT, e.KEY_SCROLLDOWN),
    }

    with uinput.UInput() as ui:
        ui.write(e.EV_KEY, e.KEY_LEFTCTRL, 1)
        ui.write(e.EV_KEY, e.ecodes[KEY], 1)
        ui.syn()

def change_language():
    capabilities = {
        e.EV_REL : (e.REL_X, e.REL_Y, e.REL_WHEEL),
        e.EV_KEY : (e.BTN_LEFT, e.KEY_ENTER, e.KEY_S, e.KEY_V, e.BTN_RIGHT, e.KEY_SCROLLDOWN),
    }

    with uinput.UInput() as ui:
        ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 1)
        ui.write(e.EV_KEY, e.KEY_LEFTALT, 1)
        ui.syn()

def save_page(username):
    press_ctrl_plus('KEY_S')
    press_key()
    # save file writing letter by letter
    # for letter in username.lower():
    #     if letter in _alphabet:
    #         press_key("KEY_%s" %letter.upper())
    #     elif letter == " ":
    #         press_key("KEY_SPACE")
    #     else:
    #         try:
    #             # encode non-english letter
    #             ascii_letter = repr(letter)
    #             for l in ascii_letter:
    #                 if l in _alphabet:
    #                     press_key("KEY_%s" %l.upper())
    #                 elif l == " ":
    #                     press_key("KEY_SPACE")
    #                 else:
    #                     continue
    #         except:
    #             continue