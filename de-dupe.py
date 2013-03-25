from itertools import groupby
from operator import itemgetter

lines = [line.split() for line in open('sha1s.txt')]
others = open('sha1s-2.txt', 'w')

for (key, group) in groupby(lines, key=itemgetter(0)):

    files = map(itemgetter(1), group)
    
    if len(files) != 2:
        if len(files) > 2:
            for file in files:
                print >> others, key, file

        continue
    
    parts1 = files[0].split('/')
    parts2 = files[1].split('/')
    
    if parts1[2].isdigit():
        print 'git rm -r', '/'.join(parts1[:3])
    
    elif parts2[2].isdigit():
        print 'git rm -r', '/'.join(parts2[:3])
    
    else:
        print 'dunno', files

others.close()
