def we_wish_you():
   text="We wish you a Merry Christmas"
   for i in range(3):
        if i==3-1:
           text=text+" and a happy new year\n"
        print(text)

def good_tidings_we_bring():
    print("\n"+"Good tidings we bring to you and your kin")
    print("We wish you a Merry Christmass and a Happy new Year")
    print("\n")

def wishes(text1,text2,times):
    for i in range(times):
        if i==times-1:
            text1=text1+text2
        print(text1)


we_wish_you()
good_tidings_we_bring()
wishes("Now bring us some figgy pudding",", now bring some out here\n",3)
good_tidings_we_bring()
wishes("we wont go until we get some"," , so bring some out here\n",3)
good_tidings_we_bring()
we_wish_you()
    