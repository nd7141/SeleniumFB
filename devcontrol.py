from __future__ import division
from evdev import ecodes as e, UInput, uinput

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

def save_page(username):
	press_ctrl_plus('KEY_S')
	for letter in username.upper():
		try:
			press_key('KEY_%s' %letter)
		except KeyError:
			press_key('KEY_SPACE')
	press_key()