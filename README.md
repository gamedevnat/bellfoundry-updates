# bellfoundry-updates

Two small public files for [Bellfoundry](https://connectioneering.itch.io/bellfoundry),
whose own repository is private.

| File | Read by | Why it lives here |
| --- | --- | --- |
| `version.json` | the app's **Check for updates** button | A private repository cannot serve a file to an app in the field. |
| `privacy.md` | the Chrome Web Store reviewer, and anyone else | The store requires a privacy policy at a URL anyone can open. |

`site/version.json` is the same file again, for GitHub Pages. The app tries
the Pages URL first — it survives a corporate proxy that dislikes
`raw.githubusercontent` — and falls back to the raw URL, which works with no
Pages setup at all.

Nothing here is downloaded automatically. `version.json` is fetched only when
somebody presses the button, and all it does is name a version and a store
page to open by hand.

## Publishing

Normally written by the `publish-version` workflow in the main repository,
which needs `UPDATES_DEPLOY_KEY` or `UPDATES_TOKEN` set there as a secret.
Until one exists the workflow warns and skips, and this file has to be
updated by hand.

**Only ever name a version that people can actually download.** A
`version.json` ahead of the store tells everyone an update exists and then
sends them to a page that does not have it.
