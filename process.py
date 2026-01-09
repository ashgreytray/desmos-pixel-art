import cv2
import os
import easygui


#- select directory with image
img_path = easygui.diropenbox(
    msg="Select Folder With Images",
    title="Folder")
directory = './desmos_result/'
output_path = os.path.join(directory)
grid = 64  #- probably can work up to 100


os.makedirs(output_path, exist_ok=True)
#- cv2 magic
for fname in os.listdir(img_path):
    img = cv2.imread(os.path.join(img_path, fname))
    if img is None:
        continue

    img = cv2.resize(img, (grid, grid), interpolation=cv2.INTER_AREA)
#-rgb pointss
    points1 = []
    points2 = []
    points3 = []

    txt_name = os.path.splitext(fname)[0] + ".txt"
    txt_path = os.path.join(output_path, txt_name)
#-colours and write file
    with open(txt_path, "w") as f:
        for x in range(grid):
            for y in range(grid):
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
        print("All Done")





