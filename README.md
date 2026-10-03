# Tomo Community Marketplace

Submit community plugin listings here. Plugin source stays in its author's
repository; this repository contains reviewed discovery metadata.

Tomo loads this catalog independently from the official catalog at
[Alg0rix/tomo-plugins](https://github.com/Alg0rix/tomo-plugins). Official plugins
do not need to submit here. Authors can also distribute plugins directly without
joining any marketplace.

## Submit a plugin

1. Publish a public GitHub repository with a Tomo SDK v1 plugin.
2. Fork this repository and add `plugins/<plugin-id>.json`.
3. Install `requirements-dev.txt`, run `python scripts/build_catalog.py`, then
   `python scripts/validate.py`.
4. Open a pull request with usage documentation, dependencies, permissions,
   storage behavior, and validation results.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the entry format. Maintainers review
listings before merging. A listing does not imply sandboxing or a security audit.
Refreshing this catalog never installs, updates, or executes plugin code.

## Use in Tomo

Tomo Community is a default source in `/settings/marketplaces`. Refresh it, then
browse Plugins. CLI: `tomo plugins install plugin_id@tomo-community`.

The published manifest is
[marketplace.json](https://raw.githubusercontent.com/Alg0rix/tomo-marketplace/main/marketplace.json).
