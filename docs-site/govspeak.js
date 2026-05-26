// govspeak.js
//
// markdown-it plugin implementing a subset of GOV.UK publishing "GovSpeak"
// extensions, matched to the GOV.UK Design System (govuk-frontend v5) CSS
// classes.
//
// Adapted from the OfDIA data-schema-docs repo. Kept compatible so that
// source Markdown using `$CTA`, `$E`, `%...%`, `^...^` etc. renders the
// same way it would in a GOV.UK publishing pipeline.

function govSpeakPlugin(md) {
  // ---------------------------------------------------------------------------
  // Helpers for block rules
  // ---------------------------------------------------------------------------
  function createWrappedBlockRule(name, startRegex, endRegex, renderOpen, renderClose) {
    const openRuleName = `${name}_open`;
    const closeRuleName = `${name}_close`;

    md.block.ruler.before('paragraph', openRuleName, function (state, startLine, endLine, silent) {
      const pos = state.bMarks[startLine] + state.tShift[startLine];
      const max = state.eMarks[startLine];
      const line = state.src.slice(pos, max);

      const match = line.match(startRegex);
      if (!match) return false;
      if (silent) return true;

      let nextLine = startLine + 1;
      let found = false;
      while (nextLine < endLine) {
        const nextPos = state.bMarks[nextLine] + state.tShift[nextLine];
        const nextMax = state.eMarks[nextLine];
        const nextLineContent = state.src.slice(nextPos, nextMax);
        if (nextLineContent.match(endRegex)) { found = true; break; }
        nextLine++;
      }
      if (!found) return false;

      const openToken = state.push(openRuleName, 'div', 1);
      openToken.markup = match[0];
      openToken.map = [startLine, startLine + 1];

      // Gather inner lines and reparse them as block content so nested
      // markdown (paragraphs, lists, headings) renders correctly.
      const contentLines = [];
      for (let i = startLine + 1; i < nextLine; i++) {
        const contentPos = state.bMarks[i] + state.tShift[i];
        const contentMax = state.eMarks[i];
        contentLines.push(state.src.slice(contentPos, contentMax));
      }
      if (contentLines.length > 0) {
        state.md.block.parse(contentLines.join('\n'), state.md, state.env, state.tokens);
      }

      const closeToken = state.push(closeRuleName, 'div', -1);
      closeToken.markup = match[0];
      closeToken.map = [nextLine, nextLine + 1];

      state.line = nextLine + 1;
      return true;
    });

    md.renderer.rules[openRuleName] = renderOpen;
    md.renderer.rules[closeRuleName] = renderClose;
  }

  function createSingleLineBlockRule(name, regex, render) {
    md.block.ruler.before('paragraph', name, function (state, startLine, endLine, silent) {
      const pos = state.bMarks[startLine] + state.tShift[startLine];
      const max = state.eMarks[startLine];
      const line = state.src.slice(pos, max);

      const match = line.match(regex);
      if (!match) return false;
      if (silent) return true;

      const token = state.push(name, 'div', 0);
      token.content = match[1] || match[0];
      token.map = [startLine, startLine + 1];

      state.line = startLine + 1;
      return true;
    });

    md.renderer.rules[name] = render;
  }

  // ---------------------------------------------------------------------------
  // Wrapped block components
  // ---------------------------------------------------------------------------
  createWrappedBlockRule(
    'cta',
    /^\s*\$CTA\s*$/,
    /^\s*\$CTA\s*$/,
    () => '<div class="call-to-action">',
    () => '</div>'
  );

  createWrappedBlockRule(
    'example',
    /^\s*\$E\s*$/,
    /^\s*\$E\s*$/,
    () => '<div class="example">',
    () => '</div>'
  );

  createWrappedBlockRule(
    'contact',
    /^\s*\$C\s*$/,
    /^\s*\$C\s*$/,
    () => '<div class="contact">',
    () => '</div>'
  );

  createWrappedBlockRule(
    'download',
    /^\s*\$D\s*$/,
    /^\s*\$D\s*$/,
    () => '<div class="form-download">',
    () => '</div>'
  );

  createWrappedBlockRule(
    'address',
    /^\s*\$A\s*$/,
    /^\s*\$A\s*$/,
    () => '<div class="address"><div class="adr org fn">',
    () => '</div></div>'
  );

  // ---------------------------------------------------------------------------
  // Single-line blocks: ^help^ and %warning%
  // ---------------------------------------------------------------------------
  createSingleLineBlockRule(
    'help',
    /^\s*\^(.+)\^\s*$/,
    function (tokens, idx) {
      const content = md.utils.escapeHtml(tokens[idx].content);
      return `<div class="application-notice help-notice" role="note" aria-label="Help">
  <p class="govuk-body">${content}</p>
</div>`;
    }
  );

  createSingleLineBlockRule(
    'warning',
    /^\s*%(.+)%\s*$/,
    function (tokens, idx) {
      const content = md.utils.escapeHtml(tokens[idx].content);
      return `<div class="govuk-warning-text" role="note" aria-label="Information">
  <span class="govuk-warning-text__icon" aria-hidden="true">!</span>
  <strong class="govuk-warning-text__text">
    <span class="govuk-visually-hidden">Warning</span>
    ${content}
  </strong>
</div>`;
    }
  );

  // ---------------------------------------------------------------------------
  // GOV.UK styling — add classes to common elements
  // ---------------------------------------------------------------------------
  function addClassToToken(token, className) {
    const classIndex = token.attrIndex('class');
    if (classIndex < 0) token.attrPush(['class', className]);
    else token.attrs[classIndex][1] += ` ${className}`;
  }

  const defaultHeadingOpen =
    md.renderer.rules.heading_open ||
    function (tokens, idx, options, env, renderer) { return renderer.renderToken(tokens, idx, options); };
  const defaultHeadingClose =
    md.renderer.rules.heading_close ||
    function (tokens, idx, options, env, renderer) { return renderer.renderToken(tokens, idx, options); };

  md.renderer.rules.heading_open = function (tokens, idx, options, env, renderer) {
    const token = tokens[idx];
    // Layout provides the page's <h1>. Down-shift content headings so h1→h2.
    if (token.tag === 'h1') { token.tag = 'h2'; addClassToToken(token, 'govuk-heading-l'); }
    else if (token.tag === 'h2') addClassToToken(token, 'govuk-heading-l');
    else if (token.tag === 'h3') addClassToToken(token, 'govuk-heading-m');
    else if (token.tag === 'h4') addClassToToken(token, 'govuk-heading-s');
    return defaultHeadingOpen(tokens, idx, options, env, renderer);
  };

  md.renderer.rules.heading_close = function (tokens, idx, options, env, renderer) {
    const token = tokens[idx];
    if (token.tag === 'h1') token.tag = 'h2';
    return defaultHeadingClose(tokens, idx, options, env, renderer);
  };

  md.renderer.rules.paragraph_open = function (tokens, idx, options, env, renderer) {
    addClassToToken(tokens[idx], 'govuk-body');
    return renderer.renderToken(tokens, idx, options);
  };

  md.renderer.rules.blockquote_open = function (tokens, idx, options, env, renderer) {
    addClassToToken(tokens[idx], 'govuk-inset-text');
    return renderer.renderToken(tokens, idx, options);
  };

  md.renderer.rules.bullet_list_open = function (tokens, idx, options, env, renderer) {
    addClassToToken(tokens[idx], 'govuk-list govuk-list--bullet');
    return renderer.renderToken(tokens, idx, options);
  };

  md.renderer.rules.ordered_list_open = function (tokens, idx, options, env, renderer) {
    addClassToToken(tokens[idx], 'govuk-list govuk-list--number');
    return renderer.renderToken(tokens, idx, options);
  };

  // Links inside markdown should get the govuk-link class.
  const defaultLinkOpen =
    md.renderer.rules.link_open ||
    function (tokens, idx, options, env, renderer) { return renderer.renderToken(tokens, idx, options); };
  md.renderer.rules.link_open = function (tokens, idx, options, env, renderer) {
    addClassToToken(tokens[idx], 'govuk-link');
    return defaultLinkOpen(tokens, idx, options, env, renderer);
  };

  // Tables get the govuk-table scaffolding.
  md.renderer.rules.table_open = function () { return '<table class="govuk-table">\n'; };
  md.renderer.rules.thead_open = function () { return '<thead class="govuk-table__head">\n'; };
  md.renderer.rules.tbody_open = function () { return '<tbody class="govuk-table__body">\n'; };
  md.renderer.rules.tr_open = function () { return '<tr class="govuk-table__row">\n'; };
  md.renderer.rules.th_open = function () { return '<th scope="col" class="govuk-table__header">'; };
  md.renderer.rules.td_open = function () { return '<td class="govuk-table__cell">'; };
}

module.exports = govSpeakPlugin;
