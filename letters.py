import string
import yaml
import build_arcs as barc
from build_arcs import Dimentions

class Letter(object):
    def __init__(self, letter, builders, size=None, center_x=100, center_y=100):
        self.letter = letter
        self.builders = builders
        if size:
            self.make_letter(size, center_x, center_y)
        else:
            self.dimentions = None
            self.arcs = None

    def make_letter(self, size, center_x=100, center_y=100):
        self.dimentions = Dimentions(size, center_x, center_y)
        self.arcs = [builder(self.dimentions) for builder in self.builders]

    def set_size(self, size):
        if not self.dimentions:
            self.make_letter(size)
        else:
            center_x = dimentions.x
            center_y = dimentions.y
            self.make_letter(size, center_x, center_y)

    def place(self, center_x, center_y, size=None):
        def is_even(n):
            return n % 2 == 0
        if not size and self.dimentions:
            size = self.dimentions.size
        else:
            raise InputError('Letter %s has not yet been built. Please provide a size.' % self.letter)
        self.make_letter(size, center_x, center_y)

    def __repr__(self):
        return self.letter


class Letters(object):
    def __init__(self, size=None, file_name='letters.yaml'):
        self.builders = {'top': barc.top_arc,
                         'left': barc.left_arc,
                         'bottom': barc.bottom_arc,
                         'right': barc.right_arc,
                         'vertical': barc.vertical_center,
                         'horizontal': barc.horizontal_center,
                         'topright': barc.top_right_angle,
                         'bottomright': barc.bottom_right_angle,
                         'topleft': barc.top_left_angle,
                         'bottomleft': barc.bottom_left_angle,
                         'updiagonal': barc.up_diagonal,
                         'downdiagonal': barc.down_diagonal,
                         'notch': barc.notch,
                         'longvertical': barc.long_vertical,
                         'highbottomright': barc.high_bottom_right,
                         'highbottomleft': barc.high_bottom_left}
        self.parts = self.get_letter_parts(file_name)
        self.parts[' '] = []
        self.size = size

    def get_letter_parts(self, file_name):
        with open(file_name) as f:
            parts = yaml.load(f)
        return parts

    def new(self, letter):
        parts = self.parts[letter]
        builders = [self.builders[arc] for arc in parts]
        return Letter(letter, builders, self.size)

    def clean_text(self, text):
        whitelist = ''.join([string.ascii_lowercase, ' ', string.ascii_uppercase])
        clean = ''.join(filter(whitelist.__contains__, text))
        return clean.lower()

    def build_text(self, text, width):
        text = self.clean_text(text)
        width = min(width, len(text))
        length = -(-len(text)/width)
        X = [(w + 1) * self.size - self.size / 2.0 for w in range(width)]
        Y = [(l + 1) * self.size - self.size / 2.0 for l in range(length)]
        letters = []
        i = 0
        for t in text:
            l = self.new(t)
            x = (i % width + 1) * self.size - self.size / 2.0 
            y = (i / width + 1) * self.size - self.size / 2.0
            l.place(x, y)
            letters.append(l)
            i += 1
        return [l.arcs for l in letters], width * self.size, length * self.size

if __name__ == '__main__':
    letters = Letters(60)
    print letters.clean_text('enter \nth.e $Night')