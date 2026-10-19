Documentation

# For server owners

Understanding bStats metrics collection, what data is shared, and how to manage your
preferences.

## bStats is a free, open source hobby project

bStats is run as a passion project. It's completely [open source](https://github.com/Bastian/bStats) and free to use. There's no company behind it, no paid plans, and no intention
to monetize your data.

## What is bStats?

bStats is a free metrics service for Minecraft and Hytale server plugins. When plugin authors
integrate bStats into their plugins, they can see how many servers use their work,
which server versions are popular, and how their plugins are configured.

As a server owner, your server automatically shares basic usage statistics with
plugin authors when you install plugins that use bStats. This happens in the
background and doesn't affect your server's performance. The data collected is
anonymous and not linked to your individual server.

## What data is collected?

bStats collects only non-personal data and shows them as aggregated metrics. We
never collect player names, chat logs, world data, or any personally identifiable
information.

### Example of collected data

- • Number of players currently online
- • Server software and version (e.g., Spigot 1.20.1)
- • Java version
- • Operating system type
- • Server location (country only)

### Plugin-specific data

Some plugins collect custom metrics about how you use their features. For
example, a plugin might track which configuration options are most popular.
This helps authors understand which features to prioritize.

All collected data is public and can be viewed on each plugin's dashboard.

## Why keep metrics enabled?

bStats helps the Minecraft and Hytale server community in several ways:

### Supports the community

Many plugin authors maintain their plugins for free. Metrics provide a
tangible way to show appreciation and validate the time they invest in the
community.

### Guides development priorities

Authors can see which server versions are most popular, which features
are heavily used, and where to focus their development efforts. This leads
to better plugins for everyone.

### Privacy-first and community-run

bStats is open source and run by volunteers, not a company. It collects only
minimal, anonymous data, and the code is public so you can verify exactly
what's shared.

### Motivates developers

Seeing real usage statistics encourages plugin authors to continue
maintaining and improving their plugins. It's incredibly motivating to see
other people actually using your work.

## How to disable bStats

We respect your choice if you prefer not to share metrics. You can disable bStats
globally for all plugins on your server:

### Step 1: Locate the config file

Navigate to your server directory and find the bStats configuration file
usually at:

`/plugins/bStats/config.yml` Location might differ depending on server platform.

### Step 2: Edit the config

Open the file with any text editor and change `enabled` to `false`:

```
enabled: false
```

## Frequently asked questions

### Does bStats affect server performance?

No. bStats sends data asynchronously in the background and has negligible
performance impact. Data is sent once every 30 minutes, taking only a few
milliseconds.

### Can I view what data my server sends?

Yes. All bStats data is public. Visit any plugin's page on bStats to see
exactly what metrics are being collected and view the charts showing
aggregated data from all servers.

You can also enable debug logging in the bStats config file to see the
raw data your server sends.

### Is bStats GDPR compliant?

Yes. bStats doesn't collect any personally identifiable information. IP
addresses are used only for rate limiting and are never linked to any metrics
data. All data is anonymous and aggregated.

### Who can see my server's data?

No one can identify your specific server. All data is aggregated and displayed
as charts showing overall trends.

### Why do I see a bStats folder in my plugins directory?

The `/plugins/bStats/` folder contains the shared configuration file used by all plugins. This allows
you to enable or disable metrics globally instead of configuring each plugin individually.

## Learn more

If you have questions or concerns about bStats, we're here to help:

[View documentation](../docs) [Privacy policy](../privacy-policy) [Join Discord](https://discord.gg/qTXtXuf)
