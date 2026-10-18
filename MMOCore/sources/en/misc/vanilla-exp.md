# 🌟 Vanilla Exp {#🌟-vanilla-exp}

This simple RPG option lets you display the player's current main class level on the vanilla experience bar. Players can also see how close/far they are from reaching the next level by looking at the actual EXP bar progression. This option can be enabled in `config.yml`:

```yml
# Enable this open to override vanilla EXP and display
# level progress on the vanilla experience bar.
# Requires a SERVER reload when changed.
override-vanilla-exp: true
```

![SbErxxz](https://docs.phoenixdevt.fr/assets/vanilla_exp.CW9qSvtl.png)

It matches the experience progress and level displayed in the `/p` menu.

![](https://docs.phoenixdevt.fr/assets/exp_progress.BKg6SjB0.png)

## Vanilla EXP redirection {#vanilla-exp-redirection}

When enabled, a set portion of the EXP you earn via experience orbs is redirected to your main MMOCore class exp. You can change this option in `config.yml`.

```yml
# Redirects vanilla experience obtained to MMOCore
# class experience. You can define the % of the vanilla
# experience that is being transfered as MMOCore exp.
# Requires a SERVER reload when changed.
vanilla-exp-redirection:
  enabled: false
  ratio: 0.8
```

This feature can be useful for survival or simple RPG servers which do not want to spend time on setting up [experience sources](https://docs.phoenixdevt.fr/mmocore/level/sources) and are okay with relying on vanilla exp dropped by mobs and blocks.
