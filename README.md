# Kinde News Assistant

More information coming soon...

## Getting Started

Install [calibre](https://calibre-ebook.com) and [install the command line tools](https://manual.calibre-ebook.com/generated/en/cli-index.html).

Set up virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel # Update build tools
yarn install # or npm install
```

If dependency installation fails, the folowing guides may help build dependencies from source:

- [`scikit-learn`](https://scikit-learn.org/stable/developers/advanced_installation.html#platform-specific-instructions)
- [`newspaper3k`](https://newspaper.readthedocs.io/en/latest/index.html#get-it-now)

## Train the model

```bash
yarn start --train
```

## Test the model

```bash
yarn start --test
```
