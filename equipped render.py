import subprocess
import os
import numpy as np
import pandas as pd
import json


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
        item_anim.append(int(df.anim[i]))
        item_rota.append(int(df.rotation[i]))
        item_render_set.append(int(df.render_set[i]))

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



        male_proc = f"java -jar E:/Renderer/renderer-all.jar --playerkit {male_player_kit} --playercolors {male_player_colors} --poseanim {anim[i]} --yan2d {rota[i]} --cache E:/Caches/{version[0]}/cache --out {out}"
        female_proc = f"java -jar E:/Renderer/renderer-all.jar --playerkit {female_player_kit} --playercolors {female_player_colors} --playerfemale --anim {anim[i]} --yan2d {rota[i]} --cache E:/Caches/{version[0]}/cache --out {out}"

        subprocess.call(male_proc)
        subprocess.call(female_proc)
        print(f"(female) {name[i]} : {female_player_kit}")
        print(f"(male) {name[i]} : {male_player_kit}")
        os.rename(f"{out}/player/[{male_player_kit.replace(',', ', ')}]_[{male_player_colors.replace(',', ', ')}].png",f"{out}/player/{get_item_name_from_cache(id[i] - 512) if name[i] == '' else name[i]} equipped male.png")
        os.rename(f"{out}/player/[{female_player_kit.replace(',', ', ')}]_[{female_player_colors.replace(',', ', ')}].png",f"{out}/player/{get_item_name_from_cache(id[i] - 512) if name[i] == '' else name[i]} equipped female.png")

def render_sets():
    id, name, slot, anim, rota, set = read_data()
    sets = {}
    # sets = {int(set[0]) : [name[0]]}

    x = {int(set[0]) : [name[0]]}
    y = {int(set[1]): [name[1]]}
    sets.update(x)
    sets.update(y)

    print(sets)
    # for i in range(len(set)):
    #     if set[i] > 0:
    #         sets[] = [name[i]]

    # male_player_kit = f"{str(id[i]) if slot[i] == 'head' else 0}," \
    #                   f"{str(id[i]) if slot[i] == 'cape' else 0}," \
    #                   f"{str(id[i]) if slot[i] == 'neck' else 0}," \
    #                   f"{str(id[i]) if slot[i] == 'weapon' else 0}," \
    #                   f"{str(id[i]) if slot[i] == 'chest' else 363}," \
    #                   f"{str(id[i]) if slot[i] == 'shield' else 0}," \
    #                   f"{0 if slot[i] == 'chest' else 342}," \
    #                   f"{str(id[i]) if slot[i] == 'legs' else 356}," \
    #                   f"{str(id[i]) if slot[i] == 'hair' else 259}," \
    #                   f"{str(id[i]) if slot[i] == 'hands' else 289}," \
    #                   f"{str(id[i]) if slot[i] == 'feet' else 298}," \
    #                   f"{str(id[i]) if slot[i] == 'jaw' else 270}"

    # if set.count(1) > 1:
    #     subprocess.call(
    #         f"java -jar E:/Renderer/renderer-all.jar --playerkit  --playercolors {male_player_colors} --anim {anim} --yan2d {rota} --cache E:/Caches/{version[0]}/cache2 --out {out}")


render_single_items()
