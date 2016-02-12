#!/usr/bin/env python3
# -*- coding: utf-8 -*-


for i in range(110,120):
    query = "INSERT INTO glpi.glpi_phones (name, phonemodels_id, manufacturers_id, users_id, states_id) VALUES ('967457%s', '2', '16', '14', '2');"%i
    print(query)
