import subprocess
import os
import csv


def eq():
    #  default kit [0, 0, 0, 0, 363, 0, 342, 356, 259, 289, 298, 270]
    #  kit {head},{cape},{neck},{weapon},{chest},{shield},{arms},{legs},{hair},{hands},{feet},{jaw}
    rev = "208.2"
    player_colors = "0,3,15,1,0"

    with open("equipped.csv", "r") as f:
        data = csv.reader(f, delimiter=",")
        for f in data:
            id = f[0]
            item = int(id) + 512
            name = f[1]
            slot = f[2]
            anim = f[3]
            rota = f[4]
            player_kit = f"{str(item) if slot == 'head' else 0}," \
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
            # print("------------------")
            # print(player_kit)
            print(f"Rendering Equipped Item '{name}' in slot '{slot}'")
            # print("------------------")
            subprocess.call(f"java -jar E:/Renderer/renderer-all.jar --playerkit {player_kit} --playercolors {player_colors} --anim {anim} --yan2d {rota} --cache E:/Caches/{rev}/cache --out out1")
            os.rename(f"out1/player/[{player_kit.replace(',', ', ')}]_[{player_colors.replace(',', ', ')}].png", f"out1/player/{name} equipped male.png")

eq()
