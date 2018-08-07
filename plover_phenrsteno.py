# phenrsteno

#   | ə p t w     f t ʃ l i |  ~>  | # X p T w     f t ʃ l i |
#   | s b d r  *  n d g z ə |  ~>  | # s b D r  *  n d g z x |
#   |                       |  ~>  | #                       |
#   |      a e   I U        |  ~>  | #      a e   I U        |

KEYS = (
    '#',
    'X-', 's-', 'p-', 'b-', 'T-', 'D-', 'w-', 'r-',
    'a-', 'e-',
    '*',
    '-I', '-U',
    '-f', '-n', '-t', '-d', '-ʃ', '-g', '-l', '-z', '-i', '-x'
)

IMPLICIT_HYPHEN_KEYS = ('a-', 'e-', '5-', '0-', '-I', '-U', '*')

#PREFIX_KEYS = ('X-') # Seems like prefix keys are not implemented in Plover
SUFFIX_KEYS = ('-f', '-n', '-d', '-ʃ', '-g', '-l', '-z', '-i', '-x')

NUMBER_KEY = '#'

NUMBERS = {
    'X-': '1-',
    'p-': '2-',
    'T-': '3-',
    'w-': '4-',
    'a-': '5-',
    'e-': '0-',
    '-f': '-6',
    '-t': '-7',
    '-ʃ': '-8',
    '-l': '-9',
}

UNDO_STROKE_STENO = '*'

ORTHOGRAPHY_RULES = [
    # == +ly ==
    # artistic + ly = artistically
    (r'^(.*[aeiou]c) \^ ly$', r'\1ally'),
        
    # == +ry ==      
    # statute + ry = statutory
    (r'^(.*t)e \^ ry$', r'\1ory'),
        
    # == t +cy ==      
    # frequent + cy = frequency (tcy/tecy removal)
    (r'^(.*[naeiou])te? \^ cy$', r'\1cy'),

    # == +s ==
    # establish + s = establishes (sibilant pluralisation)
    (r'^(.*(?:s|sh|x|z|zh)) \^ s$', r'\1es'),
    # speech + s = speeches (soft ch pluralisation)
    (r'^(.*(?:oa|ea|i|ee|oo|au|ou|l|n|(?<![gin]a)r|t)ch) \^ s$', r'\1es'),
    # cherry + s = cherries (consonant + y pluralisation)
    (r'^(.+[bcdfghjklmnpqrstvwxz])y \^ s$', r'\1ies'),

    # == y ==
    # die+ing = dying
    (r'^(.+)ie \^ ing$', r'\1ying'),
    # metallurgy + ist = metallurgist
    (r'^(.+[cdfghlmnpr])y \^ ist$', r'\1ist'),
    # beauty + ful = beautiful (y -> i)
    (r'^(.+[bcdfghjklmnpqrstvwxz])y \^ ([a-hj-xz].*)$', r'\1i\2'),

    # == e ==
    # write + en = written
    (r'^(.+)te \^ en$', r'\1tten'),
    # free + ed = freed 
    (r'^(.+e)e \^ (e.+)$', r'\1\2'),
    # narrate + ing = narrating (silent e)
    (r'^(.+[bcdfghjklmnpqrstuvwxz])e \^ ([aeiouy].*)$', r'\1\2'),

    # == misc ==
    # defer + ed = deferred (consonant doubling)   XXX monitor(stress not on last syllable)
    (r'^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ ([aeiouy].*)$', r'\1\2\2\3'),
]

ORTHOGRAPHY_RULES_ALIASES = {
    'able': 'ible',
}

ORTHOGRAPHY_WORDLIST = 'american_english_words.txt'

KEYMAPS = {
    'Keyboard': {
        # Number bar
        '#' : ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],

        # Left-hand consonants      #  1  2  3  4
        'X-': ['q'], 's-': ['a'],   #  X  p  T  w
        'p-': ['w'], 'b-': ['s'],   #  s  b  D  r 
        'T-': ['e'], 'D-': ['d'],
        'w-': ['r'], 'r-': ['f'],

        # Left-hand vowels          #  5  0
        'a-': ['c'], 'e-': ['v'],   #  a  e

        # Undo key                  #  *
        '*' : ['t', 'g', 'y', 'h'], 

        # Right-hand vowels         #  I  U
        '-I': ['n'], '-U': ['m'],

        # Right-hand consonants     #  6  7  8  9
        '-f': ['u'], '-n': ['j'],   #  f  t  ʃ  l  i
        '-t': ['i'], '-d': ['k'],   #  n  d  g  z  x
        '-ʃ': ['o'], '-g': ['l'],
        '-l': ['p'], '-z': [';'],
        '-i': ['['], '-x': ['\''],

        # Other
        'arpeggiate': ['space'],
        'no-op': ['z', 'x', 'b', ',', '.', '/', ']', '\\']
    }
}

DICTIONARIES_ROOT = 'asset:plover:assets'
DEFAULT_DICTIONARIES = ()
