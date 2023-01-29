import subprocess
import os
import pandas as pd
import json
from itertools import cycle


#  male default kit [0,0,0,0,363,0,342,356,259,289,298,270]
#  female default kit [0, 0, 0, 0, 312, 0, 317, 326, 377, 324, 335, 0]
# female default color [7, 16, 26, 0, 0]
#  kit {head},{cape},{neck},{weapon},{chest},{shield},{arms},{legs},{hair/head},{hands},{feet},{jaw}

item_id = []
item_name = []
item_slot = []
item_anim = []
item_rota = []
item_render_set = []
cache_version = 0

def read_data():
    reader = pd.read_excel("C:/Users/Brok/Documents/Python/PycharmProjects/wiki_scripts/test2.xlsm", usecols="A:F")
    df = pd.DataFrame(reader)
    for i in range(len(df.id.dropna())):
        item_id.append(int(df.id[i]) + 512)
        item_name.append(df.fillna("").name[i])
        # item_slot.append(df.slot[i])
        item_anim.append(int(df.fillna(0).anim[i]))
        item_rota.append(int(df.fillna(0).rotation[i]))
        item_render_set.append(df.fillna("").render_set[i])

    cache_version = df.cache_version
    return item_id, item_name, item_anim, item_rota, item_render_set, cache_version

def get_item_name_from_cache(item_id: int):
    version = read_data()[5][0]
    path_to_defs = f"E:/Caches/{version}/definitions/item_defs/"
    name = ""

    with open(f"{path_to_defs}{item_id}.json") as f:
        json_data = json.load(f)
        name = json_data["name"]

    return name

def get_item_data_from_cache(item_id: int):
    version = read_data()[5][0]
    path_to_defs = f"E:/Caches/{version}/definitions/item_defs/"

    with open(f"{path_to_defs}{item_id}.json") as f:
        json_data = json.load(f)
        wearpos1 = json_data["wearPos1"]
        wearpos2 = json_data["wearPos2"]
        wearpos3 = json_data["wearPos3"]


    return wearpos1, wearpos2, wearpos3


def render_single_items():
    out = "out99"

    id, name, anim, rota, set, version = read_data()

    male_player_colors = "0,3,15,1,0"
    female_player_colors = "7,16,26,0,0"


    for i in range(len(id)):
        slot = get_item_data_from_cache(id[i] - 512)
        # print(get_item_name_from_cache(id[i]-512), slot)

        # f"{str(id[i]) if slot[0] == 'hair' else 259}," \ ---377 for female----

        # 0 helm
        # 1 cape
        # 2 amulet
        # 3 weapon
        # 4 top
        # 5 shield
        # 6 hair
        # 7 bottom
        # 8 arms
        # 9 gloves
        # 10 boots
        # 11 jaw


        male_player_kit = f"{str(id[i]) if slot[0] == 0 else 0}," \
             f"{str(id[i]) if slot[0] == 1 else 0}," \
             f"{str(id[i]) if slot[0] == 2 else 0}," \
             f"{str(id[i]) if slot[0] == 3 else 0}," \
             f"{str(id[i]) if slot[0] == 4 else 363}," \
             f"{str(id[i]) if slot[0] == 5 else 0}," \
             f"{0 if slot[1] == 8 else 259}," \
             f"{0 if slot[1] == 6 else 342}," \
             f"{str(id[i]) if slot[0] == 7 else 356}," \
             f"{0 if slot[2] == 9 and slot[0] == 3 else str(id[i]) if slot[0] == 9 else 289}," \
             f"{str(id[i]) if slot[0] == 10 else 298}," \
             f"{0 if slot[2] == 11 else 270}"


        female_player_kit = f"{str(id[i]) if slot[0] == 0 else 0}," \
             f"{str(id[i]) if slot[0] == 1 else 0}," \
             f"{str(id[i]) if slot[0] == 2 else 0}," \
             f"{str(id[i]) if slot[0] == 3 else 0}," \
             f"{str(id[i]) if slot[0] == 4 else 312}," \
             f"{str(id[i]) if slot[0] == 5 else 0}," \
             f"{0 if slot[1] == 8 else 377}," \
             f"{0 if slot[1] == 6 else 317}," \
             f"{str(id[i]) if slot[0] == 7 else 326}," \
             f"{0 if slot[2] == 9 and slot[0] == 3 else str(id[i]) if slot[0] == 9 else 324}," \
             f"{str(id[i]) if slot[0] == 10 else 335}," \
             f"0"

        if slot[0] == 0:
            head_proc = f"java -jar E:/Renderer/renderer-all.jar --playerkit {male_player_kit} --playercolors {male_player_colors} --playerchathead --anim 589 --cache E:/Caches/{version[0]}/cache --out {out}"
            subprocess.call(head_proc)
            os.rename(f"{out}/playerchathead/[{male_player_kit.replace(',', ', ')}]_[{male_player_colors.replace(',', ', ')}].png",f"{out}/playerchathead/{get_item_name_from_cache(id[i] - 512)} chathead.png")



        male_proc = f"java -jar E:/Renderer/renderer-all.jar --playerkit {male_player_kit} --playercolors {male_player_colors} --poseanim {808 if anim[i] == 0 else anim[i]} --yan2d {128 if rota[i] == 0 else rota[i]} --cache E:/Caches/{version[0]}/cache --out {out}/male"
        female_proc = f"java -jar E:/Renderer/renderer-all.jar --playerkit {female_player_kit} --playercolors {female_player_colors} --playerfemale --anim {808 if anim[i] == 0 else anim[i]} --yan2d {128 if rota[i] == 0 else rota[i]} --cache E:/Caches/{version[0]}/cache --out {out}/female"
        print(male_proc)

        # print(f"(female) {name[i]} : {female_player_kit}")
        # print(f"(male) {name[i]} : {male_player_kit}")

        pre_render_male_equipped_name = f"{out}/male/player/[{male_player_kit.replace(',', ', ')}]_[{male_player_colors.replace(',', ', ')}].png"
        pre_render_female_equipped_name = f"{out}/female/player/[{female_player_kit.replace(',', ', ')}]_[{female_player_colors.replace(',', ', ')}].png"

        render_male_equipped_name = f"{out}/male/player/{get_item_name_from_cache(id[i] - 512)}{' equipped male.png' if name[i] == '' else ' '+name[i]+' equipped male.png'}"
        render_female_equipped_name = f"{out}/female/player/{get_item_name_from_cache(id[i] - 512)}{' equipped female.png' if name[i] == '' else ' '+name[i]+' equipped female.png'}"

        if not os.path.isfile(render_male_equipped_name):
            print("Rendering (male): ", get_item_name_from_cache(id[i] - 512))
            print(male_proc)
            subprocess.call(male_proc)
            os.rename(pre_render_male_equipped_name, render_male_equipped_name)
        if not os.path.isfile(render_female_equipped_name):
            print("Rendering (female): ", get_item_name_from_cache(id[i] - 512))
            subprocess.call(female_proc)
            os.rename(pre_render_female_equipped_name, render_female_equipped_name)

def render_sets():
    out = "out99"
    male_player_colors = "0,3,15,1,0"
    female_player_colors = "7,16,26,0,0"
    #  male default kit [0, 0, 0, 0, 363, 0, 342, 356, 259, 289, 298, 270]

    #  kit {head},{cape},{neck},{weapon},{chest},{shield},{arms},{legs},{hair},{hands},{feet},{jaw}

    id, name, anim, rota, armour_set, version = read_data()
    l = ()

    male_player_kit = {
        0: 0, # helm
        1: 0, # cape
        2: 0, # amulet
        3: 0, # weapon
        4: 363, # top
        5: 0, # shield
        8: 356, # hair
        6: 259, # arms
        7: 342, # legs
        9: 289, # gloves
        10: 298, # boots
        11: 270 # jaw
    }

    for c, i in enumerate(set(id)):

        slot = get_item_data_from_cache(i - 512)
        print(slot)
        male_player_kit[slot[0]] = i

        if slot[0] == 0:
            if slot[1] == 8:
                male_player_kit[8] = 0
            if slot[2] == 11:
                male_player_kit[11] = 0
        if slot[0] == 4:
            if slot[1] == 6:
                male_player_kit[6] = 0
    print(male_player_kit)
    male_proc = f"java -jar E:/Renderer/renderer-all.jar --playerkit {convert_to_player_kit(male_player_kit)} --playercolors {male_player_colors} --poseanim {808 if anim[0] == 0 else anim[0]} --yan2d {128 if rota[0] == 0 else rota[0]} --cache E:/Caches/{version[0]}/cache --out {out}/male"
    print(male_proc)
    subprocess.call(male_proc)

def convert_to_player_kit(kit: dict):
    player_kit = []
    final_kit = ","

    for keys, values in kit.items():
        player_kit.append(str(values))

    return final_kit.join(player_kit)


# render_single_items()
render_sets()
