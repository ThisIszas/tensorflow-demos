# -*- coding: utf-8 -*-
NUMBER = '0123456789'
CHAR_SMALL = 'abcdefghijklmnopqrstuvwxyz'
CHAR_BIG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

MAX_CAPTCHA = 4  # 测试1位的训练准确率
VALIDATE_STRING = NUMBER  # + CHAR_SMALL #+ CHAR_BIG
CHAR_SET_LEN = len(VALIDATE_STRING)

IMAGE_HEIGHT = 60
IMAGE_WIDTH = 160
FONT_SIZE = 35

MAX_ACCURACY = 0.5
