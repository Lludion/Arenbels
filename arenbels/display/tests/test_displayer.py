
from arenbels.game import game
from arenbels.display import Displayer
from arenbels.display.engine import SpriteNode

fen = Displayer()

g = game.Game()
g.world.from_grid("arenbels/game/data/2.arb")

fen.link_world(g.world)
fen.init_camera()
fen.init_images()

sn = SpriteNode()
sn.create_sps("castle")
fen.cam.aff([sn],1)
fen.flip()

##

fen.display_world()

for region in fen.world.regions:
    print(region.name)
    print(region.__class__.__name__)