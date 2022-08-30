from tkinter import *
from tkinter import messagebox

window = Tk()
window.eval("tk::PlaceWindow %s center" % window.winfo_toplevel())
window.withdraw()

messagebox.showinfo("Info", "Do you have brown hair")
messagebox.showerror("Error", "Do you have brown hair")
messagebox.showwarning("Warning", "Do you have brown hair")
messagebox.askyesno("Yes No", "Do you have brown hair")
messagebox.askokcancel("Ok Cancel", "Do you have brown hair")
messagebox.askretrycancel("Retry Cancel", "Do you have brown hair")
messagebox.askyesno("Yes No", "Do you have brown hair", icon='error') # icon = error, warning, question

if messagebox.askyesno("Yes No", "Do you have brown hair") == True:
	print("yes")
else:
	print("no")


window.deiconify()
window.destroy()
window.quit()



