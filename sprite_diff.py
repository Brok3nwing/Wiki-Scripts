from glob import glob
import hashlib
from PIL import Image
import shutil
import os

rev1 = input("Enter old cache: ")
rev2 = input("Enter new cache: ")

path1 = f'C:/AbexRenderer/Cache Definitions/{rev1}/sprites/'
path2 = f'C:/AbexRenderer/Cache Definitions/{rev2}/sprites/'


def sp1():
    hash = {}
    for images in glob(f'{path1}*.png'):
        filename = images.split('\\')[1]
        md5hash = hashlib.md5(Image.open(images).tobytes())
        hash[f'{filename}'] = f'{md5hash.hexdigest()}'

    return hash


def sp2():
    hash = {}
    for images in glob(f'{path2}*.png'):
        filename = images.split('\\')[1]
        md5hash = hashlib.md5(Image.open(images).tobytes())
        hash[f'{filename}'] = f'{md5hash.hexdigest()}'

    return hash


def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    shared_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o : (d1[o], d2[o]) for o in shared_keys if d1[o] != d2[o]}
    same = set(o for o in shared_keys if d1[o] == d2[o])
    return added, removed, modified, same


d1_keys = set(sp1().keys())
d2_keys = set(sp2().keys())
added, removed, modified, same = dict_compare(sp1(), sp2())

missing = list(sorted(d1_keys - d2_keys))


def copy_files():
    os.chdir(path2)
    os.makedirs("../sprite_diffs", exist_ok=True)
    os.makedirs("../sprite_diffs/Modified", exist_ok=True)
    os.makedirs("../sprite_diffs/New", exist_ok=True)
    os.makedirs("../sprite_diffs/Removed", exist_ok=True)
    for files_to_copy in set(modified.keys()):
        try:
            shutil.copy(f"{os.getcwd()}/{files_to_copy}", "../sprite_diffs/Modified")
        except:
            pass

    for files_to_copy in d1_keys.symmetric_difference(d2_keys):
        try:
            shutil.copy(f"{os.getcwd()}/{files_to_copy}", "../sprite_diffs/New")
        except:
            pass

    for files_to_copy in missing:
        try:
            shutil.copy(f"{path1}/{files_to_copy}", f"{path2}../sprite_diffs/Removed")
        except:
            pass


copy_files()
