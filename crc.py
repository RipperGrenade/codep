import subprocess
import os
import sys

rcfile = '/Users/mark/.bash_profile.bak2'
albin = '/usr/local/bin/al'
newrcf = '/Users/mark/.bash_profile.cpy'

if os.path.exists(newrcf):
    print('removing cpy file')
    os.remove(newrcf)
cmdl = ['touch', newrcf]
try:
    rtn = subprocess.check_output(cmdl)
except subprocess.CalledProcessError as err:
    print('al called err::', err.returncode, '--', err.output)
    sys.exit(1)

print('succeed create cpy file')

with open(newrcf, 'at') as newrchandle:
    with open(rcfile, 'r+') as rchandle:
        filec = rchandle.read()
        for line in filec.splitlines():
            print('reading line\n')
            tmpl1 = line.strip('\n').split('="')
            if line.startswith('alias ') and 'cd ' in tmpl1[1] and '..' not in tmpl1[1]:
                (head, sep, tail) = tmpl1[1].partition('cd ')
                key = tail.split(';')[0]
                listtmp = tmpl1[0].split(' ')
                key1 = listtmp[1]
                cmdlist = [albin, key1, key]
                try:
                    rtn = subprocess.check_output(cmdlist)
                except subprocess.CalledProcessError as err:
                    print("called error::", err.returncode, '--', err.output)
                    print('al error::', key1, '--', key, '==', cmdlist)
            else:
                newrchandle.seek(0, 2)
                newrchandle.write(line)
                newrchandle.write('\n')
