---
title: 支持的版本
source_url: https://wiki.citizensnpcs.co/Supported_Versions
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5645
---


<a id="top"></a>

# 支持的版本

<p>如果您被发送到此页面，则您 are:</p>
<ul>
<li>无法运行 Citizens</li>
<li>在使用不受支持的 Minecraft 版本时寻求帮助</li>
<li>寻求与可能的错误相关的帮助，但使用的是不受支持或有限支持的 Minecraft 版本</li>
<li>由于插件不支持最新补丁版本而无法更新</li>
</ul>
<p>本页解释了您可以和应该做什么，同时还提供其他有用的工具来帮助您维护服务器。</p>
<a id="Running_a_server_requires_maintenance"></a><h3 id="running-a-server-requires-maintenance">运行服务器需要维护</h3>
<p>我们知道运行 Minecraft 服务器是有益且有趣的，但不幸的是，即使您购买了设置，它也需要维护工作。
保持服务器更新至关重要，因为新版本附带安全补丁、错误修复和玩家功能。</p>
<p>例如，<a href="https://en.wikipedia.org/wiki/Log4Shell">Log4Shell</a> 漏洞展示了过时的版本如何使服务器容易受到严重的安全威胁。</p>
<p>定期备份对于确保 Minecraft 服务器数据的安全至关重要。
制作它们的一个简单方法是 .zip 或 .tar Minecraft 服务器，然后使用 FTP 客户端从服务器主机下载它。如果您正在寻找更高级的工具，您可以考虑使用 BorgBackup。它允许您免费自动进行备份。</p>
<a id="Which_Versions_does_Citizens_support?"></a><h3 id="which-versions-does-citizens-support">Citizens支持哪些版本？</h3>
<p>Citizens 支持 Minecraft 的多个版本，但由于 Spigot 文件大小限制、有限的开发时间以及较旧的 Minecraft 版本带来的安全风险和错误，主动支持的版本会随着时间的推移而变化。</p>
<p>根据一般经验，仅完全支持三个最新 Minecraft 主版本中每个版本的最新补丁版本。例如，在Minecraft 1.20中，最新补丁版本是1.20.6，因此Citizens的最新版本仅适用于Minecraft版本1.20.6，而不是1.20或1.20.4。</p>
<p>但是，具体版本可能会有所不同，具体取决于 bStats 的使用数据或 Spigot 文件大小限制。这意味着在某些情况下，可能会跳过某个版本。例如，由于使用率低或技术限制，Citizens 可能支持版本 1.19.4、1.21.4、1.22.1，并放弃对 1.20.6（而不是 1.19.4）的支持。</p>
<p>某些版本仅获得有限的支持，这意味着我们将回答基本问题，但无法修复这些特定版本的错误或添加功能请求，并且最新的 Citizens 版本将无法在其上运行。对于不受支持的旧版本，在您迁移到受支持的版本之前，我们不会提供任何帮助。如果您使用的是 1.8，请参阅 <a href="minecraft-1.8.md" title="Minecraft 1.8">Minecraft 1.8</a>。</p>
<p>当Minecraft发布新的更新时，我们会在短时间内对之前的版本提供有限的支持。例如，如果最新版本是 1.21.4，我们可能仍为 1.21.3 提供有限支持。</p>
<p>您可以找到最新的 Citizens 开发版本 <a href="https://ci.citizensnpcs.co/job/citizens2/">这里</a>。如果您正在寻找较旧的版本，您可以在我们的 <a href="https://discord.gg/Q6pZGSR">不和谐</a> 上的 #news 频道中找到它们的链接。请注意，您可能最终会完全依靠自己，并失去获得支持的机会。</p>
<a id="What_to_do?"></a><h2 id="what-to-do">该怎么办？</h2>
<a id="Having_trouble_getting_Citizens_to_run"></a><h3 id="having-trouble-getting-citizens-to-run">无法运行 Citizens</h3>
<p>如果您在运行 Citizens 时遇到问题，您可能会注意到类似的行</p>
<div class="highlight"><pre>Error occurred while enabling Citizens v2.0.37-SNAPSHOT (build 3648) (Is it up to date?)</pre></div>
<p>在您的 latest.log 文件中。此行通常意味着您的 Minecraft 版本或 Citizens 不是最新的。
在这种情况下，您需要 <a href="supported-versions.md#How_to_update_a_Minecraft_server">更新您的 Minecraft 服务器</a>。我们知道这可能很困难，特别是如果您刚刚设置服务器或购买了设置。然而，如上所述，服务器维护至关重要。</p>
<p>如果您将服务器托管在免费主机上并且在更新服务器时遇到问题，请参阅 <a href="frequently-asked-questions.md#I_have_a_free_server_(Aternos,_Minehut,_...)_but_there's_problems">这个</a>。</p>
<a id="Unable_to_update_because_of_a_plugin_that_does_not_support_the_latest_patch_version"></a><h3 id="unable-to-update-because-of-a-plugin-that-does-not-support-the-latest-patch-version">由于插件不支持最新补丁版本而无法更新</h3>
<p>有时，您依赖的插件可能会阻止您更新服务器。当插件不再维护、Minecraft 更新发生复杂的更改（需要插件开发人员花费更多时间和工作）或者插件的维护由社区驱动时，可能会发生这种情况。</p>
<p>验证插件是否仍在维护。该插件的作者可能已停止开发。在插件的官方网站、官方 Discord 或 Spigot/Hangar 页面上查找更新。如果该插件在过去一年没有更新，它可能不再被维护。如果不再维护该插件，请考虑寻找提供类似功能并受到积极支持的替代方案并更新您的服务器。</p>
<a id="Asking_for_help_on_an_unsupported_Minecraft_version"></a><h3 id="asking-for-help-on-an-unsupported-minecraft-version">寻求有关不受支持的 Minecraft 版本的帮助</h3>
<p>如前所述，Citizens 并不支持 Minecraft 的所有版本。如果您使用的是过时的版本，很遗憾，我们无法提供支持。</p>
<p>请将您的 Minecraft 服务器更新到我们完全支持的版本。
更新服务器后，请随时联系我们寻求帮助！</p>
<a id="Reporting_a_potential_bug,_but_on_an_unsupported_Minecraft_version"></a><h3 id="reporting-a-potential-bug-but-on-an-unsupported-minecraft-version">报告潜在的错误，但在不受支持的 Minecraft 版本上</h3>
<p>如果您在不受支持或受有限支持的版本上遇到错误，尤其是在最新的 Minecraft 主版本上，该问题可能已在最新的 Citizens 版本中得到修复。因此，请将您的 Minecraft 服务器更新到我们支持的补丁版本。</p>
<p>如果您无法更新，因为插件不支持此版本，或者您正在使用 Paper 并且最新版本尚未稳定，这不是问题！</p>
<p>请帮助我们尝试在最新补丁版本的本地测试服务器上复制该行为。如果您可以成功复制该问题，请提供更新后服务器上的 latest.log，并告诉我们重现该问题的步骤，以便我们进一步排除故障。</p>
<a id="How_to_update_a_Minecraft_server"></a><h2 id="how-to-update-a-minecraft-server">如何更新 Minecraft 服务器</h2>
<p>更新 Minecraft 服务器是一个简单明了的过程，但谨慎处理以避免遇到问题至关重要。以下解释涵盖了基本过程。</p>
<a id="Have_a_backup_on_hand"></a><h4 id="have-a-backup-on-hand">手头有备份</h4>
<p>在进行任何更改之前，请确保您有服务器的有效备份。以防万一发生不可预测的情况而您需要恢复它。</p>
<a id="Test_the_update_locally_on_your_computer"></a><h4 id="test-the-update-locally-on-your-computer">在您的计算机上本地测试更新</h4>
<p>通过在计算机上本地下载并运行服务器并更新来执行试运行。为此，您需要 to:</p>
<ul>
<li>将服务器的 .jar 文件和任何插件 .jar 文件替换为您从相关插件页面下载的更新版本。</li>
<li>启动服务器并检查日志中是否有错误和警告。</li>
<li>登录到本地服务器并测试必须工作的重要内容。</li>
</ul>
<p>如果您没有看到出现问题，则可能需要进行更新。</p>
<p>如果遇到issues:</p>
<ul>
<li>检查相关插件的官方页面或支持渠道以获取新闻。</li>
<li>在插件的 Discord 服务器上查找帮助（如果有）。</li>
</ul>
<a id="Proceed_to_update_your_production_server"></a><h4 id="proceed-to-update-your-production-server">继续更新您的生产服务器</h4>
<p>一旦您对本地测试充满信心，就可以继续更新生产服务器。</p>

