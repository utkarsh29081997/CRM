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
tree_frame.pack(pady=10)

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
        ["Jim", "Brown", 9, 8759, "SSE","NY","USA"],
        ["Jill", "White", 10, 7895, "Manager","CA","USA"]
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

btm_frame = Frame(root)
btm_frame.pack(pady=1)
label_frame = LabelFrame(btm_frame, text="Modify a Cell", bg="#D3D3D3")
label_frame.pack(pady=10,ipadx=350,expand=Y)
label_name = ttk.Label(label_frame,text="Name")
label_name.pack(padx=10,side=LEFT)
entry_name = ttk.Entry(label_frame,width=20)
entry_name.pack(padx=10,pady=20,side=LEFT)


root.mainloop()
