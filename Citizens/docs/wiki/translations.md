---
title: 多语言翻译
source_url: https://wiki.citizensnpcs.co/Translations
source_kind: official-wiki
translation_review: reviewed
source_version: 2.0.43-SNAPSHOT (build 4210); official Wiki snapshot 2026-10-19 oldid=5553
---


<a id="top"></a>

# 多语言翻译

<p>最新版本的 Citizens2 可以完全翻译成多种语言。服主可以轻松选择他们希望 Citizens 消息以哪种语言显示，只要该语言的翻译已经完成。</p>
<p>要将 Citizens 设置为服务器上的其他语言，只需打开“plugins\Citizens\config.yml”并更改“locale: en”（在 general: translations: 下）。将“en”设置为要切换到的语言的语言（ISO 代码），例如“de”表示德语。</p>
<p>您还可以通过打开 Citizens\lang\ 中的语言文件来编辑服务器上任何语言的消息</p>
<a id="Available_translations"></a><h2 id="available-translations">可用翻译</h2>
<p>目前，Citizens已翻译为以下languages:</p>
<ul>
<li>法语 (fr) by leagris</li>
<li>德语 (de) by SpaceEmotion</li>
<li>荷兰语 (nl) by sjoerdtim</li>
</ul>
<p>我们感谢我们的翻译人员，并欢迎翻译成其他语言。</p>
<a id="So_how_do_I_make_my_own?"></a><h2 id="so-how-do-i-make-my-own">那么我该如何制作自己的呢？</h2>
<p>要开始使用新翻译，请复制 messages_en.properties 文件并更改其文件名以使用新的语言，例如意大利语的 messages_it.properties。翻译该文件中的字符串，就完成了！</p>
<a id="How_do_language_files_work?"></a><h2 id="how-do-language-files-work">语言文件如何工作？</h2>
<p>语言文件是属性文件中句子（“字符串”）的集合。它们允许 Citizens 请求基于键的特定操作的字符串，例如 citizens.notifications.enabled。每个语言文件的名称中都包含一个语言 - 即该语言的 ISO 代码。例如，英语的语言文件名为“messages_en.properties”</p>
<p>默认情况下，Citizens 将使用系统语言进行翻译，但将使用 Citizens' config.yml 中的 general.translation.locale 设置（如果存在）。</p>

