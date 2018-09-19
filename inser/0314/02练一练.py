def open_run():
    f=open('user1.txt','w')
    f.write('helloworld')
    f.close()
def read_book():
    f=open('user1.txt','r')
    print(f.read())
    f.close()
open_run()
read_book()
