from glob import glob
import json
import os
import re
from os import path
import traceback

illegal_characters_start = "<col=......>"
illegal_characters_end = "</col>"
illegal_characters_start2 = "<COL=......>"
illegal_characters_end2 = "</COL>"
regex_only_numbers = "^[0-9]*$"


def remove_ilegal_characters(string):
    replace_1 = re.sub(illegal_characters_start, "", string)
    replaced_name = re.sub(illegal_characters_end, "", replace_1)
    return replaced_name


def rename_item():
    arr = []
    try:
        for b in glob("item/*.png"):
            id2 = re.sub("item\\\\", "", b)
            id = re.sub(".png", "", id2)
            path_to_json = "C:/AbexRenderer/Cache Definitions/" + rev + "/item_defs/" + id + ".json"
            if id.isnumeric():
                with open(path_to_json) as n:
                    data = json.load(n)
                    item_name = data["name"]
                    if arr.count(str(item_name).upper()) == 0:  # fewer or equal to 1
                        if re.match(illegal_characters_start, item_name):
                            replace_1 = re.sub(illegal_characters_start, "", item_name)
                            replaced_name = re.sub(illegal_characters_end, "", replace_1)
                            os.rename(b, f"item/{replaced_name} detail.png")
                            arr.append(str(remove_ilegal_characters(item_name)).upper())
                        else:
                            os.rename(b, f"item/{item_name} detail.png")
                            arr.append(str(remove_ilegal_characters(item_name)).upper())
                    else:
                        if re.match(illegal_characters_start, item_name):
                            replace_1 = re.sub(illegal_characters_start, "", item_name)
                            replaced_name = re.sub(illegal_characters_end, "", replace_1)
                            os.rename(b, f"item/{replaced_name} ({arr.count(str(item_name).upper())}) detail.png")
                            arr.append(str(remove_ilegal_characters(item_name)).upper())
                        else:
                            os.rename(b, f"item/{item_name} ({arr.count(str(item_name).upper())}) detail.png")
                            arr.append(str(remove_ilegal_characters(item_name)).upper())
            else:
                pass
    except:
        traceback.print_exc()


def rename_equipped():
    arr = []
    try:
        for b in glob("item/*.png"):
            id2 = re.sub("player\\\\", "", b)
            id = re.sub(".png", "", id2)
            path_to_json = "C:/AbexRenderer/Cache Definitions/" + rev + "/item_defs/" + id + ".json"
            if id.isnumeric():
                with open(path_to_json) as n:
                    data = json.load(n)
                    chathead_name = data["name"]
                    arr.append(chathead_name)
                    if arr.count(chathead_name) <= 1:
                        if re.match(illegal_characters_start, chathead_name):
                            replace_1 = re.sub(illegal_characters_start, "", chathead_name)
                            replaced_name = re.sub(illegal_characters_end, "", replace_1)
                            os.rename(b, f"item/{replaced_name} detail.png")
                        else:
                            os.rename(b, f"item/{chathead_name} detail.png")
                    else:
                        if re.match(illegal_characters_start, chathead_name):
                            replace_1 = re.sub(illegal_characters_start, "", chathead_name)
                            replaced_name = re.sub(illegal_characters_end, "", replace_1)
                            os.rename(b, f"player/{replaced_name} ({arr.count(chathead_name)}) equipped male.png")
            else:
                pass
    except:
        traceback.print_exc()


def rename_chathead():
    arr = []
    try:
        for b in glob("chathead/*.png"):
            id2 = re.sub("chathead\\\\", "", b)
            id = re.sub(".png", "", id2)
            path_to_json = "C:/AbexRenderer/Cache Definitions/" + rev + "/npc_defs/" + id + ".json"
            if id.isnumeric():
                with open(path_to_json) as n:
                    data = json.load(n)
                    item_name = data["name"]
                    if arr.count(str(item_name).upper()) == 0:  # fewer or equal to 1
                        if re.match(illegal_characters_start, item_name):
                            replace_1 = re.sub(illegal_characters_start, "", item_name)
                            replaced_name = re.sub(illegal_characters_end, "", replace_1)
                            os.rename(b, f"chathead/{replaced_name} chathead.png")
                            arr.append(str(remove_ilegal_characters(item_name)).upper())
                        else:
                            os.rename(b, f"chathead/{item_name} chathead.png")
                            arr.append(str(remove_ilegal_characters(item_name)).upper())
                    else:
                        if re.match(illegal_characters_start, item_name):
                            replace_1 = re.sub(illegal_characters_start, "", item_name)
                            replaced_name = re.sub(illegal_characters_end, "", replace_1)
                            os.rename(b, f"chathead/{replaced_name} ({arr.count(str(item_name).upper())}) chathead.png")
                            arr.append(str(remove_ilegal_characters(item_name)).upper())
                        else:
                            os.rename(b, f"chathead/{item_name} ({arr.count(str(item_name).upper())}) chathead.png")
                            arr.append(str(remove_ilegal_characters(item_name)).upper())

            else:
                pass
    except:
        traceback.print_exc()


def rename_object():
    arr = []
    try:
        for b in glob("object/*.png"):
            id2 = re.sub("object\\\\", "", b)
            id = re.sub(".png", "", id2)
            path_to_json = "C:/AbexRenderer/Cache Definitions/" + rev + "/object_defs/" + id + ".json"
            if id.isnumeric():
                with open(path_to_json) as n:
                    data = json.load(n)
                    item_name = data["name"]
                    arr.append(item_name)
                    if arr.count(item_name) <= 1:  # fewer or equal
                        if re.match(illegal_characters_start, item_name):
                            replace_1 = re.sub(illegal_characters_start, "", item_name)
                            replaced_name = re.sub(illegal_characters_end, "", replace_1)
                            os.rename(b, f"object/{replaced_name}.png")
                        else:
                            os.rename(b, f"object/{item_name}.png")
                    else:
                        if re.match(illegal_characters_start, item_name):
                            replace_1 = re.sub(illegal_characters_start, "", item_name)
                            replaced_name = re.sub(illegal_characters_end, "", replace_1)
                            os.rename(b, f"object/{replaced_name} ({arr.count(item_name)}).png")
                        else:
                            os.rename(b, f"object/{item_name} ({arr.count(item_name)}).png")
            else:
                pass
    except:
        traceback.print_exc()


def rename_npc():
    arr = []
    try:
        for b in glob("npc/*.png"):
            id2 = re.sub("npc\\\\", "", b)
            id = re.sub(".png", "", id2)
            path_to_json = "C:/AbexRenderer/Cache Definitions/" + rev + "/npc_defs/" + id + ".json"
            if id.isnumeric():
                with open(path_to_json) as n:
                    data = json.load(n)
                    item_name = data["name"]
                    if arr.count(str(item_name).upper()) == 0:  # fewer or equal to 1
                        if re.match(illegal_characters_start, item_name):
                            replace_1 = re.sub(illegal_characters_start, "", item_name)
                            replaced_name = re.sub(illegal_characters_end, "", replace_1)
                            os.rename(b, f"npc/{replaced_name}.png")
                            arr.append(str(remove_ilegal_characters(item_name)).upper())
                        else:
                            os.rename(b, f"npc/{item_name}.png")
                            arr.append(str(remove_ilegal_characters(item_name)).upper())
                    else:
                        if re.match(illegal_characters_start, item_name):
                            replace_1 = re.sub(illegal_characters_start, "", item_name)
                            replaced_name = re.sub(illegal_characters_end, "", replace_1)
                            os.rename(b, f"npc/{replaced_name} ({arr.count(str(item_name).upper())}).png")
                            arr.append(str(remove_ilegal_characters(item_name)).upper())
                        else:
                            os.rename(b, f"npc/{item_name} ({arr.count(str(item_name).upper())}).png")
                            arr.append(str(remove_ilegal_characters(item_name)).upper())

            else:
                pass
    except:
        traceback.print_exc()


def rename_miniitems():
    arr = []
    try:
        for b in glob("miniitems/*.png"):
            id2 = re.sub("miniitems\\\\", "", b)
            id = re.sub(".png", "", id2)
            path_to_json = "C:/AbexRenderer/Cache Definitions/" + rev + "/item_defs/" + id + ".json"
            if id.isnumeric():
                with open(path_to_json) as n:
                    data = json.load(n)
                    item_name = data["name"]
                    if arr.count(str(item_name).upper()) == 0:  # fewer or equal to 1
                        if re.match(illegal_characters_start, item_name):
                            replace_1 = re.sub(illegal_characters_start, "", item_name)
                            replaced_name = re.sub(illegal_characters_end, "", replace_1)
                            os.rename(b, f"miniitems/{replaced_name}.png")
                            arr.append(str(remove_ilegal_characters(item_name)).upper())
                        else:
                            os.rename(b, f"miniitems/{item_name}.png")
                            arr.append(str(remove_ilegal_characters(item_name)).upper())
                    else:
                        if re.match(illegal_characters_start, item_name):
                            replace_1 = re.sub(illegal_characters_start, "", item_name)
                            replaced_name = re.sub(illegal_characters_end, "", replace_1)
                            os.rename(b, f"miniitems/{replaced_name} ({arr.count(str(item_name).upper())}).png")
                            arr.append(str(remove_ilegal_characters(item_name)).upper())
                        else:
                            os.rename(b, f"miniitems/{item_name} ({arr.count(str(item_name).upper())}).png")
                            arr.append(str(remove_ilegal_characters(item_name)).upper())
            else:
                pass
    except:
        traceback.print_exc()


rev = input("Enter Revision: ")
# rev = "192.7"
rename_item()
rename_chathead()
rename_object()
rename_npc()
rename_miniitems()
