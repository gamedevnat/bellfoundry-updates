# bellfoundry-updates

Two small public files for [Bellfoundry](https://connectioneering.itch.io/bellfoundry),
whose own repository is private.

| File | Read by | Why it lives here |
| --- | --- | --- |
| `version.json` | the app's **Check for updates** button | A private repository cannot serve a file to an app in the field. |
| `privacy.html` | the Chrome Web Store reviewer, and anyone else | The store requires a privacy policy at a URL anyone can open. |

Published by GitHub Pages, **Deploy from a branch → `main` → `/ (root)`**, so
every file here is served exactly as it is committed. `.nojekyll` is present
because these are static files and Jekyll has no business processing them.

`version.json` is served two ways and the app tries both:

| | URL |
| --- | --- |
| Pages, tried first | `https://gamedevnat.github.io/bellfoundry-updates/version.json` |
| Raw, the fallback | `https://raw.githubusercontent.com/gamedevnat/bellfoundry-updates/main/version.json` |

The raw URL works with Pages switched off entirely, so Pages is the nicer of
two paths rather than a load-bearing one.

Nothing here is downloaded automatically. `version.json` is fetched only when
somebody presses the button, and all it does is name a version and a store
page to open by hand.

## Publishing a new version

Normally written by the `publish-version` workflow in the main repository,
which needs `UPDATES_DEPLOY_KEY` or `UPDATES_TOKEN` set there as a secret.
Until one exists the workflow warns and skips, and `version.json` has to be
edited here by hand.

**Only ever name a version people can actually download.** A `version.json`
ahead of the store tells everybody an update exists and then sends them to a
page that does not have it.

## Changing the privacy policy

`privacy.html` is generated. The source is `docs/privacy-extension.md` in the
main repository, where it sits with the code it describes. Edit it there and
regenerate — the header comment in `privacy.html` has the command.
