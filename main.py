# IP PROJECT


def main_menu():

    print("")

    MARKDOWN = "# Information-Pracices Project"
    md = Markdown(MARKDOWN)
    print(md)
    print("")
    print("[i]BY:\nPiyush Kaushik Bhattacharyya\nZidan Ahmed[/i]")
    print("")

    print("*" * 65)

    print("[u][b][yellow]Data Collection[/yellow][/b][/u]")

    print("|-----------------------------------------------------|")
    print("| 1. [i][red]Data import from CSV to SQL[/i][/red]                      |")
    print("| 2. [i][red]Data import from CSV to DataFrame[/i][/red]                |")
    print("|-----------------------------------------------------|")

    print("=" * 65)

    print("[u][b][yellow]Data Manipulation on SQL[/u][/b][/yellow]")

    print("|-----------------------------------------------------|")
    print("| 3. [i][red]Insert rows[/i][/red]                                      |")
    print("| 4. [i][red]Delete rows[/i][/red]                                      |")
    print("| 5. [i][red]Update information[/i][/red]                               |")
    print("| 6. [i][red]Sort data[/i][/red]                                        |")
    print("|-----------------------------------------------------|")
    print("=" * 65)

    print("[u][b][yellow]Data Analysis[/u][/b][/yellow]")

    print("|-----------------------------------------------------|")
    print("| 7. [i][red]Display top records[/i][/red]                              |")
    print("| 8. [i][red]Display bottom records[/i][/red]                           |")
    print("| 9. [i][red]Display particular fields depending on criterias[/i][/red] |")
    print("|-----------------------------------------------------|")

    print("=" * 65)

    print("[u][b][yellow]Data Visualization[/u][/b][/yellow]")

    print("|-----------------------------------------------------|")
    print("| 10. [i][red]Line Graph[/i][/red]                                      |")
    print("| 11. [i][red]Bar Graph[/i][/red]                                       |")
    print("| 12. [i][red]Histogram Graph[/i][/red]                                 |")
    print("|-----------------------------------------------------|")

    print("=" * 65)

    print("[u][b][yellow]Data Export to CSV[/u][/b][/yellow]")

    print("|-----------------------------------------------------|")
    print("| 13. [i][red]Transfer the changes back to csv[/i][/red]                |")
    print("|-----------------------------------------------------|")

    print("*" * 65)


def spincursor():
    def spinning_cursor():

        while True:

            for cursor in "|/-\\":

                yield cursor

    spinner = spinning_cursor()
    for _ in range(15):

        sys.stdout.write(next(spinner))

        sys.stdout.flush()

        time.sleep(0.1)
        sys.stdout.write("\b")


def typewriter(message):

    for char in message:

        sys.stdout.write(char)

        sys.stdout.flush()

        time.sleep(0.1)


def ShowTableMenu():

    cursor.execute("USE forest_coverage;")
    print("[b]Do you want to view the table:[/b]")

    root = ttk.Tk()
    root.wm_attributes("-topmost", 1)
    root.title("Menu")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = ["1. Yes", "2. No"]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Do you want to view the table").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    opm = tkvar.get()
    print(opm)

    if opm == "1. Yes":

        cursor.execute("USE forest_coverage;")

        df = pd.read_sql("SELECT * FROM forest_coverage", conn)

        df = df.style.hide_index()
        display(df)
    elif opm == "2. Exit":

        clr()
        print("*" * 26, "[b][green]Thank You[/b][/green]", "*" * 26)


def DataImportCSVtoSQL():

    MARKDOWN = "# Data Import from CSV to MySQL"
    md = Markdown(MARKDOWN)
    print(md)

    cursor.execute("USE forest_coverage;")
    message = "You're connected to database: forest_coverage\n "
    typewriter(message)
    spincursor()
    message = "Creating table....\n"
    typewriter(message)
    spincursor()
    message = "Table has been created....\n"
    typewriter(message)
    spincursor()
    message = "Fetching data from forest_coverage table...\n"
    typewriter(message)
    df = pd.read_sql("SELECT * FROM forest_coverage", conn)
    df = df.style.hide_index()
    display(df)

    print("[b]Do you want to continue:[/b]")

    root = ttk.Tk()
    root.wm_attributes("-topmost", 1)
    root.title("MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = ["1. Go back to Main Menu", "2. Exit"]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Select option:").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    opm = tkvar.get()
    print(opm)
    print("")

    if opm == "1. Go back to Main Menu":

        clr()
        opt()
    elif opm == "2. Exit":

        clr()
        print("*" * 26, "[b][green]Thank You[/b][/green]", "*" * 26)


def DataImportCSVtoDF():

    MARKDOWN = "# Data Import from CSV to DF"
    md = Markdown(MARKDOWN)
    print(md)
    message = "Reading data from CSV...\n"
    typewriter(message)
    spincursor()
    message = "Converting data into dataframe...\n"
    typewriter(message)
    df = pd.read_csv("ForestCoverage.csv")
    df = df.style.hide_index()
    display(df)

    print("[b]Do you want to continue:[/b]")

    root = ttk.Tk()
    root.wm_attributes("-topmost", 1)
    root.title("MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = ["1. Go back to Main Menu", "2. Exit"]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Select option:").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

    opm = tkvar.get()
    print(opm)
    print("")

    if opm == "1. Go back to Main Menu":

        clr()
        opt()
    elif opm == "2. Exit":

        clr()
        print("*" * 26, "[b][green]Thank You[/b][/green]", "*" * 26)


def InsertRows():

    MARKDOWN = "# Insert Rows"
    md = Markdown(MARKDOWN)
    print(md)
    cursor.execute("USE forest_coverage;")
    df = pd.read_sql("SELECT * FROM forest_coverage", conn)

    print("[b]Select the new-state to be entered into the table[/b]:")

    root = ttk.Tk()
    root.wm_attributes("-topmost", 1)
    root.title("STATE SELECT MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = ["Telengana", "Ladakh"]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Choose the new state to be inserted").grid(
        row=1, column=1
    )
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()
    st = str(tkvar.get())
    print(st)

    count = 0

    x = df["State_UT"].values.tolist()
    for i in x:
        if st in x:
            count = 1
            print(
                "[b][red]The state [/red][/b]"
                + st
                + "[b][red] already exists[/red][/b]"
            )
            print("[b]Do you want to continue:[/b]")

            root = ttk.Tk()
            root.wm_attributes("-topmost", 1)
            root.title("MENU")

            mainframe = ttk.Frame(root)
            mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
            mainframe.columnconfigure(0, weight=1)
            mainframe.rowconfigure(0, weight=1)
            mainframe.pack(pady=100, padx=100)

            tkvar = ttk.StringVar(root)

            choices = ["1. Go back to Insert Menu", "2. Go back to Main Menu"]

            popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
            ttk.Label(mainframe, text="Select option:").grid(row=1, column=1)
            popupMenu.grid(row=2, column=1)

            def change_dropdown(*args):

                tkvar.get()

            tkvar.trace("w", change_dropdown)

            kswitch = ttk.Button(root, text="OK", command=root.destroy)
            kswitch.pack(pady=10)

            def on_closing():
                if messagebox.askokcancel("Quit", "Do you want to quit?"):
                    root.destroy()

            root.protocol("WM_DELETE_WINDOW", on_closing)

            root.mainloop()

            opm = tkvar.get()
            print(opm)
            print("")

            if opm == "1. Go back to Insert Menu":

                clr()
                InsertRows()
            elif opm == "2. Go back to Main Menu":

                clr()
                opt()
        else:
            count = 0
    if count == 0:
        print(
            """[b]Enter Forest coverage for the year  in square kilometers in the 
                following format 20000 not 20,000 for """
            + st
            + """ [/b]"""
        )
        print("")

        val = [st]
        yr = [
            1987,
            1989,
            1991,
            1993,
            1995,
            1997,
            1999,
            2001,
            2003,
            2005,
            2007,
            2011,
            2013,
        ]
        for step in track(range(0, len(yr))):

            def values():
                try:

                    e = int(
                        input(
                            "Enter Forest coverage for the year " + str(yr[step]) + ":"
                        )
                    )
                    val.append(e)
                except ValueError:
                    print("[cyan]Enter valid data[/cyan]")
                    return values()

            values()
        message = "Inserting values into the table...\n"
        typewriter(message)
        spincursor()
        sql = """INSERT INTO forest_coverage VALUES
                    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        cursor.execute(sql, val)
        conn.commit()
        message = "Values Inserted...\n"
        typewriter(message)
        ShowTableMenu()
    print("[b]Do you want to continue:[/b]")

    root = ttk.Tk()
    root.wm_attributes("-topmost", 1)
    root.title("MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = ["1. Go back to Insert Menu", "2. Go back to Main Menu", "3. Exit"]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Select option:").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    opm = tkvar.get()
    print(opm)
    print("")

    if opm == "1. Go back to Insert Menu":

        clr()
        InsertRows()
    elif opm == "2. Go back to Main Menu":

        clr()
        opt()
    elif opm == "3. Exit":

        clr()
        print("*" * 26, "[b][green]Thank You[/b][/green]", "*" * 26)


def DeleteRows():

    MARKDOWN = "# Delete Rows"
    md = Markdown(MARKDOWN)
    print(md)

    cursor.execute("USE forest_coverage;")
    df = pd.read_sql("SELECT * FROM forest_coverage", conn)

    print("[b]Select the state for which the records need to be deleted:[/b]")

    root = ttk.Tk()
    root.wm_attributes("-topmost", 1)
    root.title("DELETE MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = df["State_UT"].values.tolist()

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(
        mainframe, text="Select the state for which the records need to be deleted:"
    ).grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()
    val = (tkvar.get(),)
    v = tkvar.get()
    print(tkvar.get())

    print("")

    df = pd.read_sql(
        "SELECT * FROM forest_coverage WHERE State_UT =" + "'" + v + "'", conn
    )
    df = df.style.hide_index()
    display(df)

    print("[b]Do you really want to delete the fields:[/b]")

    root = ttk.Tk()
    root.wm_attributes("-topmost", 1)
    root.title("MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = ["1. Yes,Confirm delete", "2. No"]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Select option:").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    opm = tkvar.get()
    print(opm)
    print("")

    if opm == "1. Yes,Confirm delete":

        sql = "DELETE FROM forest_coverage WHERE State_UT = %s"
        spincursor()
        cursor.execute(sql, val)
        message = "Fields deleted...\n"
        typewriter(message)
        conn.commit()
        ShowTableMenu()
    print("[b]Do you want to continue:[/b]")

    root = ttk.Tk()
    root.wm_attributes("-topmost", 1)
    root.title("MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = ["1. Go back to Delete Menu", "2. Go back to Main Menu", "3. Exit"]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Select option:").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    opm = tkvar.get()
    print(opm)
    print("")

    if opm == "1. Go back to Delete Menu":

        clr()
        DeleteRows()
    elif opm == "2. Go back to Main Menu":

        clr()
        opt()
    elif opm == "3. Exit":

        clr()
        print("*" * 26, "[b][green]Thank You[/b][/green]", "*" * 26)


def UpdateInformation():

    MARKDOWN = "# Update Information"
    md = Markdown(MARKDOWN)
    print(md)

    cursor.execute("USE forest_coverage;")
    df = pd.read_sql("SELECT * FROM forest_coverage", conn)

    print("[b]Select the state for which the records need to be updated:[/b]")

    root = ttk.Tk()
    root.title("UPDATE MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = df["State_UT"].values.tolist()

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(
        mainframe, text="Select the state for which the records need to be updated:"
    ).grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    val_3 = tkvar.get()
    print(val_3)
    print("")

    print("[b]Select the year for which the records need to be updated:[/b]")

    root = ttk.Tk()
    root.title("UPDATE MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = [
        "year_1987",
        "year_1989",
        "year_1991",
        "year_1993",
        "year_1995",
        "year_1997",
        "year_1999",
        "year_2001",
        "year_2003",
        "year_2005",
        "year_2007",
        "year_2011",
        "year_2013",
    ]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(
        mainframe, text="Select the year for which the records need to be updated:"
    ).grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    val_1 = tkvar.get()
    print(val_1)
    print("")

    try:

        val_2 = int(
            input(
                "Enter the new Forest coverage for the field "
                + val_1
                + " in square kilometres: "
            )
        )
        sql = "UPDATE forest_coverage SET " + val_1 + " =%s WHERE State_UT = %s"
        val = (val_2, val_3)
        cursor.execute(sql, val)

        spincursor()
        message = "Fields updated...\n"
        typewriter(message)

        conn.commit()
        ShowTableMenu()
    except ValueError:

        print("[cyan]Enter valid data[/cyan]")
        clr()
        UpdateInformation()
    print("[b]Do you want to continue:[/b]")

    root = ttk.Tk()
    root.title("MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = ["1. Go back to Update Menu", "2. Go back to Main Menu", "3. Exit"]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Select option:").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    opm = tkvar.get()
    print(opm)
    print("")

    if opm == "1. Go back to Update Menu":

        clr()
        UpdateInformation()
    elif opm == "2. Go back to Main Menu":

        clr()
        opt()
    elif opm == "3. Exit":

        clr()
        print("*" * 26, "[b][green]Thank You[/b][/green]", "*" * 26)


def SortData():

    MARKDOWN = "# Sort Data"
    md = Markdown(MARKDOWN)
    print(md)

    cursor.execute("USE forest_coverage;")
    print("[b]Select wheter to sort data in ascending or descending:[/b]")

    root = ttk.Tk()
    root.title("SORT MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = ["Ascending", "Descending"]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(
        mainframe, text="Select wheter to sort data in ascending or descending:"
    ).grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    way = tkvar.get()
    print(way)
    print("")

    print("[b]Select the field on which sorting needs to be done:[/b]")

    root = ttk.Tk()
    root.title("SORT MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = [
        "State_UT",
        "year_1987",
        "year_1989",
        "year_1991",
        "year_1993",
        "year_1995",
        "year_1997",
        "year_1999",
        "year_2001",
        "year_2003",
        "year_2005",
        "year_2007",
        "year_2011",
        "year_2013",
    ]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(
        mainframe, text="Select the field on which the records need to be sorted:"
    ).grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    field = tkvar.get()
    print(field)
    message = "Sorting Data...\n"
    typewriter(message)

    df = pd.read_sql("SELECT * FROM forest_coverage", conn)

    if way == "Ascending":

        df = pd.read_sql("SELECT * FROM forest_coverage ORDER BY " + field, conn)
        df = df.style.hide_index()
        display(df)
    elif way == "Descending":

        df = pd.read_sql(
            "SELECT * FROM forest_coverage ORDER BY " + field + " DESC", conn
        )
        df = df.style.hide_index()
        display(df)
    print("[b]Do you want to continue:[/b]")

    root = ttk.Tk()
    root.title("MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = ["1. Go back to Sort Menu", "2. Go back to Main Menu", "3. Exit"]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Select option:").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    opm = tkvar.get()
    print(opm)
    print("")

    if opm == "1. Go back to Sort Menu":

        clr()
        SortData()
    elif opm == "2. Go back to Main Menu":

        clr()
        opt()
    elif opm == "3. Exit":

        clr()
        print("*" * 26, "[b][green]Thank You[/b][/green]", "*" * 26)


def DisplayTopRecords():

    MARKDOWN = "# Display Top Records"
    md = Markdown(MARKDOWN)
    print(md)

    df = pd.read_sql("SELECT * FROM forest_coverage", conn)

    print("[b]Select the number of top rows to be shown:[/b]")

    root = ttk.Tk()
    root.title("OPTION MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
    ]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Select the number of top rows to be shown:").grid(
        row=1, column=1
    )
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    rows = int(tkvar.get())
    print(rows)

    trdf = df.head(rows)
    trdf = trdf.style.hide_index()
    message = "Fetching data...\n"
    typewriter(message)
    display(trdf)

    print("[b]Do you want to continue:[/b]")

    root = ttk.Tk()
    root.title("MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = [
        "1. Go back to Dispaly top Records Menu",
        "2. Go back to Main Menu",
        "3. Exit",
    ]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Select option:").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    opm = tkvar.get()
    print(opm)
    print("")

    if opm == "1. Go back to Dispaly top Records Menu":

        clr()
        DisplayTopRecords()
    elif opm == "2. Go back to Main Menu":

        clr()
        opt()
    elif opm == "3. Exit":

        clr()
        print("*" * 26, "[b][green]Thank You[/b][/green]", "*" * 26)


def DisplayBottomRecords():

    MARKDOWN = "# Display Bottom Records"
    md = Markdown(MARKDOWN)
    print(md)
    df = pd.read_sql("SELECT * FROM forest_coverage", conn)

    print("[b]Select the number of bottom rows to be shown:[/b]")

    root = ttk.Tk()
    root.title("OPTION MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
    ]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Select the number of bottom rows to be shown:").grid(
        row=1, column=1
    )
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    rows = int(tkvar.get())
    print(rows)

    brdf = df.tail(rows)
    brdf = brdf.style.hide_index()
    message = "Fetching data...\n"
    typewriter(message)
    display(brdf)

    print("[b]Do you want to continue:[/b]")

    root = ttk.Tk()
    root.title("MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = [
        "1. Go back to Dispaly bottom Records Menu",
        "2. Go back to Main Menu",
        "3. Exit",
    ]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Select option:").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    opm = tkvar.get()
    print(opm)
    print("")

    if opm == "1. Go back to Dispaly bottom Records Menu":

        DisplayBottomRecords()
    elif opm == "2. Go back to Main Menu":

        opt()
    elif opm == "3. Exit":

        clr()
        print("*" * 26, "[b][green]Thank You[/b][/green]", "*" * 26)


def DisplayOnCriteria():

    MARKDOWN = "# Display on Criteria"
    md = Markdown(MARKDOWN)
    print(md)
    cursor.execute("USE forest_coverage;")
    df = pd.read_sql("SELECT * FROM forest_coverage", conn)

    st = df["State_UT"]
    print("[b]Select the criterions on which fields need to be displayed:[/b]")

    root = ttk.Tk()
    root.title("CRITERION MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = [
        """1. Display the highest forest coverage along with the state 
    of a particular year""",
        """2. Display the lowest forest coverage along with the state 
    of a particular year""",
        "3. Display the Sum of forest coverage for a particular year",
        "4. Display the forest coverage for a particular state year-wise",
        "5. Display the forest coverage for a particular year state-wise",
        "6. Display State/UT names",
    ]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(
        mainframe, text="Select the criterions on which fields need to be displayed"
    ).grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    criteria = tkvar.get()
    print(criteria)

    if (
        criteria
        == """1. Display the highest forest coverage along with the state 
    of a particular year"""
    ):
        print("[b]Select the year:[/b]")
        root = ttk.Tk()
        root.title("CRITERIA YEAR MENU")

        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe.pack(pady=100, padx=100)

        tkvar = ttk.StringVar(root)

        choices = [
            "year_1987",
            "year_1989",
            "year_1991",
            "year_1993",
            "year_1995",
            "year_1997",
            "year_1999",
            "year_2001",
            "year_2003",
            "year_2005",
            "year_2007",
            "year_2011",
            "year_2013",
        ]

        popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
        ttk.Label(
            mainframe,
            text="Select the year for which highest forest cover needs to be shown:",
        ).grid(row=1, column=1)
        popupMenu.grid(row=2, column=1)

        def change_dropdown(*args):

            tkvar.get()

        tkvar.trace("w", change_dropdown)

        kswitch = ttk.Button(root, text="OK", command=root.destroy)
        kswitch.pack(pady=10)

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_closing)

        root.mainloop()

        field = tkvar.get()
        print(field)

        df = pd.read_sql("SELECT * FROM forest_coverage", conn)
        df1 = df[field].max()
        df2 = df[df[field] == df1]
        df2 = df2["State_UT"]
        df2 = pd.DataFrame(df2)
        df2 = df2.style.hide_index()
        print(
            "The highest forest coverage for " + field + " is ",
            df1,
            " occuring in the following states/UTs:",
        )
        display(df2)
    elif (
        criteria
        == """2. Display the lowest forest coverage along with the state 
    of a particular year"""
    ):

        print("[b]Select the year[/b]")
        root = ttk.Tk()
        root.title("CRITERIA YEAR MENU")

        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe.pack(pady=100, padx=100)

        tkvar = ttk.StringVar(root)

        choices = [
            "year_1987",
            "year_1989",
            "year_1991",
            "year_1993",
            "year_1995",
            "year_1997",
            "year_1999",
            "year_2001",
            "year_2003",
            "year_2005",
            "year_2007",
            "year_2011",
            "year_2013",
        ]

        popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
        ttk.Label(
            mainframe,
            text="Select the year for which lowest forest cover needs to be shown:",
        ).grid(row=1, column=1)
        popupMenu.grid(row=2, column=1)

        def change_dropdown(*args):

            tkvar.get()

        tkvar.trace("w", change_dropdown)

        kswitch = ttk.Button(root, text="OK", command=root.destroy)
        kswitch.pack(pady=10)

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_closing)

        root.mainloop()

        field = tkvar.get()
        print(field)

        df = pd.read_sql("SELECT * FROM forest_coverage", conn)
        df1 = df[field].min()
        df2 = df[df[field] == df1]
        df2 = df2["State_UT"]
        df2 = pd.DataFrame(df2)
        df2 = df2.style.hide_index()
        print(
            "The lowest forest coverage for " + field + " is ",
            df1,
            " occuring in the following states/UTs:",
        )
        display(df2)
    elif criteria == "3. Display the Sum of forest coverage for a particular year":

        print("[b]Select the year:[/b]")
        root = ttk.Tk()
        root.title("CRITERIA YEAR MENU")

        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe.pack(pady=100, padx=100)

        tkvar = ttk.StringVar(root)

        choices = [
            "year_1987",
            "year_1989",
            "year_1991",
            "year_1993",
            "year_1995",
            "year_1997",
            "year_1999",
            "year_2001",
            "year_2003",
            "year_2005",
            "year_2007",
            "year_2011",
            "year_2013",
        ]

        popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
        ttk.Label(
            mainframe,
            text="Select the year for which lowest forest cover needs to be shown:",
        ).grid(row=1, column=1)
        popupMenu.grid(row=2, column=1)

        def change_dropdown(*args):

            tkvar.get()

        tkvar.trace("w", change_dropdown)

        kswitch = ttk.Button(root, text="OK", command=root.destroy)
        kswitch.pack(pady=10)

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_closing)

        root.mainloop()

        field = tkvar.get()
        print(field)

        df = pd.read_sql("SELECT * FROM forest_coverage", conn)
        df = df[field].sum()
        print("The sum of forest coverage for " + field + " is " + str(df))
    elif criteria == "4. Display the forest coverage for a particular state year-wise":

        print("[b]Select the state:[/b]")
        root = ttk.Tk()
        root.title("STATE MENU")

        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe.pack(pady=100, padx=100)

        tkvar = ttk.StringVar(root)

        choices = df["State_UT"].values.tolist()

        popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
        ttk.Label(
            mainframe,
            text="Select the state for which forest coverage needs to be shown:",
        ).grid(row=1, column=1)
        popupMenu.grid(row=2, column=1)

        def change_dropdown(*args):

            tkvar.get()

        tkvar.trace("w", change_dropdown)

        kswitch = ttk.Button(root, text="OK", command=root.destroy)
        kswitch.pack(pady=10)

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_closing)

        root.mainloop()

        field = tkvar.get()
        print(field)

        df = pd.read_sql("SELECT * FROM forest_coverage", conn)
        df = df[df["State_UT"] == field]
        df = df.style.hide_index()

        display(df)
    elif criteria == "5. Display the forest coverage for a particular year state-wise":

        print("[b]Select the year:[/b]")
        root = ttk.Tk()
        root.wm_attributes("-topmost", 1)
        root.title("CRITERIA YEAR MENU")

        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe.pack(pady=100, padx=100)

        tkvar = ttk.StringVar(root)

        choices = [
            "year_1987",
            "year_1989",
            "year_1991",
            "year_1993",
            "year_1995",
            "year_1997",
            "year_1999",
            "year_2001",
            "year_2003",
            "year_2005",
            "year_2007",
            "year_2011",
            "year_2013",
        ]

        popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
        ttk.Label(
            mainframe,
            text="Select the year for which forest cover needs to be shown state-wise:",
        ).grid(row=1, column=1)
        popupMenu.grid(row=2, column=1)

        def change_dropdown(*args):

            tkvar.get()

        tkvar.trace("w", change_dropdown)

        kswitch = ttk.Button(root, text="OK", command=root.destroy)
        kswitch.pack(pady=10)

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_closing)

        root.mainloop()

        field = tkvar.get()
        print(field)
        df = pd.read_sql(
            "SELECT State_UT, " + field + " FROM forest_coverage GROUP BY State_UT",
            conn,
        )
        df = df.style.hide_index()
        display(df)
    elif criteria == "6. Display State/UT names":

        df = pd.read_sql("SELECT * FROM forest_coverage", conn)
        df1 = df["State_UT"]
        df1 = pd.DataFrame(df1)
        df1 = df1.T
        df1 = df1.style.hide_index()

        display(df1)
    print("[b]Do you want to continue:[/b]")

    root = ttk.Tk()
    root.wm_attributes("-topmost", 1)
    root.title("MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = [
        "1. Go back to Criteria selection Menu",
        "2. Go back to Main Menu",
        "3. Exit",
    ]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Select option:").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    opm = tkvar.get()
    print(opm)
    print("")

    if opm == "1. Go back to Criteria selection Menu":

        clr()
        DisplayOnCriteria()
    elif opm == "2. Go back to Main Menu":

        clr()
        opt()
    elif opm == "3. Exit":

        clr()
        print("*" * 26, "[b][green]Thank You[/b][/green]", "*" * 26)


def Linegraph():

    MARKDOWN = "# Line-Graph"
    md = Markdown(MARKDOWN)
    print(md)
    cursor.execute("USE forest_coverage;")
    df = pd.read_sql("SELECT * FROM forest_coverage", conn)

    st = df["State_UT"]

    print("[b]Select specific Line Chart as given below:[/b]")
    print("")
    print("[i]Select 1 to visualize the data of for State vs year forest coverage[/i]")
    print("[i]Select 2 to compare the data of two years forest coverage[/i]")
    print("[i]Select 3 to merge all data in one Line Graph[/i]")

    print("")

    print("[b]Select option:[/b]")

    root = ttk.Tk()
    root.wm_attributes("-topmost", 1)
    root.title("LINE-GRAPH OPTION MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = [
        "1. Visualize the data for State vs year forest coverage",
        "2. Compare the data of two years' forest coverage",
        "3. Merge all data in one Line Graph",
    ]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Choose Option -- Line Graph").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    op = tkvar.get()
    print(op)

    with plt.style.context("ggplot"):

        f = plt.figure()

        font = {"size": 30}
        plt.rc("font", **font)

        f.set_figwidth(30)
        f.set_figheight(10)

        if op == "1. Visualize the data for State vs year forest coverage":

            print("[b]Select the year:[/b]")

            root = ttk.Tk()
            root.wm_attributes("-topmost", 1)
            root.title("Year-Menu")

            mainframe = ttk.Frame(root)
            mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
            mainframe.columnconfigure(0, weight=1)
            mainframe.rowconfigure(0, weight=1)
            mainframe.pack(pady=100, padx=100)

            tkvar = ttk.StringVar(root)

            choices = [
                "year_1987",
                "year_1989",
                "year_1991",
                "year_1993",
                "year_1995",
                "year_1997",
                "year_1999",
                "year_2001",
                "year_2003",
                "year_2005",
                "year_2007",
                "year_2011",
                "year_2013",
            ]

            popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
            ttk.Label(
                mainframe,
                text="Select the year for which forest cover needs to be shown:",
            ).grid(row=1, column=1)
            popupMenu.grid(row=2, column=1)

            def change_dropdown(*args):

                tkvar.get()

            tkvar.trace("w", change_dropdown)

            kswitch = ttk.Button(root, text="OK", command=root.destroy)
            kswitch.pack(pady=10)

            def on_closing():
                if messagebox.askokcancel("Quit", "Do you want to quit?"):
                    root.destroy()

            root.protocol("WM_DELETE_WINDOW", on_closing)

            root.mainloop()

            opyr = tkvar.get()
            print(opyr)
            print("")
            yr = df[opyr]

            plt.plot(st, yr)
            plt.xlabel("State/UTs")
            plt.xticks(rotation=90)
            plt.show()
        elif op == "2. Compare the data of two years' forest coverage":

            def l2():
                print("[b]Select the years to be compared:[/b]")
                print("[b]First-Year:[/b]")

                root = ttk.Tk()
                root.wm_attributes("-topmost", 1)
                root.title("Year-Menu")

                mainframe = ttk.Frame(root)
                mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
                mainframe.columnconfigure(0, weight=1)
                mainframe.rowconfigure(0, weight=1)
                mainframe.pack(pady=100, padx=100)

                tkvar = ttk.StringVar(root)

                choices = [
                    "year_1987",
                    "year_1989",
                    "year_1991",
                    "year_1993",
                    "year_1995",
                    "year_1997",
                    "year_1999",
                    "year_2001",
                    "year_2003",
                    "year_2005",
                    "year_2007",
                    "year_2011",
                    "year_2013",
                ]

                popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
                ttk.Label(
                    mainframe,
                    text="""Select the first year for which forest cover
                        needs to be compared:""",
                ).grid(row=1, column=1)
                popupMenu.grid(row=2, column=1)

                def change_dropdown(*args):

                    tkvar.get()

                tkvar.trace("w", change_dropdown)

                kswitch = ttk.Button(root, text="OK", command=root.destroy)
                kswitch.pack(pady=10)

                def on_closing():
                    if messagebox.askokcancel("Quit", "Do you want to quit?"):
                        root.destroy()

                root.protocol("WM_DELETE_WINDOW", on_closing)

                root.mainloop()

                opyr1 = tkvar.get()
                print(opyr1)
                print("")

                print("[b]Second-Year:[/b]")

                root = ttk.Tk()
                root.wm_attributes("-topmost", 1)
                root.title("Year-Menu")

                mainframe = ttk.Frame(root)
                mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
                mainframe.columnconfigure(0, weight=1)
                mainframe.rowconfigure(0, weight=1)
                mainframe.pack(pady=100, padx=100)

                tkvar = ttk.StringVar(root)

                choices = [
                    "year_1987",
                    "year_1989",
                    "year_1991",
                    "year_1993",
                    "year_1995",
                    "year_1997",
                    "year_1999",
                    "year_2001",
                    "year_2003",
                    "year_2005",
                    "year_2007",
                    "year_2011",
                    "year_2013",
                ]

                popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
                ttk.Label(
                    mainframe,
                    text="""Select the second year for which forest cover
                        needs to be compared:""",
                ).grid(row=1, column=1)
                popupMenu.grid(row=2, column=1)

                def change_dropdown(*args):

                    tkvar.get()

                tkvar.trace("w", change_dropdown)

                kswitch = ttk.Button(root, text="OK", command=root.destroy)
                kswitch.pack(pady=10)

                def on_closing():
                    if messagebox.askokcancel("Quit", "Do you want to quit?"):
                        root.destroy()

                root.protocol("WM_DELETE_WINDOW", on_closing)

                root.mainloop()

                opyr2 = tkvar.get()
                print(opyr2)
                print("")

                yr1 = df[opyr1]
                yr2 = df[opyr2]

                if opyr1 != opyr2:

                    plt.plot(st, yr1, label=opyr1)
                    plt.plot(st, yr2, label=opyr2)
                    plt.xlabel("State/UTs")
                    plt.xticks(rotation=90)
                    plt.legend(frameon=False, bbox_to_anchor=(1.0, 1.0))
                    plt.show()
                if opyr1 == opyr2:

                    print("[cyan]Cannot Compare data for the same years[/cyan]")
                    return l2()

            l2()
        elif op == "3. Merge all data in one Line Graph":

            choices = [
                "year_1987",
                "year_1989",
                "year_1991",
                "year_1993",
                "year_1995",
                "year_1997",
                "year_1999",
                "year_2001",
                "year_2003",
                "year_2005",
                "year_2007",
                "year_2011",
                "year_2013",
            ]

            plt.ylabel("Forest Coverage")

            for yr in choices:

                plt.plot(st, df[yr], label=yr)
            plt.legend(frameon=False, bbox_to_anchor=(1.0, 1.0))
            plt.xlabel("State/UTs")
            plt.xticks(rotation=90)
            plt.show()
            print("[b]Do you want to continue:[/b]")
    root = ttk.Tk()
    root.wm_attributes("-topmost", 1)
    root.title("MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = ["1. Go back to Line-Graph Menu", "2. Go back to Main Menu", "3. Exit"]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Select option:").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    opm = tkvar.get()
    print(opm)
    print("")

    if opm == "1. Go back to Line-Graph Menu":

        clr()
        Linegraph()
    elif opm == "2. Go back to Main Menu":

        clr()
        opt()
    elif opm == "3. Exit":

        clr()
        print("*" * 26, "[b][green]Thank You[/b][/green]", "*" * 26)


def BarGraph():

    MARKDOWN = "# Bar-Graph"
    md = Markdown(MARKDOWN)
    print(md)
    cursor.execute("USE forest_coverage;")
    df = pd.read_sql("SELECT * FROM forest_coverage", conn)

    st = df["State_UT"]

    print("[b]Select specific Bar Chart as given below:[/b]")
    print("")

    print("[i]Select 1 to visualize the Year-wise data for a specific State[/i]")
    print("[i]Select 2 to Compare  year-wise forest coverage data of two states")
    print("")

    print("[b]Select option:[/b]")

    root = ttk.Tk()
    root.wm_attributes("-topmost", 1)
    root.title("Bar-GRAPH OPTION MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = [
        "1. Visualize the Year-wise data for a specific State",
        "2. Compare  year-wise forest coverage data of two states",
    ]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Choose Option -- Bar Graph").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    op = tkvar.get()
    print(op)

    with plt.style.context("ggplot"):

        f = plt.figure()

        font = {"size": 30}
        plt.rc("font", **font)

        f.set_figwidth(40)
        f.set_figheight(20)

        if op == "1. Visualize the Year-wise data for a specific State":

            print("[b]Select the State:[/b]")

            root = ttk.Tk()
            root.wm_attributes("-topmost", 1)
            root.title("STATE SELECT MENU")

            mainframe = ttk.Frame(root)
            mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
            mainframe.columnconfigure(0, weight=1)
            mainframe.rowconfigure(0, weight=1)
            mainframe.pack(pady=100, padx=100)

            tkvar = ttk.StringVar(root)

            choices = df["State_UT"].values.tolist()

            year = [
                "year_1987",
                "year_1989",
                "year_1991",
                "year_1993",
                "year_1995",
                "year_1997",
                "year_1999",
                "year_2001",
                "year_2003",
                "year_2005",
                "year_2007",
                "year_2011",
                "year_2013",
            ]
            st2 = pd.DataFrame(year)

            popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
            ttk.Label(
                mainframe,
                text="Select State for which Year-wise forest cover needs to be shown:",
            ).grid(row=1, column=1)
            popupMenu.grid(row=2, column=1)

            def change_dropdown(*args):

                tkvar.get()

            tkvar.trace("w", change_dropdown)

            kswitch = ttk.Button(root, text="OK", command=root.destroy)
            kswitch.pack(pady=10)
            st = tkvar.get()

            df0 = df.values.tolist()
            df1 = pd.DataFrame(data=df0)
            df1 = df1.T
            df2 = pd.DataFrame(df1)

            df2.insert(0, column="Year", value=st)
            df2.to_csv("Forest1", header=True)
            df2 = pd.read_csv("Forest1", skiprows=1)

            def on_closing():
                if messagebox.askokcancel("Quit", "Do you want to quit?"):
                    root.destroy()

            root.protocol("WM_DELETE_WINDOW", on_closing)

            root.mainloop()

            opst = tkvar.get()

            print(opst)
            print("")
            data = df2[opst]
            st = df2["0"]

            barWidth1 = 0.7
            barWidth2 = 0.35

            plt.bar(st2[0], data, label=opst, width=barWidth1)

            plt.xticks(rotation=90)

            plt.legend(frameon=False, bbox_to_anchor=(1.0, 1.0))
            plt.show()
        elif op == "2. Compare  year-wise forest coverage data of two states":

            def b2():

                print("[b]Select the years to be compared:[/b]")
                print("[b]First-State:[/b]")

                root = ttk.Tk()
                root.wm_attributes("-topmost", 1)
                root.title("STATE SELECT MENU")

                mainframe = ttk.Frame(root)
                mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
                mainframe.columnconfigure(0, weight=1)
                mainframe.rowconfigure(0, weight=1)
                mainframe.pack(pady=100, padx=100)

                tkvar = ttk.StringVar(root)

                choices = df["State_UT"].values.tolist()

                year = [
                    "year_1987",
                    "year_1989",
                    "year_1991",
                    "year_1993",
                    "year_1995",
                    "year_1997",
                    "year_1999",
                    "year_2001",
                    "year_2003",
                    "year_2005",
                    "year_2007",
                    "year_2011",
                    "year_2013",
                ]
                st2 = pd.DataFrame(year)

                popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
                ttk.Label(
                    mainframe,
                    text="""Select the first state for which year wise forest cover
                                needs to be compared:""",
                ).grid(row=1, column=1)
                popupMenu.grid(row=2, column=1)

                def change_dropdown(*args):

                    tkvar.get()

                tkvar.trace("w", change_dropdown)

                kswitch = ttk.Button(root, text="OK", command=root.destroy)
                kswitch.pack(pady=10)
                st = tkvar.get()

                df0 = df.values.tolist()
                df1 = pd.DataFrame(data=df0)
                df1 = df1.T
                df2 = pd.DataFrame(df1)

                df2.insert(0, column="Year", value=st)
                df2.to_csv("Forest1", header=True)
                df2 = pd.read_csv("Forest1", skiprows=1)

                def on_closing():
                    if messagebox.askokcancel("Quit", "Do you want to quit?"):
                        root.destroy()

                root.protocol("WM_DELETE_WINDOW", on_closing)

                root.mainloop()
                opst1 = tkvar.get()
                print(opst1)

                print("")
                data1 = df2[opst1].T
                st = df2["0"]
                print("[b]Second-:[/b]")

                root = ttk.Tk()
                root.wm_attributes("-topmost", 1)
                root.title("State-Menu")
                tkvar = ttk.StringVar(root)
                mainframe = ttk.Frame(root)
                mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
                mainframe.columnconfigure(0, weight=1)
                mainframe.rowconfigure(0, weight=1)
                mainframe.pack(pady=100, padx=100)

                tkvar1 = ttk.StringVar(root)
                choices = df["State_UT"].values.tolist()
                year = [
                    "year_1987",
                    "year_1989",
                    "year_1991",
                    "year_1993",
                    "year_1995",
                    "year_1997",
                    "year_1999",
                    "year_2001",
                    "year_2003",
                    "year_2005",
                    "year_2007",
                    "year_2011",
                    "year_2013",
                ]

                popupMenu = ttk.OptionMenu(mainframe, tkvar1, *choices)
                ttk.Label(
                    mainframe,
                    text="""Select the second state for which year wise forest cover
                                needs to be compared:""",
                ).grid(row=1, column=1)
                popupMenu.grid(row=2, column=1)

                def change_dropdown(*args):

                    tkvar1.get()

                tkvar.trace("w", change_dropdown)

                kswitch = ttk.Button(root, text="OK", command=root.destroy)
                kswitch.pack(pady=10)

                def on_closing():
                    if messagebox.askokcancel("Quit", "Do you want to quit?"):
                        root.destroy()

                root.protocol("WM_DELETE_WINDOW", on_closing)

                root.mainloop()

                opst2 = tkvar1.get()
                print(opst2)
                data2 = df2[opst2].T
                st = df2["0"]

                barWidth1 = 0.7
                barWidth2 = 0.35

                if opst1 != opst2:

                    plt.bar(st2[0], data1, label=opst1, width=barWidth1)
                    plt.bar(st2[0], data2, label=opst2, width=barWidth2)
                    plt.xlabel("Years")
                    plt.xticks(rotation=90)
                    plt.ylabel("Forest coverage")
                    plt.legend(frameon=False, bbox_to_anchor=(1.0, 1.0))
                    plt.show()
                if opst1 == opst2:

                    print("[cyan]Cannot Compare data for the same state[/cyan]")
                    return b2()

            b2()
    root = ttk.Tk()
    root.wm_attributes("-topmost", 1)
    root.title("MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = ["1. Go back to Bar-Graph Menu", "2. Go back to Main Menu", "3. Exit"]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Select option:").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    opm = tkvar.get()
    print(opm)
    print("")

    if opm == "1. Go back to Bar-Graph Menu":

        clr()
        BarGraph()
    elif opm == "2. Go back to Main Menu":

        clr()
        opt()
    elif opm == "3. Exit":

        clr()
        print("*" * 26, "[b][green]Thank You[/b][/green]", "*" * 26)


def HistogramGraph():

    MARKDOWN = "# Histogram"
    md = Markdown(MARKDOWN)
    print(md)
    cursor.execute("USE forest_coverage;")
    df = pd.read_sql("SELECT * FROM forest_coverage", conn)

    st = df["State_UT"]

    print("[b]Select specific Histogram as given below:[/b]")
    print("")
    print("[i]Visualize the data for State vs year forest coverage[/i]")
    print("")

    print("[b]Select option:[/b]")

    root = ttk.Tk()
    root.wm_attributes("-topmost", 1)
    root.title("HISTOGRAM OPTION MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = ["Visualize the data for State vs year forest coverage"]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Choose Option -- Histogram").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    op = tkvar.get()
    print(op)

    if op == "Visualize the data for State vs year forest coverage":

        print("[b]Select the year for which forest cover needs to be shown:[/b]")

        root = ttk.Tk()
        root.wm_attributes("-topmost", 1)
        root.title("Year-Menu")

        mainframe = ttk.Frame(root)
        mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe.pack(pady=100, padx=100)

        tkvar = ttk.StringVar(root)

        choices = [
            "year_1987",
            "year_1989",
            "year_1991",
            "year_1993",
            "year_1995",
            "year_1997",
            "year_1999",
            "year_2001",
            "year_2003",
            "year_2005",
            "year_2007",
            "year_2011",
            "year_2013",
        ]

        popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
        ttk.Label(
            mainframe, text="Select the year for which forest cover needs to be shown:"
        ).grid(row=1, column=1)
        popupMenu.grid(row=2, column=1)

        def change_dropdown(*args):

            tkvar.get()

        tkvar.trace("w", change_dropdown)

        kswitch = ttk.Button(root, text="OK", command=root.destroy)
        kswitch.pack(pady=10)

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_closing)

        root.mainloop()

        opyr = tkvar.get()

        print(opyr)
        print("")
        yr = df[opyr]

        with plt.style.context("ggplot"):

            font = {"size": 30}
            plt.rc("font", **font)

            f = plt.figure()
            f.set_figwidth(40)
            f.set_figheight(60)

            plt.hist(yr, bins=np.arange(0, max(yr) + 1, 10000), edgecolor="white")
            plt.xlabel("Distribution")
            plt.ylabel("Frequency/No. of States")
            plt.xticks(rotation=90)

            plt.show()
    print("[b]Do you want to continue:[/b]")

    root = ttk.Tk()
    root.wm_attributes("-topmost", 1)
    root.title("MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = ["1. Go back to Main Menu", "2. Exit"]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Select option:").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    opm = tkvar.get()
    print(opm)
    print("")

    if opm == "1. Go back to Main Menu":

        clr()
        opt()
    elif opm == "2. Exit":

        clr()
        print("*" * 26, "[b][green]Thank You[/b][/green]", "*" * 26)


def DataExportCSV():

    MARKDOWN = "# Data Export to CSV"

    md = Markdown(MARKDOWN)
    print(md)
    message = "Reading data from Database...\n"

    typewriter(message)

    message = "Exporting data to CSV...\n"

    typewriter(message)

    cursor.execute("USE forest_coverage;")

    df = pd.read_sql("SELECT * FROM forest_coverage", conn)

    savewin = ttk.Tk()
    savewin.geometry("300x150")
    savewin.title("Save Data Frame to CSV")
    font1 = ("Times", 24, "bold")

    def save():
        files = [("CSV File", "*.csv"), ("Text Document", "*.txt")]
        file = asksaveasfile(filetypes=files, defaultextension=files)
        df.to_csv(file)
        btn.pack_forget()
        ttk.Label(
            savewin, width="30", text="File Saved as", bg="white", fg="black"
        ).pack()
        ttk.Label(savewin, width="30", text=file.name, bg="blue", fg="white").pack()
        kswitch = ttk.Button(savewin, text="OK", command=savewin.destroy)
        kswitch.pack(pady=20)

    ttk.Label(savewin, width="30", text="", bg="orange", fg="white").pack()
    btn = ttk.Button(savewin, text="File Save As", command=lambda: save())
    btn.pack(pady=20)

    savewin.mainloop()

    print("[b]Do you want to continue:[/b]")

    root = ttk.Tk()
    root.wm_attributes("-topmost", 1)
    root.title("MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)

    tkvar = ttk.StringVar(root)

    choices = ["1. Go back to Main Menu", "2. Exit"]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Select option:").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Select option:").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    opm = tkvar.get()
    print(opm)
    print("")

    if opm == "1. Go back to Main Menu":

        clr()
        opt()
    elif opm == "2. Exit":

        clr()
        print("*" * 26, "[b][green]Thank You[/b][/green]", "*" * 26)


def clr():

    sleep(1)
    for i in range(10):
        clear_output(wait=True)


def opt():

    print("[b]Select option:[/b]")

    root = ttk.Tk()
    root.wm_attributes("-topmost", 1)
    root.title("OPTION MENU")

    mainframe = ttk.Frame(root)
    mainframe.grid(column=0, row=0, sticky=(ttk.N, ttk.W, ttk.E, ttk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=100, padx=100)
    tkvar = ttk.StringVar(root)

    choices = [
        "1. Data import from CSV to SQL",
        "2. Data import from CSV to DataFrame",
        "3. Insert rows",
        "4. Delete rows",
        "5. Update information",
        "6. Sort data",
        "7. Display top records",
        "8. Display bottom records",
        "9. Display particular fields depending on criterias",
        "10. Line Graph",
        "11. Bar Graph",
        "12. Histogram",
        "13. Transfer the changes done back to csv",
        "14. EXIT",
    ]

    popupMenu = ttk.OptionMenu(mainframe, tkvar, *choices)
    ttk.Label(mainframe, text="Choose Option").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)

    def change_dropdown(*args):

        tkvar.get()

    tkvar.trace("w", change_dropdown)

    kswitch = ttk.Button(root, text="OK", command=root.destroy)
    kswitch.pack(pady=10)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

    opt = tkvar.get()
    print(opt)
    print("")

    clr()
    if opt == "1. Data import from CSV to SQL":

        DataImportCSVtoSQL()
    elif opt == "2. Data import from CSV to DataFrame":

        DataImportCSVtoDF()
    elif opt == "3. Insert rows":

        InsertRows()
    elif opt == "4. Delete rows":

        DeleteRows()
    elif opt == "5. Update information":

        UpdateInformation()
    elif opt == "6. Sort data":

        SortData()
    elif opt == "7. Display top records":

        DisplayTopRecords()
    elif opt == "8. Display bottom records":

        DisplayBottomRecords()
    elif opt == "9. Display particular fields depending on criterias":

        DisplayOnCriteria()
    elif opt == "10. Line Graph":

        Linegraph()
    elif opt == "11. Bar Graph":

        BarGraph()
    elif opt == "12. Histogram":

        HistogramGraph()
    elif opt == "13. Transfer the changes done back to csv":

        DataExportCSV()
    elif opt == "14. EXIT":

        clr()
        print("*" * 26, "[b][green]Thank You[/b][/green]", "*" * 26)


try:
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import tkinter as ttk
    from rich.markdown import Markdown
    from tkinter import filedialog, messagebox
    from tkinter.filedialog import asksaveasfile
    import mysql.connector as mysql
    from mysql.connector import Error
    from IPython.display import display, clear_output
    from time import sleep
    from rich import print
    from rich.progress import track
    import sys, time
    from time import sleep

    def login():
        uname = username.get()
        pwd = password.get()
        if username.get() == uname or password.get() == "":
            kswitch = ttk.Button(
                login_screen,
                text="APPLY",
                width=100,
                height=10,
                command=login_screen.destroy,
            )
            kswitch.pack()
        else:

            Loginform()

    def Loginform():

        global login_screen
        login_screen = ttk.Tk()
        login_screen.wm_attributes("-topmost", 1)
        login_screen.title("Login Form")

        login_screen.geometry("300x250+250+100")

        global message
        global username
        global password
        global uname
        global pwd
        global conn
        global cursor

        username = ttk.StringVar()
        password = ttk.StringVar()
        message = ttk.StringVar()
        ttk.Label(
            login_screen,
            width="300",
            text="Please enter details below",
            bg="orange",
            fg="white",
        ).pack()
        ttk.Label(login_screen, text="Username * ").place(x=20, y=40)
        ttk.Entry(login_screen, textvariable=username).place(x=90, y=42)
        ttk.Label(login_screen, text="Password * ").place(x=20, y=80)
        ttk.Entry(login_screen, textvariable=password, show="*").place(x=90, y=82)
        ttk.Label(login_screen, text="", textvariable=message).place(x=95, y=100)
        ttk.Button(
            login_screen, text="Login", width=10, height=1, bg="orange", command=login
        ).place(x=105, y=130)

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                login_screen.destroy()

        login_screen.protocol("WM_DELETE_WINDOW", on_closing)
        login_screen.mainloop()

    try:

        fc = pd.read_csv("ForestCoverage.csv", delimiter=",")

        Loginform()
        uname = username.get()
        pwd = password.get()

        try:

            conn = mysql.connect(
                host="localhost", user=username.get(), password=password.get()
            )

            if conn.is_connected():

                cursor = conn.cursor(buffered=True)

                cursor.execute("DROP DATABASE IF EXISTS forest_coverage;")
                cursor.execute("CREATE DATABASE forest_coverage;")
                cursor.execute("USE forest_coverage;")

                cursor.execute(
                    """CREATE TABLE forest_coverage(State_UT varchar(25),
                        year_1987 bigint, year_1989 bigint,year_1991 bigint,
                        year_1993 bigint, year_1995 bigint, year_1997 bigint,
                        year_1999 bigint,year_2001 bigint, year_2003 bigint,
                        year_2005 bigint, year_2007 bigint, year_2011 bigint,
                        year_2013 bigint, PRIMARY KEY (State_UT))"""
                )

                for i, row in fc.iterrows():

                    sql = """INSERT INTO forest_coverage VALUES
                            (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                    cursor.execute(sql, tuple(row))

                    conn.commit()
                main_menu()
                opt()
                print()
        except Error as e:

            print("[red][b]Error:[/b][/red]", e)
    except FileNotFoundError as e:

        print("[red][b]Error:[/b][/red]", e)
except ModuleNotFoundError as e:

    print("Importing error", e)
