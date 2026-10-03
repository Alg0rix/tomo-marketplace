# Submit a community plugin

Keep executable code in your own GitHub repository. Add a listing at
`plugins/<id>.json` using this format:

```json
{
  "id": "my_plugin",
  "name": "My Plugin",
  "description": "What users can do with it.",
  "version": "0.1.0",
  "sdk_version": 1,
  "author": "your-github-name",
  "source": {
    "type": "git",
    "url": "https://github.com/your-name/tomo-my-plugin.git",
    "ref": "v0.1.0",
    "subdirectory": ""
  }
}
```

Use a release tag or commit when possible. The source directory must contain
`tomo-plugin.json` and `plugin.py`. Its id, version, and SDK version must match the
listing. Supply a README with setup, dependencies, API/tools, data storage,
cleanup, and permissions. Plugins run trusted Python with server privileges.

Run `python -m pip install -r requirements-dev.txt`,
`python scripts/build_catalog.py`, and `python scripts/validate.py`. Commit both
the listing and generated marketplace.json. CI validates metadata only and never
runs submitted plugins. Maintainers review source and documentation separately.

Official plugins live in Alg0rix/tomo-plugins and do not submit to this catalog.
