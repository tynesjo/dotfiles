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


# Zooming
nmap('<Ctrl-e>', 'zoom-in')
nmap('<Ctrl-n>', 'zoom-out')
c.zoom.default=120

# Style Sheets
c.content.user_stylesheets = [
    '~/qutebrowser/qutebrowser_dark_solarized/solarized-dark.css',
    '~/qutebrowser/qutebrowser_dark_solarized/custom_solarized.css'
]

# Cycle Through Style Sheets
config.bind(
    '<Ctrl-s>',
    'config-cycle content.user_stylesheets ~/qutebrowser/qutebrowser_dark_solarized/custom_solarized.css ""'
)

# Pass
config.bind('p,', 'spawn --userscript qute-pass --dmenu-invocation dmenu')
config.bind('Pw', 'spawn --userscript qute-pass --dmenu-invocation dmenu --password-only')

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
    {'DEFAULT': 'https://www.google.com/search?lr=lang_en&q={}',
     'd': 'https://duckduckgo.com/?q={}',
     'w': 'http://en.wikipedia.org/w/index.php?search={}',
    }
