from __future__ import print_function
import sys
sourceFile = sys.argv[1]
newFile = sys.argv[2]
new = open(newFile,'w+')
for line in open(sourceFile):
    list=line.split()
    if list[0]=='ATOM':
        start = line[:31]
        x =float(line[31:38])
        y = float(line[39:46])
        z = float(line[47:54])
        end = line[54:78]
        if abs(x - 139.996) < 25:
            if abs(y - 120.571) < 25:
                if abs(z - 132.262) < 25:  
                    print("%s%3.3f %3.3f %3.3f%s"%(start, x, y, z, end), file=new)
