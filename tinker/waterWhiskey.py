def tsp_to_oz(tsp):
  oz = 0.166667
  return tsp * oz

def calc_new_abv(tsp_water, oz_whiskey, init_abv):
	oz_water = tsp_to_oz(tsp_water)
	oz_alc = oz_whiskey * (init_abv / 100)
	new_water_total = oz_water + (oz_whiskey - oz_alc)
	pct_water = new_water_total / (oz_whiskey + oz_water)
	return round(((1 - pct_water) * 100), 2)


amt_glass_oz = 1.5
pct_alc = 100
tsp_water = .5
new_abv = calc_new_abv(tsp_water, amt_glass_oz, pct_alc)
new_proof = new_abv * 2
print(f'amt_glass_oz = {amt_glass_oz}, abv/proof to start = {pct_alc}/{(pct_alc * 2)}. tsp_water = {tsp_water}, new abv/proof = {new_abv}/{new_proof}')




