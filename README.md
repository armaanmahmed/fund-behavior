# Fund Behavior: 13F Holdings Analysis

Analyze institutional investor holdings in AI stocks using SEC Form 13F filings.

## Overview

This project parses SEC Form 13F bulk data to examine how hedge funds and institutional investors are positioned in AI-related equities. The analysis enables questions such as:

- Which AI stocks have the largest institutional ownership?
- Which investment managers hold the most AI stock by value?

## Current Capabilities

The `analysis.ipynb` notebook provides:

- **Data loading**: Reads quarterly SEC 13F bulk TSV files (INFOTABLE, COVERPAGE, SUBMISSION)
- **AI stock matching**: Maps issuer names to a curated list of AI-related tickers
- **Aggregation by stock**: Ranks AI stocks by total institutional investment value
- **Aggregation by manager**: Identifies funds with the largest AI holdings

## Setup

### Prerequisites

- Python 3.11+, although Python 3.13 is recommended
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

```bash
# Install uv if needed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone and install dependencies
git clone https://github.com/armaanmahmed/fund-behavior.git
uv sync
```

## Usage

```bash
# Start Jupyter
uv run jupyter lab
```

Then open `analysis.ipynb` and run the cells.

### Data

The project uses SEC 13F bulk data in TSV format. Each quarter directory (e.g., `data/raw/2023q4/`) contains:

- `INFOTABLE.tsv` — Holdings data (issuer name, CUSIP, value, shares)
- `COVERPAGE.tsv` — Filer metadata (manager name, report date)
- `SUBMISSION.tsv` — Filing metadata (submission type, filing date)

**Data sources:**
- [SEC 13F Data Sets](https://www.sec.gov/data-research/sec-markets-data/form-13f-data-sets)

## Project Structure

```
fund-behavior/
├── analysis.ipynb      # Main analysis notebook
├── ai_stocks.py        # AI stock ticker definitions
├── data/
│   ├── raw/            # 13F bulk data by quarter
│   └── reference/      # Ticker lookup files
└── pyproject.toml      # Dependencies
```

## AI Stock Universe

The `ai_stocks.py` module defines the AI stock universe across categories:

- **Semiconductors**: NVDA, AMD, AVGO, TSM, ASML, MU, INTC
- **Cloud infrastructure**: MSFT, GOOGL, AMZN, ORCL
- **Enterprise platforms**: PLTR, AI
- **Consumer applications**: META, DUOL, ADBE
- **Hardware infrastructure**: ANET, DELL, SMCI, AMAT, LRCX, KLAC, QCOM
- **Robotics/autonomy**: TSLA

## Additional Resources

- [SEC Form 13F FAQ](https://www.sec.gov/rules-regulations/staff-guidance/division-investment-management-frequently-asked-questions/frequently-asked-questions-about-form-13f)
- [SEC Company Tickers](https://www.sec.gov/files/company_tickers.json)
- The README for the Form 13F datasets (included in `data/reference/`)

## License

MIT