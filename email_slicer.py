
status = 0
while status == 0: 
    #get user email address 
    email = input("What is your email?: ").strip()
    #Validate email
    check1 = email.find("@")
    check2 = email.find(" ")
    if check1 == -1: 
        print ("Please enter valid email (e.g. gonyea.luke@gmail.com).Please re-enter")
    elif check2 != -1:
        print ("Emails cannot contain spaces.Please re-enter.")
    else: 
        #slice out user name
        user_name = email[:(email.find("@"))]
        #slice domain name
        provider = email[(email.find("@")+1):]
        #format message 
        message = "Your user name is {1} and email provider is {0}".format(provider,user_name)
        #display output message 
        print(message)
        #end while loop
        status = 1

