// Exercise the exact Material search worker shipped by the build.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const site = path.resolve(__dirname, '../.cache/site');
const workers = path.join(site, 'assets/javascripts/workers');
const worker = fs.readdirSync(workers).find(name => name.endsWith('.min.js'));
const messages = [];
let listener;
const sandbox = {console, setTimeout, clearTimeout, URL, TextEncoder, TextDecoder};
sandbox.self = sandbox;
sandbox.addEventListener = (name, callback) => {if (name === 'message') listener = callback;};
sandbox.postMessage = message => messages.push(message);
const context = vm.createContext(sandbox);
sandbox.importScripts = (...urls) => {
  for (const url of urls) {
    const filename = path.resolve(workers, url);
    if (!filename.startsWith(site + path.sep)) throw new Error('Unexpected script path');
    vm.runInContext(fs.readFileSync(filename, 'utf8'), context, {filename});
  }
};
vm.runInContext(fs.readFileSync(path.join(workers, worker), 'utf8'), context, {filename: worker});
(async () => {
  const data = JSON.parse(fs.readFileSync(path.join(site, 'search/search_index.json'), 'utf8'));
  await listener({data: {type: 0, data: {...data, options: {suggest: true}}}});
  if (messages.pop()?.type !== 1) throw new Error('Worker did not become ready');
  const queries = [
    ['resource-pack.hosting.simple_self_host.server_address', 'itemsadder/configuration/config/#'],
    ['Inventory_Control.Group_Bazookas.Sounds_Exceeded', 'crackshot/configuration/general/#'],
    ['websocket.auth', 'typewriter/configuration/config/#'],
    ['blacklist.logging.database.dsn', 'worldguard/configuration/config/#'],
    ['storage-method', 'luckperms/configuration/config/#'],
    ['Afk.AutoAfkCmds', 'configuration/afk/'],
    ['EnchantExtractionFail', 'configuration/scavenge/'],
    ['DataBaseInfo.yml', 'configuration/'],
    ['typewriter.connect', 'typewriter/docs/helpful-features/commands/'],
    ['Give Item Action', 'typewriter/adapters/BasicAdapter/entries/action/give_item/'],
    ['交互边界', 'typewriter/'],
    ['过场动画', ['typewriter/', 'mythicmobs/wiki/cinematics/']],
    ['residence.randomtp', 'residence/permissions/#permission-residence.randomtp'],
    ['cmi.command.heal.others', 'commands/'],
    ['随机传送', 'commands/rtp/'],
    ['mmoitems.admin', 'mmoitems/general/permissions/#permission-mmoitems.admin'],
    ['mmocore.admin', 'mmocore/general/permissions/#permission-mmocore.admin'],
    ['mmoprofiles.admin', 'mmoprofiles/general/permissions/#permission-mmoprofiles.admin'],
    ['bountyhunters.add', 'bounty-hunters/general/permissions/#permission-bountyhunters.add'],
    ['灵魂绑定', 'mmoitems/features/soulbound/'],
    ['代理端档案', 'mmoprofiles/features/proxy-based/'],
    ['ItemsAdder 发光效果', 'itemsadder/wiki/adding-content/items/item-properties/light-emission/', true],
    ['Citizens NPC 点击命令', 'citizens/wiki/npc-commands/', true],
    ['WorldEdit 选区', 'worldedit/wiki/usage/regions/', true],
    ['WorldGuard 区域旗标', 'worldguard/wiki/regions/flags/', true],
    ['CrackShot 完整指南', 'crackshot/wiki/The-Complete-Guide-to-CrackShot/', true],
    ['MythicMobs 元技能', ['mythicmobs/wiki/skills/metaskills/', 'mythicmobs/wiki/skills/dynamic-metaskills/'], true]
  ];
  const results = [];
  for (const [query, expected, inTopResults] of queries) {
    if (process.argv[2] && query !== process.argv[2]) continue;
    await listener({data: {type: 2, data: query}});
    const response = messages.pop();
    const firstGroup = response?.data?.items?.[0] || [];
    const first = firstGroup[0];
    const candidates = inTopResults ? response.data.items.slice(0, 10).flat() : [first];
    const matching = candidates.find(item => (Array.isArray(expected) ? expected : [expected]).some(prefix => item?.location?.startsWith(prefix)));
    if (!matching) {console.error(JSON.stringify(response.data.items.slice(0,4).map(group => group.slice(0,2).map(item => ({location:item.location,title:item.title,score:item.score}))),null,2)); throw new Error(`Unexpected first result for ${query}: ${first?.location}`);};
    results.push({query, first: first.location, matched: matching.location, title: first.title.replace(/<[^>]*>/g, '')});
  }
  console.log(JSON.stringify({worker, queries: results}, null, 2));
})().catch(error => {console.error(error.message); process.exitCode = 1;});
