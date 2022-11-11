import os
import datetime
import pyttsx3



def diary():
    print('''Things to do:
    1. Write
    2. Read
    3. Delete
    4. Change username
    5. Change password
    6. Reading(Speak)
    7. Change name
     ''')
    try:option = int(input("Type the number of function to do: "))
    except: print(Exception)







    if option==1:

        dfday = input("Day: ")
        dftime = input("Time: ")
        dfdate = input("Date: ")
        dfsubject = input("Subject: ")
        dfmessage = input("Message: ")
        dfendl = input("Type the ending line: ")

        dfdayo = str('Day:',dfday)
        dftimeo = str('Time:',dftime)
        dfdateo = str('Date:',dfdate)
        dfsubjecto = str('Subject:',dfsubject)
        dfmessageo = str('Message:',dfmessage)
        dfendlo = str(dfendl)

        newfilename = input("Type the name of the file: ")
            

        if newfilename == ("date"):
            a = input("Auto, type y/n: ")
            if a==("y"):
                newfilename=str(str(datetime.date())+str('.txt'))
            else:
                newfilename=dfdate
        try:
                acb = open(newfilename, 'x')
        except:
            print("Sorry this name is already taken retry")
            a = input("Type to exit for not losing your old data: ")
            if a==("exit"):
                exit()

   
        dfwritefile = open(newfilename, 'w')
        dfwritefile.writelines(dfdayo)
        dfwritefile.writelines('\n')
        dfwritefile.writelines(dftimeo)
        dfwritefile.writelines('\n')
        dfwritefile.writelines(dfdateo)
        dfwritefile.writelines('\n')
        dfwritefile.writelines(dfsubjecto)
        dfwritefile.writelines('\n')
        dfwritefile.writelines(dfmessageo)
        dfwritefile.writelines('\n')
        dfwritefile.writelines(dfendlo)
        dfwritefile.close()
    




    if option==2:
        print(os.listdir())
        rfn = input("Type the name of the file you want to read: ")
        drf = open(rfn, 'r')
        drfo = drf.read()
        print(drfo)



    

    if option==3:
        print(os.listdir())
        dfn = input("Type the nam eof the file you want to delete: ")
        ddf = os.remove(dfn)
        print("Successfully deleted...")
        
    

    if option==4:
        print("---------Change username----------")
        oldusername = input("Type the old username: ")
        newusername = input("Type the new username: ")

        userfo = open('user.txt', 'r')
        username = userfo.read()
        if oldusername==username:
            abc=open('user.txt','w')
            cba=abc.write(newusername)
            print("Successfully changed the username")
        else:
            print("Please retry...")
        
        abc.close()


    


    if option==5:
        print("-------Change password--------")
        oldpassword = input("Type the old password: ")
        newpassword = input("Type the new password: ")

        passfo = open('user.txt', 'r')
        password = passfo.read()
        if oldpassword==password:
            abc=open('pass.txt','w')
            cba=abc.write(newpassword)
            print("Successfully changed the password")
        else:
            print("Please retry...")
        
        abc.close()



    def speak(audio, a):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate',a)
        engine.say(audio)
        engine.runAndWait()


    if option==6:
        print(os.listdir())
        rfn = input("Type the name of the file you want to read: ")
        drf = open(rfn, 'r')
        drfo = drf.read()
        bn = int(input("Type the rate of speaking for speech: "))
        speak(drfo, bn)




    if option==7:
        a = input("Type the new name: ")
        abc = open('name.txt', 'w')
        abc.write(a)
        abc.close()





def acception():
    namefo = open('name.txt', 'r')
    name = namefo.read()
    print('Welcome back,',name)
    namefo.close()


    usernameinp = input("Type the username: ")
    passwordinp = input("Type the password: ")


    userfo = open('user.txt', 'r')
    username = userfo.read()

    passfo = open('pass.txt', 'r')
    password = passfo.read()

    if usernameinp==username and passwordinp==password:
        diary()
        userfo.close()
        passfo.close()
        
    else:
        a = input("Wanna retry... y/n: ")
        if a==('y'):
            acception()
        else:
            print("Goodbye...")
        exit()



def ini():
    try: open('name.txt', 'r')
    except: 
        b=open('name.txt', 'x')
        a = input("Please type a name: ")
        b.write(a)
        b.close()
    try: open('user.txt', 'r')
    except: 
        b=open('user.txt', 'x')
        a = input("Please type a username: ")
        b.write(a)
        b.close()
    try: open('pass.txt', 'r')
    except: 
        b=open('pass.txt', 'x')
        a = input("Please type a pass: ")
        b.write(a)
        b.close()


ini()

acception()



    