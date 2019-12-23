# Helper Functions
def bind(key, command, mode):
    """Bind key to command in mode."""
    config.bind(key, command, mode=mode)

def nmap(key, command):
    """Bind key to command in normal mode."""
    bind(key, command, 'normal')

# Zooming
nmap('<Ctrl-e>', 'zoom-in')
nmap('<Ctrl-n>', 'zoom-out')

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
c.hints.chars = 'tnseridhaosukv'
