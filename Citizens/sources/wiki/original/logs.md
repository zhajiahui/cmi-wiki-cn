This page explains some information about posting server logs to get support.

## How To Post Logs

- Go into your server files, find the `logs` folder, and inside of that find `latest.log`.
- That's a simple text file, so just open it in any text editor.
- Copy the contents of the file.
- Go to [The Server Log Pastebin](https://paste.denizenscript.com/New/Log) and paste in the copied data.
- If on Pastebin, click "Create New Paste". If on /Haste, click "Server Log" then "Submit".
- Then, copy the URL of the page you're now on, and paste that URL back into the channel or issue where you were asked to post logs.
- If you're on the Denizen&Citizens Discord, you can use the `!checklog` command with the link you gave to automatically check the log for common issues (eg outdated plugin versions, etc) which will look like:

[![](https://wiki.citizensnpcs.co/images/0/09/CheckLog.png)](https://wiki.citizensnpcs.co/File:CheckLog.png)

## Why Post Logs?

We often ask people to post their logs when a user reports an issue that is likely to related to a common issue, such as an outdated plugin or server version, or incompatibility with another plugin (for example, if NPC combat isn't working, a log will show things like WorldGuard on the server, which will often be the reason for combat is blocked).

## What's in a log?

A complete startup log contains the following pieces of information:

- Full server version (in the above example, that's `CraftBukkit version git-Spigot-1a3504a-e7700ab (MC: 1.13.2)`)
- Full versions of all installed plugins (in the above example we see `Citizens v2.0.26-SNAPSHOT (build 1822)` and a few more)
  - The Meta bot we have on our Discord will compare the server version and some plugin versions to the known current version available for download, and report how far behind (if at all) a version is.
- Any error messages. It's not uncommon to find a bunch of plugins failing to load or producing error messages the first time you check your logs, if you don't review them often.
  - Even when an error doesn't seem like it's going to be relevant to a problem, it often is. As a general rule of thumb, if you have ANY errors in your logs, those are absolute first priority to fix.
- A whole lot of minor loading data that usually doesn't matter, but in those rare cases when they do, are incredibly helpful to diagnosing related issues.
- Commands you've entered. When your issue relates to usage of a command, having the text of that command exactly as you typed it is often helpful (often, issues arise from just typos or slight formatting mistakes!).

## Should I Edit Or Trim The Logs?

No, never edit or trim your logs. Always provide the full contents of `latest.log`, untouched.

If it's full of unrelated data (like hours of day-to-day minecraft server activity logs), restart your server (and join it and replicate the issue) before copying the logs.

Generally the startup logs (and basic issue replication where relevant) are the most important part.

## Do Logs Contain Private Information?

We sometimes see users worried that their logs contain private information they might not want to post.

Generally speaking: **no, logs do not contain private information**.

If you're copying logs from a live&active public server, you might have player IPs and/or chat messages in the logs, which you might prefer to be better-safe-than-sorry with (though of course: IPs are generally considered public data, and hopefully players aren't sharing secrets on a minecraft server). If this applies to you, the log pastebin linked above has an option to automatically filter out IPs or Chat when you go to make the paste. Alternately, you could [Start a Local Test Server](https://guide.denizenscript.com/guides/first-steps/local-test-server.html) or restart your server to reset the latest.log to just the startup information and any quick testing you do to demonstrate a problem (if needed) without random players joining. (If you do either of these latter two options, please make sure you replicate the issue before posting the log).
