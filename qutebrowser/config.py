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
