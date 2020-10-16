import os
import click
from bs4 import BeautifulSoup
from kindle_news_assistant.agent import Agent
from kindle_news_assistant.history import History
from joblib import load

dirname = os.path.dirname(__file__)
relative_path = "../../userdata/model.joblib"
absolute_path = os.path.join(dirname, relative_path)

def start_test():
  """Start the assistant model's test
  """
  history = History()
  agent = Agent(history)

  if not os.path.isfile(absolute_path): # model doesn't exist
    raise LookupError()

  clf = load(absolute_path)
  entries = agent.batch(False, clf)

  for entry in entries:
    print(entry.title)