---
title: 自行托管网页界面
source_url: https://luckperms.net/wiki/Self-hosting-the-web-interfaces
source_kind: official-wiki
translation_review: reviewed
source_version: fc2919c3d5e6bfba82af31f9930273b00f08ddbf
---

LuckPerms 插件内置了多个在线编辑器和查看器。这些界面在设计上不要求每位用户或每台服务器自行托管实例；任何人都可以使用的公共版本已部署在以下地址：

* https://luckperms.net/editor/
* https://luckperms.net/verbose/
* https://luckperms.net/treeview/

有时会有人希望自行托管。总体而言，**我们不建议这样做**；不过，代码是开源的，有相应经验的管理员也可以尝试。以下说明可作为起点。

此外，还需要准备或处理：

* 用于托管的 Linux 服务器
* 域名
* DNS 记录设置
* TLS 证书

等等，以及随之而来的各种事项，例如打补丁、维护和安全。

___

<a id="deploy-luckpermsweb-stack-on-a-server"></a>
### 在服务器上部署 LuckPermsWeb 服务栈

在服务器上执行：

```bash
git clone git@github.com:LuckPerms/LuckPermsWeb.git
cd LuckPermsWeb
docker compose up -d
```

这会在端口 `8080` 上提供界面。

此时，应该可以通过 `http://<your server ip>:8080/` 访问界面，但这种方式不太安全，所以下一步通常是将应用放到反向代理（例如 NGINX）后面，然后配置域名和 DNS，再配置 TLS 证书。这些都不在本指南的讨论范围内。


<a id="configuring-the-plugin-to-use-your-custom-stack"></a>
### 配置插件以使用自建服务栈

例如，假设服务栈已托管在 `https://luckperms.yourdomain.com/`，并且可以正常访问：

将以下内容添加到 LuckPerms 的 `config.yml` 文件末尾。


```yml
bytebin-url: https://luckperms.yourdomain.com/data/
bytesocks-url: https://luckperms.yourdomain.com/ws/

web-editor-url: https://luckperms.yourdomain.com/editor/
verbose-viewer-url: https://luckperms.yourdomain.com/verbose/
tree-viewer-url: https://luckperms.yourdomain.com/treeview/
```
