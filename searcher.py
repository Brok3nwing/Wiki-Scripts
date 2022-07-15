import os
import json
import re
import traceback
from glob import glob

input_name = input("Name or ID: ")
rev = input("Cache Rev: ")
spec = input("items, objects or npcs: ")
input_key = input("Keys: ")
pattern = re.compile(r',')


def do_name_search():
    os.chdir(f"C:/AbexRenderer/Cache Definitions/{rev}/{spec}/")
    print("Name Search")
    for data in glob("*.json"):
        with open(data) as n:
            datas = json.load(n)
            try:
                # model = datas["objectModels"]
                # model = datas["models"]
                # maleModel = datas["maleModel0"]
                # femaleModel = datas["femaleModel0"]
                item_id = datas["id"]
                name = datas["name"]
                # model = datas["inventoryModel"]
                # 40418
                # if model != -1 and item_id >= 25625:
                # if maleModel[0] == 32200:

                if input_name.lower() == str(name).lower() and input_key is not False:
                    key = datas[input_key]
                    print(name, item_id, key)
                elif input_name.lower() == str(name).lower():
                    print(name, item_id)
                # with open("C:/Users/pr0pj/PycharmProjects/id_search/object_models.txt", "a") as f:
                #     f.write(f"{name}\t{item_id}\t{model}\n")


                # if item_model_id != -1 and not re.findall(r"Wear", str(interface)):
                # if re.findall(r",", str(model)):
                #     print(str(name) + ";" + str(item_id) + ";" + str(model))
                #     if not re.findall(r"Wield", str(interface)):
                #         print(str(name)+";" + str(item_id)+";" + str(item_model_id) + ";" + str(interface))

            except KeyError:
                pass



def do_id_search():
    os.chdir(f"C:/AbexRenderer/Cache Definitions/{rev}/{spec}/")
    print("ID Search")
    for data in glob("*.json"):
        with open(data) as n:
            datas = json.load(n)
            try:
                # model = datas["objectModels"]
                # model = datas["models"]
                # maleModel = datas["maleModel0"]
                # femaleModel = datas["femaleModel0"]
                item_id = datas["id"]
                name = datas["name"]
                key = datas[input_key]
                # model = datas["inventoryModel"]
                # 40418
                # if model != -1 and item_id >= 25625:
                # if maleModel[0] == 32200:

                if input_name == item_id and key is not False:
                    print(name, item_id, key)
                else:
                    print(name, item_id)

                # with open("C:/Users/pr0pj/PycharmProjects/id_search/object_models.txt", "a") as f:
                #     f.write(f"{name}\t{item_id}\t{model}\n")

                # if item_model_id != -1 and not re.findall(r"Wear", str(interface)):
                # if re.findall(r",", str(model)):
                #     print(str(name) + ";" + str(item_id) + ";" + str(model))
                #     if not re.findall(r"Wield", str(interface)):
                #         print(str(name)+";" + str(item_id)+";" + str(item_model_id) + ";" + str(interface))

            except KeyError:
                pass



if input_name.isnumeric():
    do_id_search()
else:
    do_name_search()
