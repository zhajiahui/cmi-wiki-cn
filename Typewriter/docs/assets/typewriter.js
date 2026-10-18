/* Chinese rendering of the official 0.8.0 StatusEditor example.
 * Source: sources/repository/src/components/StatusEditor/index.tsx */
(() => {
  const states = {
    inactive: {title: '未激活的任务', description: '任务尚未开始，或当前不可用。', details: ['等待激活触发']},
    active: {title: '进行中的任务', description: '任务正在进行，会自动被追踪并显示。', details: ['玩家可以追踪进度', '显示任务目标', '玩家的行为可以推进任务']},
    completed: {title: '已完成的任务', description: '任务已完成，会自动隐藏并取消追踪。', details: ['玩家不再看到该任务']}
  };
  for (const editor of document.querySelectorAll('.tw-status-editor')) {
    let value = Number(editor.dataset.value || 0);
    const render = () => {
      const state = value <= 0 ? 'inactive' : value === 5 ? 'completed' : 'active';
      const data = states[state];
      editor.dataset.state = state;
      editor.querySelector('[data-status-title]').textContent = data.title;
      editor.querySelector('[data-status-description]').textContent = data.description;
      editor.querySelector('[data-status-fact]').textContent = `Permanent Fact = ${value}` + (value <= 0 ? ' (Inactive)' : value === 5 ? ' (Complete)' : '');
      editor.querySelector('output').textContent = String(value);
      editor.querySelector('[data-status-details]').replaceChildren(...data.details.map(text => {
        const item = document.createElement('li'); item.textContent = text; return item;
      }));
    };
    for (const button of editor.querySelectorAll('[data-change]')) {
      button.addEventListener('click', () => {value += Number(button.dataset.change); render();});
    }
    render();
  }
})();