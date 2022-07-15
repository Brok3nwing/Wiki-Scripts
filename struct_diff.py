import json
import os
import natsort


def read_structs():

    old_rev = "206.4"
    new_rev = "206.5"

    old_dir = f"C:/AbexRenderer/Cache Definitions/{old_rev}/structs"
    new_dir = f"C:/AbexRenderer/Cache Definitions/{new_rev}/structs"

    names1 = os.listdir(old_dir)
    names2 = os.listdir(new_dir)

    common_names = set(names1) & set(names2)
    sorted_names = natsort.natsorted(common_names)

    # print(sorted_names)

    new_files = [name for name in names2 if name not in names1]
    removed_files = [name for name in names1 if name not in names2]
    print("\n*** Diffs ****\n")
    for files in sorted_names:
        ext = os.path.splitext(files)
        if ext[1] == ".json":
            json1 = json.load(open(os.path.join(old_dir, files)))
            json2 = json.load(open(os.path.join(new_dir, files)))
            if json1 != json2:
                print(json1)
                print(json2)
                print("\n")

    print("\n*** New Structs ***\n")
    for files in new_files:
        ext = os.path.splitext(files)
        if ext[1] == ".json":
            json2 = json.load(open(os.path.join(new_dir, files)))
            print(json2)

    print("\n*** Removed Structs ***\n")
    for files in removed_files:
        ext = os.path.splitext(files)
        if ext[1] == ".json":
            json1 = json.load(open(os.path.join(old_dir, files)))
            print(json1)


read_structs()
