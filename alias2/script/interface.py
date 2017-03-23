import click
from alias2.script.command import *
from pkg_resources import resource_filename

userData = None
bashLink = None

userLink = resource_filename('alias2.data', 'user.data')


@click.group()
def init():
    '''A simple project written in Python 3.
    It helps you creating and managing alias in Terminal.
    '''
    global bashLink
    while True:
        try:
            # file save user data
            userData = open(userLink, 'r')
            user = userData.readline()
            if user == 'root':
                bashLink = '/root/.bashrc'
            else:
                bashLink = '/home/%s/.bashrc' % user  # check user is true
            with open(bashLink):
                pass
        except:
            resetFunc()
        else:
            break


@init.command()
@click.argument('key', required=True)
@click.argument('content', required=True)
def add(key, content):
    '''Add new alias'''
    command(bashLink).add(key, content)


@init.command()
def list():
    '''Displays your alias'''
    command(bashLink).list()


@init.command()
@click.argument('aliasnum', required=True, type=int)
@click.argument('new', required=True)
@click.option('--key', '-k', 'mode', flag_value='key',
              help='Edit key of your alias')
@click.option('--content', '-c', 'mode', flag_value='content',
              help='Edit content of your alias')
def edit(mode, aliasnum, new):
    '''Edit your alias'''
    command(bashLink).edit(mode, aliasnum, new)


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
        command(bashLink).delAll()
    else:
        command(bashLink).optionDel(aliasnum)


@init.command()
def backup():
    '''Backup your alias'''
    command(bashLink).backup()


@init.command()
def restore():
    '''Restore your alias'''
    command(bashLink).restore()


@init.command()
def reset():
    '''Reset infomation of user'''
    resetFunc()


def resetFunc():
    '''Reset infomation of user'''
    user = input("enter user: ")
    with open(userLink, 'w') as userData:  # create file
        userData.write(user)


if __name__ == '__main__':
    init()
