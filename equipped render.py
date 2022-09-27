import subprocess
import os
import csv
import pandas as pd


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

def read_data():
    reader = pd.read_excel("C:/Users/Brok/Documents/Python/PycharmProjects/wiki_scripts/test.xlsx", usecols="A:F")
    df = pd.DataFrame(reader)

    for i in range(len(df.dropna())):
        item_id.append(int(df.id[i]))
        item_name.append(df.name[i])
        item_slot.append(df.slot[i])
        item_anim.append(int(df.anim[i]) + 512)
        item_rota.append(int(df.rotation[i]))
        item_render_set.append(int(df.render_set[i]))

    return item_id, item_name, item_slot, item_anim, item_rota, item_render_set

def render_single_items():
    rev = "208.3"
    out = "out99"

    id, name, slot, anim, rota, set = read_data()

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
            print(male_player_kit)
            # subprocess.call(f"java -jar E:/Renderer/renderer-all.jar --playerkit {male_player_kit} --playercolors {male_player_colors} --playerchathead --anim 589 --cache E:/Caches/{rev}/cache2 --out {out}")
            # os.rename(f"{out}/playerchathead/[{male_player_kit.replace(',', ', ')}]_[{male_player_colors.replace(',', ', ')}].png",f"{out}/playerchathead/{name} chathead.png")

        # subprocess.call(f"java -jar E:/Renderer/renderer-all.jar --playerkit {male_player_kit} --playercolors {male_player_colors} --anim {anim} --yan2d {rota} --cache E:/Caches/{rev}/cache2 --out {out}")
        # subprocess.call(f"java -jar E:/Renderer/renderer-all.jar --playerkit {female_player_kit} --playercolors {female_player_colors} --playerfemale --anim {anim} --yan2d {rota} --cache E:/Caches/{rev}/cache2 --out {out}")
        # print(f"(female) {name[i]} : {female_player_kit}")
        print(f"(male) {name[i]} : {male_player_kit}")
        # os.rename(f"{out}/player/[{male_player_kit.replace(',', ', ')}]_[{male_player_colors.replace(',', ', ')}].png",f"{out}/player/{name} equipped male.png")
        # os.rename(f"{out}/player/[{female_player_kit.replace(',', ', ')}]_[{female_player_colors.replace(',', ', ')}].png", f"{out}/player/{name} equipped female.png")



def render_sets():
    id, name, slot, anim, rota, set = read_data()


    for i in range(len(set)):


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
    #         f"java -jar E:/Renderer/renderer-all.jar --playerkit  --playercolors {male_player_colors} --anim {anim} --yan2d {rota} --cache E:/Caches/{rev}/cache2 --out {out}")


render_sets()
