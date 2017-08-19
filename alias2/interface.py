import click
from alias2.command import *


@click.group()
def init():
    '''A simple project written in Python 3.
    It helps you creating and managing alias in Terminal.
    '''
    pass


@init.command()
@click.argument('key', required=True)
@click.argument('content', required=True)
def add(key, content):
    '''Add new alias'''
    Command().add(key, content)


@init.command()
def list():
    '''Displays your alias'''
    Command().list()


@init.command()
@click.argument('aliasnum', required=True, type=int)
@click.argument('new', required=True)
@click.option('--key', '-k', 'mode', flag_value='key',
              help='Edit key of your alias')
@click.option('--content', '-c', 'mode', flag_value='content',
              help='Edit content of your alias')
def edit(mode, aliasnum, new):
    '''Edit your alias'''
    Command().edit(mode, aliasnum, new)


@init.command()
@click.argument('aliasnum', required=False, type=int)
@click.option('--all', '-a', 'mode', flag_value='all',
              help='Delete your alias')
def delete(mode, aliasnum):
    '''delete your alias'''
    if mode == 'all':
        print('Delete all alias? [y/n]')
        answer = input()
        if answer == 'n' or answer == 'N':
            return
        Command().delAll()
    else:
        Command().optionDel(aliasnum)


@init.command()
def backup():
    '''Backup your alias'''
    Command().backup()


@init.command()
def restore():
    '''Restore your alias'''
    Command().restore()


if __name__ == '__main__':
    init()
