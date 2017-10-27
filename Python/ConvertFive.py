#! /usr/bin/env python

userinput = int(raw_input("Enter an integer : "))


class CFive():
    def convertfive(self, n):
        self.n = n
        out = []
        while (n > 0):
            r = n%10
            if (r == 0):
                r = 5
                out.append(r)
            else:
                out.append(r)
            n = n/10
        out1 = out[::-1]
        print ''.join(map(str,out1))
        return
xyz = CFive()
xyz.convertfive(userinput)
