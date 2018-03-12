#!/usr/bin/env python3
import sys
import create
import update


def main(action):
    if action == 'create':
        create.Initializer.initialize()
    if action == 'update':
        update.Updater.update_and_print()

if __name__ == '__main__':
    main(sys.argv[1])
