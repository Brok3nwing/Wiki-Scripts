import json
import os
import possible_keys
import natsort
import re
import colorsys


deleted_string = "Deleted"
old = input("Old Cache: ")
new = input("New Cache: ")
out = input("Output: ")
# out = "Test"

table_creation = '{| class="wikitable sortable"\n'


table_creation_2_diff_items = '\n|-\n! style=width:15em | Name !! ID !! Key !! Previous Value !! New Value\n|-\n'
table_creation_2_diff_npcs = '\n|-\n! style=width:15em | Name !! ID !! Key !! Previous Value !! New Value\n|-\n'
table_creation_2_diff_objects = '\n|-\n! style=width:15em | Name !! ID !! Key !! Previous Value !! New Value\n|-\n'


table_creation_2_new_items = '\n|-\n! style=width:15em | Name !! ID !! Members !! Tradeable in GE !! Equipable !! Stackable !! Noteable !! Options !! Placeholder !! Cost !! Weight\n|-\n'
table_creation_2_new_npcs = '\n|-\n! style=width:15em | Name !! ID !! Combat Level !! Options\n|-\n'
table_creation_2_new_objects = '\n|-\n! style=width:15em | Name !! ID !! Options\n|-\n'

table_creation_2_removed_items = '\n|-\n! style=width:15em | Name !! ID\n|-\n'
table_creation_2_removed_npcs = '\n|-\n! style=width:15em | Name !! ID\n|-\n'
table_creation_2_removed_objects = '\n|-\n! style=width:15em | Name !! ID\n|-\n'

single_q = "'"

format_options_regex1 = "[\[\]']|None"
format_options_regex2 = "[\[\]']|None"
name_array = 0
o = 0
#
# old_dir = f"E:/Caches/205.3/definitions/"
# new_dir = f"E:/Caches/205.4/definitions/"

old_dir = f"E:/Caches/{old}/definitions/"
new_dir = f"E:/Caches/{new}/definitions/"

occ = []


def convert_jagex_color_to_hex(number):
    def get_hue():
        h = number / 1024
        l = h * 5.625
        if l < 0:
            return int(360 + (l))
        else:
            return int(l)

    def get_lightness():
        h = number % 128
        return int(h * 0.591)


    def get_saturation():
        h = number / 1024
        l = h % 1
        return int(round(l, 2) * 100)

    def hsl_to_rgb():
        frac = colorsys.hls_to_rgb(get_hue()/360, get_lightness()/100, get_saturation()/100)
        return frac[0]*255, frac[1]*255, frac[2]*255

    def rgb_to_hex():
        t = (int(hsl_to_rgb()[0]), int(hsl_to_rgb()[1]), int(hsl_to_rgb()[2]))
        hex_color = '%02x%02x%02x' % t

        return hex_color

    return rgb_to_hex()

def format_options(rgx_list, text):
    new_text = text
    for rgx_match in rgx_list:
        new_text = re.sub(rgx_match, '', new_text)
    return new_text


def get_same_key_count_items():
    print("Calculating item diffs")
    count = 0
    f = []
    occ = []
    dir1 = old_dir + "/item_defs/"
    dir2 = new_dir + "/item_defs/"
    names1 = os.listdir(dir1)
    names2 = os.listdir(dir2)
    common_names = set(names1) & set(names2)
    dt = possible_keys.Keys.item_data
    sorted_names = natsort.natsorted(common_names)

    for filename in sorted_names:
        count += 1
        if count % 5000 == 0:
            print(count)
        ext = os.path.splitext(filename)
        if ext[1] == ".json":
            json1 = json.load(open(os.path.join(dir1, filename)))
            json2 = json.load(open(os.path.join(dir2, filename)))
            for change in dt:
                try:
                    data1 = json1[change]
                    data2 = json2[change]
                    if data1 != data2:
                        occ.append(json2[dt[0]])
                        res = []
                        for i in occ:
                            if i not in res:
                                res.append(i)
                        f = [occ.count(i) for i in res]
                except KeyError:
                    pass
    return f


def get_same_key_count_npcs():
    print("Calculating npc diffs")
    occ = []
    dir1 = old_dir + "/npc_defs/"
    dir2 = new_dir + "/npc_defs/"
    old_npcs = os.listdir(dir1)
    new_npcs = os.listdir(dir2)
    c = 0
    common_names = set(old_npcs) & set(new_npcs)

    dt = possible_keys.Keys.npcs_data
    sorted_names = natsort.natsorted(common_names)
    k = []
    files_to_process = len(sorted_names) / 100
    for count, filename in enumerate(sorted_names):
        print(count, end="\r")

        ext = os.path.splitext(filename)
        if ext[1] == ".json":
            json1 = json.load(open(os.path.join(dir1, filename)))
            json2 = json.load(open(os.path.join(dir2, filename)))

            for change in dt:
                try:
                    data1 = json1[change]
                    data2 = json2[change]
                    if data1 != data2:
                        occ.append(json2[dt[0]])
                        res = []
                        for i in occ:
                            if i not in res:
                                res.append(i)
                        k = [occ.count(i) for i in res]
                except KeyError:
                    pass
    return k


def get_same_key_count_objects():
    print("Calculating object diffs")
    occ = []
    count = 0
    f = []
    dir1 = old_dir + "/object_defs/"
    dir2 = new_dir + "/object_defs/"
    names1 = os.listdir(dir1)
    names2 = os.listdir(dir2)
    common_names = set(names1) & set(names2)
    dt = possible_keys.Keys.objects_data
    sorted_names = natsort.natsorted(common_names)
    y = 0

    for filename in sorted_names:
        count += 1
        ext = os.path.splitext(filename)
        if ext[1] == ".json":
            json1 = json.load(open(os.path.join(dir1, filename)))
            json2 = json.load(open(os.path.join(dir2, filename)))
            for change in dt:
                try:
                    data1 = json1[change]
                    data2 = json2[change]
                    if data1 != data2:
                        occ.append(json2[dt[0]])
                        res = []
                        for i in occ:
                            if i not in res:
                                res.append(i)
                        f = [occ.count(i) for i in res]
                except KeyError:
                    pass
    return f


def get_item_count():
    t = []
    y = 0
    for x in get_same_key_count_items():
        y += x
        t.append(y)
    return t


def get_npc_count():
    t = []
    y = 0
    for x in get_same_key_count_npcs():
        y += x
        t.append(y)
    return t


def get_object_count():
    t = []
    y = 0
    for x in get_same_key_count_objects():
        y += x
        t.append(y)
    return t


def items_wiki():
    g = get_item_count()
    dir1 = old_dir + "/item_defs/"
    dir2 = new_dir + "/item_defs/"
    toc = "{{ToC}}"

    names1 = os.listdir(dir1)
    names2 = os.listdir(dir2)

    base_moid_url = "https://chisel.weirdgloop.org/moid/item_id.html#"

    common_names = set(names1) & set(names2)
    keys = possible_keys.Keys.item_data
    sorted_names = natsort.natsorted(common_names)
    z = get_same_key_count_items()
    c = 0
    loop_count = 0
    count = 0
    with open(f"equipped.txt", "w") as file:
        file.write("ID\tName\n")

        with open(f"{out}.txt", "a") as f:
            comma_count = 0
            f.write(f"{toc}\n==Items==\n===New Items===\n{table_creation}!colspan='11'|New Items{table_creation_2_new_items}")
            missing = [name for name in names2 if name not in names1]
            deleted = [name for name in names1 if name not in names2]
            print("Writing New Items")
            for m in missing:
                with open(dir2 + str(m)) as names:
                    missing_files = json.load(names)



                    if "Wear" in str(missing_files[keys[22]]) or "Wield" in str(missing_files[keys[22]]):

                        file.write(f"{str(missing_files[keys[0]])}\t{str(missing_files[keys[1]])}\n")
                        print(f"Writing:   {str(missing_files[keys[0]])}\t{str(missing_files[keys[1]])}\n")

                    f.write(f'| [[{str(missing_files[keys[1]])}]] '  # Name
                            f'|| [{base_moid_url}{str(missing_files[keys[0]])} {str(missing_files[keys[0]])}] '  # ID
                            f'|| {"Yes" if str(missing_files[keys[15]]) == "True" else "No"} '  # Members
                            f'|| {"Yes" if str(missing_files[keys[9]]) == "True" else "No"} '  # Tradeable
                            f'|| {"No" if str(missing_files[keys[23]]) == "-1" else "Yes"} '  # male equipped 1
                            f'|| {"No" if str(missing_files[keys[10]]) == "0" else "Yes"} '  # Stackable
                            f'|| {"No" if str(missing_files[keys[35]]) == "-1" else "Yes"} '  # Noteable
                            # f'|| {format_options(format_options_regex1, str(missing_files[keys[19]]))} '  # InterfaceOptions
                            f'|| {", ".join(filter(None, missing_files[keys[22]]))} '  # InterfaceOptions
                            f'|| {"No" if str(missing_files[keys[42]]) == "-1" else "Yes"} '  # Placeholder
                            f'|| {str(missing_files[keys[8]])}\n' # Cost
                            f'|| {str(missing_files[keys[38]])}\n' # Weight
                            )
                    f.write("|-" + "\n")
            f.write("|-\n|}" + "\n")




            # Removed Items
            print("Writing Removed Items")
            f.write(f"===Removed Items===\n{table_creation}!colspan='2'|Removed Items{table_creation_2_removed_items}")
            for m in deleted:
                with open(dir1 + str(m)) as names:
                    missing_files = json.load(names)
                    f.write(f'| [[{str(missing_files[keys[1]])}]] || [{base_moid_url}{str(missing_files[keys[0]])} {str(missing_files[keys[0]])}]\n')
                    f.write("|-" + "\n")
            f.write("|-\n|}" + "\n")

            print("Writing Diff Items")
            f.write(f"===Diff Items===\n{table_creation}!colspan='5'|Diff Items{table_creation_2_diff_items}")
            # Item Diffs
            for filename in sorted_names:
                ext = os.path.splitext(filename)
                if ext[1] == ".json":
                    json1 = json.load(open(os.path.join(dir1, filename)))
                    json2 = json.load(open(os.path.join(dir2, filename)))
                    for change in keys:
                        try:
                            data1 = json1[change]
                            data2 = json2[change]
                            if data1 != data2:
                                changed_value1 = json1[change]
                                changed_value2 = json2[change]
                                # print(z)
                                if (len(g)) != 0:
                                    if loop_count > 0: c += 1
                                    if c == g[0] or loop_count == 0:
                                        f.write(f'|rowspan="{z[0]+1}"|[[{str(json2[keys[1]])}]]\n')
                                        f.write(f'|rowspan="{z[0]+1}"|[{base_moid_url}{str(json2[keys[0]])} {str(json2[keys[0]])}]\n')
                                        f.write("|-" + "\n")
                                        if str(change) == "name":
                                            f.write(f"|{str(change)} || [[{str(changed_value1)}]] || [[{str(changed_value2)}]]\n")
                                        elif str(change) == "colorFind" or str(change) == "colorReplace":
                                            comma_count = 0
                                            f.write(f'| {str(change)} ||')
                                            for i in changed_value1:
                                                color = convert_jagex_color_to_hex(i)
                                                f.write(f'<span style = "background-color: #{color};color:white">{i}</span>')
                                                if len(list(changed_value1)) > 1:
                                                    if comma_count < (len(list(changed_value1)) - 1):
                                                        f.write(",")
                                                        comma_count += 1
                                            f.write("||")
                                            comma_count = 0
                                            for i in changed_value2:
                                                color2 = convert_jagex_color_to_hex(i)
                                                f.write(f'<span style = "background-color: #{color2};color:white">{i}</span>')
                                                if len(list(changed_value2)) > 1:
                                                    if comma_count < (len(list(changed_value2)) - 1):
                                                        f.write(",")
                                                        comma_count += 1
                                            f.write("\n")

                                        else:
                                            f.write(f"|{str(change)} || {str(changed_value1)} || {str(changed_value2)}\n")
                                        f.write("|-" + "\n")
                                        z.pop(0)
                                        if loop_count >= 1:g.pop(0)
                                    else:
                                        # print(f"|{str(change)} || {str(changed_value1)} || {str(changed_value2)}\n")
                                        if str(change) == "name":
                                            f.write(f"| {str(change)} || [[{str(changed_value1)}]] || [[{str(changed_value2)}]]\n")
                                        elif str(change) == "colorFind" or str(change) == "colorReplace":
                                            comma_count = 0
                                            f.write(f'| {str(change)} ||')
                                            for i in changed_value1:
                                                color = convert_jagex_color_to_hex(i)
                                                f.write(f'<span style = "background-color: #{color};color:white">{i}</span>')
                                                if len(list(changed_value1)) > 1:
                                                    if comma_count < (len(list(changed_value1)) - 1):
                                                        f.write(",")
                                                        comma_count += 1
                                            f.write("||")
                                            comma_count = 0
                                            for i in changed_value2:
                                                color2 = convert_jagex_color_to_hex(i)
                                                f.write(f'<span style = "background-color: #{color2};color:white">{i}</span>')
                                                if len(list(changed_value2)) > 1:
                                                    if comma_count < (len(list(changed_value2)) - 1):
                                                        f.write(",")
                                                        comma_count += 1
                                            f.write("\n")

                                        else:
                                            f.write(f"| {str(change)} || {str(changed_value1)} || {str(changed_value2)}\n")
                                        f.write("|-" + "\n")
                                    loop_count += 1
                        except KeyError:
                            pass
            f.write("|}" + "\n\n")


def npcs_wiki():
    g = get_npc_count()
    dir1 = old_dir + "/npc_defs/"
    dir2 = new_dir + "/npc_defs/"
    options = ","

    names1 = os.listdir(dir1)
    names2 = os.listdir(dir2)

    base_moid_url = "https://chisel.weirdgloop.org/moid/npc_id.html#"

    common_names = set(names1) & set(names2)
    keys = possible_keys.Keys.npcs_data
    sorted_names = natsort.natsorted(common_names)
    z = get_same_key_count_npcs()
    # c = get_count()[0]
    c = 0
    loop_count = 0
    count = 0

    with open(f"{out}.txt", "a") as f:
        comma_count = 0
        f.write(f"==Non-Player Characters==\n===New NPCs===\n{table_creation}!colspan='4'|New NPCs{table_creation_2_new_npcs}")
        print("Writing New Npc")
        missing = [name for name in names2 if name not in names1]
        deleted = [name for name in names1 if name not in names2]
        for m in missing:
            with open(dir2 + str(m)) as names:
                missing_files = json.load(names)
                data = missing_files[keys[18]]
                f.write(f'| [[{str(missing_files[keys[1]])}]] || [{base_moid_url}{str(missing_files[keys[0]])} {str(missing_files[keys[0]])}] || {str(missing_files[keys[20]]) if str(missing_files[keys[20]]) != "0" else "No Combat Level"} || {", ".join(filter(None, data))}\n')
                f.write("|-" + "\n")
        f.write("|-\n|}" + "\n")
        f.write(f"===Removed NPCs===\n{table_creation}!colspan='2'|Removed NPCs{table_creation_2_removed_npcs}")
        print("Writing removed NPcs")
        for m in deleted:
            with open(dir1 + str(m)) as names:
                missing_files = json.load(names)

                f.write(f'| [[{str(missing_files[keys[1]])}]] || [{base_moid_url}{str(missing_files[keys[0]])} {str(missing_files[keys[0]])}]\n')
                f.write("|-" + "\n")
        f.write("|-\n|}" + "\n")

        print("Writing Npc diffs")
        f.write(f"===Diff NPCs===\n{table_creation}!colspan='5'|Diff NPCs{table_creation_2_diff_npcs}")
        for filename in sorted_names:
            ext = os.path.splitext(filename)
            if ext[1] == ".json":
                json1 = json.load(open(os.path.join(dir1, filename)))
                json2 = json.load(open(os.path.join(dir2, filename)))
                for change in keys:
                    try:
                        data1 = json1[change]
                        data2 = json2[change]
                        # print("g: ", g)
                        if data1 != data2:
                            changed_value1 = json1[change]
                            changed_value2 = json2[change]
                            if (len(g)) != 0:
                                if loop_count > 0: c += 1
                                if c == g[0] or loop_count == 0:
                                    f.write(f'|rowspan="{z[0]+1}"|[[{str(json2[keys[1]])}]]\n')
                                    f.write(f'|rowspan="{z[0]+1}"|[{base_moid_url}{str(json2[keys[0]])} {str(json2[keys[0]])}]\n')
                                    f.write("|-" + "\n")
                                    if str(change) == "name":
                                        f.write(
                                            f"|{str(change)} || [[{str(changed_value1)}]] || [[{str(changed_value2)}]]\n")
                                    elif str(change) == "recolorToFind" or str(change) == "recolorToReplace":
                                        comma_count = 0
                                        f.write(f'| {str(change)} ||')
                                        for i in changed_value1:
                                            color = convert_jagex_color_to_hex(i)
                                            f.write(
                                                f'<span style = "background-color: #{color};color:white">{i}</span>')
                                            if len(list(changed_value1)) > 1:
                                                print(f"Length of {list(changed_value1)} : {len(list(changed_value1))} and comma_count {comma_count}")
                                                if comma_count < (len(list(changed_value1)) - 1):
                                                    f.write(",")
                                                    comma_count += 1
                                        f.write("||")
                                        comma_count = 0
                                        for i in changed_value2:
                                            color2 = convert_jagex_color_to_hex(i)
                                            f.write(
                                                f'<span style = "background-color: #{color2};color:white">{i}</span>')
                                            if len(list(changed_value2)) > 1:
                                                print(f"Length of {list(changed_value2)} : {len(list(changed_value2))} and comma_count {comma_count}")
                                                if comma_count < (len(list(changed_value2)) - 1):
                                                    print(f"+adding comma")
                                                    f.write(",")
                                                    comma_count += 1
                                        f.write("\n")

                                    else:
                                        f.write(f"|{str(change)} || {str(changed_value1)} || {str(changed_value2)}\n")
                                    f.write("|-" + "\n")
                                    z.pop(0)
                                    if loop_count >= 1: g.pop(0)
                                else:
                                    # print(f"|{str(change)} || {str(changed_value1)} || {str(changed_value2)}\n")
                                    if str(change) == "name":
                                        f.write(
                                            f"| {str(change)} || [[{str(changed_value1)}]] || [[{str(changed_value2)}]]\n")
                                    elif str(change) == "recolorToFind" or str(change) == "recolorToReplace":
                                        comma_count = 0
                                        f.write(f'| {str(change)} ||')
                                        for i in changed_value1:
                                            color = convert_jagex_color_to_hex(i)
                                            f.write(
                                                f'<span style = "background-color: #{color};color:white">{i}</span>')
                                            if len(list(changed_value1)) > 1:
                                                if comma_count < (len(list(changed_value1)) - 1):
                                                    f.write(",")
                                                    comma_count += 1
                                        f.write("||")
                                        comma_count = 0
                                        for i in changed_value2:
                                            color2 = convert_jagex_color_to_hex(i)
                                            f.write(
                                                f'<span style = "background-color: #{color2};color:white">{i}</span>')
                                            if len(list(changed_value2)) > 1:
                                                if comma_count < (len(list(changed_value2)) - 1):
                                                    f.write(",")
                                                    comma_count += 1
                                        f.write("\n")

                                    else:
                                        f.write(f"| {str(change)} || {str(changed_value1)} || {str(changed_value2)}\n")
                                    f.write("|-" + "\n")
                                loop_count += 1
                    except KeyError:
                        pass
        f.write("|}" + "\n\n")


def objects_wiki():
    g = get_object_count()
    count = 0
    dir1 = old_dir + "/object_defs/"
    dir2 = new_dir + "/object_defs/"

    base_moid_url = "https://chisel.weirdgloop.org/moid/object_id.html#"

    names1 = os.listdir(dir1)
    names2 = os.listdir(dir2)

    common_names = set(names1) & set(names2)
    keys = possible_keys.Keys.objects_data
    sorted_names = natsort.natsorted(common_names)
    z = get_same_key_count_objects()
    # c = get_count()[0]
    c = 0
    loop_count = 0

    with open(f"{out}.txt", "a") as f:
        comma_count = 0
        f.write(f"==Objects==\n===New Objects=== \n{table_creation}!colspan='3'|New Objects{table_creation_2_new_objects}")
        missing = [name for name in names2 if name not in names1]
        deleted = [name for name in names1 if name not in names2]
        for m in missing:
            with open(dir2 + str(m)) as names:
                missing_files = json.load(names)
                # t = (str(missing_files[keys[15]]).replace("None, ", "").replace(", None", "").replace("[", "").replace("]", "").replace(single_q, "").replace("None", "-"))
                f.write(f'| [[{str(missing_files[keys[3]])}]] || [{base_moid_url}{str(missing_files[keys[0]])} {str(missing_files[keys[0]])}] || {", ".join(filter(None, missing_files[keys[15]]))}\n')
                f.write("|-" + "\n")
        f.write("|-\n|}" + "\n")

        f.write(f"===Removed Objects===\n{table_creation}!colspan='2'|Removed Objects{table_creation_2_removed_objects}")
        print("Writing removed Objects")
        for m in deleted:
            with open(dir1 + str(m)) as names:
                missing_files = json.load(names)
                f.write(f'| [[{str(missing_files[keys[3]])}]] || [{base_moid_url}{str(missing_files[keys[0]])} {str(missing_files[keys[0]])}]\n')
                f.write("|-" + "\n")
        f.write("|-\n|}" + "\n")

        print("Writing Object diffs")
        f.write(f"===Diff Objects===\n{table_creation}!colspan='5'|Diff Objects{table_creation_2_diff_objects}")
        for filename in sorted_names:
            ext = os.path.splitext(filename)
            if ext[1] == ".json":
                json1 = json.load(open(os.path.join(dir1, filename)))
                json2 = json.load(open(os.path.join(dir2, filename)))
                for change in keys:
                    try:
                        data1 = json1[change]
                        data2 = json2[change]
                        if data1 != data2:
                            changed_value1 = json1[change]
                            changed_value2 = json2[change]
                            if (len(g)) != 0:
                                if loop_count > 0: c += 1
                                if c == g[0] or loop_count == 0:
                                    f.write(f'|rowspan="{z[0]+1}"|[[{str(json2[keys[3]])}]]\n')
                                    f.write(f'|rowspan="{z[0]+1}"|[{base_moid_url}{str(json2[keys[0]])} {str(json2[keys[0]])}]\n')
                                    f.write("|-" + "\n")
                                    if str(change) == "name":
                                        f.write(
                                            f"|{str(change)} || [[{str(changed_value1)}]] || [[{str(changed_value2)}]]\n")
                                    elif str(change) == "recolorToFind" or str(change) == "recolorToReplace":
                                        comma_count = 0
                                        f.write(f'| {str(change)} ||')
                                        for i in changed_value1:
                                            color = convert_jagex_color_to_hex(i)
                                            f.write(
                                                f'<span style = "background-color: #{color};color:white">{i}</span>')
                                            if len(list(changed_value1)) > 1:
                                                if comma_count < (len(list(changed_value1)) - 1):
                                                    f.write(",")
                                                    comma_count += 1
                                        f.write("||")
                                        comma_count = 0
                                        for i in changed_value2:
                                            color2 = convert_jagex_color_to_hex(i)
                                            f.write(
                                                f'<span style = "background-color: #{color2};color:white">{i}</span>')
                                            if len(list(changed_value2)) > 1:
                                                if comma_count < (len(list(changed_value2)) - 1):
                                                    f.write(",")
                                                    comma_count += 1
                                        f.write("\n")

                                    else:
                                        f.write(f"|{str(change)} || {str(changed_value1)} || {str(changed_value2)}\n")
                                    f.write("|-" + "\n")
                                    z.pop(0)
                                    if loop_count >= 1: g.pop(0)
                                else:
                                    # print(f"|{str(change)} || {str(changed_value1)} || {str(changed_value2)}\n")
                                    if str(change) == "name":
                                        f.write(
                                            f"| {str(change)} || [[{str(changed_value1)}]] || [[{str(changed_value2)}]]\n")
                                    elif str(change) == "recolorToFind" or str(change) == "recolorToReplace":
                                        comma_count = 0
                                        f.write(f'| {str(change)} ||')
                                        for i in changed_value1:
                                            color = convert_jagex_color_to_hex(i)
                                            f.write(
                                                f'<span style = "background-color: #{color};color:white">{i}</span>')
                                            if len(list(changed_value1)) > 1:
                                                if comma_count < (len(list(changed_value1)) - 1):
                                                    f.write(",")
                                                    comma_count += 1
                                        f.write("||")
                                        comma_count = 0
                                        for i in changed_value2:
                                            color2 = convert_jagex_color_to_hex(i)
                                            f.write(
                                                f'<span style = "background-color: #{color2};color:white">{i}</span>')
                                            if len(list(changed_value2)) > 1:
                                                if comma_count < (len(list(changed_value2)) - 1):
                                                    f.write(",")
                                                    comma_count += 1
                                        f.write("\n")

                                    else:
                                        f.write(f"| {str(change)} || {str(changed_value1)} || {str(changed_value2)}\n")
                                    f.write("|-" + "\n")
                                loop_count += 1
                    except KeyError:
                        pass
        f.write("|}" + "\n\n")


items_wiki()
npcs_wiki()
objects_wiki()
