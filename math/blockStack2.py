from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = -2
y = 1
z = 5
blockType = 103 # melon
up = 1 # 1 block above
mc.setBlock(x, y, z, blockType) 
mc.setBlock(x, y + up, z, blockType) # operator AND variable in argument