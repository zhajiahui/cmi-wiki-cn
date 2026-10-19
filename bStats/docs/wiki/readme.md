---
title: bStats 仓库与本地运行
source_url: https://github.com/Bastian/bStats/blob/master/README.md
source_kind: official-wiki
translation_review: reviewed
source_version: Bastian/bStats 仓库 master，2026-10-19 官方原文快照
---


# bStats 仓库与本地运行

[bStats](home.md) 项目的父仓库。

<a id="repository-structure"></a>

## 仓库结构

此仓库以子模块形式包含全部 bStats 仓库：

- `bstats-backend`：bStats 后端。
- `bstats-web`：bStats 前端。
- `bstats-data-processor`：处理插件传入数据的服务。
- `bstats-metrics`：bStats 的 Java 统计类。
- `bstats-pmmp`：供 PocketMine-MP 使用的 PHP 统计类。

此仓库也提供 bStats 开发环境。

<a id="run-bstats-locally"></a>

## 在本地运行 bStats

<a id="0-prerequisites"></a>

### 0. 前置条件

- Docker
- Linux。Windows 推荐使用 WSL2。macOS 应该也能运行，但尚未测试。
- GNU Make，大多数 Unix 系统通常已提供。

<a id="1-clone-repository"></a>

### 1. 克隆仓库

建议克隆时使用 `--recursive` 参数，同时克隆所有子模块。

```bash
git clone --recursive git@github.com:Bastian/bStats.git
```

也可以在克隆父仓库后执行以下命令，再克隆子模块：

```bash
git submodule init && git submodule update
```

<a id="2-update-submodules"></a>

### 2. 更新子模块

使用以下命令，将所有子模块切换到 `master` 分支：

```bash
git submodule foreach 'git checkout master'
```

<a id="3-start-the-development-environment"></a>

### 3. 启动开发环境

执行 `Makefile` 的默认目标即可启动全部服务。需要提供 [hCaptcha](https://www.hcaptcha.com/) 和 [MaxMind GeoIP](https://www.maxmind.com/en/account) 凭据：

```bash
PUBLIC_HCAPTCHA_SITE_KEY=your_site_key \
HCAPTCHA_SECRET_KEY=your_secret_key \
GEOIPUPDATE_ACCOUNT_ID=your_account_id \
GEOIPUPDATE_LICENSE_KEY=your_license_key \
make
```

全部服务启动后，应可通过 <https://bstats.localhost/> 访问 bStats，使用自签名证书。

服务在 Docker 容器中运行，无需额外安装 Node.js、npm 等依赖，不过为了 IDE 工具支持，仍建议安装。

容器以开发模式运行，代码挂载到容器中，热重载等功能可用。无需其他步骤，即可开始编辑代码。

<a id="start-production"></a>

## 启动正式运行环境

`prod` 目录包含 bStats 的正式运行环境。需要根据示例创建以下环境变量文件：

- `prod/postgres.env`
- `prod/bstats-web.env`
- `prod/bstats-backend.env`
- `prod/geoipupdate.env`

然后执行 `make start-prod` 启动服务。

<a id="backups"></a>

### 备份

Redis 和 Postgres 数据通过 SCP 备份到远程服务器。可使用 `prod` 目录下的 `add-backup-cronjobs.sh` 脚本设置 Cron 定时任务。

<a id="disaster-recovery"></a>

### 灾难恢复

假设最坏的情况发生，当前 bStats 服务器彻底损坏。恢复运行的步骤如下：

1. 配置一台新服务器，安装 Docker，并开放 http(s) 端口。
2. 克隆此仓库及所有子模块，切换到 `master` 分支。
3. 启动 `prod` 环境。
4. 停止 `prod` 环境。
5. 恢复 Redis 备份，直接替换 `prod/volumes/redis` 目录。
6. 根据示例创建环境变量文件，见上文。
7. 启动 `prod` 环境。
8. 更新 DNS 设置，指向新服务器 IP。
9. 从 postgres 备份导入历史图表数据，这一步不要求立即完成。

<a id="license"></a>

## 许可证

此项目采用 [MIT 许可证](https://github.com/Bastian/bStats/blob/master/LICENSE)。
