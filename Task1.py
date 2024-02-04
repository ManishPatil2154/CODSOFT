import tkinter as tk    

def add_task():    
    task = entry.get()    
    if task:        
        Listbox.insert(tk.END, task)        
        entry.delete(0, tk.END)    

def delete_task():    
    try:        
        index = Listbox.curselection()[0]        
        Listbox.delete(index)    
    except IndexError:        
        pass    

root = tk.Tk()    
root.title(" To-Do-list")    

Listbox = tk.Listbox(root, width=55)    
Listbox.pack(pady=9)    

entry = tk.Entry (root, font=("Arial", "19"))
entry.pack(pady=9)    

add_button = tk.Button(root, text="Add List", command=add_task)
add_button.pack(pady=13)    

delete_button = tk.Button(root, text="Delete", command=delete_task)
delete_button.pack(pady=10)    

root.mainloop()