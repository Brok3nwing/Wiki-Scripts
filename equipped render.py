import subprocess
import os
import pandas as pd
import json
from itertools import cycle


#  male default kit [0, 0, 0, 0, 363, 0, 342, 356, 259, 289, 298, 270]
#  female default kit [0, 0, 0, 0, 312, 0, 317, 326, 377, 324, 335, 0]
# female default color [7, 16, 26, 0, 0]
#  kit {head},{cape},{neck},{weapon},{chest},{shield},{arms},{legs},{hair},{hands},{feet},{jaw}

item_id = []
item_name = []
item_slot = []
item_anim = []
item_rota = []
item_render_set = []
cache_version = 0

def read_data():
    reader = pd.read_excel("C:/Users/Brok/Documents/Python/PycharmProjects/wiki_scripts/test.xlsx", usecols="A:G")
    df = pd.DataFrame(reader)
    for i in range(len(df.id.dropna())):
        item_id.append(int(df.id[i]) + 512)
        item_name.append(df.fillna("").name[i])
        item_slot.append(df.slot[i])
        item_anim.append(int(df.fillna(0).anim[i]))
        item_rota.append(int(df.fillna(0).rotation[i]))
        item_render_set.append(df.fillna("").render_set[i])

    cache_version = df.cache_version
    return item_id, item_name, item_slot, item_anim, item_rota, item_render_set, cache_version

def get_item_name_from_cache(item_id: int):
    version = read_data()[6][0]
    path_to_defs = f"E:/Caches/{version}/definitions/item_defs/"
    name = ""
    with open(f"{path_to_defs}{item_id}.json") as f:
        json_data = json.load(f)
        name = json_data["name"]

    return name

def render_single_items():
    out = "out99"

    id, name, slot, anim, rota, set, version = read_data()

    male_player_colors = "0,3,15,1,0"
    female_player_colors = "7,16,26,0,0"

    for i in range(len(id)):


        male_player_kit = f"{str(id[i]) if slot[i] == 'head' else 0}," \
                     f"{str(id[i]) if slot[i] == 'cape' else 0}," \
                     f"{str(id[i]) if slot[i] == 'neck' else 0}," \
                     f"{str(id[i]) if slot[i] == 'weapon' else 0}," \
                     f"{str(id[i]) if slot[i] == 'chest' else 363}," \
                     f"{str(id[i]) if slot[i] == 'shield' else 0}," \
                     f"{0 if slot[i] == 'chest' else 342}," \
                     f"{str(id[i]) if slot[i] == 'legs' else 356}," \
                     f"{str(id[i]) if slot[i] == 'hair' else 259}," \
                     f"{str(id[i]) if slot[i] == 'hands' else 289}," \
                     f"{str(id[i]) if slot[i] == 'feet' else 298}," \
                     f"{str(id[i]) if slot[i] == 'jaw' else 270}"

        female_player_kit = f"{str(id[i]) if slot[i] == 'head' else 0}," \
                     f"{str(id[i]) if slot[i] == 'cape' else 0}," \
                     f"{str(id[i]) if slot[i] == 'neck' else 0}," \
                     f"{str(id[i]) if slot[i] == 'weapon' else 0}," \
                     f"{str(id[i]) if slot[i] == 'chest' else 312}," \
                     f"{str(id[i]) if slot[i] == 'shield' else 0}," \
                     f"{0 if slot[i] == 'chest' else 317}," \
                     f"{str(id[i]) if slot[i] == 'legs' else 326}," \
                     f"{str(id[i]) if slot[i] == 'hair' else 377}," \
                     f"{str(id[i]) if slot[i] == 'hands' else 324}," \
                     f"{str(id[i]) if slot[i] == 'feet' else 335}," \
                     f"{str(id[i]) if slot[i] == 'jaw' else 0}"

        if slot[i] == "head":
            head_proc = f"java -jar E:/Renderer/renderer-all.jar --playerkit {male_player_kit} --playercolors {male_player_colors} --playerchathead --anim 589 --cache E:/Caches/{version[0]}/cache --out {out}"
            subprocess.call(head_proc)
            os.rename(f"{out}/playerchathead/[{male_player_kit.replace(',', ', ')}]_[{male_player_colors.replace(',', ', ')}].png",f"{out}/playerchathead/{name[i]} chathead.png")



        male_proc = f"java -jar E:/Renderer/renderer-all.jar --playerkit {male_player_kit} --playercolors {male_player_colors} --poseanim {808 if anim[i] == 0 else anim[i]} --yan2d {128 if rota[i] == 0 else rota[i]} --cache E:/Caches/{version[0]}/cache --out {out}/male"
        female_proc = f"java -jar E:/Renderer/renderer-all.jar --playerkit {female_player_kit} --playercolors {female_player_colors} --playerfemale --anim {808 if anim[i] == 0 else anim[i]} --yan2d {128 if rota[i] == 0 else rota[i]} --cache E:/Caches/{version[0]}/cache --out {out}/female"


        # print(f"(female) {name[i]} : {female_player_kit}")
        # print(f"(male) {name[i]} : {male_player_kit}")

        pre_render_male_equipped_name = f"{out}/male/player/[{male_player_kit.replace(',', ', ')}]_[{male_player_colors.replace(',', ', ')}].png"
        pre_render_female_equipped_name = f"{out}/female/player/[{female_player_kit.replace(',', ', ')}]_[{female_player_colors.replace(',', ', ')}].png"

        render_male_equipped_name = f"{out}/male/player/{get_item_name_from_cache(id[i] - 512) if name[i] == '' else name[i]} equipped male.png"
        render_female_equipped_name = f"{out}/female/player/{get_item_name_from_cache(id[i] - 512) if name[i] == '' else name[i]} equipped female.png"

        if not os.path.isfile(render_male_equipped_name):
            subprocess.call(male_proc)
            os.rename(pre_render_male_equipped_name, render_male_equipped_name)
        elif not os.path.isfile(render_female_equipped_name):
            subprocess.call(female_proc)
            os.rename(pre_render_female_equipped_name, render_female_equipped_name)

def render_sets():
    male_player_colors = "0,3,15,1,0"
    id, name, slot, anim, rota, armour_set, version = read_data()
    sets = set()
    full_set = {}
    for x in range(len(armour_set)):
        if armour_set[x] != "":
            sets.add(armour_set[x])

    for x in range(len(sets)):
        full_set = {
            list(sets)[x]:
                {
                    "head": 0,
                    "cape": 0,
                    "neck": 0,
                    "weapon": 0,
                    "chest": 363,
                    "shield": 0,
                    "arms": 342,
                    "legs": 356,
                    "hair": 259,
                    "hands": 289,
                    "feet": 298,
                    "jaw": 270,
                }
        }
        for y in range(len(armour_set)):
            if armour_set[y] != "":
                if armour_set[y] == list(sets)[x]:
                    full_set[list(sets)[x]][slot[y]] = id[y]
                    if slot[y] == "chest":
                        full_set[list(sets)[x]]["arms"] = 0
                    elif slot[y] == "head":
                        full_set[list(sets)[x]]["hair"] = 0
                        full_set[list(sets)[x]]["jaw"] = 0
        male_proc = f"java -jar E:/Renderer/renderer-all.jar --playerkit {convert_to_player_kit(full_set)} --playercolors {male_player_colors} --poseanim 808 --yan2d 128 --cache E:/Caches/{version[0]}/cache --out out99/male"
        print(male_proc)
        subprocess.call(male_proc)




def convert_to_player_kit(kit : dict):
    player_kit = []
    final_kit = ","
    for i in kit.keys():
        for j, b in kit[i].items():
            player_kit.append(str(b))

    return final_kit.join(player_kit)


# render_single_items()
render_sets()
