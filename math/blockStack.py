from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 7
y = 1
z = 5
blockType = 103 # melon
mc.setBlock(x, y, z, blockType) 

y = y + 1
mc.setBlock(x, y, z, blockType)