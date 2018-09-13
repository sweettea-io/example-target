import os
from src.definitions import model_path, model_dir
from time import sleep


def train():
  print('Training...')

  os.makedirs(model_dir, exist_ok=True)
  with open(model_path, 'w+') as f:
    f.write('model filler')

  sleep(1)

  print('Done training.')


def predict(data):
  return 'prediction'
