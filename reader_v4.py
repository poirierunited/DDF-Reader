import sqlite3

from pathlib import Path

import os
import tempfile

import tkinter as tk
from tkinter import filedialog, Text


# Create an instance of tkinter frame or window
root = tk.Tk()

filePaths = []

def addFile():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(title='Select File', filetypes=(("DDF", "*.ddf"), ("All Files", "*.*")))

    if len(filePaths) >= 2:
        filePaths.pop(0)
        filePaths.append(filename)
    else:
        filePaths.append(filename)

    for file in filePaths:
        label = tk.Label(frame, text=file, bg="gray")
        label.pack()


def compare_ddf():
    # Connecting to sqlite
    conn1 = sqlite3.connect(Path(str(filePaths[0])))
    conn2 = sqlite3.connect(Path(str(filePaths[1])))
    
    # Creating a cursor object using the cursor() method
    cursor1 = conn1.cursor()
    cursor2 = conn2.cursor()
    

    ddf_data1 = []
    ddf_data2 = []

    # Display columns

# ======================================           Analizing 1st DDF File              ========================================

    data1=cursor1.execute('''SELECT * FROM L1''')
    for column in data1.description:
        ddf_data1.append(column[0])
    


    # SELECT TableName FROM 'Levels' WHERE DSCTableName="DKIDS02" or DSCTableName="BOYSPEC1" or DSCTableName="GIRLSPEC1" or DSCTableName="resp_age_kid"

    #DKIDS02
    row = cursor1.execute('''SELECT TableName FROM Levels WHERE DSCTableName="DKIDS02"''').fetchone()
    if row[0] != None:
        DKIDS02_query = "SELECT * FROM " + row[0]
        DKIDS02_data = cursor1.execute(DKIDS02_query)

        ddf_data1.append('==== DKIDS02 Variables:')
        for column in DKIDS02_data.description:
            ddf_data1.append(column[0])

    #BOYSPEC1
    row = cursor1.execute('''SELECT TableName FROM Levels WHERE DSCTableName="BOYSPEC1"''').fetchone()
    if row[0] != None:
        BOYSPEC1_query = "SELECT * FROM " + row[0]
        BOYSPEC1_data = cursor1.execute(BOYSPEC1_query)

        ddf_data1.append('==== BOYSPEC1 Variables:')
        for column in BOYSPEC1_data.description:
            ddf_data1.append(column[0])
    
    #GIRLSPEC1
    row = cursor1.execute('''SELECT TableName FROM Levels WHERE DSCTableName="GIRLSPEC1"''').fetchone()
    if row[0] != None:
        GIRLSPEC1_query = "SELECT * FROM " + row[0]
        GIRLSPEC1_data = cursor1.execute(GIRLSPEC1_query)

        ddf_data1.append('==== GIRLSPEC1 Variables:')
        for column in GIRLSPEC1_data.description:
            ddf_data1.append(column[0])

    #resp_age_kid
    row = cursor1.execute('''SELECT TableName FROM Levels WHERE DSCTableName="resp_age_kid"''').fetchone()
    if row[0] != None:
        resp_age_kid_query = "SELECT * FROM " + row[0]
        resp_age_kid_data = cursor1.execute(resp_age_kid_query)

        ddf_data1.append('==== resp_age_kid Variables:')
        for column in resp_age_kid_data.description:
            ddf_data1.append(column[0])

# ============================================================================================================================ 









# ======================================           Analizing 2nd DDF File              ========================================

    data2=cursor2.execute('''SELECT * FROM L1''')
    for column in data2.description:
        ddf_data2.append(column[0])



    # SELECT TableName FROM 'Levels' WHERE DSCTableName="DKIDS02" or DSCTableName="BOYSPEC1" or DSCTableName="GIRLSPEC1" or DSCTableName="resp_age_kid"

    #DKIDS02
    row = cursor2.execute('''SELECT TableName FROM Levels WHERE DSCTableName="DKIDS02"''').fetchone()
    if row[0] != None:
        DKIDS02_query = "SELECT * FROM " + row[0]
        DKIDS02_data = cursor2.execute(DKIDS02_query)

        ddf_data2.append('==== DKIDS02 Variables:')
        for column in DKIDS02_data.description:
            ddf_data2.append(column[0])

    #BOYSPEC1
    row = cursor2.execute('''SELECT TableName FROM Levels WHERE DSCTableName="BOYSPEC1"''').fetchone()
    if row[0] != None:
        BOYSPEC1_query = "SELECT * FROM " + row[0]
        BOYSPEC1_data = cursor2.execute(BOYSPEC1_query)

        ddf_data2.append('==== BOYSPEC1 Variables:')
        for column in BOYSPEC1_data.description:
            ddf_data2.append(column[0])
    
    #GIRLSPEC1
    row = cursor2.execute('''SELECT TableName FROM Levels WHERE DSCTableName="GIRLSPEC1"''').fetchone()
    if row[0] != None:
        GIRLSPEC1_query = "SELECT * FROM " + row[0]
        GIRLSPEC1_data = cursor2.execute(GIRLSPEC1_query)

        ddf_data2.append('==== GIRLSPEC1 Variables:')
        for column in GIRLSPEC1_data.description:
            ddf_data2.append(column[0])

    #resp_age_kid
    row = cursor2.execute('''SELECT TableName FROM Levels WHERE DSCTableName="resp_age_kid"''').fetchone()
    if row[0] != None:
        resp_age_kid_query = "SELECT * FROM " + row[0]
        resp_age_kid_data = cursor2.execute(resp_age_kid_query)

        ddf_data2.append('==== resp_age_kid Variables:')
        for column in resp_age_kid_data.description:
            ddf_data2.append(column[0])



    
# ============================================================================================================================   

    




    set_data2 = set(ddf_data2)
    ddf1_extra = [x for x in ddf_data1 if x not in set_data2]

    set_data1 = set(ddf_data1)
    ddf2_extra = [x for x in ddf_data2 if x not in set_data1]

    



    file = filedialog.asksaveasfile(mode='w',
                                    defaultextension='.txt',
                                    filetypes=[('Text file', '.txt')],
                                    initialfile="Result_Output"
                                    # initialdir='/'
                                    
    )

    # file.write(str(filePaths[0]))
    file.write('===================================' + '\n')
    file.write(os.path.basename(os.path.normpath(str(filePaths[0]))))
    file.write(' - Exclusive variables:' + '\n')
    file.write('===================================' + '\n')


    file.write('\n'.join(ddf1_extra))


    file.write('\n')
    file.write('===================================' + '\n')
    file.write(os.path.basename(os.path.normpath(str(filePaths[1]))))
    file.write(' - Exclusive variables:' + '\n')
    file.write('===================================' + '\n')


    file.write('\n'.join(ddf2_extra))
    
    
    file.close()

    
    # os.startfile('DDF_result.txt')



    print("\n Exclusive data in " + str(filePaths[0]))
    print("\n")
    print(ddf1_extra)

    print("\n")

    print("\n Exclusive data in " + str(filePaths[1]))
    print("\n")
    print(ddf2_extra)



canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white",bg="#263D42", command=addFile).pack()

run_script = tk.Button(root, text="Run Script", padx=10, pady=5, fg="white",bg="#263D42", command=compare_ddf).pack()

close_w = tk.Button(root, text="Close", padx=10, pady=5, fg="white",bg="#263D42", command=root.destroy).pack()


root.mainloop()

