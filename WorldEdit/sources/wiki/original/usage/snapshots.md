# Snapshots { #snapshots }

A very powerful feature of WorldEdit is that it can load a section of your world, defined by your [selection region](https://worldedit.enginehub.org/en/latest/usage/regions/selections/), and restore it from a backup without having to shutdown your server or use an offline map editor. A large number of problems can be easily fixed this way, from undoing a griefer’s work to fixing a world save error to even rolling back from a project you gave up with half-way through.

<a id="contents"></a>

- [Configuring Snapshots](https://worldedit.enginehub.org/en/latest/usage/snapshots/#configuring-snapshots)



  - [Supported Archive Formats](https://worldedit.enginehub.org/en/latest/usage/snapshots/#supported-archive-formats)

- [Using Snapshots](https://worldedit.enginehub.org/en/latest/usage/snapshots/#using-snapshots)

## Configuring Snapshots { #configuring-snapshots }

In order for WorldEdit to be able to read your backups, you will have to choose a directory to place backups inside. The path can be set in the [configuration](https://worldedit.enginehub.org/en/latest/config/) and is relative to the server/`.minecraft` root folder (not the WorldEdit folder!). You can also use an absolute path if your backups are stored outside your server folder (like on another disk, which is recommended in case of hardware failures).

Once set, just toss either copies of your world folder or zipped copies of your world folder into your backup folder. An example of how you could lay out your backups folder is below.

Example: Possible structures of backup storage

**![f](https://worldedit.enginehub.org/en/latest/_images/folder.png) `backups/` (this is the folder name in the config)**

**![f](https://worldedit.enginehub.org/en/latest/_images/folder.png) `world/` (this is the name of a world)**

**![z](https://worldedit.enginehub.org/en/latest/_images/zip.png) `2019-06-15-03-00-00.zip` (a backup for just this world)**

**![f](https://worldedit.enginehub.org/en/latest/_images/folder.png) `world/` (must match the world name above)**

![f](https://worldedit.enginehub.org/en/latest/_images/folder.png) `region/` (contains `.mca` files for this world)

**![f](https://worldedit.enginehub.org/en/latest/_images/folder.png) `2019-05-15-03-00-00` (backups don’t have to be zipped)**

![f](https://worldedit.enginehub.org/en/latest/_images/folder.png) `world/`

**![f](https://worldedit.enginehub.org/en/latest/_images/folder.png) `world_nether/` (another world name)**

![z](https://worldedit.enginehub.org/en/latest/_images/zip.png) `2019-06-15-03-00-00.zip`

**![z](https://worldedit.enginehub.org/en/latest/_images/zip.png) `2019-06-01-03-00-00.zip` (this is one backup holding multiple worlds)**

**![f](https://worldedit.enginehub.org/en/latest/_images/folder.png) `world/`**

![f](https://worldedit.enginehub.org/en/latest/_images/folder.png) `region/` (all the `.mca` files are in here)

![f](https://worldedit.enginehub.org/en/latest/_images/folder.png) `world_nether/`

![z](https://worldedit.enginehub.org/en/latest/_images/zip.png) `2019-05-01-03-00-00.zip` (another backup from a month before)

As you might have noticed, each individual backup must have a timestamp. WorldEdit expects these timestamps in order to determine which backups are the newest. The world folder must be inside the backup, with a region folder inside that world folder. You can either have backups at the top level with multiple world folders inside, or multiple world folders with backups inside for each individual world.

!!! tip "Tip"

    If you use a Linux-like system, you can use the following line to create a world backup ZIP having an acceptable filename: ``zip -v backups/`date "+%Y-%m-%d-%H-%M-%S"`.zip -r world``.

### Supported Archive Formats { #supported-archive-formats }

WorldEdit natively supports ZIP files, using Java’s zip library. However, Java’s zip support only supports basic zip files. If you receive cryptic errors while using zip files, you may want to install TrueZip. If you want to use another archive format, such as tarballs, TrueZip will also support these.

TrueZip can be installed by downloading the [JAR file from the maven repository](https://repo.maven.apache.org/maven2/de/schlichtherle/truezip/6.8.1/truezip-6.8.1.jar) and saving it as `truezip.jar`. The jar should be placed in the `plugins` or `plugins/WorldEdit` folder on Bukkit, or in the `mods` folder on other platforms.

!!! tip "Tip"

    Using backup archives (e.g. zip files) will save disk space at the cost of increasing CPU when actually restoring. The trade-off is up to you to decide.

## Using Snapshots { #using-snapshots }

Now that your snapshots are configured, using them is a breeze. Just [select an area](https://worldedit.enginehub.org/en/latest/usage/regions/selections/), and use `//restore`.

By default, WorldEdit will find the most recent backup for your current world, and restore your selected area from it.

If you don’t want to use the most recent snapshot (perhaps the damage was already done and you need an older one), there are additional commands to choose which snapshot to use.

To get started, use `/snap list`. This will list all snapshots available for your current world.

You can either use `/snap use latest` or `/snap use [name]` to select either the latest snapshot, or by name. You can also use `/snap sel <number>` to use the one with that number in the list.

If you know a time point which you either need a backup before or after that point, you can use `/snap before <time>` or `/snap after <time>` to find the closest snapshot before/after the given time. These commands take a timestamp like the file names, or even a natural time, such as `/snap before "last friday"`.
