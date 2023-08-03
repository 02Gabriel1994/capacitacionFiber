import tkinter as tk
from tkcalendar import DateEntry

def show_calendar_from(cal_from):
    cal_from.place(x=10, y=70)

def show_calendar_to():
    cal_to.place(x=10, y=120)

def select_date_from():
    date_from.set(cal_from.get_date())
    cal_from.place_forget()

def select_date_to():
    date_to.set(cal_to.get_date())
    cal_to.place_forget()