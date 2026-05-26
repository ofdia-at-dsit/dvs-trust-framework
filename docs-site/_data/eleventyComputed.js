module.exports = {
  layout: (data) => data.layout || 'page',

  permalink: (data) => {
    const inputPath = data.page.inputPath || '';
    let p = inputPath.replace(/^(\.\.\/|\.\/)+/, '').replace(/\.md$/, '');

    if (p === 'README') return '/index.html';
    if (p.endsWith('/README')) return '/' + p.slice(0, -'/README'.length) + '/index.html';
    return '/' + p + '/index.html';
  },

  title: (data) => {
    if (data.title) return data.title;
    const slug = (data.page && data.page.fileSlug) || '';
    if (!slug || slug === 'README') return (data.site && data.site.title) ? data.site.title : 'Home';
    return slug;
  }
};
