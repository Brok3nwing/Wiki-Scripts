import json
import os
import possible_keys
import natsort
import argparse

parser = argparse.ArgumentParser(description="Creates cache diffs in .txt file with tab as delimiter")
parser.add_argument("--old", action="store", type=str, help="Path to old revision")
parser.add_argument("--new", action="store", type=str, help="Path to new revision")
parser.add_argument("--out", action="store", type=str, help="Output path")
newly_created = "NEW ID"
deleted_string = "Deleted"
name_array = 0
args = parser.parse_args()
old = args.old
new = args.new
path = args.out
old_dir = "C:/AbexRenderer/Cache Definitions/" + str(old)
new_dir = "C:/AbexRenderer/Cache Definitions/" + str(new)
occ = []



def items_csv():
    dir1 = old_dir + "/items/"
    dir2 = new_dir + "/items/"

    names1 = os.listdir(dir1)
    names2 = os.listdir(dir2)

    missing = [name for name in names2 if name not in names1]
    deleted = [name for name in names1 if name not in names2]

    common_names = set(names1) & set(names2)
    keys = possible_keys.Keys.item_data
    sorted_names = natsort.natsorted(common_names)
    with open(f"{args.out}.txt", "a") as f:
        f.write("Items\n")
        f.write(f"Name\tID\tKey\tPrevious Value\tChanged into\n")

        for m in missing:
            with open(dir2 + str(m)) as names:
                missing_files = json.load(names)
                f.write(f"{str(missing_files[keys[1]])}\t{str(missing_files[keys[0]])}\t{newly_created}\t{newly_created}\t{newly_created}\n")


        for m in deleted:
            with open(dir1 + str(m)) as names:
                missing_files = json.load(names)
                f.write(f"{str(missing_files[keys[1]])}\t{str(missing_files[keys[0]])}\t{deleted_string}\t{deleted_string}\t{deleted_string}\n")

        print("Writing Item  diffs")
        for filename in sorted_names:
            ext = os.path.splitext(filename)
            if ext[1] == ".json":
                print(filename)
                json1 = json.load(open(os.path.join(dir1, filename)))
                json2 = json.load(open(os.path.join(dir2, filename)))
                for change in keys:
                    try:
                        data1 = json1[change]
                        data2 = json2[change]
                        if data1 != data2:
                            changed_value1 = json1[change]
                            changed_value2 = json2[change]
                            if str(change) == "name":
                                f.write(f"{str(json2[keys[1]])}\t{str(json2[keys[0]])}\t{str(change)}\t{str(changed_value1)}\t{str(changed_value2)}\n")

                            else:
                                f.write(f"{str(json2[keys[1]])}\t{str(json2[keys[0]])}\t{str(change)}\t{str(changed_value1)}\t{str(changed_value2)}\n")

                    except KeyError:
                        pass


def npcs_csv():
    dir1 = old_dir + "/npcs/"
    dir2 = new_dir + "/npcs/"

    names1 = os.listdir(dir1)
    names2 = os.listdir(dir2)

    missing = [name for name in names2 if name not in names1]
    deleted = [name for name in names1 if name not in names2]

    common_names = set(names1) & set(names2)
    keys = possible_keys.Keys.npcs_data
    sorted_names = natsort.natsorted(common_names)
    with open(f"{args.out}.txt", "a") as f:
        f.write("Non-Player Characters\n")
        f.write(f"Name\tID\tKey\tPrevious Value\tChanged into\n")

        for m in missing:
            with open(dir2 + str(m)) as names:
                missing_files = json.load(names)
                f.write(f"{str(missing_files[keys[1]])}\t{str(missing_files[keys[0]])}\t{newly_created}\t{newly_created}\t{newly_created}\n")

        for m in deleted:
            with open(dir1 + str(m)) as names:
                missing_files = json.load(names)
                f.write(f"{str(missing_files[keys[1]])}\t{str(missing_files[keys[0]])}\t{deleted_string}\t{deleted_string}\t{deleted_string}\n")

        print("Writing Npc  diffs")
        for filename in sorted_names:
            ext = os.path.splitext(filename)
            if ext[1] == ".json":
                print(filename)
                json1 = json.load(open(os.path.join(dir1, filename)))
                json2 = json.load(open(os.path.join(dir2, filename)))
                for change in keys:
                    try:
                        data1 = json1[change]
                        data2 = json2[change]
                        if data1 != data2:
                            changed_value1 = json1[change]
                            changed_value2 = json2[change]
                            if str(change) == "name":
                                f.write(f"{str(json2[keys[1]])}\t{str(json2[keys[0]])}\t{str(change)}\t{str(changed_value1)}\t{str(changed_value2)}\n")

                            else:
                                f.write(f"{str(json2[keys[1]])}\t{str(json2[keys[0]])}\t{str(change)}\t{str(changed_value1)}\t{str(changed_value2)}\n")

                    except KeyError:
                        pass


def objects_csv():
    dir1 = old_dir + "/objects/"
    dir2 = new_dir + "/objects/"

    names1 = os.listdir(dir1)
    names2 = os.listdir(dir2)

    missing = [name for name in names2 if name not in names1]
    deleted = [name for name in names1 if name not in names2]

    common_names = set(names1) & set(names2)
    keys = possible_keys.Keys.objects_data
    sorted_names = natsort.natsorted(common_names)
    with open(f"{args.out}.txt", "a") as f:
        f.write("Objects\n")
        f.write(f"Name\tID\tKey\tPrevious Value\tChanged into\n")

        for m in missing:
            with open(dir2 + str(m)) as names:
                missing_files = json.load(names)
                f.write(f"{str(missing_files[keys[3]])}\t{str(missing_files[keys[0]])}\t{newly_created}\t{newly_created}\t{newly_created}\n")

        for m in deleted:
            with open(dir1 + str(m)) as names:
                missing_files = json.load(names)
                f.write(f"{str(missing_files[keys[3]])}\t{str(missing_files[keys[0]])}\t{deleted_string}\t{deleted_string}\t{deleted_string}\n")

        print("Writing Object diffs")
        for filename in sorted_names:
            ext = os.path.splitext(filename)
            if ext[1] == ".json":
                print(filename)
                json1 = json.load(open(os.path.join(dir1, filename)))
                json2 = json.load(open(os.path.join(dir2, filename)))
                for change in keys:
                    try:
                        data1 = json1[change]
                        data2 = json2[change]
                        if data1 != data2:
                            changed_value1 = json1[change]
                            changed_value2 = json2[change]
                            if str(change) == "name":
                                f.write(f"{str(json2[keys[3]])}\t{str(json2[keys[0]])}\t{str(change)}\t{str(changed_value1)}\t{str(changed_value2)}\n")
                            else:
                                f.write(f"{str(json2[keys[3]])}\t{str(json2[keys[0]])}\t{str(change)}\t{str(changed_value1)}\t{str(changed_value2)}\n")

                    except KeyError:
                        pass


# test()
items_csv()
npcs_csv()
objects_csv()
