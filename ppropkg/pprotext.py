# -*- coding: utf-8 -*-

import os

NK_HORSE_URL_HEAD = "http://db.netkeiba.com/horse/"


class POHStatusHTMLUpdated:

    def __init__(self):
        self.path = os.getenv("HOMEDRIVE", "None") + os.getenv("HOMEPATH", "None") + "/Dropbox/POG/"
        self.htmlpath = (self.path + "POH_status_list.html").replace("\\", "/")
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


def main():
    test = POHStatusHTMLUpdated()
    test.write_content_row(["a", "b", 1, "c", "d"])
    test.close()


if __name__ == "__main__":
    main()
