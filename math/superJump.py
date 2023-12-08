from mcpi.minecraft import Minecraft
mc = Minecraft.create()

positon = mc.player.getTilePos()
x = positon.x
y = positon.y
z = positon.z

x = x + 5
mc.player.setTilePos(x, y, z)