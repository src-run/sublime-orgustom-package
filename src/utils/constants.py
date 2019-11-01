
##
 # This file is part of the `src-run/sublime-orton-package` project.
 #
 # (c) Rob Frawley 2nd <rmf@src.run>
 #
 # For the full copyright and license information, please view the LICENSE.md
 # file that was distributed with this source code.
 ##

from os.path import abspath, dirname, join
from sublime import packages_path

ORTON_PKG_ORG = 'src-run'
ORTON_PKG_KEY = 'sublime-orton-package'
ORTON_URL_WEB = 'https://github.com/{}/{}'.format(ORTON_PKG_ORG, ORTON_PKG_KEY)
ORTON_URL_GIT = '{}.git'.format(ORTON_URL_WEB)

ORTON_PATH_PKG_ROOT = abspath(join(dirname(abspath(__file__)), '..', '..'))

ORTON_FILE_CFG_MAIN = 'SublimeOrton.sublime-settings'
ORTON_PATH_CFG_MAIN = '{}/{}'.format(ORTON_PATH_PKG_ROOT, ORTON_FILE_CFG_MAIN)

ORTON_FILE_KEY_MAPS = 'Default ($PLATFORM).sublime-keymap'
ORTON_PATH_KEY_MAPS = '{}/{}'.format(ORTON_PATH_PKG_ROOT, ORTON_FILE_KEY_MAPS)

ORTON_FILE_CFG_CMDS = 'SublimeOrton.sublime-commands'
ORTON_PATH_CFG_CMDS = '{}/{}'.format(ORTON_PATH_PKG_ROOT, ORTON_FILE_CFG_CMDS)
