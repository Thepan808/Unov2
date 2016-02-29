
# Colors
RED = 'r'
BLUE = 'b'
GREEN = 'g'
YELLOW = 'y'

COLORS = (RED, BLUE, GREEN, YELLOW)

# Values
ZERO = '0'
ONE = '1'
TWO = '2'
THREE = '3'
FOUR = '4'
FIVE = '5'
SIX = '6'
SEVEN = '7'
EIGHT = '8'
NINE = '9'
DRAW_TWO = 'draw'
REVERSE = 'reverse'
SKIP = 'skip'

VALUES = (ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, DRAW_TWO,
          REVERSE, SKIP)

# Special cards
CHOOSE = 'colorchooser'
DRAW_FOUR = 'draw_four'

SPECIALS = (CHOOSE, DRAW_FOUR)

IMAGE_PATTERN = 'https://raw.githubusercontent.com/jh0ker/mau_mau_bot/' \
                'master/images/jpg/%s.jpg'
THUMB_PATTERN = 'https://raw.githubusercontent.com/jh0ker/mau_mau_bot/' \
                'master/images/thumb/%s.jpg'


class Card(object):

    def __init__(self, color, value, special=None):
        self.color = color
        self.value = value
        self.special = special

    def __str__(self):
        if self.special:
            return self.special
        else:
            return '%s_%s' % (self.color, self.value)

    def __repr__(self):
        return ' '.join([s.capitalize() for s in str(self).split('_')])

    def __eq__(self, other):
        return str(self) == str(other)

    def get_image_link(self):
        return IMAGE_PATTERN % str(self)

    def get_thumb_link(self):
        return THUMB_PATTERN % str(self)


def from_str(string):
    if string not in SPECIALS:
        color, value = string.split('_')
        return Card(color, value)
    else:
        return Card(None, None, string)
