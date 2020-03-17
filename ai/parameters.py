# ds: distance; tc: touch; vc: voice; vs: vision; free: free move
MODELS = ['ds', 'tc', 'vc', 'vs', 'free']

# ita   : interactive
# stroke: 抚摸
# snap  : 扑
# flap  : 拍打
# rub   : 蹭

BEHAVIOURS = {
'move'     : ['run', 'walk', 'turn'],
'relax'    : ['lie_down', 'sit', 'stand'],
'play'     : ['stretch', 'knead', 'lick'],
'ita_human': ['stare_at', 'walk_towards'],

'ita_obj'  : ['rub_object', 'flap', 'pre_attack'],
'other'    : ['stop'],
'voice'    : ['start_listen', 'make_sound', 'lower_sound'],
'touch'    : ['run_away', 'touch_head', 'touch_jaw', 'touch_back',],

'eye'      : ['squint', 'blink', 'refresh', 'heart', 'lighting'],
'sound'    : ['meow_quick', 'meow_long', 'purr', 'angry', 'ha']
}

# power_on includes Scratch
ENERGY_LOW_TTH = 30
ENERGY_CONS = { # average + bias 偏移量
"play_tail" : [10, 3],  "lick_claw"  : [8, 3],  "snap"      : [10, 3], 'smell': [10, 3], 'sharpen_claw': [8, 3],
'run'       : [30, 10], 'walk'       : [15, 5], 'turn'      : [15, 5],
'lay_down'  : [3,  2],  'climb_down' : [3, 2],  'sit'       : [4, 2],
'stare_at'  : [8,  3],  'rub_human'  : [12, 5], 'step_on'   : [10, 5], 'stroke': [3, 2],
'rub_object': [12, 5],  'flap'       : [10, 5], 'pre_attack': [8, 3],
'hide'      : [15, 5],  'fear'       : [8, 2],  'tire'      : [4, 2],
'recharge'  : [2,  1],  'power_on'   : [15, 5],
'head_move' : [5,  2],  'tail_move'  : [5, 2],
'play_sound': [4,  1],  'eye_display': [2, 1]
}

# in seconds
TIME_MIN_CONS = {
"walk"    : 10, "run"         : 10, 'turn'   : 2,
"lie_down": 20, "sit"         : 12, "stand"  : 5,
'stretch' : 20, 'knead'       : 20, 'sharpen': 20, 'bury': 20, 'money': 20,
'stare_at': 20, 'walk_towards': 20,

'rub_object': 20, 'flap'      : 20, 'pre_attack'  : 20,
'run_away'  : 20, 'touch_head': 20, 'touch_jaw'   : 20, 'touch_back' : 20,
'stop'      : 0,  'make_sound': 1,  'start_listen': 0,  'lower_sound': 1
}

# ACTION
RELAX = 'relax'
ACTION_NUMBER_TTH = 4
FREE_MOVE_BEHAVIOUR = ['play', 'move', 'relax', 'special']

ACTIVITY = 0.2

# VISION
VISION_GET_OBG_PROB    = 0.3 * ACTIVITY   #4
VISION_GET_HUMAN_PROB  = 0.3 * ACTIVITY   #5
VISION_GET_QR_TTH      = 0.1              #5

# VOICE
VOICE_TTH              = 0.1 * ACTIVITY

NUMBER_OF_COMMANDS     = 15
SPECIAL_COMMANDS       = []

VOICE_DB_BASE          = 20
VOICE_DB_STEP          = 20
VOICE_DB_TTH           = 60

# TOUCH
TOUCH_TTH_1            = 0.55 * ACTIVITY  #0.15
TOUCH_TTH_2            = 0.3  * ACTIVITY

# DISTANCE
DISTANCE_TTH           = 0.5

# BATTERY
BATTERY_TTH            = 0.2
LOW_POWER_TTH          = 0.15

# POWER
PWR_TTH                = 0.042            #0.002

'''
    003-comfortableCat          - meow quick
    004-fierceCat               - meow quick
    010-sleepingCat             - meow long
    005-happyCat                - meow long

    006-hurryCat                - purr

    002-angrymoreCat            - angry 
    008-painCat                 - angry

    009-pitifulCat              - ha~
'''
