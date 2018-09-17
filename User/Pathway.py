# inspired by Rod Dodson's http://robdodson.me/blog/2012/05/14/hacking-the-path-variable-in-sublime-text/

import os

SYSTEM = '/usr/bin:/bin:/usr/sbin:/sbin'
LOCAL = '/usr/local/bin:/usr/local/sbin'
HOME = os.environ.get('HOME', None)
if HOME is not None:
    HOME_BIN = HOME + '/bin'
    CARGO_BIN = HOME + '/.cargo/bin'
    # RVM_BIN = HOME + '/.rvm/bin'
else:
    HOME_BIN = None
    CARGO_BIN = None
    # RVM_BIN = None
HOME = os.environ['HOME']  # uncomment if you want to use binaries from your home
CARGO = HOME + '/.cargo/bin'
LUA = HOME + '/Developer/hererocks/lua5.3/bin'
# RVM = HOME + '/.rvm/bin'

# Sublime's default path is
# /usr/bin:/bin:/usr/sbin:/sbin
# but we rebuild the path from zero to avoid redundancy on multiple reload
paths = [path for path in (HOME_BIN, LOCAL, CARGO_BIN, SYSTEM) if path is not None]
os.environ['PATH'] = ':'.join(paths)

print('PATH = ' + os.environ['PATH'])
