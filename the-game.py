import question
import random
import time
import sys

# input questions and answers to be shuffled

q1 = question.Qst("I can't believe Netflix is using ____ to promote House of Cards.", 1)
q2 = question.Qst("I'm not going to lie. I despise ____. There, I said it.", 1)
q3 = question.Qst("Cancel all my meetings. We've got a situation with ____ that require my immediate attendtion.", 1)
q4 = question.Qst("Our relationship is strictly professional. Let's not complicate things with ____.", 1)
q5 = question.Qst("A wise man said, 'Everything is about s**. Except s**. S** is about ____.'", 1)
q6 = question.Qst("We're not like other news organizations. Here at Slugline, we welcome ____ in the office.", 1)
q7 = question.Qst("If you need him to, Remy Danton can pull some strings and get you ____, but it'll cost you.", 1)
q8 = question.Qst("Corruption. Betrayal. ____. Coming soon to Netflix, 'House of ____'.", 2)
q9 = question.Qst("Because you enjoyed ____, we thought you'd like _____.", 2)

a1 = question.Ans("A childless marriage")
a2 = question.Ans("Making it look like a suicide.")
a3 = question.Ans("Strangling a dog to make a point to the audience.")
a4 = question.Ans("Getting eaten out while on the phone with Dad.")
a5 = question.Ans("Punching a congressman in the face.")
a6 = question.Ans("An older man.")
a7 = question.Ans("A much younger woman.")
a8 = question.Ans("My constituents.")
a9 = question.Ans("Ribs so good they transcend race and class.")
a10 = question.Ans("The sensitive European photographer who's f**king my wife.")
a11 = question.Ans("An origami swan that's some kind of symbol?")
a12 = question.Ans("25 shitty jokes about House of Cards.")
a13 = question.Ans("Carbon monoxide poisoning.")
a14 = question.Ans("A homoerotic subplot.")
a15 = question.Ans("Discharging a firearm in a residential area.")
a16 = question.Ans("Forcing a handjob on a dying man.")

# put questions and answers into separate lists

qlist = [q1, q2, q3, q4, q5, q6, q7, q8, q9]
alist = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16]


# randomly choose a question -> show the number of answers required -> pause for 2 seconds -> 
# show 1 answer or 2 answers according to the requirement -> pause for 2 seconds

def qaloop():
    for q in qlist:
        q = random.choice(qlist)
        q.show_number()
        q.show_text()
        time.sleep(2)
        for a in alist:
            a = random.choice(alist)
            a.show_text()
            if q.number == 1:
                time.sleep(2)
            if q.number == 2:
                a = random.choice(alist)
                a.show_text()
                time.sleep(2)
 
 #ask the user whether they want to continue, and let them rate the answer if they want to.        

            cont = input("Enter 'y' (including the quotation marks) if you want to go on to the next question, " + 
            "enter 'n' if you want to stop here, " + 
            "and enter 'a' if you want to rate this answer before going to the next question :) ")
            if cont == 'y':
                time.sleep(2)
                qaloop()
            elif cont == 'n':
                print("The game stops here, hope you enjoyed it! :)")
                sys.exit(0)
            elif cont == 'a':
                a.rate()
                print("Thank you for your feedback. Now let's continue.")
                time.sleep(2)
                qaloop()
                
                

qaloop()

