# -*- coding: utf-8 -*-

import os

NK_HORSE_URL_HEAD = "http://db.netkeiba.com/horse/"

POH_STATUS_HTML_HEADER = """
<head>
<link rel="stylesheet" type="text/css" href="style.css">
<meta name="viewport" content="width=device-width,initial-scale=1">
</head>
"""

POH_STATUS_HTML_UPDATED_HEADER = """
全頭リストは<a href="https://nkymz.github.io/ppro_status_list/">こちら</a></p>
"""


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

    def write_header(self):
        self.f.write(POH_STATUS_HTML_UPDATED_HEADER)

    def write_content_row(self, row):
        horse_name, owner_gender_rank, horse_id, status, next_race, is_status_updated, is_next_race_updated = row
        s = '<a href="' + self._get_horse_url(horse_id) + '">' + horse_name + owner_gender_rank + '</a>' + " "
        if is_status_updated:
            s += '<span class="bold_red">' + status + '</span> '
        else:
            s += status + ' '
        if is_next_race_updated:
            s += '<span class="bold_red">' + next_race + '</span><br />\n '
        else:
            s += next_race + '<br />'

        self.f.write(s)


class POHStatusHTML:

    def __init__(self):
        self.path = os.getenv("HOMEDRIVE", "None") + os.getenv("HOMEPATH", "None") + "/Dropbox/POG/ppro_status_list/"
        self.htmlpath = (self.path + "index.html").replace("\\", "/")
        self.f = open(self.htmlpath, mode="w", encoding="utf-8")

    def close(self):
        self.f.close()

    @staticmethod
    def _get_horse_url(horse_id):
        return NK_HORSE_URL_HEAD + str(horse_id) + "/"

    def write_header(self, date_time):
        s = POH_STATUS_HTML_HEADER
        s += '<p class="right">' + date_time + ' 現在' + '</p>\n'
        s += '<table>\n'
        s += '<tr><th>オーナー</th><th>性別</th><th>順位</th><th>馬名</th><th>状況</th><th>次走予定</th></tr>\n'
        self.f.write(s)

    def write_footer(self):
        self.f.write('</table>\n')

    def write_content_row(self, row):
        owner, gender, nom_rank, horse_name, horse_id, status, next_race, is_status_updated, is_next_race_updated = row
        if gender == "牡" and nom_rank == "1":
            s = '<tr><td rowspan="10">' + owner + '</td>' + '<td rowspan="5">' + gender + '</td>' + '<td>' + nom_rank \
                + '</td>'
        elif gender == "牝" and nom_rank == "1":
            s = '<tr><td rowspan="5">' + gender + '</td>' + '<td>' + nom_rank + '</td>'
        else:
            s = '<tr><td>' + nom_rank + '</td>'
        s += '<td><a href="' + self._get_horse_url(horse_id) + '">' + horse_name + '</a></td>'
        if is_status_updated:
            s += '<td><span class="bold_red">' + status + '</span></td>'
        else:
            s += '<td>' + status + '</td>'
        if is_next_race_updated:
            s += '<td><span class="bold_red">' + next_race + '</span></td></tr>\n'
        else:
            s += '<td>' + next_race + '</td></tr>\n'

        self.f.write(s)


def main():
    test = POHStatusHTMLUpdated()
    test.write_content_row(["a", "b", 1, "c", "d"])
    test.close()


if __name__ == "__main__":
    main()
