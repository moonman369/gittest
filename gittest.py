import os
import sys

#def check_reboot():
	return os.path.exists('/run/reboot-required')

def main():
	if check_reboot():
		print('Pending reboot.')
		sys.exit(1)
	print('Everything is ok.')
	sys.exit(0)


main()
