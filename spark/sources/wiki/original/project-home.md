## About

spark is a performance profiler, made up of three main components.

### Profiler

spark can help to diagnose performance problems and bottlenecks with its built-in profiler.

### Memory Inspection

spark can produce full heap dumps, present a summary of what’s using the most memory, and monitor GC activity.

### Health Reporting

spark monitors and reports a number of key metrics which are useful for tracking performance over time.

More information about spark can be found on [GitHub](https://github.com/lucko/spark), or you can come chat with us on [Discord](https://discord.gg/PAGT2fu).

## Viewer

This website is also an online viewer for spark data.

In order to use it:

1. Generate a [profile](https://spark.lucko.me/docs/Command-Usage#spark-profiler) or [heap summary](https://spark.lucko.me/docs/Command-Usage#spark-heapsummary) using the appropriate spark commands.
2. After the data has been uploaded, click the link to open the viewer.

You can also generate or export a `.sparkprofile` or `.sparkheap` file and open it by dragging it into the box below.

Drag & drop a profile/heap file here or click to select

*(only `.sparkprofile` or `.sparkheap` files are accepted)*

The website/viewer is written in JavaScript using the React framework, and open-source'd on GitHub. Pull requests are much appreciated!
