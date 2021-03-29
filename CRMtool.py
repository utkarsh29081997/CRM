from tkinter import *
from tkinter import ttk

root = Tk()
root.title("CRM tool")
root.geometry("1000x500")

style = ttk.Style()

style.theme_use("default")

style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, feildbackground="#D3D3D3")
style.map("Treeview", background=[("selected", "#347083")])

tree_frame = Frame(root)
tree_frame.pack(pady=30)

#  This will initialize the menu
top_menu = Menu(root)
root.config(menu=top_menu)

#  This will add the stuff in the menu
file_menu = Menu(top_menu,tearoff=False)
top_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Quit",command=root.destroy)

# sub_menu = Menu(file_menu,tearoff=False)
# file_menu.add_cascade(label="Sub_Menu",menu=sub_menu)
# sub_menu.add_command(label="Quit",command=root.destroy)


tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)

my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set,selectmode="extended")
my_tree.pack()

tree_scroll.config(command=my_tree.yview)

my_tree['columns'] = ("First Name", "Last Name", "ID", "Code", "Job Name","Address","Country")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("First Name", width=140)
my_tree.column("Last Name", width=140)
my_tree.column("ID", width=100, anchor=CENTER)
my_tree.column("Code", width=140,anchor=CENTER)
my_tree.column("Job Name", width=140)
my_tree.column("Address", width=140)
my_tree.column("Country", width=140)


my_tree.heading("#0", text="", anchor=W)
my_tree.heading("First Name", text="First Name", anchor=CENTER)
my_tree.heading("Last Name", text="Last Name", anchor=CENTER)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Code", text="Code", anchor=CENTER)
my_tree.heading("Job Name", text="Job Name", anchor=CENTER)
my_tree.heading("Address", text="Address", anchor=CENTER)
my_tree.heading("Country", text="Country", anchor=CENTER)

data = [["Utkarsh", "Singh", 1, 1234, "SE","Mumbai","INDIA"],
        ["Shanu", "Singh", 2, 4567, "SE","London","UK"],
        ["Karan", "Jadav", 3, 6378, "SSE","Dubai","SA"],
        ["Jhon", "Doe", 4, 8907, "SSE","NY","USA"],
        ["Jhon", "Elder", 5, 1245, "Manager","CA","USA"],
        ["Raj", "Kumar", 6, 5488, "SE","Mumbai","INDIA"],
        ["Praful", "Patel", 7, 7894, "SE","London","UK"],
        ["Karan", "Singh", 8, 5458, "SSE","Dubai","SA"],
        ["Jhon", "Brown", 9, 8759, "SSE","NY","USA"],
        ["Jhon", "White", 10, 7895, "Manager","CA","USA"],
        ["Jim", "Brown", 11, 8759, "SSE","NY","USA"],
        ["Jill", "White", 12, 7895, "Manager","CA","USA"]
        ]

my_tree.tag_configure("oddrows", background="white")
my_tree.tag_configure("evenrows", background="lightblue")

global count
count = 0

for x in data:
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(x[0], x[1], x[2], x[3], x[4],x[5],x[6]),
                       tags=('oddrows',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(x[0], x[1], x[2], x[3], x[4],x[5],x[6]),
                       tags=('evenrows',))
    count += 1

label_frame = LabelFrame(root, text="Modify a Cell", bg="#D3D3D3")
label_frame.pack(padx=20,expand="yes",fill="x")

# Name
label_name = ttk.Label(label_frame,text="Name")
label_name.grid(row=0,column=0,padx=10)
entry_name = ttk.Entry(label_frame,width=20)
entry_name.grid(row=0,column=1,padx=10)

# LastName
label_lastname = ttk.Label(label_frame,text="Last Name")
label_lastname.grid(row=0,column=2,padx=10)
entry_lastname = ttk.Entry(label_frame,width=20)
entry_lastname.grid(row=0,column=3,padx=10)

# ID
label_lastname = ttk.Label(label_frame,text="ID")
label_lastname.grid(row=0,column=4,padx=10)
entry_lastname = ttk.Entry(label_frame,width=20)
entry_lastname.grid(row=0,column=5,pady=10)

# Code
label_code = ttk.Label(label_frame,text="Code")
label_code.grid(row=1,column=0,padx=10)
entry_code = ttk.Entry(label_frame,width=20)
entry_code.grid(row=1,column=1,pady=10)

# Job Name
label_jobname = ttk.Label(label_frame,text="Job Name")
label_jobname.grid(row=1,column=2,padx=10)
entry_jobname = ttk.Entry(label_frame,width=20)
entry_jobname.grid(row=1,column=3,pady=10)

# Address
label_add = ttk.Label(label_frame,text="Add.")
label_add.grid(row=1,column=4,padx=10)
entry_add = ttk.Entry(label_frame,width=20)
entry_add.grid(row=1,column=5,pady=10)

# Country
label_cntry = ttk.Label(label_frame,text="Country")
label_cntry.grid(row=1,column=6,padx=8)
entry_cntry = ttk.Entry(label_frame,width=15)
entry_cntry.grid(row=1,column=7,pady=10)

root.mainloop()
