# Storage Drivers { #storage-drivers }

Region data can be stored using either:

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Storage Driver</th>
<th markdown="span">Advantages</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">YAML</td>
<td markdown="block">

<ul markdown="block"> <li markdown="span"><p markdown="span">No database server required.</p> </li> <li markdown="span"><p markdown="span">Can simply modify the file to edit the region data manually.</p> </li> <li markdown="span"><p markdown="span">Easy to backup with the world.</p> </li> <li markdown="span"><p markdown="span">Fast full load and full save.</p> </li> </ul>

</td>
</tr>
<tr>
<td markdown="span">MySQL</td>
<td markdown="block">

<ul markdown="block"> <li markdown="span"><p markdown="span">Can access data from other systems more easily.</p> </li> <li markdown="span"><p markdown="span">When saving, saves only changed data.</p> </li> </ul>

</td>
</tr>
</tbody>
</table>

!!! note "Note"

    Other SQL-supporting databases (PostgreSQL, SQL Server, SQLite, etc.) are currently not supported.

!!! warning "Warning"

    SQL support for region storage was contributed by a third-party developer and despite large rewrites, there are major issues with using it. It is highly recommended to never use SQL for storing your WorldGuard regions.

    **If you are already using SQL for region storage, you should migrate back to YAML using the migrate command covered below. SQL support for region storage will be removed from WorldGuard in a future version.**

## Switching Drivers { #switching-drivers }

The default mode is to use YAML files.

In the [Configuration](https://worldguard.enginehub.org/en/latest/config/), `regions.sql.use` can be enabled to switch to MySQL, therefore disabling YAML. If you are switching to MySQL, the database tables will be created automatically, though be sure to provide the necessary permissions for the SQL user account.

!!! warning "Warning"

    It is highly recommended that you make a backup before switching drivers.

### Migrating Data { #migrating-data }

If you simply switch between two different storage drivers, you will end up with no regions because the new storage medium will have no data. However, you can use a special migration command to migrate the data between two storage mediums, and you are able to do this before **or** after switching to the new driver.

To migrate data, use: `/rg migratedb from to`, specifying the source and target driver. For example, to migrate from YAML to MySQL, you would use:

```text
/rg migratedb yaml mysql
```

Please make sure that the target database is empty.

## Storage Drivers { #id1 }

!!! warning "Warning"

    Remember to make backups if you manually modify data outside WorldGuard.

### YAML { #yaml }

Region data stored in YAML is found within WorldGuard’s configuration folder as “region.yml” in each world folder. The file can be modified while the server is running and reloaded using `/rg load` without issue.

The region file is structured like the following example:

```text
regions:
    test:
        min: {x: 1730.0, y: 0.0, z: -169.0}
        max: {x: 1742.0, y: 255.0, z: -158.0}
        members:
            players: [bobby]
            unique-ids: [0ea8eca3-dbf6-47cc-9d1a-c64551ca975c]
        flags: {use: allow, greeting: Welcome!, pvp: allow, pvp-group: MEMBERS}
        owners:
            groups: [admins]
        type: cuboid
        priority: 4
    __global__:
        members: {}
        flags: {}
        owners: {}
        type: global
        priority: 0
```

UUIDs are normally stored, but player names can also be added using `-n` on some of the commands.

### MySQL { #mysql }

- Only one server instance can use one set of tables.

- A table prefix setting is provided to use the same database for different data sets or installations.

- Changes are made in a transaction and will be rolled back if an error occurs.

- By default, WorldGuard will only save changes to region data rather than re-save the entire region data set.

The tables used are explained below:

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">Table</th>
<th markdown="span">Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">region</td>
<td markdown="span">Region data, with shape, priority, and parent information.</td>
</tr>
<tr>
<td markdown="span">region_cuboid</td>
<td markdown="span">Data for cuboid regions, with bounds.</td>
</tr>
<tr>
<td markdown="span">region_poly2d</td>
<td markdown="span">Data for polygonal regions, with minimumum and maximum Y values.</td>
</tr>
<tr>
<td markdown="span">region_poly2d_point</td>
<td markdown="span">Individual rows for points of polygonal regions.</td>
</tr>
<tr>
<td markdown="span">region_flag</td>
<td markdown="span">Per-region flag data.</td>
</tr>
<tr>
<td markdown="span">region_players</td>
<td markdown="span">List of players on regions.</td>
</tr>
<tr>
<td markdown="span">region_groups</td>
<td markdown="span">List of groups on regions.</td>
</tr>
<tr>
<td markdown="span">world</td>
<td markdown="span">Normalizes worlds into a world ID.</td>
</tr>
<tr>
<td markdown="span">user</td>
<td markdown="span">Normalizes users into a user ID.</td>
</tr>
<tr>
<td markdown="span">group</td>
<td markdown="span">Normalizes groups into a group ID.</td>
</tr>
</tbody>
</table>

Each user row will either have a UUID or name set.

!!! warning "Warning"

    Modification of the data stored in MySQL while WorldGuard is running on a server is not recommended. Because WorldGuard will save only changes to region data, it may cause problems if external modifications change the state of the region data in a way that WorldGuard is unable to expect.

## High-Latency Environment { #high-latency-environment }

Data is loaded and saved in its entirety and in the background, so a slow hard disk or a remote MySQL server should not pose too much of an issue.
