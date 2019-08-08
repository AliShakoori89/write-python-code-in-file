#import string
print("option: ")
print("              1.  Enter a name an date of birth ")
print("              2.  search ")
print("              3.  delete ")
a=int(input("choice 1 or 2 :"))

if a==1: 
    f=open('list_afrad.txt','a')   
    name=str(input('enter name: '))
    family=str(input('enter family: '))
    date_of_birth=str(input('enter date of brith: '))
    f.write('\n'+name+'    '+family+'     '+date_of_birth)

elif a==2:
    f = open("list_afrad.txt","r")
    word = input("Enter word to search data : ")
    for line in f.readlines():
        #if word is not line:
        #    print("dont have data in text")
        if word is line: 
            print(line)
elif a==3:
    def deleteLine():
        f = open('list_afrad.txt')
        output = []
        word = input("Enter word to delete data : ")
        for line in f:
            if not line.startswith(word):
                output.append(line)
        f.close()
        f = open('list_afrad.txt', 'w')
        f.writelines(output)
        f.close()
    deleteLine()