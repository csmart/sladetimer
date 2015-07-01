#!/bin/env python

from pprint import pprint

import datetime
import time
import yaml
import sys

cache = 'cache.yaml'



class d(object):
	epoch = int(time.time())
	t = datetime.datetime.fromtimestamp(epoch)

class index(object):
	db = { 'time' : { d.t.year : { d.t.month : { d.t.day : [] }}}}
	year = { d.t.year : { d.t.month : { d.t.day : [] }}}
	month = { d.t.month : { d.t.day : [] }}
	day = { d.t.day : [] }

def main(args):

	try:
		with open(cache, 'r') as f:
			data = yaml.load(f)

	except IOError:
		with open(cache, 'w') as f:
			data = index.db
			init_db = data
			yaml.dump(init_db, f, default_flow_style=False)
	if len(args) < 2:
		try:
			scope = data['time'][d.t.year][d.t.month][d.t.day]
		except KeyError as e:
			if e.args[0] == d.t.day:
				data['time'][d.t.year][d.t.month].update(index.day)

			elif e.args[0] == d.t.month:
				data['time'][d.t.year].update(index.month)

			elif e.args[0] == d.t.year:
				data['time'].update(index.year)

			scope = data['time'][d.t.year][d.t.month][d.t.day]

		finally:
			if len(scope) is 0:
				scope.append([d.epoch])
			else:
				print('scope: %s' %(scope))
			
				if len(scope[-1]) == 1:
					scope[-1].append(d.epoch)
					#for i in scope[-1]:
					#	print(i)
					#	print('here')
					#	scope[-1].append(d.epoch)
				else:
					scope.append([d.epoch])
			
			with open(cache, 'w') as f:
				yaml.dump(data, f)
		
	pprint(data)


if __name__ == '__main__':
	sys.exit(main(sys.argv))
