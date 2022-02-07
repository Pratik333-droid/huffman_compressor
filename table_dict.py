# Python program to create a table

from tkinter import *
# import tk
class Table:
    
    def __init__(self,root):
        
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                
                self.e = Entry(root, width=15, fg='black',
                            font=('Arial',15))
                
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

# take the data
lst = {1:'Raj',
    2:'Aaryan',
    3:'Vaishnavi',
    4:'Rachna',
    5:'Shubham'}
# lst = test1()
lst=list(lst.items())


# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

def run1():
    # create root window
    root1 = Tk()
    root1.title('Table')
    t = Table(root1)
    root1.mainloop()

if __name__ == '__main__':
    run1()