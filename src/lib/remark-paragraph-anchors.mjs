// Adds id="p-1", id="p-2", ... to top-level paragraphs in entry markdown.
// Build-time only. Anchors are stable as long as paragraph order is stable.
// If a paragraph is inserted or deleted, downstream paragraph IDs shift.
// Read-through prose edits do not affect IDs; only structural inserts/deletes do.

export default function remarkParagraphAnchors() {
  return (tree) => {
    let n = 0;
    for (const node of tree.children) {
      if (node.type !== 'paragraph') continue;
      n += 1;
      const id = `p-${n}`;
      node.data = node.data || {};
      node.data.hProperties = node.data.hProperties || {};
      node.data.hProperties.id = id;
      node.data.hProperties['data-anchor'] = id;
    }
  };
}
