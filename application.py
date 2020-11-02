import click
from kindle_news_assistant.model.train import start_training
from kindle_news_assistant.model.test import start_test

@click.command()
@click.option('--train', is_flag=True, help="Train the assistant model.")
@click.option('--test', is_flag=True, help="Preview a list compiled by the assistant model.")
def run(train: bool, test: bool):
  if train:
    start_training()
  elif test:
    start_test()
  else:
    print("main")

if __name__ == '__main__':
  # pylint: disable=no-value-for-parameter
  run()