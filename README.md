# desmos-pixel-art
Takes an image (maybe multiple) from a directory and gets the colours exported in GBR, which can be amended in desmos

# What to copy into desmos
w=64
h=64
N=\left[1...,wh\right]
X=\operatorname{mod}\left(N-1,w\right)
Y=\operatorname{floor}\left(\frac{N-1}{w}\right)
\left(X,\ -Y\right)
G= (R values)
B= (B values)
R= (G values)
c= rgb(B,G,R)

hold left click on the colour option of (x,-y) and change to c.

