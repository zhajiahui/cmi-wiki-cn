For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://meta.denizenscript.com/).

If you want a full tutorial to help get you set up, check out the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

Requirements are no longer needed as of 0.9 thanks to the - IF { .. } command, however they are still supported to avoid breaking old scripts.

# How To Use Requirements

They are written near the top of interact scripts like so:

```
MyInteractScript:
    Type: Interact
    Requirements:
        Mode: 
        List:
        - FirstReq
        - SecondReq etc. etc.
```

# List Of Requirements

enchanted, flagged, holding, ingroup, item, isliquid, money, op, owner, permission, ispowered, oxygen, procedure, script, sneaking, storming, sunny, rainy, time, inregion

```
- enchanted (iteminhand)
- flagged [player/npc/global] [<name>([<#>])](:<value>)
- holding [<item>] [qty:<#>] [exact]
- ingroup (global) [<group>]
- item [<item>] (qty:<#>)
- isliquid [location:<location>]
- money [qty:<#>]
- op
- owner
- permission (global) [<permission>]
- ispowered [location:<location>]
- oxygen (range:below/equals/above) [qty:<#>]
- procedure [<script>]
- script [finished/failed] [script:<name>]
- sneaking
- storming (????????????????????) (This req is ill-defined)
- sunny
- rainy
- time [dawn/day/dusk/night]
- inregion [name:<region>]
```
