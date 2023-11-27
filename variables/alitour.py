from mcpi.minecraft import Minecraft

serverAddress="192.168.68.132" # change to your minecraft server
pythonApiPort=4711 #default port for RaspberryJuice plugin is 4711, it could be changed in plugins\RaspberryJuice\config.yml
playerName="Bunnibub" # change to your username

mc = Minecraft.create(serverAddress,pythonApiPort)

import time #import is like the "#include" in C++

#set x, y, z variable to your coords
x = 10
y = 110
z = 12

#change the player's position
mc.player.setTilePos(x, y, z)

# Wait 10 seconds
time.sleep(10)

# Do everything again, but with different coords
x = 100
y = 64
z = 200

#change the player's position
mc.player.setTilePos(x, y, z)

x
