from Data import *
from tkinter import *

root=Tk()
root.title("Questions Board")
root.geometry("400x350")
l=Label(root,text="Question 1 .")

q_prompt=["1) Which one is Output Device?\n(a) Mouse \n(b) Printer \n(c) Keyboard \n \n ",
          "2) Which one is Input Device?\n(a) Monitor \n(b) Speakers \n(c) Keyboard\n\n",
          "3) Which is India's National Language?\n(a) Marathi \n(b) Hindi \n(c) Tamil\n\n",
          "4) Who is Playing role of IRON MAN?\n(a) Robert Downey Jr. \n(b) Bradd Pit \n(c) Shahrukh Khan\n\n",
          "5) From Given option which reptile is worlds longest reptile on Earth\n(a) King Kobra \n(b) Anaconda \n(c) Python\n\n",
          "6) Who got Nobel Prize in Literature from India?\n(a) Lokmanya Tilak \n(b) Vinoba Bhave \n(c) Ravindranath Tagore\n\n",
          "7) Who is the Founder of Tesla?\n(a) Elon Musk \n(b) Bill Gates \n(c) Steave Jobs\n\n",
          "8) Who was India's First Prime Minister?\n(a) Mahatma Gandhi \n(b) VallabhBhai Patel \n(c) Jawaharlal Nehru\n\n",
          "9) Which is Python's Latest Version?\n(a) 2.0 \n(b) 3.0 \n(c) 3.7\n\n",
          "10) Which one is Indian IT Company?\n(a)Infosys \n(b) Google \n(c) IBM\n\n"]

questions=[
    Data(q_prompt[0],"b"),
    Data(q_prompt[1],"c"),
    Data(q_prompt[2],"b"),
    Data(q_prompt[3],"a"),
    Data(q_prompt[4],"b"),
    Data(q_prompt[5],"c"),
    Data(q_prompt[6],"a"),
    Data(q_prompt[7],"c"),
    Data(q_prompt[8],"c"),
    Data(q_prompt[9],"a")]




def run_test(questions):
    score=0
    for q in questions:
        answer=input(q.prompt)
        if answer==q.answer:
            score+=1
    print("You Have Got "+str(score)+"/"+str(len(questions))+"Correct")


run_test(questions)