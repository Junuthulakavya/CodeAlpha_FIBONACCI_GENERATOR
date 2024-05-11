import tkinter as tk #importing tkinter module

def generate_fibonacci_numbers(): #defining a funtion to generate the fibonacci sequence
    n = int(entry.get())          #accessing the input from user
    fibonacci_sequence = [0, 1]  # Initialize with the first two Fibonacci numbers

    while len(fibonacci_sequence) < n:  #using while loop generating the sequence
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2] 
        fibonacci_sequence.append(next_fib) 

    result_label.config(text=f"Fibonacci Sequence: {', '.join(map(str, fibonacci_sequence))}")

root = tk.Tk()
root.title("Fibonacci Number Generator") #tittle of the project

label = tk.Label(root, text="Enter the number of Fibonacci numbers You Want to generate:", font=("Roman", 16,"bold")) #creating the label 
label.pack()

entry = tk.Entry(root, font=("Helvetica", 16)) #taking input from the user
entry.pack()

generate_button = tk.Button(root, text="Generate", command=generate_fibonacci_numbers, font=("Roman", 16,"bold"))#creating a button 
generate_button.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 16))#displaying the result
result_label.pack()
l1=tk.Label(root,text="TASK BY CODEALPHA",bg="Purple",fg="yellow").pack(ipadx=10,ipady=10)
root.mainloop()