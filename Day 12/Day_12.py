import tkinter as tk

master = tk.Tk()
master.title('')
# master.geometry('410x370')
# master.maxsize(410,370)
# master.minsize(410,370)
master['bg'] = 'black'

Screen = tk.Text(master, width=22, height=2, border=3, font=("Segoe UI", 24, "bold"), background="#012a4a", fg='white')
Screen.grid(row=0,column=0, columnspan=4,padx=2,pady=2)

def res(numbers, ops) :
    check = 0

    total = float(numbers[0])
    
    while check < len(ops) :
        if ops[check] == '+':
            total += float(numbers[check + 1])
        elif ops[check] == '-':
            total -= float(numbers[check + 1])
        elif ops[check] == '*':
            total *= float(numbers[check + 1])
        elif ops[check] == '/':
            total /= float(numbers[check + 1])
            
        check += 1
    return total

def addTextInScreen(button):
    if button.cget('text') != "=":
        Screen.insert(tk.END,button.cget('text'))

    elif  button.cget('text') == "=":
        NumbersAndOp = Screen.get("1.0", tk.END)
        numbers = []
        ops = []
        op = ['+','-','/','*',"x","÷"]
        nums = ['1','2','3','4','5','6','7','8','9','0']
        check = 0
        x = ''
        # 50+*10-10
        while check < len(NumbersAndOp):
            if NumbersAndOp[check] in op :
                if NumbersAndOp[check] == "÷" :
                    ops.append("/")
                    numbers.append(x)
                    x = ""
                elif NumbersAndOp[check] == "x" :
                    ops.append("*")
                    numbers.append(x)
                    x = ""
                else :
                    ops.append(NumbersAndOp[check])
                    numbers.append(x)
                    x = ""

            elif NumbersAndOp[check] in nums : 
                x += NumbersAndOp[check]

            else :
                break

            check += 1

        if x != "" :
            numbers.append(x)
    
        
        final = res(numbers, ops)
        Screen.delete("1.0", tk.END)
        Screen.insert(tk.END,final)


row = 1
column = 0

TaxtOfButtons = ['7','8','9','+','4','5','6','-','1','2','3','x','.','0','=','÷']

for i in range(0,16):

    if column == 4:
        column = 0
        row += 1

    button = tk.Button(master, text=TaxtOfButtons[i]  , background='white', fg='black', width=8, height=2, font='20', border=2)
    button.grid(row=row, column=column, padx=2, pady=2)
    button.config(command= lambda checkbutton = button : addTextInScreen(checkbutton))

    if TaxtOfButtons[i] == '+' or TaxtOfButtons[i] == 'x' or TaxtOfButtons[i] == '÷' or TaxtOfButtons[i] == '-':
        button.config(background='#62b6cb')
        button.config(fg='white')
        
    elif TaxtOfButtons[i] == '=':
        button.config(background='#1b4965')
        button.config(fg='white')
        button.config(font='30')

    column += 1


master.mainloop()

