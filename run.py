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
	age = os.path.getmtime(config.src_dir + provider)
	ddir = config.dest_dir + provider
	if curtime - age < 86400:
		if dirExists(ddir) == True:
			shutil.rmtree(ddir)
		shutil.copytree(config.src_dir + provider, ddir)
