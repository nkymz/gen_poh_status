# -*- coding: utf-8 -*-

import os

NK_HORSE_URL_HEAD = "http://db.netkeiba.com/horse/"


class POHStatusHTMLUpdated:

    def __init__(self):
        self.path = os.getenv("HOMEDRIVE", "None") + os.getenv("HOMEPATH", "None") + "/Dropbox/POG/"
        self.htmlpath = (self.path + "POH_status_list_updated.html").replace("\\", "/")
        self.f = open(self.htmlpath, mode="w")

    def close(self):
        self.f.close()

    @staticmethod
    def _get_horse_url(horse_id):
        return NK_HORSE_URL_HEAD + str(horse_id) + "/"

    def write_content_row(self, row):
        horse_name, owner_gender_rank, horse_id, status, status_old = row
        s = '<a href="' + self._get_horse_url(horse_id) + '">' + horse_name + owner_gender_rank + '</a>' + " " \
            + status_old + "→" + status + '<br>\n'
        self.f.write(s)


class POHStatusHTML:

    def __init__(self):
        self.path = os.getenv("HOMEDRIVE", "None") + os.getenv("HOMEPATH", "None") + "/Dropbox/POG/"
        self.htmlpath = (self.path + "POH_status_list.html").replace("\\", "/")
        self.f = open(self.htmlpath, mode="w")

    def close(self):
        self.f.close()

    @staticmethod
    def _get_horse_url(horse_id):
        return NK_HORSE_URL_HEAD + str(horse_id) + "/"

    def write_table_header(self):
        s = '<table>\n'
        s += '<tr><th>オーナー</th><th>性別</th><th>順位</th><th>馬名</th><th>状況</th></tr>\n'
        self.f.write(s)

    def write_table_footer(self):
        s = '</table>\n'
        self.f.write(s)

    def write_content_row(self, row):
        owner, gender, nom_rank, horse_name, horse_id, status, status_old = row
        if gender == "牡" and nom_rank == "1":
            s = '<tr><td rowspan="10">' + owner + '</td>' + '<td rowspan="5">' + gender + '</td>' + '<td>' + nom_rank \
                + '</td>'
        elif gender == "牝" and nom_rank == "1":
            s = '<tr><td rowspan="5">' + gender + '</td>' + '<td>' + nom_rank + '</td>'
        else:
            s = '<tr><td>' + nom_rank + '</td>'
        s += '<td><a href="' + self._get_horse_url(horse_id) + '">' + horse_name + '</a></td>'
        if status == status_old:
            s += '<td>' + status + '</td></tr>\n'
        else:
            s += '<td>' + status + '←' + status_old + '</td></tr>\n'

        self.f.write(s)


def main():
    test = POHStatusHTMLUpdated()
    test.write_content_row(["a", "b", 1, "c", "d"])
    test.close()


if __name__ == "__main__":
    main()
