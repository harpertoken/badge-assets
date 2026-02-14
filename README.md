# Badge Assets

This repository automatically generates light and dark mode badges
from a single source icon using Python and GitHub Actions.

## How it works

- `assets/icon.png` is the source image
- GitHub Actions runs on push, release, or manual trigger
- Light and dark badges are regenerated automatically

## Usage (GitHub Markdown)

```md
![Badge](assets/badge-light.png#gh-light-mode-only)
![Badge](assets/badge-dark.png#gh-dark-mode-only)
```

GitHub will automatically switch based on the viewer's theme.

## Files

* `scripts/generate_badges.py` – badge generator
* `.github/workflows/generate-badges.yml` – automation
* `assets/` – icon + generated badges
