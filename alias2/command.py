import os
from getpass import getuser


class Alias:
    def __init__(self, pos, line):
        self.startPos = pos
        self.rawAlias = line

    def split(self):
        for i in range(0, len(self.rawAlias)):
            if self.rawAlias[i] == '=':
                break
        key = self.rawAlias[6:i]
        content = self.rawAlias[i + 1:len(self.rawAlias) - 1]
        return [key, content]


class Command():
    username = getuser()
    if username == 'root':
        path = '/root/.bashrc'
    else:
        path = '/home/%s/.bashrc' % username

    def __init__(self):
        self.nAlias = 0
        self.path = self.__class__.path
        self.alias = []
        with open(self.path, 'r') as bashrc:
            while True:
                pos = bashrc.tell()
                str = bashrc.readline()
                if len(str) == 0:
                    break
                if str[0:5] == 'alias':
                    self.alias.append(Alias(pos, str))
                    self.nAlias += 1

    def insert(self, num, str):
        with open(self.path, 'r') as bashrc:
            bashrc.\
                seek(self.alias[num].startPos + len(self.alias[num].rawAlias))
            after = bashrc.read()
        with open(self.path, 'a') as bashrc:
            bashrc.truncate(self.alias[num].startPos)
            bashrc.write(str + after)

    def add(self, key, content):
        line = 'alias %s="%s"\n' % (key, content)
        with open(self.path, 'a') as f:
            f.write(line)
        print('Add alias %r = %r successfully' % (key, content))

    def list(self):
        if self.nAlias == 0:
            print("You don't have any alias")
            return
        for index in range(0, self.nAlias):
            key, content = self.alias[index].split()
            print('%-2i %-8s:%s' % (index + 1, key, content))

    def edit(self, mode, num, new):
        num -= 1
        try:
            key, content = self.alias[num].split()
            if mode == 'key':
                line = 'alias %s=%s\n' % (new, content)
            elif mode == 'content':
                line = 'alias %s="%s"\n' % (key, new)
            self.insert(num, line)
        except IndexError:
            print('Alias is not exist')
        else:
            print("Edit alias 's %s number %i -> %r successfully\
                " % (mode, num + 1, new))

    def delAll(self):
        if self.nAlias == 0:
            print("You don't have any alias")
            return
        for index in range(self.nAlias - 1, -1, -1):
            self.insert(index, '')
        print('Delete all alias successfully')

    def optionDel(self, num):
        try:
            self.insert(num - 1, '')
        except IndexError:
            print('Alias is not exist')
        else:
            print('Delete alias number %i successfully' % num)

    def backup(self):
        source = self.path
        direct = self.path + '.backup'
        copyCmd = 'cp %s %s' % (source, direct)
        os.system(copyCmd)
        print('Backup successfully')

    def restore(self):
        direct = self.path
        source = self.path + '.backup'
        copyCmd = 'cp %s %s' % (source, direct)
        if os.path.exists(source):
            os.system(copyCmd)
            print('Restore successfully')
        else:
            print("You don't have backup file")
