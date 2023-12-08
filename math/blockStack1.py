from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 0
y = 1
z = 5
blockType = 103 # melon
mc.setBlock(x, y, z, blockType) 
mc.setBlock(x, y + 1, z, blockType) # operator in argument
