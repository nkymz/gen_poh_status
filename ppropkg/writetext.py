# -*- coding: utf-8 -*-

import os


class POHStatusListUpdated():

    def __int__(self):
        self.path = os.getenv("HOMEDRIVE", "None") + os.getenv("HOMEPATH", "None") + "/Dropbox/POG/"
        self.htmlpath = (path + "POH_status_list.html").replace("\\", "/")

    def open(self):
        self.f = open(htmlpath, mode="w")

    def write_content_row(self, row):
        horse_name, owner_gender_rank, horse_id, status, status_old = row




for i in race_horse_list:

    f.write("<!--" + str(i) + "-->\n")

    race_date = i[1]
    race_time = i[2]
    track = i[3]
    race_no = i[4]
    race_name = i[5]
    grade = i[6]
    course = i[7].replace("\xa0", " ")
    race_cond2 = i[9].replace("\xa0", " ")
    horse_no = i[10]
    box_no = i[11]
    horse_name = i[12]
    jockey = i[13]
    odds = i[14]
    pop_rank = i[15]
    race_url = i[16]
    horse_url = i[17]
    owner = i[18]
    origin = i[19]
    result = i[20]
    status = i[21]
    isSeal = i[22]
    result_url = i[23]
    training_date, training_course, training_course_condition, training_jockey, training_time_list, \
    training_result_texts_list, training_position, training_stride, training_eval_text, training_eval_rank, \
    prediction_marks, stable_comment = i[24], i[25], i[26], i[27], i[28], i[29], i[30], i[31], i[32], i[33], \
                                       i[34], i[35]

    sp = ' '

    if result != "00":
        race_url = result_url
        status = "【結果確定】"
    elif horse_no != "00":
        status = "【枠順確定】"
    elif status == "出走確定":
        status = "【出走確定】"
    else:
        status = "【出走想定】"

    if box_no == "1":
        frame = '<span style="border: 1px solid; background-color:#ffffff; color:#000000;">1</span> '
    elif box_no == "2":
        frame = '<span style="border: 1px solid; background-color:#000000; color:#ffffff;">2</span> '
    elif box_no == "3":
        frame = '<span style="border: 1px solid; background-color:#ff0000; color:#ffffff;">3</span> '
    elif box_no == "4":
        frame = '<span style="border: 1px solid; background-color:#0000ff; color:#ffffff;">4</span> '
    elif box_no == "5":
        frame = '<span style="border: 1px solid; background-color:#ffff00; color:#000000;">5</span> '
    elif box_no == "6":
        frame = '<span style="border: 1px solid; background-color:#00ff00; color:#ffffff;">6</span> '
    elif box_no == "7":
        frame = '<span style="border: 1px solid; background-color:#ff8000; color:#000000;">7</span> '
    elif box_no == "8":
        frame = '<span style="border: 1px solid; background-color:#ff8080; color:#000000;">8</span> '
    else:
        frame = None

    s = '<h4>' + race_date + '</h4>\n'
    if prev_date is None:
        f.write(s)
    elif race_date != prev_date:
        f.write('</ul></li></ul>' + s)

    s = '<li> <a href="' + race_url + '">' + track + race_no + sp + race_name + status + '</a><br />\n'
    s2 = race_time + sp + course + sp + race_cond2 + '<br />\n<ul style="margin-left:-1em;">'
    if prev_date is None or (prev_date is not None and race_date != prev_date):
        f.write('<ul style="margin-left:-1em;">' + s)
        f.write(s2)
    elif race_date + race_no + race_time + track != prev_date + prev_race_no + prev_race_time + prev_track:
        f.write('</ul></li>' + s)
        f.write(s2)

    if result == "01":
        s1 = '<li><span style="font-weight: 900; color:#FF0000;">1着</span>' + sp + frame + str(horse_no) + sp \
             + '<a href="' + horse_url + '">'
    elif result == "02" and grade != "NG":
        s1 = '<li><span style="font-weight: 700; color:#0000FF;">2着</span>' + sp + frame + str(horse_no) + sp \
             + '<a href="' + horse_url + '">'
    elif result != "00":
        s1 = "<li>" + result.lstrip("0") + '着' + sp + frame + str(horse_no) + sp + '<a href="' + horse_url + '">'
    elif horse_no != "00":
        s1 = '<li>' + frame + str(horse_no) + sp + '<a href="' + horse_url + '">'
    else:
        s1 = '<li> <a href="' + horse_url + '">'
    if isSeal:
        s2 = '<s>' + horse_name + '</s>'
    else:
        s2 = horse_name
    s3 = sp + jockey if jockey else ""
    f.write(s1 + s2 + owner + '</a>' + s3 + '<br />\n')

    f.write(origin + '<br />\n')

    if odds is not None:
        f.write(str(odds) + '倍' + sp + str(pop_rank) + '番人気' + sp + prediction_marks + '<br />\n')
    if training_date[:4] != "0000":
        s = training_jockey + sp + training_date.split("/")[1] + "/" + training_date.split("/")[2].split("(")[0] + sp \
            + training_course + sp + training_course_condition + sp + training_stride + sp + "<br />\n"
        for t in training_time_list:
            s += t + " " if t != "-" else ""
        s += "[" + training_position + "]" + "<br />\n" if training_position else "<br />\n"
        for t in training_result_texts_list:
            s += t + sp
        s += "<br />\n" if training_result_texts_list else ""
        s += training_eval_text + training_eval_rank + "<br />\n"
        f.write(s)
    if stable_comment != "":
        f.write(stable_comment + "<br />\n")
    f.write('</li>\n')

    prev_date = race_date
    prev_race_no = race_no
    prev_race_time = race_time
    prev_track = track

s = str(mynow.year) + "/" + ("0" + str(mynow.month))[-2:] + "/" + ("0" + str(mynow.day))[-2:] \
    + WEEKDAY[mynow.weekday()] + " " + ("0" + str(mynow.hour))[-2:] + ":" + ("0" + str(mynow.minute))[-2:]
f.write('</ul></li></ul><p>' + s + ' 時点の情報より作成</p>\n')

f.close()
