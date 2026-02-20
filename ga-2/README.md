# TDS GA-2 Assignment Solutions

## Question 2: Git History Rewriting
**Task:** Purge a sensitive `.env` file from the entire Git history and implement best practices.
- **Identify:** Found `.env` added in commit `746a240`.
- **Purge:** Executed `git filter-branch --index-filter 'git rm --cached --ignore-unmatch .env' --prune-empty --all`.
- **Cleanup:** Removed backup refs (`refs/original/`) and ran `git gc --prune=now --aggressive`.
- **Security:** Added `.gitignore` to block `.env` and created `.env.example` with placeholders.

## Question 3: Git History Exploration
**Task:** Identify the 7-character short hash of the parent of the commit that set `timeout` to `90` in `config.json`.
- **Search:** Found the change in commit `c015716` ("Update timeout settings").
- **Parent:** Checked parent using `git log -1 --format=%P c015716`.
- **Answer:** The parent commit short hash is **`06d25d2`**.

## Question 5: Static API (StaticShop)
**Task:** Create a static JSON product catalog hosted on GitHub Pages.
- **Metadata:** Included email and version `3c99b79e`.
- **Products:** Populated 17 products with IDs, categories, and pricing.
- **Aggregations:** Computed category-level stats.
  - **Sports:** Count: 1, Inventory Value: **29180.97**.
- **URL:** [https://24ds1000061.github.io/TDS/ga-2/q-5/products.json](https://24ds1000061.github.io/TDS/ga-2/q-5/products.json)
