#!/usr/bin/python3
import config
import subprocess
import os
import shutil
import time

print(subprocess.Popen(['git', 'pull'], stdout=subprocess.PIPE, cwd=config.src_dir).communicate())

curtime = time.time()

def dirExists(path):
	if os.path.isdir(path):
		return True
	else:
		return False

for provider in config.providers_list:
	mtime = os.path.getmtime(config.src_dir + provider)
	age = curtime - mtime
	ddir = config.dest_dir + provider
	print(age)
	if age < 86400*4:
		print('ddir age - ', curtime - os.path.getctime(ddir))
		if dirExists(ddir) == True:
			if curtime - os.path.getctime(ddir) > 86400:
				shutil.rmtree(ddir)
				shutil.copytree(config.src_dir + provider, ddir)
