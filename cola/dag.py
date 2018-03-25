from __future__ import division, absolute_import, unicode_literals
import argparse
import os
import sys

from cola import app
from cola.widgets.dag import git_dag


def main():
    """Run git-dag"""
    args = parse_args()
    return args.func(args)


def winmain():
    return app.winmain(main)


def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser()
    parser.set_defaults(func=cmd_dag)

    app.add_common_arguments(parser)
    parser.add_argument('-c', '--count', '--max-count', metavar='<count>',
                        type=int, default=1000,
                        help='number of commits to display')
    parser.add_argument('args', nargs='*', metavar='<args>',
                        help='git log arguments')
    args, rest = parser.parse_known_args()
    if rest:
        # splice unknown arguments to the beginning ~
        # these are forwarded to git-log(1).
        args.args[:0] = rest
    return args


def cmd_dag(args):
    """Run git-dag via the `git cola dag` sub-command"""
    context = app.application_init(args)
    view = git_dag(context.model, args=args, settings=args.settings)
    return app.application_start(context, view)
