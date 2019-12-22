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
