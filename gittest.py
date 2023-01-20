import os
import sys

def check_reeboot():
	return os.path.exist('/run/rebot-required')

def main():
	if check_reboot():
		print('Pending reboot.')
		sys.exit(1)
	print('Everything is ok.')
	sys.exit(0)


main()
