Documentation

# Troubleshooting

Common issues and solutions for integrating bStats. If you're still stuck after reading
this guide, reach out on [Discord](https://discord.gg/qTXtXuf) or open an issue on GitHub.

## How long until data appears?

Understanding the timeline for when your data becomes visible on bStats:

### Initial delay

After the server starts, the first data is sent after a random **3-6 minute delay**.

### Publication schedule

The bStats website publishes updates at **hh:00 and hh:30** (every half hour). Once data is sent, it may take **up to 30 minutes** to become visible on your plugin's dashboard.

### Total time

In total, expect to wait **3-36 minutes** after server startup before
seeing your first data point on the dashboard.

## Data not showing up

If you've waited the expected time and still don't see any data, check these common
issues:

### Enable debug logging

Enable debug logging in the bStats configuration file by setting `logFailedRequests`, `logSentData`,
and `logResponseStatusText` to `true`.

### Ratelimits

Plugins are limited to sending data once per 30-minute interval (hh:00 and
hh:30). When you have debug logging enabled and see `429 Too Many Requests` in the logs, it means your plugin is being ratelimited. **This is completely normal** and can be safely ignored.

### Metrics class not instantiated

Verify that you're actually creating an instance of the `Metrics` class in
your plugin's initialization code. Simply including the class file isn't enough.
You must instantiate it with your plugin ID.

### Wrong plugin ID

Double-check that the plugin ID in your code matches the ID shown on your
plugin's dashboard.

### Metrics disabled in config

Server owners can disable bStats by editing. Check that `enabled` is set to `true`.

### Firewall or network blocking

Ensure that your server can reach the bStats servers. A common issue is PiHole
or other ad-blocking software blocking the connection.

## Still having issues?

If you've checked everything above and still can't see your data, please reach out
for help:

[Join Discord](https://discord.gg/qTXtXuf) [Open GitHub Issue](https://github.com/Bastian/bStats/issues)
