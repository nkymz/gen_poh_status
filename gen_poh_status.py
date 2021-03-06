# -*- coding: utf-8 -*-

import datetime

from ppropkg.pproxls import POHorseList
from ppropkg.pprows import JRAHorseSearch, NetKeiba
from ppropkg.pprotext import POHStatusHTMLUpdated, POHStatusHTML


def main():
    mynow = datetime.datetime.today()
    date_time_now = mynow.strftime("%Y/%m/%d %H:%M:%S")
    poh_list = POHorseList()
    nk_id, nk_pw = poh_list.get_nk_auth_info()
    nk = NetKeiba(nk_id, nk_pw, 0)
#    jra_horse_search = JRAHorseSearch("headless")

    horse_list = []
    for poh in poh_list.get_horse_list():
        nk_url_sp, xlrow = poh
        horse_name, origin, status, next_race = nk.get_horse_info(nk_url_sp)
        horse_list.append([xlrow, horse_name, origin, status, next_race])
    nk.quit()

    if poh_list.update_horse_list(horse_list):
        print("更新あり")
        poh_html_updated = POHStatusHTMLUpdated()
        poh_html_updated.write_header()
        for poh in poh_list.get_status_list("updated_only"):
            poh_html_updated.write_content_row(poh)
        poh_html_updated.close()
    else:
        print("更新なし")

    poh_html = POHStatusHTML()
    poh_html.write_header(date_time_now)
    for poh in poh_list.get_status_list():
        poh_html.write_content_row(poh)
    poh_html.write_footer()
    poh_html.close()

    poh_list.save()
    poh_list.close()


    # poh_status_list = []
    # for poh in poh_list.get_name_list():
    #     horse_name, xlrow = poh
    #     if len(horse_name) >= 6 and horse_name[-5] == "の":
    #         continue
    #     horse_status = jra_horse_search.get_status(horse_name)
    #     print(horse_name + horse_status)
    #     poh_status_list.append([xlrow, horse_status])
    # jra_horse_search.quit()
    # if poh_list.update_status(poh_status_list):
    #     print("更新あり")
    #     poh_html_updated = POHStatusHTMLUpdated()
    #     poh_html_updated.write_header()
    #     for poh in poh_list.get_status_list("updated_only"):
    #         poh_html_updated.write_content_row(poh)
    #     poh_html_updated.close()
    # else:
    #     print("更新なし")
    #


if __name__ == "__main__":
    main()
