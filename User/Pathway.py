# inspired by Rod Dodson's http://robdodson.me/blog/2012/05/14/hacking-the-path-variable-in-sublime-text/

import os

SYSTEM = '/usr/bin:/bin:/usr/sbin:/sbin'
LOCAL = '/usr/local/bin:/usr/local/sbin'
HOME = os.environ['HOME']  # uncomment if you want to use binaries from your home
# RVM = HOME + '/.rvm/bin:'

# Sublime's default path is
# /usr/bin:/bin:/usr/sbin:/sbin
# but we rebuild the path from zero to avoid redundancy
os.environ['PATH'] = ''
os.environ['PATH'] += HOME + '/bin'
os.environ['PATH'] += ':'
os.environ['PATH'] += LOCAL
os.environ['PATH'] += ':'
os.environ['PATH'] += SYSTEM
# os.environ['PATH'] += RVM

print('PATH = ' + os.environ['PATH'])
