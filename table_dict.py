# Python program to create a table

from tkinter import *

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
lst = [(1,'Raj','Mumbai',19),
    (2,'Aaryan','Pune',18),
    (3,'Vaishnavi','Mumbai',20),
    (4,'Rachna','Mumbai',21),
    (5,'Shubham','Delhi',21)]

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