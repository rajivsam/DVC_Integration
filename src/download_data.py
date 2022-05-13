import requests, zipfile, io, os
r = requests.get('https://files.grouplens.org/datasets/movielens/ml-100k.zip', verify=False)
z = zipfile.ZipFile(io.BytesIO(r.content))
path_parent = os.path.dirname(os.getcwd())
data_dir = path_parent + '/data'
z.extractall(data_dir)
