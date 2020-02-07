


from arenbels.game import game,player,building,city,ai,region
from arenbels.display import graphics

g = game.Game()

burgundy = region.Region()
burgundy.name = "Burgundy"
sweden = region.Tundra()
sweden.name = "Sweden"
alps = region.Icy()
alps.name = "Alps"
nordsee = region.Oceanic()
nordsee.name = "Nordsee"

pa = ai.AI("Anna")
pa.female = True
pa.state.name = "France"

dijon = city.City("Dijon")
dijon.pop = 20
dijon.bdg += [building.House(),building.Bakery(),building.Barn()]
dijon.set_region(burgundy)

lyon = city.City("Lyon")
lyon.pop = 120
lyon.bdg += [building.House()]*20 + [building.Quarter(),building.Fountain(),building.Chapel()]
lyon.set_region(burgundy)

lens = city.City("Lens")
lens.set_region(nordsee)

chamonix = city.City("Chamonix")
chamonix.bdg += [building.IceHarvest()]
chamonix.set_region(alps)

pa.state.add_cities(dijon,lyon,chamonix,lens)

pb = ai.AI("Bob")
pb.state.name = "Sweden"

lulea = city.City("Lulea")
lulea.bdg += [building.IceHarvest(),building.IceHarvestResaler()]
lulea.set_region(sweden)

stock = city.City("Stockholm")
stock.bdg += [building.House()]*20 + [building.Restaurant(),building.Fields(),building.Fields(),building.Fields(),building.Chapel(),building.IceHarvestResaler(),building.Quarter(),]
stock.oldPopBdg = 200
stock.pop = 220
stock.set_region(sweden)

aalborg = city.City("Aalborg")
aalborg.set_region(nordsee)
bremen = city.City("Bremen")
bremen.set_region(nordsee)

pb.state.treasure = 0
pb.state.add_cities(stock,lulea,bremen,aalborg)

pc = ai.AI("Charles")
pc.state.name = "Switzerland"

basel = city.City("Basel")
basel.pop = 50
basel.bdg += [building.House(),building.House(),building.House(),building.IceHarvest(),building.IceHarvestResaler(),building.Restaurant()]
basel.set_region(alps)

pc.state.add_cities(basel)


g.players = [pa,pb,pc]


g.play(150)

graphics.city(g,spec=1)

graphics.state(g,spec=3)

#To play until turn n° N, type g.play(N)
