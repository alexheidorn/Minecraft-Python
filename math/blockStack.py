from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 7
y = 1
z = 5
blockType = 103 # melon
mc.setBlock(x, y, z, blockType) 

y = y + 1
mc.setBlock(x, y, z, blockType)

# make 4 blocks
x = 9
y = 0
blockType = 103 # melon
for i in range(4):
    y = y + 1
    mc.setBlock(x, y, z, blockType)