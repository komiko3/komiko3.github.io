import cgi

def main():
    form=cgi.FiledStorage()
    pos=form.getValue("pos","")
    print("<html><body></body></html>")

        
if __name__=="__main__":
    main()
