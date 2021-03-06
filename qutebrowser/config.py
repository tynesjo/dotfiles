# Helper Functions
def bind(key, command, mode):
    """Bind key to command in mode."""
    config.bind(key, command, mode=mode)

def nmap(key, command):
    """Bind key to command in normal mode."""
    bind(key, command, 'normal')

def imap(key, command):
    """Bind key to command in insert mode."""
    bind(key, command, 'insert')

def cmap(key, command):
    """Bind key to command in command mode."""
    bind(key, command, 'command')

def tmap(key, command):
    """Bind key to command in caret mode."""
    bind(key, command, 'caret')

def pmap(key, command):
    """Bind key to command in passthrough mode."""
    bind(key, command, 'passthrough')

def unmap(key, mode):
    """Unbind key in mode."""
    config.unbind(key, mode=mode)

def nunmap(key):
    """Unbind key in normal mode."""
    unmap(key, mode='normal')

# Settings
# ** Session
# always restore opened sites when opening qutebrowser
c.auto_save.session = True
c.session.lazy_restore = True

# Tabs
# open new tabs (middleclick/ctrl+click) in the background
c.tabs.background = True
# select previous tab instead of next tab when deleting current tab
c.tabs.select_on_remove = 'prev'
# open unrelated tabs after the current tab not last
c.tabs.new_position.unrelated = 'next'
c.tabs.min_width = 200
c.tabs.title.format = '{index}{private}{title_sep}{current_title}'

c.statusbar.position = "top"

# Zooming
nmap('<Ctrl-e>', 'zoom-in')
nmap('<Ctrl-n>', 'zoom-out')
c.zoom.default=120

# Style Sheets
c.content.user_stylesheets = [
    '~/qutebrowser/custom-solarized/custom-mono.css'
]

# Cycle Through Style Sheets
config.bind(
    '<Ctrl-s>',
    'config-cycle content.user_stylesheets ~/qutebrowser/custom-solarized/custom-mono.css ~/qutebrowser/custom-solarized/custom-solarized.css ""'
)

# Pass
config.bind('p,', 'spawn --userscript qute-pass --dmenu-invocation dmenu')
config.bind('Pw', 'spawn --userscript qute-pass --dmenu-invocation dmenu --password-only')

# Hiding statusbar and/or tabs

config.bind('xx', 'config-cycle statusbar.show always in-mode ;; config-cycle tabs.show always switching')
config.bind('xt', 'config-cycle tabs.show always switching')
config.bind('xb','config-cycle statusbar.show in-mode')

# Hints (Colemak-easy characters only)
c.hints.chars = 'tnseridhao'
c.hints.auto_follow = 'always'

# Editor
c.editor.command = ['urxvt', '-e', 'env', 'TERM=xterm-256color', 'emacsclient', '-nw', '-s', 'instance1', '{}']
nmap('gF', 'view-source --edit')
imap('<Ctrl-i>', 'open-editor')

# Colemak Customizations
nmap('l', 'search-next')
nmap('L', 'search-prev')

c.scrolling.bar = 'never'

# Media
c.content.autoplay = False

# Hints
c.colors.hints.bg = \
    'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 247, 133, 1), ' \
    + 'stop:1 rgba(255, 197, 66, 1))'

nmap('t.', 'config-source')
nmap('ti', 'inspector')

# Downloads
#c.downloads.location.directory = '~/move'
#c.downloads.location.prompt = False
#c.downloads.open_dispatcher = 'dl_move {}'

# Search Keywords
c.url.searchengines = \
    {'DEFAULT': 'https://www.google.com/search?q={}',
     'go': 'https://www.google.com/search?q={}',
     'd': 'https://duckduckgo.com/?q={}',
     'w': 'http://en.wikipedia.org/w/index.php?search={}',
     'y': 'http://www.youtube.com/results?search_query={}',
     'gh': 'http://github.com/search?q={}',
    }


# Colemak

tmap('h', 'move-to-next-line')
tmap('n', 'move-to-next-line')
tmap('e', 'move-to-prev-line')
tmap('i', 'move-to-next-char')

nmap('n', 'scroll-page 0 0.2')
nmap('e', 'scroll-page 0 -0.2')
nmap('N', 'tab-prev')
nmap('E', 'tab-next')

# Passthrough mode (all keys go to website)
nmap(',', 'enter-mode passthrough')
pmap('<Escape>', 'leave-mode')

# open new private window
nmap('tp', 'open -p')

# lose scroll left
nmap('h', 'back')
nmap('H', 'forward')

# lose scroll right
nmap('l', 'tab-focus last')
nmap('b', 'set-cmd-text --space :buffer')

nunmap('i')

nmap('\'', 'enter-mode insert' )

# Google Accounts

config.set('content.headers.user_agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/77.0', 'https://accounts.google.com/*')

