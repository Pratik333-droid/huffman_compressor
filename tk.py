from tkinter import *
import tkinter as tk
from encoder_decoder import buildHuffmanTree, returnEncodedString, returnDecodedString, returnFrequencyDictionary , returnHuffmanDictionary
from table_dict import run1

root= tk.Tk()
root.title('Huffman Compression')


#variable x1 = original text
def run():

    canvas1 = tk.Canvas(root, width = 1000, height = 500,  relief = 'raised',bg='sky blue')
    canvas1.pack()

    label1 = tk.Label(root, text='Huffman Coding to compress data.')
    label1.config(font=('helvetica', 20))
    canvas1.create_window(500, 25, window=label1)
    label1.config(bg='pink',fg='black')

    label2 = tk.Label(root, text='Type the string to be compressed:')
    label2.config(font=('helvetica', 14))
    canvas1.create_window(350, 70, window=label2)
    label2.config(bg='sky blue',fg='black')


    entry1 = tk.Entry (root,width=30,font=('helvetica',12))
    canvas1.create_window(650, 70, window=entry1)



    def huff ():
        
        original_text = entry1.get()
        # btn1=tk.Button(root,command=entry1.delete(1),bg='red', fg='white', font=('helvetica', 9, 'bold'),text="x")
        # canvas1.create_window(800,70,window=btn1)
        if original_text:

            label00 = tk.Label(text='Data is compressed.', bg='brown', fg='white', font=('helvetica', 12, 'bold'))
            canvas1.create_window(500, 130, window=label00)

            options=["Original String","Encoded String","Decoded String","Dictionary","View all"]
            variable = StringVar(root)
            variable.set("Select an option")

            w = OptionMenu(root, variable, *options)
            canvas1.create_window(500, 170, window=w)

            def view():
                opt=variable.get()

                if opt=="Original String":
                    label3 = tk.Label(root, text= 'Results',font=('helvetica', 15, 'underline'))
                    canvas1.create_window(500, 200, window=label3)
                    label3.config(bg='sky blue',fg='black')

                    label4 = tk.Label(root, text= 'Original String: ',font=('helvetica', 10))
                    canvas1.create_window(500, 230, window=label4)
                    label4.config(bg='sky blue',fg='black')


                    label5 = tk.Label(root, text=original_text,font=('helvetica', 10, 'bold'))
                    canvas1.create_window(500, 250, window=label5)
                    
                    label5.config(bg='sky blue',fg='black')
                    button0 = tk.Button(text='Clear Screen', command=lambda: [label00.destroy(),label3.destroy(),label4.destroy(),label5.destroy(),label6.destroy(),label7.destroy(),label8.destroy(),label9.destroy(),label0.destroy(),label11.destroy(),button0.destroy(),button00.destroy(),w.destroy(),button.destroy()], bg='red', fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(650, 130, window=button0)

                if opt=="View all":
                    label3 = tk.Label(root, text= 'Results',font=('helvetica', 15, 'underline'))
                    canvas1.create_window(500, 200, window=label3)
                    label3.config(bg='sky blue',fg='black')

                    buildHuffmanTree(original_text)
                    x2 = returnHuffmanDictionary() #x2 is a  dictionary
                    x3 = returnEncodedString() #encoded string
                    x4 = returnDecodedString() #decoded string
                    x5 = returnFrequencyDictionary() #x5 is a dictionary
            


                    label4 = tk.Label(root, text= 'Original String: ',font=('helvetica', 10))
                    canvas1.create_window(500, 230, window=label4)
                    label4.config(bg='sky blue',fg='black')


                    label5 = tk.Label(root, text=original_text,font=('helvetica', 10, 'bold'))
                    canvas1.create_window(500, 250, window=label5)
                    label5.config(bg='sky blue',fg='black')

                    label6 = tk.Label(root, text= 'Dictionary: ',font=('helvetica', 10))
                    canvas1.create_window(500, 270, window=label6)
                    label6.config(bg='sky blue',fg='black')

                    label7 = tk.Label(root, text= x2,font=('helvetica', 10, 'bold'))
                    canvas1.create_window(500, 290, window=label7)
                    label7.config(bg='sky blue',fg='black')


                    label8 = tk.Label(root, text= 'Encoded string: ',font=('helvetica', 10))
                    canvas1.create_window(500, 310, window=label8)
                    label8.config(bg='sky blue',fg='black')

                    label9 = tk.Label(root, text= x3,font=('helvetica', 10, 'bold'))
                    canvas1.create_window(500, 330, window=label9)
                    label9.config(bg='sky blue',fg='black')

                    label0 = tk.Label(root, text= 'Decoded String: ',font=('helvetica', 10))
                    canvas1.create_window(500, 350, window=label0)
                    label0.config(bg='sky blue',fg='black')

                    label11 = tk.Label(root, text= x4,font=('helvetica', 10, 'bold'))
                    canvas1.create_window(500, 370, window=label11)
                    label11.config(bg='sky blue',fg='black')

                    button0 = tk.Button(text='Clear Screen', command=lambda: [label00.destroy(),label3.destroy(),label4.destroy(),label5.destroy(),label6.destroy(),label7.destroy(),label8.destroy(),label9.destroy(),label0.destroy(),label11.destroy(),button0.destroy(),button00.destroy(),w.destroy(),button.destroy()], bg='red', fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(650, 130, window=button0)

                    button00=tk.Button(text='View dictionary as table',command=run1,bg='red',fg='white', font=('helvetica', 9, 'bold'))
                    canvas1.create_window(650,270,window=button00)


            button = Button(root, text="Show", command=lambda: view())
            canvas1.create_window(600, 170, window=button)





        else:
            label12 = tk.Label(root, text= 'String not entered. Error.',font=('helvetica', 10))
            canvas1.create_window(500, 230, window=label12)
            label12.config(bg='sky blue',fg='black')


            button0 = tk.Button(text='Clear Screen', command=lambda: [label12.destroy(),button0.destroy()], bg='red', fg='white', font=('helvetica', 9, 'bold'))
            canvas1.create_window(500, 162, window=button0)




    button1 = tk.Button(text='Compress the data', command=huff, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
    canvas1.create_window(500, 130, window=button1)
    

    

    root.mainloop()
if __name__=='__main__':
    run()