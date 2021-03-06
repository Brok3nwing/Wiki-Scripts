import json
import os
import possible_keys
import natsort
import argparse
import re
import xlsxwriter
import csv


deleted_string = "Deleted"
old = input("Old Cache: ")
new = input("New Cache: ")
out = input("Output: ")
table_creation = '{| class="wikitable sortable"\n'
table_creation_2 = '\n|-\n! Name !! ID !! Key !! Previous Value !! Changed into\n|-\n'
table_creation_2_item = '\n|-\n! Name !! ID !! Key !! Previous Value !! New Value !! Members !! Tradeable in GE !! Equipable !! Stackable !! Noteable !! Options !! Placeholder !! Cost\n|-\n'
format_options_regex1 = "[\[\]']|None"
format_options_regex2 = "[\[\]']|None"
name_array = 0
o = 0

old_dir = f"C:/AbexRenderer/Cache Definitions/{old}/"
new_dir = f"C:/AbexRenderer/Cache Definitions/{new}/"
occ = []


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
        if count % 100 == 0:
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
    count = 0
    dir1 = old_dir + "/npc_defs/"
    dir2 = new_dir + "/npc_defs/"
    names1 = os.listdir(dir1)
    names2 = os.listdir(dir2)
    common_names = set(names1) & set(names2)
    dt = possible_keys.Keys.npcs_data
    sorted_names = natsort.natsorted(common_names)
    y = 0
    k = []

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
        file.write("ID\tName\tSlot\tAnim\tRotation\n")
        with open(f"{out}.txt", "a") as f:
            f.write(f"{toc}\n==Items==\n{table_creation}!colspan='13'|Items{table_creation_2_item}")
            missing = [name for name in names2 if name not in names1]
            deleted = [name for name in names1 if name not in names2]
            single_q = "'"
            print("Writing Item diffs")
            for m in missing:
                with open(dir2 + str(m)) as names:
                    missing_files = json.load(names)

                    if "Wear" in str(missing_files[keys[19]]) or "Wield" in str(missing_files[keys[19]]):
                        print(str(missing_files[keys[19]]))
                        file.write(f"{str(missing_files[keys[0]])}\t{str(missing_files[keys[1]])}\n")

                    f.write(f'| [[{str(missing_files[keys[1]])}]] '  # Name
                            f'|| [{base_moid_url}{str(missing_files[keys[0]])} {str(missing_files[keys[0]])}] '  # ID
                            f'|| colspan = "3" | New ID '
                            f'|| {"Yes" if str(missing_files[keys[12]]) == "True" else "No"} '  # Members
                            f'|| {"Yes" if str(missing_files[keys[9]]) == "True" else "No"} '  # Tradeable
                            f'|| {"No" if str(missing_files[keys[20]]) == "-1" else "Yes"} '  # male equipped 1
                            f'|| {"No" if str(missing_files[keys[10]]) == "0" else "Yes"} '  # Stackable
                            f'|| {"No" if str(missing_files[keys[32]]) == "-1" else "Yes"} '  # Noteable
                            # f'|| {format_options(format_options_regex1, str(missing_files[keys[19]]))} '  # InterfaceOptions
                            f'|| {(str(missing_files[keys[19]])).replace("[", "").replace("]", "").replace("None,", "").replace(single_q, "")} '  # InterfaceOptions
                            f'|| {"No" if str(missing_files[keys[38]]) == "-1" else "Yes"} '  # Placeholder
                            f'|| {str(missing_files[keys[8]])}\n')  # Cost
                    f.write("|-" + "\n")

            for m in deleted:
                with open(dir1 + str(m)) as names:
                    missing_files = json.load(names)
                    f.write(f'| [[{str(missing_files[keys[1]])}]] || [{base_moid_url}{str(missing_files[keys[0]])} {str(missing_files[keys[0]])}] || colspan = "3" | Removed\n')
                    f.write("|-" + "\n")

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
                                        else:
                                            f.write(f"|{str(change)} || {str(changed_value1)} || {str(changed_value2)}\n")
                                        f.write("|-" + "\n")
                                        z.pop(0)
                                        if loop_count >= 1:g.pop(0)
                                    else:
                                        # print(f"|{str(change)} || {str(changed_value1)} || {str(changed_value2)}\n")
                                        if str(change) == "name":
                                            f.write(f"| {str(change)} || [[{str(changed_value1)}]] || [[{str(changed_value2)}]]\n")
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
        f.write(f"==Non-Player Characters==\n{table_creation}!colspan='5'|Non-Player Characters{table_creation_2}")
        missing = [name for name in names2 if name not in names1]
        deleted = [name for name in names1 if name not in names2]
        for m in missing:
            with open(dir2 + str(m)) as names:
                missing_files = json.load(names)
                f.write(f'| [[{str(missing_files[keys[1]])}]] || [{base_moid_url}{str(missing_files[keys[0]])} {str(missing_files[keys[0]])}] || colspan = "4" | New ID\n')
                f.write("|-" + "\n")

        for m in deleted:
            with open(dir1 + str(m)) as names:
                missing_files = json.load(names)
                f.write(f'| [[{str(missing_files[keys[1]])}]] || [{base_moid_url}{str(missing_files[keys[0]])} {str(missing_files[keys[0]])}] || colspan = "4" | Removed\n')
                f.write("|-" + "\n")

        print("Writing Npc diffs")
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
                                        f.write(f"|{str(change)} || [[{str(changed_value1)}]] || [[{str(changed_value2)}]]\n")
                                    else:
                                        f.write(f"|{str(change)} || {str(changed_value1)} || {str(changed_value2)}\n")
                                    f.write("|-" + "\n")
                                    z.pop(0)
                                    if loop_count >= 1:g.pop(0)
                                else:
                                    # print(f"|{str(change)} || {str(changed_value1)} || {str(changed_value2)}\n")
                                    if str(change) == "name":
                                        f.write(f"| {str(change)} || [[{str(changed_value1)}]] || [[{str(changed_value2)}]]\n")
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
        f.write(f"==Objects==\n{table_creation}!colspan='5'|Objects{table_creation_2}")
        missing = [name for name in names2 if name not in names1]
        deleted = [name for name in names1 if name not in names2]
        for m in missing:
            with open(dir2 + str(m)) as names:
                missing_files = json.load(names)
                f.write(f'| [[{str(missing_files[keys[3]])}]] || [{base_moid_url}{str(missing_files[keys[0]])} {str(missing_files[keys[0]])}] || colspan = "4" | New ID\n')
                f.write("|-" + "\n")

        for m in deleted:
            with open(dir1 + str(m)) as names:
                missing_files = json.load(names)
                f.write(f'| [[{str(missing_files[keys[3]])}]] || [{base_moid_url}{str(missing_files[keys[0]])} {str(missing_files[keys[0]])}] || colspan = "4" | Removed\n')
                f.write("|-" + "\n")

        print("Writing Object diffs")
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
                                        f.write(f"|{str(change)} || [[{str(changed_value1)}]] || [[{str(changed_value2)}]]\n")
                                    else:
                                        f.write(f"|{str(change)} || {str(changed_value1)} || {str(changed_value2)}\n")
                                    f.write("|-" + "\n")
                                    z.pop(0)
                                    if loop_count >= 1:g.pop(0)
                                else:
                                    # print(f"|{str(change)} || {str(changed_value1)} || {str(changed_value2)}\n")
                                    if str(change) == "name":
                                        f.write(f"| {str(change)} || [[{str(changed_value1)}]] || [[{str(changed_value2)}]]\n")
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
