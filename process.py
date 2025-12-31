import cv2
import os


#- things to add to desmos are in the readme.md
# - put ur file paths :)
IMAGE_PATH = r"directory with ur image (might work with multiple)"
OUTPUT_PATH = r"directory that the RGB outputs are going into"
GRID_SIZE = 64  #- probably can work up to 100



os.makedirs(OUTPUT_PATH, exist_ok=True)
#- cv2 magic
for fname in os.listdir(IMAGE_PATH):
    img = cv2.imread(os.path.join(IMAGE_PATH, fname))
    if img is None:
        continue

    img = cv2.resize(img, (GRID_SIZE, GRID_SIZE), interpolation=cv2.INTER_AREA)
#-rgb pointss
    points1 = []
    points2 = []
    points3 = []

    txt_name = os.path.splitext(fname)[0] + ".txt"
    txt_path = os.path.join(OUTPUT_PATH, txt_name)
#-colours and write file
    with open(txt_path, "w") as f:
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                b, g, r = img[x, y]
                points1.append(
                    int(r)
                )
                points2.append(
                    int(g)
                )
                points3.append(
                    int(b)
                )
        f.write(f"R={points1} \n G={points2} \n B={points3}")



