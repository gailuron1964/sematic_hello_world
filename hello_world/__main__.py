import argparse

from .pipeline import pipeline

if __name__ == "__main__":
  parser = argparse.ArgumentParser("Hello World")
  parser.add_argument("--name", type=str, required=True)

  args = parser.parse_args()

  # Starts the web app if needed
  # start()

  pipeline(args.name).resolve()
