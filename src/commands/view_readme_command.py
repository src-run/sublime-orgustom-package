
##
 # This file is part of the `src-run/sublime-orton-package` project.
 #
 # (c) Rob Frawley 2nd <rmf@src.run>
 #
 # For the full copyright and license information, please view the LICENSE.md
 # file that was distributed with this source code.
 ##

from sublime_plugin import TextCommand

class HtmlprettifyOpenHelpCommand(TextCommand):
    def run(self, _):
        open_new_tab("https://github.com/victorporof/Sublime-HTMLPrettify/blob/master/README.md")