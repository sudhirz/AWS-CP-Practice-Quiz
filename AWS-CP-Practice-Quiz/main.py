import tkinter as tk
from tkinter import *
from tkinter import ttk
import json


def start_quiz():
    with open("aws-cp-last.txt", "w") as write_file:
        write_file.write(str(counter))
    question_number = counter + 1
    feedback.set("")
    main_frame = Frame(root)
    main_frame.grid()       # laying out a frame on top of root frame
    first_row = "Question: " + str(question_number) + ' of ' + str(total_question) + '\n'
    first_row_label = ttk.Label(main_frame, text=first_row, wraplength=550)
    first_row_label.config(font=("Times", 13, "bold"))
    first_row_label.grid(row=0, column=0, padx=20)
    question = aws_cp[counter]['questionText'] + '\n'
    question_label = ttk.Label(main_frame, text=question, wraplength=550)
    question_label.config(font=("Times", 13, "bold"))
    question_label.grid(row=1, column=0, padx=20)

    # For Question type - multiple choice with single answer question
    if aws_cp[counter]['questionType'] == 'one':
        radio_variable = IntVar()
        radio_variable.set(-1)

        radio_one = Radiobutton(
            main_frame,
            text=aws_cp[counter]['options'][0],
            variable=radio_variable,
            font=("Times", 11),
            value=0
        )
        radio_one.grid(row=5, column=0, sticky="W", padx=20)

        radio_two = Radiobutton(
            main_frame,
            text=aws_cp[counter]['options'][1],
            variable=radio_variable,
            font=("Times", 11),
            value=1
        )
        radio_two.grid(row=6, column=0, sticky="W", padx=20)

        radio_three = Radiobutton(
            main_frame,
            text=aws_cp[counter]['options'][2],
            variable=radio_variable,
            font=("Times", 11),
            value=2
        )
        radio_three.grid(row=7, column=0, sticky="W", padx=20)

        radio_four = Radiobutton(
            main_frame,
            text=aws_cp[counter]['options'][3],
            variable=radio_variable,
            font=("Times", 11),
            value=3
        )
        radio_four.grid(row=8, column=0, sticky="W", padx=20)

    # For Question type - multiple choice with multiple answers - select two or select three
    elif aws_cp[counter]['questionType'] == 'three' or aws_cp[counter]['questionType'] == 'two':
        check_var_0 = tk.IntVar()
        check_var_1 = tk.IntVar()
        check_var_2 = tk.IntVar()
        check_var_3 = tk.IntVar()
        check_var_4 = tk.IntVar()

        check_var_0.set(0)
        check_var_1.set(0)
        check_var_2.set(0)
        check_var_3.set(0)
        check_var_4.set(0)

        check_box_one = Checkbutton(
            main_frame,
            text=aws_cp[counter]['options'][0],
            variable=check_var_0,
            font=("Times", 11),
            onvalue=1,
            offvalue=0
        )
        check_box_one.grid(row=5, column=0, sticky="W", padx=20)

        check_box_two = Checkbutton(
            main_frame,
            text=aws_cp[counter]['options'][1],
            variable=check_var_1,
            font=("Times", 11),
            onvalue=1,
            offvalue=0
        )
        check_box_two.grid(row=6, column=0, sticky="W", padx=20)

        check_box_three = Checkbutton(
            main_frame,
            text=aws_cp[counter]['options'][2],
            variable=check_var_2,
            font=("Times", 11),
            onvalue=1,
            offvalue=0
        )
        check_box_three.grid(row=7, column=0, sticky="W", padx=20)

        check_box_four = Checkbutton(
            main_frame,
            text=aws_cp[counter]['options'][3],
            variable=check_var_3,
            font=("Times", 11),
            onvalue=1,
            offvalue=0
        )
        check_box_four.grid(row=8, column=0, sticky="W", padx=20)

        check_box_five = Checkbutton(
            main_frame,
            text=aws_cp[counter]['options'][4],
            variable=check_var_4,
            font=("Times", 11),
            onvalue=1,
            offvalue=0
        )
        check_box_five.grid(row=9, column=0, sticky="W", padx=20)

    def previous_question():
        global counter
        if counter == 0:  # check if already at first question
            feedback_msg.config(fg="red", font=("Times", 13, "bold"))
            feedback.set("Can't go back any further. This is the first question in the quiz")
        else:
            # decrement counter to go to previous question
            counter = counter - 1
            # Destroy all the previous widget
            main_frame.destroy()

            start_quiz()

    def check_answer():
        global answer
        check_box_list = []
        if aws_cp[counter]['questionType'] == 'one':
            if radio_variable.get() == aws_cp[counter]['correct'][0]:
                feedback_msg.config(fg="green", font=("Times", 13, "bold"))  # bg="blue" for background
                feedback.set("Correct")  # feedback message to display if answer is correct
            elif radio_variable.get() == -1:
                feedback_msg.config(fg="red", font=("Times", 13, "bold"))  # bg="red" for background
                feedback.set("Please select option")  # if user missed to select any option
            else:
                answer = "Wrong \n" + "Correct answer: \n" + aws_cp[counter]['options'][aws_cp[counter]['correct'][0]] + '\n'
                #answer += aws_cp[counter]['resource']
                feedback_msg.config(fg="red", font=("Times", 13, "bold"))  # bg="red" for background
                feedback.set(answer)  # display the correct answer
        elif aws_cp[counter]['questionType'] == 'two':
            check_box_list.append(check_var_0.get())
            check_box_list.append(check_var_1.get())
            check_box_list.append(check_var_2.get())
            check_box_list.append(check_var_3.get())
            check_box_list.append(check_var_4.get())

            if check_box_list == aws_cp[counter]['correct']:
                feedback_msg.config(fg="green", font=("Times", 13, "bold"))
                feedback.set("Correct")
            elif check_box_list.count(1) != 2:
                feedback_msg.config(fg="red", font=("Times", 13, "bold"))
                feedback.set("Incorrect, make sure you have selected two options")
            else:
                answer = "Wrong \n" + "Correct answer: \n"
                for i in range(5):
                    if aws_cp[counter]['correct'][i] == 1:
                        answer += aws_cp[counter]['options'][i] + '\n'
                #answer += aws_cp[counter]['resource']
                feedback_msg.config(fg="red", font=("Times", 13, "bold"))
                feedback.set(answer)

        else:
            check_box_list.append(check_var_0.get())
            check_box_list.append(check_var_1.get())
            check_box_list.append(check_var_2.get())
            check_box_list.append(check_var_3.get())
            check_box_list.append(check_var_4.get())

            if check_box_list == aws_cp[counter]['correct']:
                feedback_msg.config(fg="green", font=("Times", 13, "bold"))
                feedback.set("Correct")
            elif check_box_list.count(1) != 3:
                feedback_msg.config(fg="red", font=("Times", 13, "bold"))
                feedback.set("Incorrect, make sure you have selected three options")
            else:
                answer = "Wrong \n" + "Correct answer: \n"
                for i in range(5):
                    if aws_cp[counter]['correct'][i] == 1:
                        answer += aws_cp[counter]['options'][i] + '\n'
                #answer += aws_cp[counter]['resource']
                feedback_msg.config(fg="red", font=("Times", 13, "bold"))
                feedback.set(answer)

    def next_question():
        global counter

        if counter == len(aws_cp) - 1:  # check program reached to the last question
            feedback_msg.config(fg="red", font=("Times", 13, "bold"))
            feedback.set("Congratulation!! You have finished the quiz")
        else:
            # increment counter to go to next question
            counter += 1

            # Destroy all the previous widget
            main_frame.destroy()

            start_quiz()

    back_button = ttk.Button(main_frame, text="Back", padding=(2, 2, 2, 2), command=previous_question)
    back_button.grid(row=10, column=0, pady=20, padx=20, sticky="W")

    check_button = ttk.Button(main_frame, text="Check", padding=(2, 2, 2, 2), command=check_answer)
    check_button.grid(row=10, column=0, pady=20)

    next_button = ttk.Button(main_frame, text="Next", padding=(2, 2, 2, 2), command=next_question)
    next_button.grid(row=10, column=0, pady=20, sticky="E")

    # feedback will display the result at the bottom of the screen after check button is pressed
    feedback_msg = Label(main_frame, textvariable=feedback, wraplength=550,
                         justify="left")  # justify is used where there is multiple lines of string
    feedback_msg.grid(row=12, column=0, padx=20, sticky="W")


root = tk.Tk()
root.geometry("600x450")
root.resizable(False, False)
root.title("AWS Cloud Practitioner Quiz")

# Setting font style to be used in root frame for specific widgets
style = ttk.Style(root)
style.configure("TRadiobutton", font=("Times", 12))
style.configure("TCheckbutton", font=("Times", 12))

feedback = tk.StringVar()

with open("aws-cp-practice-quiz.json") as my_file:
    aws_cp = json.load(my_file)

# will catch up from the question last left
try:
    with open("aws-cp-last.txt", "r") as read_file:
        counter = int(read_file.read())
except:
    counter = 0

answer = ''
total_question = len(aws_cp)

start_quiz()
root.mainloop()
