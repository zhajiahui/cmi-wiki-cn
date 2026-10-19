---
title: 聊天过滤（ChatFilter.yml）
source_kind: configuration-examples
translation_review: reviewed
source_file: Settings/ChatFilter.yml
---

# 聊天过滤（ChatFilter.yml）

文件：`plugins/CMI/Settings/ChatFilter.yml`

## `ChatFilter` { #chatfilter }

```yaml title="ChatFilter.yml · ChatFilter（1/2）"
ChatFilter:
  Enabled: false
  Deny:
    ipBlock:
      # 未设为 true 时，不使用此过滤规则
      Enabled: true
      # 过滤组名称，同时决定绕过此规则的权限：cmi.chatfilter.bypass.[groupName]
      Group: Advertising
      # 设为 true，每次触发时，在控制台记录玩家、规则及原消息
      InformConsole: true
      # 用于过滤的正则表达式。正则用法见 https://regexone.com/
      Regex:
      - '[a-zA-Z0-9\-\.]+\s?(\.|dot|\(dot\)|-|;|:|,|_|\/)\s?([a-zA-Z]{2}|aero|asia|biz|cat|com|coop|edu|gov|info|int|jobs|mil|mobi|museum|name|net|org|pro|tel|travel)\b'
      - \b[0-9]{1,3}(\.|dot|\(dot\)|-|;|:|,|(\W|\d|_)*\s)+[0-9]{1,3}(\.|dot|\(dot\)|-|;|:|,|(\W|\d|_)*\s)+[0-9]{1,3}(\.|dot|\(dot\)|-|;|:|,|(\W|\d|_)*\s)+[0-9]{1,3}\b
      # 替换成的文字；未设置时，不修改匹配内容
      ReplaceWith: ''
      # 可用值：none、others、all
      # 'none'：所有人都能收到消息
      # 'others'：只有发送者能看到消息，其他人看不到，适合静默拦截广告
      # 'all'：所有人都收不到消息
      BlockType: others
      # 启用后，此规则也应用于私聊
      includePrivateMessages: true
      # 触发规则时，拥有 cmi.chatfilter.inform 权限的玩家会收到指定提示
      msgToStaff: "&4!&6[playerName] &4正在发广告：&r[message]"
      # 触发规则时执行的命令。可用 [senderName] 插入发送者名称，也支持与语言文件相同的全局变量
      # 使用 [message] 插入玩家原始消息
      # 使用 [updatedmessage] 插入修改后的消息
      Commands: []
    swearing1:
      Enabled: true
      Group: Swearing
      InformConsole: true
      Regex:
      - \bass\b|\basshole
      ReplaceWith: dude
      BlockType: none
      includePrivateMessages: true
      msgToStaff: "&4!&6[playerName] &4正在说脏话"
      Commands:
      - "msg [senderName] &e请勿说脏话！"
    swearing2:
      Enabled: true
      Group: Swearing
      InformConsole: true
      Regex:
      - \b(?i)(f+(\W|_)*(u?)+(\W|_)*(c?)+(\W|_)*k+)
      ReplaceWith: "不好"
      BlockType: none
      includePrivateMessages: true
      msgToStaff: "&4!&6[playerName] &4正在说脏话"
      Commands:
      - "msg [senderName] &e请勿说脏话！"
  # 从拦截规则中排除的正则列表，例如拦截全部 IP 或域名，但允许自己的服务器地址
  WhiteList:
  - \bgoogle.\s?([a-zA-Z]{2,4})\b
  - \bspigotmc.\s?([a-zA-Z]{2,4})\b
  DuplicatedMessagePrevention:
    # 设为 true，阻止短时间内重复发送相同或相似消息。可通过 cmi.chatfilter.spambypass 绕过
    Use: false
    # 判定为相同消息的相似度百分比
    Percentage: 80
    # 重复发送相同或相似消息的最小间隔，单位为秒
    Interval: 5
    # 触发冷却前允许连续重复的命令次数
    MinAmount: 2
  Caps:
    # 启用后，按以下规则限制大量使用大写字母的消息
    # 可通过 cmi.chatfilter.capbypass 绕过
    Filter: true
    # 可忽略的字符数量
    # 例如 ':DDD' 由 2 个字母组成，其中有 3 个大写字母，因此大写占比为 75%
    IgnoreUnder: 6
    # 允许的大写字母百分比上限
    # 例如 'GOOD thing' 有 4 个大写和 5 个非大写字母，忽略空格后，大写比例为 44%，可通过检查
    Percentage: 50
    # 检测到过多大写字母时，是否转为小写
    LowerCase: true
    # 检测到过多大写字母时，是否取消聊天事件
    CancelEvent: false
    # 玩家使用过多大写字母时执行的命令
    Commands:
    - "asConsole! cmi titlemsg [playerName] &c大写字母太多了！ -keep:20"
    # 即使全部大写也允许的消息列表，不含颜色代码
    WhiteList:
    - AFAIK
    - AFK
    - BRB
    - IMHO
    - OMG
    - ROFL
    - ROFLMAO
    - LQTM
    - LSMH
    - LMHO
```

```yaml title="ChatFilter.yml · ChatFilter（2/2）"
ChatFilter:
  SimpleReplacer:
    # 为公共聊天和私聊启用简易替换
    Enabled: false
    # 快速将 :heart: 等输入替换为 ❤
    Replacements:
    - heart-❤
    - star-★
    - sparkles-✨
    - sunny-☀
    - umbrella-☂
    - zap-⚡
    - musical_note-♫
    - check_mark-✓
    - cross_mark-✗
    - smile-☺
    - frown-☹
    - wink-😉
    - grin-😁
    - laughing-😆
    - cool-😎
    - cry-😢
    - angry-😠
    - thumbs_up-👍
    - thumbs_down-👎
    - clapping-👏
    - ok_hand-👌
    - pray-🙏
    - fire-🔥
    - poop-💩
    - party_popper-🎉
    - balloon-🎈
    - trophy-🏆
    - coffee-☕
    - warning-⚠
    - question_mark-❓
    - exclamation_mark-❗
    - hourglass-⌛
    - light_bulb-💡
    - camera-📷
    - video_game-🎮
    - laptop-💻
    - rocket-🚀
    - sparkle_heart-💖
    - broken_heart-💔
    - note-♪
    - skull-☠
    - snowman-☃
    - shamrock-☘
    - yin_yang-☯
    - peace-☮
    - star_of_david-✡
    - cross_star-✝
    - biohazard-☣
    - radioactive-☢
    - scissors-✂
    - pencil-✏
    - telephone-☎
    - envelope-✉
    - anchor-⚓
    - recycle-♻
  # emojipicker 命令可使用的表情
  Emojies: 😀😃😄😁😆😅🤣😂🥹🙂🙃😉😊😇🥰😍🤩😘😗☺😚😙🥲😋😛😜🤪😝🤑🤗🫢🤭🤫🤔🫡🤐🤨😐😑😶😏😒🙄😬🤥😌😔😪😮💨🤤😴😷🤒🤕🤢🤮🤧🫠🥵🥶😶🌫🫥🥴🫨😵💫😵🤯🤠🥳🥸😎🤓🧐🫤😕😟🙁☹😮😯😲😳🫣🥺😦😧😨😰😥😢😭😱😖😣😞😓😩😫🥱😤😡😠🤬😈👿💀☠💩🤡👹👺👻👽👾🤖😺😸😹😻😼😽🙀😿😾🙈🙉🙊👋🤚🖐✋🖖👌🤌🤏✌🤞🫰🤟🤘🤙👈👉👆🖕👇☝🫵👍👎✊👊🤛🤜👏🙌👐🫶🤲🫳🫴🫱🫲🤝🫸🫷🙏✍💅🤳💪🦾🦿🦵🦶👂🦻👃🧠🫀🫁🦷🦴👀👁👅👄🫦💋👶🧒👦👧🧔🧑🦰🦱🦳🦱🦲👱🧓👴👵🙍🙎🙅🙆💁🙋🤦🙇🧏👨🤷⚕🎓🏫⚖🌾🍳🔧🏭💼🔬💻🎤🎨✈👩🚀🚒🚒👮🕵💂🥷👷🫅👸👳👲🧕🤵👰🫄🤱🍼👼🎅🤶🎄🦸🦹🧙🧚🧛🧜🧝🧞🧟🧌💆💇🚶🧍🧎🦯🦼🦽🏃💃🕺🕴👯🧖🧗🤺🏇⛷🏂🏌🏄🚣🏊⛹🏋🚴🚵🤸🤼🤽🤾🤹🧘🛀🛌🤝👭💏❤💋🗣👤👥🫂👣🐵🐒🦍🦧🐶🐕🦮🐕🦺🐩🐺🦊🦝🐱🐈🐈⬛🦁🐯🐅🐆🐴🐎🦄🫏🦓🦌🫎🦬🐮🐂🐃🐄🐷🐖🐗🐽🐏🐑🐐🐪🐫🦙🦒🐘🦣🦏🦛🐭🐁🐀🐹🐰🐇🐿🦫🦔🦇❄🐻🐨🐼🦥🦦🦨🦘🦡🐾🦃🐔🐓🐣🐤🐥🐦🐧🐦⬛🕊🦅🦆🪿🦢🦉🦤🦩🦚🦜🪽🪶🪹🪺🥚🐸🐊🐢🦎🐍🐲🐉🦕🦖🐳🐋🐬🦭🐟🐠🐡🦈🪼🐙🦑🦀🦞🦐🪸🦪🐚🐌🦋🐛🐜🐝🪲🐞🦗🪳🕷🕸🦂🦟🪰🪱🦠🍄💐💮🏵🌼🌻🌹🥀🌺🌷🌸🪷🪻🌱🪴🏕🌲🌳🌰🌴🌵🎋🎍🌾🌿☘🍀🍁🍂🍃🌍🌎🌏🌑🌒🌓🌔🌕🌖🌗🌘🌙🌚🌛🌜☀🌝🌞🪐💫⭐🌟✨🌠☄🌌☁⛅⛈🌤🌥🌦🌧🌨🌩🌪🌫🌬🌀🌈🌂☂☔⛱⚡❄☃⛄🏔⛰🗻🌋🔥💧🌊💥💦💨🍇🍈🍉🍊🍋🍌🍍🥭🍎🍏🍐🍑🍒🍓🫐🥝🍅🫒🥥🥑🍆🥔🥕🌽🌶🫑🥒🥬🥦🫛🧄🧅🫚🍄🫘🥜🌰🍞🥐🥖🫓🥨🥯🥞🧇🧀🍖🍗🥩🥓🍔🍟🍕🌭🥪🌮🌯🫔🥙🧆🥚🍳🥘🍲🫕🥣🥗🍿🧈🧂🥫🍱🍘🍙🍚🍛🍜🍝🍠🍢🍣🍤🍥🥮🍡🥟🥠🥡🍦🍧🍨🍩🍪🎂🍰🧁🥧🍫🍬🍭🍮🍯🍼🥛🫗☕🫖🍵🍶🍾🍷🍸🍹🍺🍻🥂🥃🥤🧋🧃🧉🧊🥢🍽🍴🥄🔪⚽⚾🥎🏀🏐🏈🏉🎾🥏🎳🏏🏑🏒🥍🏓🏸🥊🥋🥅⛳⛸🎣🤿🎽🎿🛷🥌🎯🪀🪁🎱🎖🏆🏅🥇🥈🥉🏔⛰🌋🗻🏕🏖🏜🏝🏟🏛🏗🧱🪨🪵🛖🏘🏚🏠🏡🏢🏣🏤🏥🏦🏨🏩🏪🏫🏬🏭🏯🏰💒🗼🗽⛪🕌🛕🕍⛩🕋⛲⛺🌁🌃🏙🌄🌅🌆🌇🌉🗾🏞🎠🎡🎢💈🎪🚂🚃🚄🚅🚆🚇🚈🚉🚊🚝🚞🚋🚌🚍🚎🚐🚑🚒🚓🚔🚕🚖🚗🚘🚙🛻🚚🚛🚜🏎🏍🛵🦽🦼🛺🚲🛴🛹🛼🚏🛣🛤🛢⛽🚨🚥🚦🛑🚧⚓⛵🛶🚤🛳⛴🛥🚢✈🛩🛫🛬🪂💺🚁🚟🚠🚡🛰🚀🛸🎆🎇🎑🗿🛎🧳⌛⏳⌚⏰⏱⏲🕰🌡🗺🧭🎃🎄🧨🎈🎉🎊🎎🪭🎏🎐🎀🎁🎗🎟🎫🔮🪄🧿🎮🕹🎰🎲♟🧩🧸🪅🪆🖼🎨🧵🪡🧶🪢👓🕶🥽🥼🦺👔👕👖🧣🧤🧥🧦👗👘🥻🩱🩲🩳👙👚👛👜👝🛍🎒🩴👞👟🥾🥿👠👡🩰👢👑👒🎩🎓🧢🪖⛑📿💄💍💎📢📣📯🎙🎚🎛🎤🎧📻🎷🪗🎸🎹🎺🎻🪕🪈🪇🥁🪘🪩📱📲☎📞📟📠🔋🪫🔌💻🖥🖨⌨🖱🖲💽💾💿📀🧮🎥🎞📽🎬📺📷📸📹📼🔍🔎🕯💡🔦🏮🪔📔📕📖📗📘📙📚📓📒📃📜📄📰🗞📑🔖🏷💰🪙💴💵💶💷💸💳🪪🧾✉💌📧🧧📨📩📤📥📦📫📪📬📭📮🗳✏✒🖋🖊🖌🖍📝📁📂🗂📅📆🗒🗓📇📈📉📊📋📌📍📎🖇📏📐✂🗃🗄🗑🔒🔓🔏🔐🔑🗝🔨🪓⛏⚒🛠🗡⚔💣🔫🪃🏹🛡🪚🔧🪛🔩⚙🗜⚖🦯🔗⛓🪝🧰🧲🪜🛝🛞🫙⚗🧪🧫🧬🔬🔭📡🩻💉🩸💊🩹🩺🩼🚪🛗🪞🪟🛏🛋🪑🪤🚽🪠🚿🛁🧼🫧🪒🪮🧴🧷🧹🧺🧻🪣🪥🧽🧯🛟🛒🚬⚰🪦⚱🏺🪧🕳💘💝💖💗💓💞💕💟❣💔❤🧡💛💚🩵💙💜🩷🤎🖤🩶🤍❤🔥❤🩹💯♨💢💬👁🗨🗯💭💤🌐♠♥♦♣🃏🀄🎴🎭🔇🔈🔉🔊🔔🔕🎼🎵🎶💹🏧🚮🚰♿🚹🚺🚻🚼🚾🛂🛃🛄🛅🛜⚠🚸⛔🚫🚳🚭🚯🚱🚷📵🔞☢☣⬆↗➡↘⬇↙⬅↖↕↔↩↪⤴⤵🔃🔄🔙🔚🔛🔜🔝☯🔀🔁🔂▶⏩⏭⏯◀⏪⏮🔼⏫🔽⏬⏸⏹⏺⏏🎦🔅🔆📶📳📴⚧✖➕➖➗🟰♾‼⁉❓❕〰💱💲⚕♻⚜🔱📛🔰⭕✅☑✔❌❎➰➿〽✳✴❇©®™#🔠🔡🔢🔣🔤🅰🆎🅱🆑🆒🆓ℹ🆔Ⓜ🆕🆖🅾🆗🅿🆘🆙🆚🈁🔴🟠🟡🟢🔵🟣🟤⚫⚪🟥🟧🟨🟩🟦🟪🟫⬛⬜◼◻◾◽▪▫🔶🔷🔸🔹🔺🔻💠🔘🔳🔲🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦☹☻☺ツ☚☛☜☝☞☟✍✎✌❤❥♥♡❣♨☠☮☯☪☀☣☢☭♏♒♈☂☃☁♔♕♚۩♛✿❀❃❂❁♠♤♣♧⚜™®©₪★☆✮✯✪✣✤✥✲❈☄✦❉✧♱♰๑☿⋄⋅⋆⋇☼*✖✗✘✕✓✔ღ✄✂☎☏✆✉♪♩♫♬♭❝❞‘ﾟ.･‖﹉﹊﹍﹎︱︳︴﹏﹋﹌▁┠┨┯┷┏┓﹃﹄┗┛┳⊥╝╚╔╗╬═╓╩▪▫□〓≡▬▂▃▄■▀▢▅▆▇▌▐█▓▒░┇┅✚▣▧▨▤▥▦▩回ஐ⋖⋗▲△▼♢♦▽Δ►◄⇨◈◆◇◊⋘⋙⋚⋛⋜⋝⋞⋟⋩⋪⋫⋬⋭⋈⋉⋊⋋⋌⋍⋎⋏⋐⋑⋒⋓⋔⋕∵∴⋮⋯【】⊶╯ぃ↔↕↑↓→←↘↙➹ψ♆◠◡┌┐└┘∟「」◯●◕◐◑○◔⊙◎㊚㊛¤㊣∞☾☽◘◙の➀➁➂➃➄➅➆➇➈➉ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓤⓥⓦⓧⓨⓩ½⅓⅔¼¾⅛⅜⅝⅞℅
```
