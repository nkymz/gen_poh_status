# -*- coding: utf-8 -*-

import os

import openpyxl

PPRO_PATH = os.getenv("HOMEDRIVE", "None") + os.getenv("HOMEPATH", "None") + "/Dropbox/POG/"
PO_HORSELIST_NAME = "POG_HorseList.xlsx"


class POHorseList:

    def __init__(self):
        wbpath = (PPRO_PATH + PO_HORSELIST_NAME).replace("\\", "/")
        self.wb = openpyxl.load_workbook(wbpath)
        self.ws = self.wb["POHorseList"]

    def get(self):
        xlrow = 2
        mylist = []

        while self.ws.cell(row=xlrow, column=1).value:

            horse_name = self.ws.cell(row=xlrow, column=2).value
            owner_name = self.ws.cell(row=xlrow, column=1).value
            horse_id = self.ws.cell(row=xlrow, column=7).value
            is_seal = False if self.ws.cell(row=xlrow, column=6).value == "-" else True
            mylist.append([horse_id, horse_name, owner_name, is_seal])

            xlrow += 1

        self.wb.close()

        return mylist

    def get_name_list(self):
        xlrow = 2
        mylist = []

        while self.ws.cell(row=xlrow, column=1).value:

            horse_name = self.ws.cell(row=xlrow, column=2).value
            if self.ws.cell(row=xlrow, column=6).value == "-":
                mylist.append([horse_name,  xlrow])

            xlrow += 1

        self.wb.close()

        return mylist
