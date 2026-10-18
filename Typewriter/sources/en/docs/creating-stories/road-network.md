# Road Network

**Before starting**

This guide assumes that you have already installed the Road Network Extension.  
Also, make sure you have read the [layout](https://docs.typewritermc.com/docs/getting-started/layout) documentation and created a **static** page.

Road Networks are essential if you want to make NPCs move around your map or let the player follow a path. In this guide, we will show you how to create a road network and how to use it in your story.

## What is the road network {#what-is-the-road-network}

The road network is an internal graph structure that Typewriter uses to efficiently calculate paths between two distant points.

## Creating a road network {#creating-a-road-network}

First, we need to add a `Base Road Network` entry to our page. To add it to our page, click on the + icon in the top right corner of the panel and search for `base road network` then add it to your page by clicking on the + icon.

Add Base Road Network

A definition of the words road network

+

### Opening the content mode {#opening-the-content-mode}

In the `Base Road Network` entry in the inspector, click the  icon next to the ArtifactId field to open the content mode.

### Adding a node {#adding-a-node}

Now that we have opened the content mode, we need to add a node. Nodes are points in a world that can be connected to each other using edges. To add a node, in your hotbar select the diamond and right-click it. This will open the node editor. To exit the menu of the node, click the end crystal.

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/road-network/add-node.webm"></video>

### Creating the path {#creating-the-path}

To create a path, you will always need 2 nodes. So create 2 nodes and then select the redstone from your hotbar and right-click it. Now it should look a bit like this:

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/road-network/path.webm"></video>

Now you have created a path. You can expand a road network with unlimited nodes and create paths between them.

**Node placement**

It is recommended that you create nodes at the beginning and end of a road or path in your world. This is to save resources on loading and recalculating the edges.

### Editing a node {#editing-a-node}

When in the node editor, you have 4 options:

**Change Radius**

#### Why is their radius? {#why-is-their-radius}

When performing pathfinding from node A, all nodes within a **30-block** radius will be checked, for example, nodes B, C, D, E, F, and G. If it finds that the path to node C requires passing through nodes B radius, it will stop calculating the path to C. This is because the pathfinding avoids paths that need to skip nodes like B.

![road-network radius explanation](https://docs.typewritermc.com/assets/optimized-img/radius.04ce433.1920.avif)

#### How to use? {#how-to-use}

To change the radius of a node, select the sculk sensor from your hotbar and right-click.

**Node click**

When right-clicking an item, you must not point your cursor at the node you are editing. This will open the content mode and not trigger the event.

Then, with your scroll wheel, you can change the radius of a node.

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/road-network/radius.webm"></video>

**Remove Edge**

#### Why remove an edge? {#why-remove-an-edge}

Removing an edge can be useful when you want a path to skip a node or to make a path one-way only.

#### How to use? {#how-to-use-1}

To remove an edge, select the redstone from your hotbar and right-click it on the node you want to remove the edge from.

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/road-network/remove-edges.webm"></video>

**Recalculate**

You must recalculate the edges using the redstone from your hotbar after adding or removing a negative node

#### One way path {#one-way-path}

To make it one way only, you should, instead of just right-clicking, also hold shift. This will make the edge one-way only.

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/road-network/remove-edge.webm"></video>

**Add Fast Travel Connection**

#### Why add a fast travel connection? {#why-add-a-fast-travel-connection}

Fast travel connections are used to make a path teleport the NPC to another node instead of needing to walk to it.

#### How to use? {#how-to-use-2}

To add a fast travel connection, select the emerald from your hotbar and right-click it on the node you want it to teleport to.

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/road-network/fast-travel.webm"></video>

#### One way fast travel {#one-way-fast-travel}

To make it one way only, you should, instead of just right-clicking, also hold shift. This will make the fast travel one-way only.

**Remove Node**

To remove a node, select the redstone block from your hotbar and right-click it.

**Node click**

When right-clicking an item, you must not point your cursor at the node you are editing. This will open the content mode and not trigger the event.

### Negative Nodes {#negative-nodes}

Sometimes you want pathfinding to not go via a certain path. For example, when you have a place where the pathfinding thinks it can jump down or up 1 block but shouldn't, you can add a negative node to prevent this.  
Here is an example:

**With Negative Node**

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/road-network/negative-nodes-preview.webm"></video>

**Without Negative Node**

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/road-network/non-negative-nodes-example.webm"></video>

#### How to add a negative node? {#how-to-add-a-negative-node}

You can add a negative node by selecting the netherite ingot from your hotbar in the content mode and right-clicking it.

**Recalculate**

You must recalculate the edges using the redstone from your hotbar after adding or removing a negative node

### Highlighting nodes {#highlighting-nodes}

When you have a lot of nodes, it can be hard to see which nodes are connected to each other. To make this easier, you can highlight the nodes that are connected to each other. To do this, select the glowstone from your hotbar and right-click it.

## Ending {#ending}

Now you have learned how to successfully set up the road network.
