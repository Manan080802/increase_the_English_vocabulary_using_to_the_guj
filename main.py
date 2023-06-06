from tkinter import *
import  pandas as pd
import  random
current_card={}
to_learn={}
BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pd.read_csv("data/work_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/gujandeng.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# print(data.head())

print(to_learn)
window = Tk()
window.title("Gujrati To English")
# my_Image = PhotoImage(file="images/im")
window.config(pady=50,padx=50,background=BACKGROUND_COLOR)
def filp_card():
    canvas.itemconfig(card_title,text="Gujrati",fill="white")
    canvas.itemconfig(card_word,text=current_card["Gujrati"],fill="white")
    canvas.itemconfig(card_background,image=card_back_img)



flip_timer= window.after(3000,func=filp_card)

canvas =Canvas(width=800,height=526)
card_back_img=PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_background=canvas.create_image(400,263,image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title=canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="Word",font=("Ariel",68,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

def next_card():
    global  current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    print(current_card["English"])
    canvas.itemconfig(card_title,text="English",fill="black")
    canvas.itemconfig(card_word,text=current_card["English"],fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    # window.after(3000, func=filp_card)
    flip_timer=window.after(3000,func=filp_card)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,command=next_card)
# unknown_button.config(highlightthickness=0)
unknown_button.grid(row=1,column=0)

def is_known():
    to_learn.remove(current_card)
    data=pd.DataFrame(to_learn)
    data.to_csv("data/work_to_learn.csv",index=False)
    next_card()

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image,command=is_known)
check_button.grid(row=1,column=1)
next_card()
window.mainloop()

