import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
data_dir = base_dir + '/data'
model_dir = data_dir + '/models'
model_name = 'model.ckpt'
model_path = model_dir + '/' + model_name
