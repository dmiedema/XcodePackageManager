#!/usr/bin/env python

import argparse
import subprocess
import sys

####
# Have some Color for printing
####
class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'

    def header(self, s):
        print self.HEADER + s + self.ENDC
    def ok_blue(self, s):
        print self.OKBLUE + s + self.ENDC
    def ok_gree(self, s):
        print self.OKGREEN + s + self.ENDC
    def warning(self, s):
        print self.WARNING + s + self.ENDC
    def fail(self, s):
        print self.FAIL + s + self.ENDC
    def bold(self, s, mod=''):
        print self.BOLD + mod + s + self.ENDC
    def underline(self, s, mod=''):
        print self.UNDERLINE + mod + s + self.ENDC


colors = bcolors()
####
# Arguments
####
parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description="""
XcodePackageManager

Manage your Xcode Plugins, Templates & Themes via command line utility
with a configuration file,.
""",
    epilog="""
Because I've grown to hate Alcatraz...
""")

parser.add_argument("--init", action="store_true", help="""
Initialize XcodePackageManager folder & file setup.
Configuration information is stored in
`$HOME/.xcodepackagemanager/`

If the directory already exists this is essentially a `no-op`
""")

parser.add_argument("--enabled", action="store_true", help="""
List the currently enabled Plugins, Themes, and Templates.
""")

parser.add_argument("--disabled", action="store_true", help="""
List all disabled plugins
""")

# parser.add_argument("all", action="store_true", help="""
# List all plugins, themes, and templates whether they are enabled
# or disabled.
# """)

parser.add_argument("--update", action="store_true", help="""
Update the given repos
""")

parser.add_argument("--fix",  action="store_true", help="""
Update all installed plugins Info.plist and add all installed
version of Xcode to the plist
""")

parser.add_argument("--disable", action="store_true", help="""
Disable any plugins with a name matching the input string.
""")

parser.add_argument("--enable", action="store_true", help="""
Enable any plugins with a name matching the input string.
""")

parser.add_argument("--add", action="store_true", help="""
Add a given repo with a specified type.
Default type is `plugin`
""")

parser.add_argument("--type", type=str, choices=['plugin', 'theme', 'template'], default='plugin', help="""
Type of repo this is.
Default is `plugin`
""")

parser.add_argument("--branch", dest='branch', default='master', type=str, help="""
Git branch of the repo to checkout and build from
""")

parser.add_argument("--tag", dest='tag', type=str, help="""
Git tag to checkout and build from
""")

parser.add_argument("input", nargs='?', metavar='INPUT', type=str, help="""
If adding
    Full URL of the git repo to clone for the item
If enabling/disabling
    Name/String to match. Will match anywhere in the string
    but will not 'fuzzy' match to anywhere in the string.
""")

# Setup Default Values
parser.set_defaults(all=False, add=False, init=False, update=False, disabled=False, enabled=False, fix=False, type='plugin', branch='master', tag=None, input=None)

args = parser.parse_args()


def main():
    colors.header("Having trouble? Check the help! `--help`")
    print ""
    print args


####
# File Parser
####
def check_file():
    return False

####
# Helpers
####
def run_command(cmd_array, shell=False):
    p = subprocess.Popen(cmd_array, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=shell)
    out, err = p.communicate()
    return out

if __name__ == "__main__":
    main()

