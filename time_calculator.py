def add_time(start, duration, dw=None):
    my_str1 = start.split()
    my_str2 = my_str1[0].split(":")
    my_str3 = duration.split(":")

    new_time=""
    ampm=0
    a1=None
    a2=None
    a3=None
    a4=None

    #am/pm trigger
    if my_str1[1]=="AM":
        ampm=1
    else:
        ampm=2


    #sum h
    sum1=(int(my_str2[0])+int(my_str3[0]))
    h1=sum1//12
    h2=sum1%12

    #sum min
    sum2=(int(my_str2[1])+int(my_str3[1]))
    m1=sum2//60
    m2=sum2%60

    #min
    if sum2>60:
        h2+=1
            
    if (sum1+m1)//12==0:
        a1=str(sum1) + ":"
        if m1==0:
            a1+=str(sum2).rjust(2,"0")

    #apmp
    ampm+=(sum1+m1)//12
    apmp2=ampm % 2 
    if ampm % 2 ==0:
        a2="PM"
    else:
        a2="AM"

    if (sum1+m1)//12>0:
        a1=str(h2) + ":"
        if m1==0:
            a1+=str(sum2)
        else:
            a1+=str(m2).rjust(2,"0")

    #days later
    if ampm>2:
        laterday = ampm//2
        if laterday==1:
            a4="(next day)"
        if laterday>=2:
            a4="("+ str(laterday) + " days later)"


    #get number
    if dw!= None:

        dayofweek=["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        input_dayofweek = dw.lower()

        i=dayofweek.index(input_dayofweek)
        i_plues = ampm//2
        if ampm >2: 
            i=i+i_plues
            ii=i%7
            a3=dayofweek[ii]
        else:
            a3=input_dayofweek

    if a3==None and a4==None:
        new_time = a1+" "+a2
    elif  a4==None:
        new_time = a1+" "+a2+", "+a3.capitalize()
    elif  a3==None:
        new_time = a1+" "+a2+" "+a4
    else:        
        new_time = a1+" "+a2+", "+a3.capitalize()+" "+a4

    return new_time
