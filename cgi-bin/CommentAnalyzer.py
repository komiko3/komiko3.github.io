#!/usr/bin/env python

import cgi

def main():
    form=cgi.FiledStorage()
    pos=form.getValue("pos","")
    print("Content-type:text/html\n")
    print("<html><body></body></html>")

        
if __name__=="__main__":
    main()
