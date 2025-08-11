import zipfile

with zipfile.ZipFile('achive.zip',mode='w',compression=zipfile.ZIP_DEFLATED) as file:
	file.write('report.txt')
	file.write('summary.txt')
