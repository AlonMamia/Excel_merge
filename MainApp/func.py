import tkinter

import pandas as pd
from tkinter import *
from tkinter import ttk


# format the reference number from xxx-x to xxx-00x
def formatRefNum(refNum):
    if '-' in str(refNum):
        res = refNum.split("-")
        res[1] = '{0:0>3}'.format(res[1])
        res = res[0] + '-' + res[1]
    else:
        res = refNum
    return str(res)


def FormatAloctaion(allocation):
    """
    format the allocation number to include only the 9 digits on the left

    :param allocation: allocation number
    :return: 9 left digits of the allocation
    """
    allocation = '{0:0>19}'.format(allocation)
    return str(allocation[10:])


def minimizeRows(data):
    """
    remove rows of duplicate allocation

    :param data:
    :return:
    """
    # next allotment is equal to current allotment
    m1 = (data['הקצאה'] == data['הקצאה'].shift(-1))
    data = data[~(m1)]
    return data


def merger(original, new):
    """
    merges the old and new versions of the excels
    takes the allocations that are in the old excel but not in the new excel and appends them to the new excel

    :param original: old excel file
    :param new: new excel file
    :return: merged excel
    """
    m1 = (original["הקצאה"].isin(new['הקצאה']))
    not_in_new = original[(~m1)]
    result = new.append(not_in_new)
    return result


def debtSum(data):
    """
    sums the debts of a certain allocation
    sets the type of the allocation column as int
    sorts the allocations and sums then minimize the duplicate rows

    :param data: the data frame the is used
    :return: the total sum of the debt of any allocation
    """
    data = data.sort_values('הקצאה')
    data['סכום במטבע מקומי'] = data['סכום במטבע מקומי'].astype(int)
    data.sort_values(['הקצאה', 'ת.פרעוןנטו'], ascending=[True, False], inplace=True)
    m1 = data.groupby('הקצאה')['סכום במטבע מקומי'].sum().reset_index()
    data = data[['הקצאה', "מספר מזהה", 'ת.פרעוןנטו', "חשבון"]]
    data = data.merge(m1, on='הקצאה')
    data = minimizeRows(data)
    return data


def removeExeptions(data):
    """
    removes any exceptions that should not appear in the final excel
    exception may ne a result of a faulty data in any of the given excels

    :param data:the merged data frame of the old and new
    :return:the data frame without the exeptions listed in the functions
    """
    m1 = data['סכום במטבע מקומי'].astype(int) < 0
    data = data[~(m1)]
    return data


def formatType(data):
    """
    format the types of columns in the data frame

    :param data: the data frame the is used
    :return: the data frame columns as their intended types
    """
    data['ת.פרעוןנטו'] = data['ת.פרעוןנטו'].dt.date
    data["סכום במטבע מקומי"] = data["סכום במטבע מקומי"].astype(float)
    return data


def nameChange(data):
    if 'תז תושב' in data:
        data = data.rename(columns={'תז תושב': 'מספר מזהה', 'סכום במטבע מקומי': 'סכום במטבע מקומי'})
    if 'ת.פרעוןנטו' in data:
        data = data.rename(columns={'ת.פרעוןנטו': 'תאריך תחילת החוב'})
    return data


def workSheetFormat(data, worksheet):
    """
    formats the worksheet from left to right, set the width of the columns and apply autofilter to the headers

    :param data: data frame in the worksheet
    :param worksheet: current excel worksheet that we apply changes to
    :return:
    """
    # Change the direction for the worksheet.
    worksheet.right_to_left()
    # Get the dimensions of the dataframe.
    (max_row, max_col) = data.shape
    # Make the columns wider for clarity.
    worksheet.set_column(0, max_col - 1, 12)
    # Set the autofilter.
    worksheet.autofilter(0, 0, max_row, max_col - 1)
    pass


def open_popup(root):
    top = Toplevel(root)
    top.title("התהליך הושלם בהצלחה")
    labelConfirm = Label(top, text="התהליך הושלם בהצלחה")
    labelConfirm.pack()
    # confirm button
    ButtonConfirm = ttk.Button(top, text="אישור", command=top.destroy)
    ButtonConfirm.pack()


# def make_menu(w):
#     global the_menu
#     the_menu = tkinter.Menu(w, tearoff=0)
#     the_menu.add_command(label="Cut")
#     the_menu.add_command(label="Copy")
#     the_menu.add_command(label="Paste")


def show_menu(e):
    """
    generates the cut paste copy function by creating a menu and assigning a command to each label
    :param e: entry label
    :return:
    """
    w = e.widget

    the_menu = tkinter.Menu(w, tearoff=0)
    the_menu.add_command(label="גזירה")
    the_menu.add_command(label="העתקה")
    the_menu.add_command(label="הדבקה")

    the_menu.entryconfigure("גזירה",
                            command=lambda: w.event_generate("<<Cut>>"))
    the_menu.entryconfigure("העתקה",
                            command=lambda: w.event_generate("<<Copy>>"))
    the_menu.entryconfigure("הדבקה",
                            command=lambda: w.event_generate("<<Paste>>"))
    the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)


def nameFormat(data, *args):
    """
    takes a data frame and an unknown number of lists
    each list contains an expected header name in the 0 index in the data frame and a replacement name in the 1 index
    the function will check in the header name is in the data frame and if true will replace it

    :param data: data frame
    :param args: a list that contains an expected header name in the 0 index
    in the data frame and a replacement name in the 1 index
    :return: the data frame with the changed names
    """
    for names in args:
        if names[0] in data:
            data = data.rename(columns={names[0]: names[1]})
    return data
