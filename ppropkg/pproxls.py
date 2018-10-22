# -*- coding: utf-8 -*-

import os

import openpyxl

PPRO_PATH = os.getenv("HOMEDRIVE", "None") + os.getenv("HOMEPATH", "None") + "/Dropbox/POG/"
PO_HORSELIST_NAME = "POG_HorseList.xlsx"


class POHorseList:

    def __init__(self):
        self.wbpath = (PPRO_PATH + PO_HORSELIST_NAME).replace("\\", "/")
        self.wb = openpyxl.load_workbook(self.wbpath)
        self.ws = self.wb["POHorseList"]

    def update_status(self, status_list):

        def get_new_status(jra_status_, status_old_):
            if jra_status_ == "放牧":
                return "放牧"
            elif jra_status_ == "非放牧":
                if status_old_ in ("未登録", "登録", "抹消", "地方", "海外"):
                    return "登録"
                elif status_old_ in ("在厩", "放牧"):
                    return "在厩"
            elif jra_status_ == "未登録":
                if status_old_ == "未登録":
                    return "未登録"
                elif status_old_ in ("登録", "在厩", "放牧"):
                    return "抹消"
                elif status_old_ in ("抹消", "地方", "海外"):
                    return status_old_

        is_updated = False

        for status_row in status_list:
            xlrow, jra_status = status_row[0], status_row[1]
            status_old = self.ws.cell(row=xlrow, column=11).value
            status_new = get_new_status(jra_status, status_old)

            if status_new != status_old:
                is_updated = True
                self.ws.cell(row=xlrow, column=11).value = status_new
                self.ws.cell(row=xlrow, column=12).value = status_old

        return is_updated

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
        return mylist

    def save(self):
        self.wb.save(self.wbpath)

    def close(self):
        self.wb.close()
