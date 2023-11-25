from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 10.0
y = 110.0
z = 12.0

#different from setTilePos -> this is more precise
mc.player.setPos(x, y, z)