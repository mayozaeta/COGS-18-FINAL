# importing tkinter as tk
import tkinter as tk
# creating GUI window and interactive canvas
HEIGHT = 600
WIDTH = 700
root = tk.Tk()  # constructs the main window
root.title("Brain Diagram")  # title for main window dispay
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
# photo image brain diagram import
brain_diagram = tk.PhotoImage(file="brainbetsy3.gif")
brain_diagram_label = tk.Label(root, image=brain_diagram)
brain_diagram_label.place(relwidth=1, relheight=1)

# funciton to input string
def exit_func(str):
    """ return a string
    parameter
    ----------
    there is a singular parameter and it is an input string value
    return
    ---------
    function returns the string inputs
    """
    output = str
    return output
    assert exit_func  # tests if variable exists
    assert isinstance(exit_func, str)  # tests that variable is string type
    assert exit_func("hello") == "hello"  # tests functions output
    assert exit_func("") == ""
# Toplevel windows- pop up containing information for the lobes
def f_func():
    """Makes a toplevel pop up display for frontal lobe
    parameters
    -----------
    label , button, title
    return
    ------------
    labels and buttons and info displayed in window
    """
    # fwindow constructs the popup window for frontal lobe setting the backbone
    fwindow = tk.Toplevel()
    fwindow.title("Frontal lobe")
    fwindow.geometry("400x300")
    # tk connects the buttons and labels to the toplevel window, in this case fwindow
    tk.Label(fwindow,
          text=exit_func("Function:"),
          font="Times 14 underline bold", fg="#555555").place(relx=0.07, rely=0.1)
    tk.Label(fwindow, text='''Involved in higher cognitive skills,
             voluntary movements, emotional regulation, planning,
             and thinking.''', font="Times", fg="#555555").place(relx=0.1, rely=0.18)
    tk.Label(fwindow, text='''Sub-associations:''',
             font="Times 14 underline bold", fg="#555555").place(relx=0.07, rely=0.5)
    tk.Label(fwindow, text='''Motor cortex''', font="Times",
             fg="#555555").place(relx=0.35, rely=0.62)
    tk.Button(fwindow, text="Done", command=fwindow.destroy).pack()
    
def p_func():
    """Makes a toplevel pop up display for parietal lobe
    parameters
    -----------
    label, button, title
    return
    -----------
    labels and buttons along with info displayed in window
    """
    # pwindow constructs the popup window for parietal lobe setting the backbone
    pwindow = tk.Toplevel()
    pwindow.title("Parietal lobe")
    pwindow.geometry("400x300")
    # tk connects the buttons and labels to the toplevel window, in this case pwindow
    tk.Label(pwindow, 
             text=exit_func("Function:"), font="Times 14 underline bold", 
             fg="#555555").place(relx=0.07, rely=0.08)
    tk.Label(pwindow, text='''The parietal lobe processes
         information about movement,
         touch, taste, and temperature.''', font="Times", fg="#555555").place(relx=0.2, rely=0.15)
    tk.Label(pwindow, text='''Sub-associations:''', font="Times 14 underline bold",
              fg="#555555").place(relx=0.09, rely=0.4)
    tk.Label(pwindow, text='''Postcentral gyrus, (Homonculus)''', font="Times",
             fg="#555555").place(relx=0.25, rely=0.5)
    tk.Button(pwindow, text="Done", command=pwindow.destroy).pack()
def o_func():
    """Makes a toplevel display for occipital lobe
    parameters
    -------------
    label, button, title
    return
    --------------
    lables and buttons and information in display
    """
    # owindow constructs the popup window for occipital lobe setting the backbone
    owindow = tk.Toplevel()
    owindow.title("Occipital lobe")
    owindow.geometry("400x300")
    # tk connects the buttons and labels to the toplevel window, in this case owindow
    tk.Label(owindow, text=exit_func("Function:"), font="Times 14 underline bold",
             fg="#555555").place(relx=0.07, rely=0.08)
    tk.Label(owindow, text='''Involved in higher cognitive skills,
             voluntary movements, emotional regulation,
             planning, and thinking.''', font="Times", fg="#555555").place(relx=0.1, rely=0.15)
    tk.Label(owindow, text='''Sub-associations:''', font="Times 14 underline bold",
             fg="#555555").place(relx=0.07, rely=0.4)
    tk.Label(owindow, text='''V1, the primary visual cortex''', font="Times",
             fg="#555555").place(relx=0.3, rely=0.5)
    tk.Button(owindow, text="Done", command=owindow.destroy).pack()
def t_func():
    """Make toplevel display window for temporal lobe
    parameters
    ------------
    label, button, title
    return
    -------------
    labels and buttons and information in display
    """
    # twindow constructs the popup window for temporal lobe setting the backbone
    twindow = tk.Toplevel()
    twindow.title("Temporal lobe")
    twindow.geometry("400x300")
    # tk connects the buttons and labels to the toplevel window, in this case tswindow
    tk.Label(twindow, text=exit_func("Function:"), font="Times 14 bold underline",
             fg="#555555").place(relx=0.07, rely=0.08)
    tk.Label(twindow, text='''The temporal lobe contains
        regions dedicated to processing sensory
        information, important for hearing,
        language recognition, and forming memories.''', font="Times",
             fg="#555555").place(relx=0.1, rely=0.19)
    tk.Label(twindow, text='''Sub-associations:''', font="Times 14 bold underline",
             fg="#555555").place(relx=0.09, rely=0.52)
    tk.Label(twindow, text='''Weirnicke's area, Hippocampus, Amygdala''',
             font="Times", fg="#555555").place(relx=0.25, rely=0.62)
    tk.Button(twindow, text="Done", command=twindow.destroy).pack()
def c_func():
    """Make toplevel window for cerebellum
    parameters
    -------------
    label, button, title
    return
    -------------
    label, button, info display
    """
    # cwindow constructs the popup window for cerebellum setting the backbone
    cwindow = tk.Toplevel()
    cwindow.title("Cerebellum")
    cwindow.geometry("410x300")
    # tk connects the buttons and labels to the toplevel window, in this case cwindow
    tk.Label(cwindow, text=exit_func("Function:"), font="Times 14 bold underline",
             fg="#555555").place(relx=0.07, rely=0.08)
    tk.Label(cwindow, text='''The cerebellum's main function
        is to regulate motor and coordination.
        This includes balance, eye movement,
        muscle actions to perform smooth
        movements, etc)''', font="Times", fg="#555555").place(relx=0.2, rely=0.18)
    tk.Label(cwindow, text='''Sub-associations:''', font="Times 14 bold underline",
             fg="#555555").place(relx=0.07, rely=0.52)
    tk.Label(cwindow, text='''The cerebellum is like a miniature
        brain, containing cortex, gray and
        white matter.''', font="Times", fg="#555555").place(relx=0.25, rely=0.63)
    tk.Button(cwindow, text="Done", command=cwindow.destroy).pack()
def bs_func():
    """ Makes a toplevel window pop up
    parameters
    ------------
    label, button, title
    return
    ------------
    information, label, and button in display
    """
    # bswindow constructs the popup window for brain stem lobe setting the backbone
    bswindow = tk.Toplevel()
    bswindow.title("Brain stem")
    bswindow.geometry("400x300")
    # tk connects the buttons and labels to the toplevel window, in this case bswindow
    tk.Label(bswindow, text=exit_func("Function:"), font="Times 14 bold underline",
        fg="#555555").place(relx=0.07, rely=0.08)
    tk.Label(bswindow, text='''The brain stem controls the
        flow of communication between the brain
        and body. It also controls basic bodyily
        functions, such as breathing, heart rate, blood
        pressure, consciousness, and sleep/wake cycles.''', font="Times",
        fg="#555555").place(relx=0.1, rely=0.15)
    tk.Label(bswindow, text='''Sub-associations:''', font="Times 14 bold underline",
        fg="#555555").place(relx=0.07, rely=0.5)
    tk.Label(bswindow, text='''Medulla Oblongota, Pons, Midbrain''',
             font="Times", fg="#555555").place(relx=0.25, rely=0.6)
    tk.Button(bswindow, text="Done", command=bswindow.destroy).pack()
    
# Interactive GUI buttons in root window - link to toplevel window pop ups
frontal_lobe = tk.Button(root, text="Frontal lobe", fg="#FFCC99",
                         command=f_func)
frontal_lobe.place(relx=0.2, rely=0.28)
parietal_lobe = tk.Button(root, text="Parietal lobe", fg="#8ECFF3",
                          command=p_func)
parietal_lobe.place(relx=0.54, rely=0.14)
occipital_lobe = tk.Button(root, text="Occipital lobe", fg="#B1E3B6",
                           command=o_func)
occipital_lobe.place(relx=0.75, rely=0.38)
temporal_lobe = tk.Button(root, text="Temporal lobe", fg="#FF91C9",
                          command=t_func)
temporal_lobe.place(relx=0.45, rely=0.43)
cerebellum = tk.Button(root, text="Cerebellum", fg="#A887C9",
                       command=c_func)
cerebellum.place(relx=0.63, rely=0.55)
brain_stem = tk.Button(root, text="Brain stem", fg="#FFD480",
                       command=bs_func)
brain_stem.place(relx=0.49, rely=0.72)

root.mainloop()
