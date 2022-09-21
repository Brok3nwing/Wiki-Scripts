import subprocess
import os
import csv


#  male default kit [0, 0, 0, 0, 363, 0, 342, 356, 259, 289, 298, 270]
#  female default kit [0, 0, 0, 0, 312, 0, 317, 326, 377, 324, 335, 0]
# female default color [7, 16, 26, 0, 0]
#  kit {head},{cape},{neck},{weapon},{chest},{shield},{arms},{legs},{hair},{hands},{feet},{jaw}

def eq():
    rev = "208.3"
    out = "out99"


    male_player_colors = "0,3,15,1,0"
    female_player_colors = "7,16,26,0,0"

    with open("equipped.csv", "r") as f:
        data = csv.reader(f, delimiter=",")
        for f in data:
            id = f[0]
            item = int(id) + 512
            name = f[1]
            slot = f[2]
            anim = f[3]
            rota = f[4]
            male_player_kit = f"{str(item) if slot == 'head' else 0}," \
                         f"{str(item) if slot == 'cape' else 0}," \
                         f"{str(item) if slot == 'neck' else 0}," \
                         f"{str(item) if slot == 'weapon' else 0}," \
                         f"{str(item) if slot == 'chest' else 363}," \
                         f"{str(item) if slot == 'shield' else 0}," \
                         f"{0 if slot == 'chest' else 342}," \
                         f"{str(item) if slot == 'legs' else 356}," \
                         f"{str(item) if slot == 'hair' else 259}," \
                         f"{str(item) if slot == 'hands' else 289}," \
                         f"{str(item) if slot == 'feet' else 298}," \
                         f"{str(item) if slot == 'jaw' else 270}"

            female_player_kit = f"{str(item) if slot == 'head' else 0}," \
                         f"{str(item) if slot == 'cape' else 0}," \
                         f"{str(item) if slot == 'neck' else 0}," \
                         f"{str(item) if slot == 'weapon' else 0}," \
                         f"{str(item) if slot == 'chest' else 312}," \
                         f"{str(item) if slot == 'shield' else 0}," \
                         f"{0 if slot == 'chest' else 317}," \
                         f"{str(item) if slot == 'legs' else 326}," \
                         f"{str(item) if slot == 'hair' else 377}," \
                         f"{str(item) if slot == 'hands' else 324}," \
                         f"{str(item) if slot == 'feet' else 335}," \
                         f"{str(item) if slot == 'jaw' else 0}"
            # print("------------------")
            # print(player_kit)
            #  print(f"Rendering Equipped Item '{name}' in slot '{slot}'")
            # print("------------------")

            if slot == "head":
                subprocess.call(f"java -jar E:/Renderer/renderer-all.jar --playerkit {male_player_kit} --playercolors {male_player_colors} --playerchathead --anim 589 --cache E:/Caches/{rev}/cache2 --out {out}")
                os.rename(f"{out}/playerchathead/[{male_player_kit.replace(',', ', ')}]_[{male_player_colors.replace(',', ', ')}].png",f"{out}/playerchathead/{name} chathead.png")

            subprocess.call(f"java -jar E:/Renderer/renderer-all.jar --playerkit {male_player_kit} --playercolors {male_player_colors} --anim {anim} --yan2d {rota} --cache E:/Caches/{rev}/cache2 --out {out}")
            subprocess.call(f"java -jar E:/Renderer/renderer-all.jar --playerkit {female_player_kit} --playercolors {female_player_colors} --playerfemale --anim {anim} --yan2d {rota} --cache E:/Caches/{rev}/cache2 --out {out}")
            print(f"(female) {name} : {female_player_kit}")
            print(f"(male) {name} : {male_player_kit}")
            os.rename(f"{out}/player/[{male_player_kit.replace(',', ', ')}]_[{male_player_colors.replace(',', ', ')}].png",f"{out}/player/{name} equipped male.png")
            os.rename(f"{out}/player/[{female_player_kit.replace(',', ', ')}]_[{female_player_colors.replace(',', ', ')}].png", f"{out}/player/{name} equipped female.png")

eq()
