# Chunk Load

## Description {#description}

Applies an [aura] component to the target entity that keeps the chunk(s) containing the aura holder force-loaded for the duration of the aura

<svg aria-hidden="true" class="wiki-alert__icon" viewbox="0 0 24 24"><path d="M9 18h6"></path><path d="M10 22h4"></path><path d="M15.09 14c.18-.63.66-1.15 1.12-1.62A6 6 0 1 0 7.79 12.38c.45.46.93.98 1.12 1.62"></path></svg>Tip

This prevents the holder from unloading (and thus freezing) when no player is nearby, which is useful for bosses that must remain active after their combatant dies

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| radius | r | chunk radius to keep loaded around the holder (0 = own chunk only, capped at the server's simulation distance | 0 |
| lag | tps, tpsthreshold | if the server's 1-minute TPS average drops at or below this value the aura terminates, releasing the force-load | 0 |

## Aliases {#aliases}

- keeploaded
- loadchunk
