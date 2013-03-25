from itertools import groupby
from operator import itemgetter

lines = [line.split() for line in open('sha1s-2.txt')]
others = open('sha1s-3.txt', 'w')

for (key, group) in groupby(lines, key=itemgetter(0)):

    files = map(itemgetter(1), group)
    
    if len(files) != 4 and False:
        for file in files:
            print >> others, key, file

        continue
    
    files = sorted(files, key=lambda f: (len(f), f))
    
    while len(files) > 1:
        parts = files[0].split('/')
        
        if not parts[2].isdigit():
            break
        
        print 'git rm -r', '/'.join(parts[:3])
        files = files[1:]

    for (index, file) in reversed(list(enumerate(files))):
        if len(files) == 1:
            # leave one
            break
    
        parts = file.split('/')
        base = '/'.join(parts[:3])
        
        if 'test' in parts[2]:
            print 'git rm -r', base
            files.pop(index)
        
    for (index, file) in reversed(list(enumerate(files))):
        if len(files) == 1:
            # leave one
            break
    
        parts = file.split('/')
        base = '/'.join(parts[:3])
        
        if parts[2].isdigit():
            print 'git rm -r', base
            files.pop(index)
        
    for (index, file) in reversed(list(enumerate(files))):
        if len(files) == 1:
            # leave one
            break
    
        parts = file.split('/')
        base = '/'.join(parts[:3])
        
        if base[-2:] in ('-2', '-3', '-4', '-5', '-6', '-7'):
            print 'git rm -r', base
            files.pop(index)
        
    if len(files) > 1:
        for file in files:
            print >> others, key, file

others.close()
