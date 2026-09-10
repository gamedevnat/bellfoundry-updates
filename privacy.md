# Privacy policy — Bellfoundry browser extension

*Last updated: 10 September 2026. Applies to the extension "Bellfoundry —
Claude session watcher" and to no other software.*

## The short version

The extension sends what it reads to one address: `http://127.0.0.1` on the
same computer it is running on. That address is your own machine and cannot
be reached from anywhere else. Nothing is sent to us, because there is no
"us" to send it to — Bellfoundry has no server, no account and no analytics.

We do not collect, store, transmit, sell or share any of your data, because
none of it ever reaches us.

## What the extension reads

On `claude.ai` pages only, it reads the data the page is already fetching for
itself, and takes from it:

- **Session and conversation identifiers** — the opaque ids claude.ai uses,
  such as `session_01ABC…` or a conversation UUID.
- **Titles** — the name shown on a session row or chat, truncated to 80
  characters.
- **State** — whether something is working, waiting for you, or finished.
- **Timing** — when a session was last active, and when a chat's response
  stream opened and closed.
- **Which model answered** — for example `claude-opus-5`.
- **The account label** — the display name or email the page shows for the
  signed-in account, used only to label which of your accounts a row came
  from when you use more than one.
- **Token counts** — only if claude.ai happens to expose them to the page. It
  usually does not, and then nothing of the sort is read.

## What it never reads

**Message content.** Not your prompts, not Claude's replies, not code, not
file names, not diffs, not attachments. The extension does not extract them
and does not transmit them.

This matters more here than for the rest of Bellfoundry, because a content
script running on claude.ai *could* see all of it. The limit is a deliberate
one, and the source is short enough to check: `extension/src/inject.js` and
`extension/src/reader.js`, published at
<https://github.com/gamedevnat/bellfoundry>.

## Where it goes

To `http://127.0.0.1:<port>/event`, where the Bellfoundry desktop application
is listening. `127.0.0.1` is the loopback address: traffic to it never leaves
your computer and cannot be routed to another machine.

The extension makes no other network request. It contacts no analytics
service, no error reporter, no update server and no site of ours.

If Bellfoundry is not running, the request fails and the extension does
nothing about it. There is no queue, no retry to elsewhere, and no fallback
destination.

## What is stored, and where

In your browser's own extension storage, on your computer:

- **Settings** — the port number and whether the extension is enabled.
- **The last state it reported** for each session, so that reloading a tab
  does not re-announce chats that have not changed.

That is all, and it never leaves the browser. Removing the extension removes
it. Anything the desktop application keeps is covered by Bellfoundry's own
privacy documentation and is likewise local to your machine.

## Permissions, and why each exists

| Permission | Why |
| --- | --- |
| `https://claude.ai/*` | The only site the extension reads. It cannot see any other site. |
| `http://127.0.0.1/*` | To deliver events to the Bellfoundry application on your own computer. |
| `storage` | To remember your port setting and the last reported state. |
| `alarms` | To re-check periodically when a page has been open a long time. |

## Children

Bellfoundry is a developer tool and is not directed at children. It does not
knowingly collect information from anyone, of any age, because it does not
collect information.

## Changes

If this policy ever changes, the updated version will be published at this
address and the date at the top will change. Because the extension transmits
nothing to us, no change here can retroactively affect data we hold; we hold
none.

## Contact

Open an issue at <https://github.com/gamedevnat/bellfoundry/issues>.

---

*Bellfoundry is not affiliated with or endorsed by Anthropic.*
