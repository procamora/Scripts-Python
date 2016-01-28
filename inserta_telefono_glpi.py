


for i in range(110,120):
	query = "INSERT INTO glpi.glpi_phones (name, phonemodels_id, manufacturers_id, users_id, states_id) VALUES ('967457%s', '23', '26', '11', '1');"%i
	print query
