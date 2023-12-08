from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
blockType = 1 

mc.player.setTilePos(x, y + 10, z)
mc.setBlock(x, y + 9, z, blockType)