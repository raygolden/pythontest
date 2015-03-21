x = '*'*30
y = '*'*10
def show():
    print x
    for i in y:
        print i,i.rjust(29)
    print x
show()
