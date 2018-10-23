# -*- coding: utf-8 -*-

from ppropkg.pproxls import POHorseList
from ppropkg.pprows import JRAHorseSearch


def main():
    jra_horse_search = JRAHorseSearch("headless")
    poh_list = POHorseList()
    poh_status_list = []
    for poh in poh_list.get_name_list():
        horse_name, xlrow = poh[0], poh[1]
        if len(horse_name) >= 6 and horse_name[-5] == "の":
            continue
        print(horse_name + jra_horse_search.get_status(horse_name))
        poh_status_list.append([xlrow, jra_horse_search.get_status(horse_name)])
    jra_horse_search.quit()
    if poh_list.update_status(poh_status_list):


    poh_list.save()
    poh_list.close()


if __name__ == "__main__":
    main()
