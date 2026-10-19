---
title: config/config-general.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: config/config-general.yml
source_version: 5.13.0-SNAPSHOT-1abf9862
---

# config/config-general.yml

文件：`config/config-general.yml`。版本：`5.13.0-SNAPSHOT-1abf9862`。

随包配置。

## `Configuration` { #configuration }

```yaml title="config/config-general.yml · Configuration"
Configuration:
  General:
    Language: en-us
    ThreadPoolSize: -1
    UseVirtualThreads: false
    AllowMetrics: true
    AnnounceOpReload: false
    CheckForUpdates: true
    DebugLevel: 0
    DebugMode: false
    DebugSpawners: false
    ErrorLogging: true
    
    # 是否缓存并复用相同的技能机制
    # 可减少内存占用，但错误中的来源信息将不再准确
    ShareComponents: false
    
    # 其他插件生成生物时，尝试按显示名称匹配并转为 Mythic 生物，
    # 供未直接支持 Mythic 的插件使用
    CompatibilityMode: false
  Version: 5.6
  
  Packet:
    # 将一次发出的多个粒子数据包包装到 ClientboundBundlePacket 中，让客户端一起渲染。
    ParticleBundleEnabled: true
    # 每个包允许的粒子数据包上限，限制在 [1, 4096]。关闭时忽略此项。
    ParticleBundleSize: 512
    # 收集同一刻发出的全部粒子数据包，在该刻结束时为每名玩家合并发送。
    # 启用后替代按调用合并的方式。关闭后恢复为每次调用分别合并。
    ParticleTickBatchEnabled: true
    # 遵循每名玩家的原版粒子设置（All / Decreased / Minimal）。
    # 设为 false（默认值）时，无论客户端偏好如何，始终发送粒子。
    RespectClientParticleVisibility: false
    # 启用上一项时，各粒子设置实际接收的粒子百分比。
    ClientParticleVisibility:
      All: 100
      Decreased: 50
      Minimal: 10
  
  # ================================================================================
  # 功能开关：设为 false 可完全关闭某项功能
  # ================================================================================
  Features:
    PlayerFactions: true
    RandomSpawning: true
    Spawners: true
  
  # ================================================================================
  # 命令相关选项
  # ================================================================================
  Commands:
    SendGiveItemFeedback: true
  
  # ================================================================================
  # 时钟相关选项，通常不建议修改。
  # 全部数值均以刻为单位
  # ================================================================================
  Clock:
    Main: 1
    Saving: 300
    Spawners: 2
    RandomSpawning: 1
    Scanner: 10
    Cleanup: 600
  
  # ================================================================================
  # 与其他插件的内置兼容设置
  # ================================================================================
  Compatibility:
    ProtocolLib:
      Enabled: true
    Heroes:
      Enabled: true
    McMMO:
      Enabled: true
      ShowXPMessage: true
      XPMessageFormat: "&7你因击杀 <dropper.name> 获得了 <drop.amount> 经验"
    SkillAPI:
      Enabled: true
      ShowXPMessage: true
      XPMessageFormat: "&7你因击杀 <dropper.name> 获得了 <drop.amount> 经验"
    Vault:
      Enabled: true
      ShowMoneyMessage: true
      MoneyMessageFormat: "&7你因击杀 <dropper.name> 获得了 <drop.amount> 金钱"
```
