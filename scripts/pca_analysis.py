<!DOCTYPE html>

<html lang="en">
<head><meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>PCA</title><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<style type="text/css">
    pre { line-height: 125%; }
td.linenos .normal { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
span.linenos { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
.highlight .hll { background-color: var(--jp-cell-editor-active-background) }
.highlight { background: var(--jp-cell-editor-background); color: var(--jp-mirror-editor-variable-color) }
.highlight .c { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment */
.highlight .err { color: var(--jp-mirror-editor-error-color) } /* Error */
.highlight .k { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword */
.highlight .o { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator */
.highlight .p { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation */
.highlight .ch { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Multiline */
.highlight .cp { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Preproc */
.highlight .cpf { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Single */
.highlight .cs { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Special */
.highlight .kc { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Pseudo */
.highlight .kr { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Type */
.highlight .m { color: var(--jp-mirror-editor-number-color) } /* Literal.Number */
.highlight .s { color: var(--jp-mirror-editor-string-color) } /* Literal.String */
.highlight .ow { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator.Word */
.highlight .pm { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation.Marker */
.highlight .w { color: var(--jp-mirror-editor-variable-color) } /* Text.Whitespace */
.highlight .mb { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Bin */
.highlight .mf { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Float */
.highlight .mh { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Hex */
.highlight .mi { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer */
.highlight .mo { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Oct */
.highlight .sa { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Affix */
.highlight .sb { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Backtick */
.highlight .sc { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Char */
.highlight .dl { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Delimiter */
.highlight .sd { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Doc */
.highlight .s2 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Double */
.highlight .se { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Escape */
.highlight .sh { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Heredoc */
.highlight .si { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Interpol */
.highlight .sx { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Other */
.highlight .sr { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Regex */
.highlight .s1 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Single */
.highlight .ss { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Symbol */
.highlight .il { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer.Long */
  </style>
<style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
 * Mozilla scrollbar styling
 */

/* use standard opaque scrollbars for most nodes */
[data-jp-theme-scrollbars='true'] {
  scrollbar-color: rgb(var(--jp-scrollbar-thumb-color))
    var(--jp-scrollbar-background-color);
}

/* for code nodes, use a transparent style of scrollbar. These selectors
 * will match lower in the tree, and so will override the above */
[data-jp-theme-scrollbars='true'] .CodeMirror-hscrollbar,
[data-jp-theme-scrollbars='true'] .CodeMirror-vscrollbar {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
}

/* tiny scrollbar */

.jp-scrollbar-tiny {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
  scrollbar-width: thin;
}

/* tiny scrollbar */

.jp-scrollbar-tiny::-webkit-scrollbar,
.jp-scrollbar-tiny::-webkit-scrollbar-corner {
  background-color: transparent;
  height: 4px;
  width: 4px;
}

.jp-scrollbar-tiny::-webkit-scrollbar-thumb {
  background: rgba(var(--jp-scrollbar-thumb-color), 0.5);
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:horizontal {
  border-left: 0 solid transparent;
  border-right: 0 solid transparent;
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:vertical {
  border-top: 0 solid transparent;
  border-bottom: 0 solid transparent;
}

/*
 * Lumino
 */

.lm-ScrollBar[data-orientation='horizontal'] {
  min-height: 16px;
  max-height: 16px;
  min-width: 45px;
  border-top: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] {
  min-width: 16px;
  max-width: 16px;
  min-height: 45px;
  border-left: 1px solid #a0a0a0;
}

.lm-ScrollBar-button {
  background-color: #f0f0f0;
  background-position: center center;
  min-height: 15px;
  max-height: 15px;
  min-width: 15px;
  max-width: 15px;
}

.lm-ScrollBar-button:hover {
  background-color: #dadada;
}

.lm-ScrollBar-button.lm-mod-active {
  background-color: #cdcdcd;
}

.lm-ScrollBar-track {
  background: #f0f0f0;
}

.lm-ScrollBar-thumb {
  background: #cdcdcd;
}

.lm-ScrollBar-thumb:hover {
  background: #bababa;
}

.lm-ScrollBar-thumb.lm-mod-active {
  background: #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal'] .lm-ScrollBar-thumb {
  height: 100%;
  min-width: 15px;
  border-left: 1px solid #a0a0a0;
  border-right: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] .lm-ScrollBar-thumb {
  width: 100%;
  min-height: 15px;
  border-top: 1px solid #a0a0a0;
  border-bottom: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-left);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-right);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-up);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-down);
  background-size: 17px;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-Widget {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
}

.lm-Widget.lm-mod-hidden {
  display: none !important;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.lm-AccordionPanel[data-orientation='horizontal'] > .lm-AccordionPanel-title {
  /* Title is rotated for horizontal accordion panel using CSS */
  display: block;
  transform-origin: top left;
  transform: rotate(-90deg) translate(-100%);
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-CommandPalette {
  display: flex;
  flex-direction: column;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-CommandPalette-search {
  flex: 0 0 auto;
}

.lm-CommandPalette-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  min-height: 0;
  overflow: auto;
  list-style-type: none;
}

.lm-CommandPalette-header {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.lm-CommandPalette-item {
  display: flex;
  flex-direction: row;
}

.lm-CommandPalette-itemIcon {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemContent {
  flex: 1 1 auto;
  overflow: hidden;
}

.lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemLabel {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.lm-close-icon {
  border: 1px solid transparent;
  background-color: transparent;
  position: absolute;
  z-index: 1;
  right: 3%;
  top: 0;
  bottom: 0;
  margin: auto;
  padding: 7px 0;
  display: none;
  vertical-align: middle;
  outline: 0;
  cursor: pointer;
}
.lm-close-icon:after {
  content: 'X';
  display: block;
  width: 15px;
  height: 15px;
  text-align: center;
  color: #000;
  font-weight: normal;
  font-size: 12px;
  cursor: pointer;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-DockPanel {
  z-index: 0;
}

.lm-DockPanel-widget {
  z-index: 0;
}

.lm-DockPanel-tabBar {
  z-index: 1;
}

.lm-DockPanel-handle {
  z-index: 2;
}

.lm-DockPanel-handle.lm-mod-hidden {
  display: none !important;
}

.lm-DockPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}

.lm-DockPanel-handle[data-orientation='horizontal'] {
  cursor: ew-resize;
}

.lm-DockPanel-handle[data-orientation='vertical'] {
  cursor: ns-resize;
}

.lm-DockPanel-handle[data-orientation='horizontal']:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}

.lm-DockPanel-handle[data-orientation='vertical']:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}

.lm-DockPanel-overlay {
  z-index: 3;
  box-sizing: border-box;
  pointer-events: none;
}

.lm-DockPanel-overlay.lm-mod-hidden {
  display: none !important;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-Menu {
  z-index: 10000;
  position: absolute;
  white-space: nowrap;
  overflow-x: hidden;
  overflow-y: auto;
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-Menu-content {
  margin: 0;
  padding: 0;
  display: table;
  list-style-type: none;
}

.lm-Menu-item {
  display: table-row;
}

.lm-Menu-item.lm-mod-hidden,
.lm-Menu-item.lm-mod-collapsed {
  display: none !important;
}

.lm-Menu-itemIcon,
.lm-Menu-itemSubmenuIcon {
  display: table-cell;
  text-align: center;
}

.lm-Menu-itemLabel {
  display: table-cell;
  text-align: left;
}

.lm-Menu-itemShortcut {
  display: table-cell;
  text-align: right;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-MenuBar {
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-MenuBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  list-style-type: none;
}

.lm-MenuBar-item {
  box-sizing: border-box;
}

.lm-MenuBar-itemIcon,
.lm-MenuBar-itemLabel {
  display: inline-block;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-ScrollBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-ScrollBar[data-orientation='horizontal'] {
  flex-direction: row;
}

.lm-ScrollBar[data-orientation='vertical'] {
  flex-direction: column;
}

.lm-ScrollBar-button {
  box-sizing: border-box;
  flex: 0 0 auto;
}

.lm-ScrollBar-track {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  flex: 1 1 auto;
}

.lm-ScrollBar-thumb {
  box-sizing: border-box;
  position: absolute;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-SplitPanel-child {
  z-index: 0;
}

.lm-SplitPanel-handle {
  z-index: 1;
}

.lm-SplitPanel-handle.lm-mod-hidden {
  display: none !important;
}

.lm-SplitPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}

.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle {
  cursor: ew-resize;
}

.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle {
  cursor: ns-resize;
}

.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}

.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
  align-items: flex-end;
}

.lm-TabBar[data-orientation='vertical'] {
  flex-direction: column;
  align-items: flex-end;
}

.lm-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}

.lm-TabBar[data-orientation='horizontal'] > .lm-TabBar-content {
  flex-direction: row;
}

.lm-TabBar[data-orientation='vertical'] > .lm-TabBar-content {
  flex-direction: column;
}

.lm-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
  touch-action: none; /* Disable native Drag/Drop */
}

.lm-TabBar-tabIcon,
.lm-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}

.lm-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}

.lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing: border-box;
}

.lm-TabBar-tab.lm-mod-hidden {
  display: none !important;
}

.lm-TabBar-addButton.lm-mod-hidden {
  display: none !important;
}

.lm-TabBar.lm-mod-dragging .lm-TabBar-tab {
  position: relative;
}

.lm-TabBar.lm-mod-dragging[data-orientation='horizontal'] .lm-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}

.lm-TabBar.lm-mod-dragging[data-orientation='vertical'] .lm-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}

.lm-TabBar.lm-mod-dragging .lm-TabBar-tab.lm-mod-dragging {
  transition: none;
}

.lm-TabBar-tabLabel .lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing: border-box;
  background: inherit;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-TabPanel-tabBar {
  z-index: 1;
}

.lm-TabPanel-stackedPanel {
  z-index: 0;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapse {
  display: flex;
  flex-direction: column;
  align-items: stretch;
}

.jp-Collapse-header {
  padding: 1px 12px;
  background-color: var(--jp-layout-color1);
  border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
  color: var(--jp-ui-font-color1);
  cursor: pointer;
  display: flex;
  align-items: center;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  text-transform: uppercase;
  user-select: none;
}

.jp-Collapser-icon {
  height: 16px;
}

.jp-Collapse-header-collapsed .jp-Collapser-icon {
  transform: rotate(-90deg);
  margin: auto 0;
}

.jp-Collapser-title {
  line-height: 25px;
}

.jp-Collapse-contents {
  padding: 0 12px;
  background-color: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  overflow: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensureUiComponents() in @jupyterlab/buildutils */

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

/* Icons urls */

:root {
  --jp-icon-add-above: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzN18xOTQ5MikiPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGQ9Ik00Ljc1IDQuOTMwNjZINi42MjVWNi44MDU2NkM2LjYyNSA3LjAxMTkxIDYuNzkzNzUgNy4xODA2NiA3IDcuMTgwNjZDNy4yMDYyNSA3LjE4MDY2IDcuMzc1IDcuMDExOTEgNy4zNzUgNi44MDU2NlY0LjkzMDY2SDkuMjVDOS40NTYyNSA0LjkzMDY2IDkuNjI1IDQuNzYxOTEgOS42MjUgNC41NTU2NkM5LjYyNSA0LjM0OTQxIDkuNDU2MjUgNC4xODA2NiA5LjI1IDQuMTgwNjZINy4zNzVWMi4zMDU2NkM3LjM3NSAyLjA5OTQxIDcuMjA2MjUgMS45MzA2NiA3IDEuOTMwNjZDNi43OTM3NSAxLjkzMDY2IDYuNjI1IDIuMDk5NDEgNi42MjUgMi4zMDU2NlY0LjE4MDY2SDQuNzVDNC41NDM3NSA0LjE4MDY2IDQuMzc1IDQuMzQ5NDEgNC4zNzUgNC41NTU2NkM0LjM3NSA0Ljc2MTkxIDQuNTQzNzUgNC45MzA2NiA0Ljc1IDQuOTMwNjZaIiBmaWxsPSIjNjE2MTYxIiBzdHJva2U9IiM2MTYxNjEiIHN0cm9rZS13aWR0aD0iMC43Ii8+CjwvZz4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTExLjUgOS41VjExLjVMMi41IDExLjVWOS41TDExLjUgOS41Wk0xMiA4QzEyLjU1MjMgOCAxMyA4LjQ0NzcyIDEzIDlWMTJDMTMgMTIuNTUyMyAxMi41NTIzIDEzIDEyIDEzTDIgMTNDMS40NDc3MiAxMyAxIDEyLjU1MjMgMSAxMlY5QzEgOC40NDc3MiAxLjQ0NzcxIDggMiA4TDEyIDhaIiBmaWxsPSIjNjE2MTYxIi8+CjxkZWZzPgo8Y2xpcFBhdGggaWQ9ImNsaXAwXzEzN18xOTQ5MiI+CjxyZWN0IGNsYXNzPSJqcC1pY29uMyIgd2lkdGg9IjYiIGhlaWdodD0iNiIgZmlsbD0id2hpdGUiIHRyYW5zZm9ybT0ibWF0cml4KC0xIDAgMCAxIDEwIDEuNTU1NjYpIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==);
  --jp-icon-add-below: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzN18xOTQ5OCkiPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGQ9Ik05LjI1IDEwLjA2OTNMNy4zNzUgMTAuMDY5M0w3LjM3NSA4LjE5NDM0QzcuMzc1IDcuOTg4MDkgNy4yMDYyNSA3LjgxOTM0IDcgNy44MTkzNEM2Ljc5Mzc1IDcuODE5MzQgNi42MjUgNy45ODgwOSA2LjYyNSA4LjE5NDM0TDYuNjI1IDEwLjA2OTNMNC43NSAxMC4wNjkzQzQuNTQzNzUgMTAuMDY5MyA0LjM3NSAxMC4yMzgxIDQuMzc1IDEwLjQ0NDNDNC4zNzUgMTAuNjUwNiA0LjU0Mzc1IDEwLjgxOTMgNC43NSAxMC44MTkzTDYuNjI1IDEwLjgxOTNMNi42MjUgMTIuNjk0M0M2LjYyNSAxMi45MDA2IDYuNzkzNzUgMTMuMDY5MyA3IDEzLjA2OTNDNy4yMDYyNSAxMy4wNjkzIDcuMzc1IDEyLjkwMDYgNy4zNzUgMTIuNjk0M0w3LjM3NSAxMC44MTkzTDkuMjUgMTAuODE5M0M5LjQ1NjI1IDEwLjgxOTMgOS42MjUgMTAuNjUwNiA5LjYyNSAxMC40NDQzQzkuNjI1IDEwLjIzODEgOS40NTYyNSAxMC4wNjkzIDkuMjUgMTAuMDY5M1oiIGZpbGw9IiM2MTYxNjEiIHN0cm9rZT0iIzYxNjE2MSIgc3Ryb2tlLXdpZHRoPSIwLjciLz4KPC9nPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMi41IDUuNUwyLjUgMy41TDExLjUgMy41TDExLjUgNS41TDIuNSA1LjVaTTIgN0MxLjQ0NzcyIDcgMSA2LjU1MjI4IDEgNkwxIDNDMSAyLjQ0NzcyIDEuNDQ3NzIgMiAyIDJMMTIgMkMxMi41NTIzIDIgMTMgMi40NDc3MiAxMyAzTDEzIDZDMTMgNi41NTIyOSAxMi41NTIzIDcgMTIgN0wyIDdaIiBmaWxsPSIjNjE2MTYxIi8+CjxkZWZzPgo8Y2xpcFBhdGggaWQ9ImNsaXAwXzEzN18xOTQ5OCI+CjxyZWN0IGNsYXNzPSJqcC1pY29uMyIgd2lkdGg9IjYiIGhlaWdodD0iNiIgZmlsbD0id2hpdGUiIHRyYW5zZm9ybT0ibWF0cml4KDEgMS43NDg0NmUtMDcgMS43NDg0NmUtMDcgLTEgNCAxMy40NDQzKSIvPgo8L2NsaXBQYXRoPgo8L2RlZnM+Cjwvc3ZnPgo=);
  --jp-icon-add: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDEzaC02djZoLTJ2LTZINXYtMmg2VjVoMnY2aDZ2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-bell: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE2IDE2IiB2ZXJzaW9uPSIxLjEiPgogICA8cGF0aCBjbGFzcz0ianAtaWNvbjIganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMzMzMzMzIgogICAgICBkPSJtOCAwLjI5Yy0xLjQgMC0yLjcgMC43My0zLjYgMS44LTEuMiAxLjUtMS40IDMuNC0xLjUgNS4yLTAuMTggMi4yLTAuNDQgNC0yLjMgNS4zbDAuMjggMS4zaDVjMC4wMjYgMC42NiAwLjMyIDEuMSAwLjcxIDEuNSAwLjg0IDAuNjEgMiAwLjYxIDIuOCAwIDAuNTItMC40IDAuNi0xIDAuNzEtMS41aDVsMC4yOC0xLjNjLTEuOS0wLjk3LTIuMi0zLjMtMi4zLTUuMy0wLjEzLTEuOC0wLjI2LTMuNy0xLjUtNS4yLTAuODUtMS0yLjItMS44LTMuNi0xLjh6bTAgMS40YzAuODggMCAxLjkgMC41NSAyLjUgMS4zIDAuODggMS4xIDEuMSAyLjcgMS4yIDQuNCAwLjEzIDEuNyAwLjIzIDMuNiAxLjMgNS4yaC0xMGMxLjEtMS42IDEuMi0zLjQgMS4zLTUuMiAwLjEzLTEuNyAwLjMtMy4zIDEuMi00LjQgMC41OS0wLjcyIDEuNi0xLjMgMi41LTEuM3ptLTAuNzQgMTJoMS41Yy0wLjAwMTUgMC4yOCAwLjAxNSAwLjc5LTAuNzQgMC43OS0wLjczIDAuMDAxNi0wLjcyLTAuNTMtMC43NC0wLjc5eiIgLz4KPC9zdmc+Cg==);
  --jp-icon-bug-dot: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiPgogICAgICAgIDxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMTcuMTkgOEgyMFYxMEgxNy45MUMxNy45NiAxMC4zMyAxOCAxMC42NiAxOCAxMVYxMkgyMFYxNEgxOC41SDE4VjE0LjAyNzVDMTUuNzUgMTQuMjc2MiAxNCAxNi4xODM3IDE0IDE4LjVDMTQgMTkuMjA4IDE0LjE2MzUgMTkuODc3OSAxNC40NTQ5IDIwLjQ3MzlDMTMuNzA2MyAyMC44MTE3IDEyLjg3NTcgMjEgMTIgMjFDOS43OCAyMSA3Ljg1IDE5Ljc5IDYuODEgMThINFYxNkg2LjA5QzYuMDQgMTUuNjcgNiAxNS4zNCA2IDE1VjE0SDRWMTJINlYxMUM2IDEwLjY2IDYuMDQgMTAuMzMgNi4wOSAxMEg0VjhINi44MUM3LjI2IDcuMjIgNy44OCA2LjU1IDguNjIgNi4wNEw3IDQuNDFMOC40MSAzTDEwLjU5IDUuMTdDMTEuMDQgNS4wNiAxMS41MSA1IDEyIDVDMTIuNDkgNSAxMi45NiA1LjA2IDEzLjQyIDUuMTdMMTUuNTkgM0wxNyA0LjQxTDE1LjM3IDYuMDRDMTYuMTIgNi41NSAxNi43NCA3LjIyIDE3LjE5IDhaTTEwIDE2SDE0VjE0SDEwVjE2Wk0xMCAxMkgxNFYxMEgxMFYxMloiIGZpbGw9IiM2MTYxNjEiLz4KICAgICAgICA8cGF0aCBkPSJNMjIgMTguNUMyMiAyMC40MzMgMjAuNDMzIDIyIDE4LjUgMjJDMTYuNTY3IDIyIDE1IDIwLjQzMyAxNSAxOC41QzE1IDE2LjU2NyAxNi41NjcgMTUgMTguNSAxNUMyMC40MzMgMTUgMjIgMTYuNTY3IDIyIDE4LjVaIiBmaWxsPSIjNjE2MTYxIi8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-bug: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0yMCA4aC0yLjgxYy0uNDUtLjc4LTEuMDctMS40NS0xLjgyLTEuOTZMMTcgNC40MSAxNS41OSAzbC0yLjE3IDIuMTdDMTIuOTYgNS4wNiAxMi40OSA1IDEyIDVjLS40OSAwLS45Ni4wNi0xLjQxLjE3TDguNDEgMyA3IDQuNDFsMS42MiAxLjYzQzcuODggNi41NSA3LjI2IDcuMjIgNi44MSA4SDR2MmgyLjA5Yy0uMDUuMzMtLjA5LjY2LS4wOSAxdjFINHYyaDJ2MWMwIC4zNC4wNC42Ny4wOSAxSDR2MmgyLjgxYzEuMDQgMS43OSAyLjk3IDMgNS4xOSAzczQuMTUtMS4yMSA1LjE5LTNIMjB2LTJoLTIuMDljLjA1LS4zMy4wOS0uNjYuMDktMXYtMWgydi0yaC0ydi0xYzAtLjM0LS4wNC0uNjctLjA5LTFIMjBWOHptLTYgOGgtNHYtMmg0djJ6bTAtNGgtNHYtMmg0djJ6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-build: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE0LjkgMTcuNDVDMTYuMjUgMTcuNDUgMTcuMzUgMTYuMzUgMTcuMzUgMTVDMTcuMzUgMTMuNjUgMTYuMjUgMTIuNTUgMTQuOSAxMi41NUMxMy41NCAxMi41NSAxMi40NSAxMy42NSAxMi40NSAxNUMxMi40NSAxNi4zNSAxMy41NCAxNy40NSAxNC45IDE3LjQ1Wk0yMC4xIDE1LjY4TDIxLjU4IDE2Ljg0QzIxLjcxIDE2Ljk1IDIxLjc1IDE3LjEzIDIxLjY2IDE3LjI5TDIwLjI2IDE5LjcxQzIwLjE3IDE5Ljg2IDIwIDE5LjkyIDE5LjgzIDE5Ljg2TDE4LjA5IDE5LjE2QzE3LjczIDE5LjQ0IDE3LjMzIDE5LjY3IDE2LjkxIDE5Ljg1TDE2LjY0IDIxLjdDMTYuNjIgMjEuODcgMTYuNDcgMjIgMTYuMyAyMkgxMy41QzEzLjMyIDIyIDEzLjE4IDIxLjg3IDEzLjE1IDIxLjdMMTIuODkgMTkuODVDMTIuNDYgMTkuNjcgMTIuMDcgMTkuNDQgMTEuNzEgMTkuMTZMOS45NjAwMiAxOS44NkM5LjgxMDAyIDE5LjkyIDkuNjIwMDIgMTkuODYgOS41NDAwMiAxOS43MUw4LjE0MDAyIDE3LjI5QzguMDUwMDIgMTcuMTMgOC4wOTAwMiAxNi45NSA4LjIyMDAyIDE2Ljg0TDkuNzAwMDIgMTUuNjhMOS42NTAwMSAxNUw5LjcwMDAyIDE0LjMxTDguMjIwMDIgMTMuMTZDOC4wOTAwMiAxMy4wNSA4LjA1MDAyIDEyLjg2IDguMTQwMDIgMTIuNzFMOS41NDAwMiAxMC4yOUM5LjYyMDAyIDEwLjEzIDkuODEwMDIgMTAuMDcgOS45NjAwMiAxMC4xM0wxMS43MSAxMC44NEMxMi4wNyAxMC41NiAxMi40NiAxMC4zMiAxMi44OSAxMC4xNUwxMy4xNSA4LjI4OTk4QzEzLjE4IDguMTI5OTggMTMuMzIgNy45OTk5OCAxMy41IDcuOTk5OThIMTYuM0MxNi40NyA3Ljk5OTk4IDE2LjYyIDguMTI5OTggMTYuNjQgOC4yODk5OEwxNi45MSAxMC4xNUMxNy4zMyAxMC4zMiAxNy43MyAxMC41NiAxOC4wOSAxMC44NEwxOS44MyAxMC4xM0MyMCAxMC4wNyAyMC4xNyAxMC4xMyAyMC4yNiAxMC4yOUwyMS42NiAxMi43MUMyMS43NSAxMi44NiAyMS43MSAxMy4wNSAyMS41OCAxMy4xNkwyMC4xIDE0LjMxTDIwLjE1IDE1TDIwLjEgMTUuNjhaIi8+CiAgICA8cGF0aCBkPSJNNy4zMjk2NiA3LjQ0NDU0QzguMDgzMSA3LjAwOTU0IDguMzM5MzIgNi4wNTMzMiA3LjkwNDMyIDUuMjk5ODhDNy40NjkzMiA0LjU0NjQzIDYuNTA4MSA0LjI4MTU2IDUuNzU0NjYgNC43MTY1NkM1LjM5MTc2IDQuOTI2MDggNS4xMjY5NSA1LjI3MTE4IDUuMDE4NDkgNS42NzU5NEM0LjkxMDA0IDYuMDgwNzEgNC45NjY4MiA2LjUxMTk4IDUuMTc2MzQgNi44NzQ4OEM1LjYxMTM0IDcuNjI4MzIgNi41NzYyMiA3Ljg3OTU0IDcuMzI5NjYgNy40NDQ1NFpNOS42NTcxOCA0Ljc5NTkzTDEwLjg2NzIgNC45NTE3OUMxMC45NjI4IDQuOTc3NDEgMTEuMDQwMiA1LjA3MTMzIDExLjAzODIgNS4xODc5M0wxMS4wMzg4IDYuOTg4OTNDMTEuMDQ1NSA3LjEwMDU0IDEwLjk2MTYgNy4xOTUxOCAxMC44NTUgNy4yMTA1NEw5LjY2MDAxIDcuMzgwODNMOS4yMzkxNSA4LjEzMTg4TDkuNjY5NjEgOS4yNTc0NUM5LjcwNzI5IDkuMzYyNzEgOS42NjkzNCA5LjQ3Njk5IDkuNTc0MDggOS41MzE5OUw4LjAxNTIzIDEwLjQzMkM3LjkxMTMxIDEwLjQ5MiA3Ljc5MzM3IDEwLjQ2NzcgNy43MjEwNSAxMC4zODI0TDYuOTg3NDggOS40MzE4OEw2LjEwOTMxIDkuNDMwODNMNS4zNDcwNCAxMC4zOTA1QzUuMjg5MDkgMTAuNDcwMiA1LjE3MzgzIDEwLjQ5MDUgNS4wNzE4NyAxMC40MzM5TDMuNTEyNDUgOS41MzI5M0MzLjQxMDQ5IDkuNDc2MzMgMy4zNzY0NyA5LjM1NzQxIDMuNDEwNzUgOS4yNTY3OUwzLjg2MzQ3IDguMTQwOTNMMy42MTc0OSA3Ljc3NDg4TDMuNDIzNDcgNy4zNzg4M0wyLjIzMDc1IDcuMjEyOTdDMi4xMjY0NyA3LjE5MjM1IDIuMDQwNDkgNy4xMDM0MiAyLjA0MjQ1IDYuOTg2ODJMMi4wNDE4NyA1LjE4NTgyQzIuMDQzODMgNS4wNjkyMiAyLjExOTA5IDQuOTc5NTggMi4yMTcwNCA0Ljk2OTIyTDMuNDIwNjUgNC43OTM5M0wzLjg2NzQ5IDQuMDI3ODhMMy40MTEwNSAyLjkxNzMxQzMuMzczMzcgMi44MTIwNCAzLjQxMTMxIDIuNjk3NzYgMy41MTUyMyAyLjYzNzc2TDUuMDc0MDggMS43Mzc3NkM1LjE2OTM0IDEuNjgyNzYgNS4yODcyOSAxLjcwNzA0IDUuMzU5NjEgMS43OTIzMUw2LjExOTE1IDIuNzI3ODhMNi45ODAwMSAyLjczODkzTDcuNzI0OTYgMS43ODkyMkM3Ljc5MTU2IDEuNzA0NTggNy45MTU0OCAxLjY3OTIyIDguMDA4NzkgMS43NDA4Mkw5LjU2ODIxIDIuNjQxODJDOS42NzAxNyAyLjY5ODQyIDkuNzEyODUgMi44MTIzNCA5LjY4NzIzIDIuOTA3OTdMOS4yMTcxOCA0LjAzMzgzTDkuNDYzMTYgNC4zOTk4OEw5LjY1NzE4IDQuNzk1OTNaIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iOS45LDEzLjYgMy42LDcuNCA0LjQsNi42IDkuOSwxMi4yIDE1LjQsNi43IDE2LjEsNy40ICIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNS45TDksOS43bDMuOC0zLjhsMS4yLDEuMmwtNC45LDVsLTQuOS01TDUuMiw1Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNy41TDksMTEuMmwzLjgtMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-left: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik0xMC44LDEyLjhMNy4xLDlsMy44LTMuOGwwLDcuNkgxMC44eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-right: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik03LjIsNS4yTDEwLjksOWwtMy44LDMuOFY1LjJINy4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-up-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iMTUuNCwxMy4zIDkuOSw3LjcgNC40LDEzLjIgMy42LDEyLjUgOS45LDYuMyAxNi4xLDEyLjYgIi8+Cgk8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-up: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik01LjIsMTAuNUw5LDYuOGwzLjgsMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-case-sensitive: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgogIDxnIGNsYXNzPSJqcC1pY29uLWFjY2VudDIiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTcuNiw4aDAuOWwzLjUsOGgtMS4xTDEwLDE0SDZsLTAuOSwySDRMNy42LDh6IE04LDkuMUw2LjQsMTNoMy4yTDgsOS4xeiIvPgogICAgPHBhdGggZD0iTTE2LjYsOS44Yy0wLjIsMC4xLTAuNCwwLjEtMC43LDAuMWMtMC4yLDAtMC40LTAuMS0wLjYtMC4yYy0wLjEtMC4xLTAuMi0wLjQtMC4yLTAuNyBjLTAuMywwLjMtMC42LDAuNS0wLjksMC43Yy0wLjMsMC4xLTAuNywwLjItMS4xLDAuMmMtMC4zLDAtMC41LDAtMC43LTAuMWMtMC4yLTAuMS0wLjQtMC4yLTAuNi0wLjNjLTAuMi0wLjEtMC4zLTAuMy0wLjQtMC41IGMtMC4xLTAuMi0wLjEtMC40LTAuMS0wLjdjMC0wLjMsMC4xLTAuNiwwLjItMC44YzAuMS0wLjIsMC4zLTAuNCwwLjQtMC41QzEyLDcsMTIuMiw2LjksMTIuNSw2LjhjMC4yLTAuMSwwLjUtMC4xLDAuNy0wLjIgYzAuMy0wLjEsMC41LTAuMSwwLjctMC4xYzAuMiwwLDAuNC0wLjEsMC42LTAuMWMwLjIsMCwwLjMtMC4xLDAuNC0wLjJjMC4xLTAuMSwwLjItMC4yLDAuMi0wLjRjMC0xLTEuMS0xLTEuMy0xIGMtMC40LDAtMS40LDAtMS40LDEuMmgtMC45YzAtMC40LDAuMS0wLjcsMC4yLTFjMC4xLTAuMiwwLjMtMC40LDAuNS0wLjZjMC4yLTAuMiwwLjUtMC4zLDAuOC0wLjNDMTMuMyw0LDEzLjYsNCwxMy45LDQgYzAuMywwLDAuNSwwLDAuOCwwLjFjMC4zLDAsMC41LDAuMSwwLjcsMC4yYzAuMiwwLjEsMC40LDAuMywwLjUsMC41QzE2LDUsMTYsNS4yLDE2LDUuNnYyLjljMCwwLjIsMCwwLjQsMCwwLjUgYzAsMC4xLDAuMSwwLjIsMC4zLDAuMmMwLjEsMCwwLjIsMCwwLjMsMFY5Ljh6IE0xNS4yLDYuOWMtMS4yLDAuNi0zLjEsMC4yLTMuMSwxLjRjMCwxLjQsMy4xLDEsMy4xLTAuNVY2Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-check: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik05IDE2LjE3TDQuODMgMTJsLTEuNDIgMS40MUw5IDE5IDIxIDdsLTEuNDEtMS40MXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-circle-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDJDNi40NyAyIDIgNi40NyAyIDEyczQuNDcgMTAgMTAgMTAgMTAtNC40NyAxMC0xMFMxNy41MyAyIDEyIDJ6bTAgMThjLTQuNDEgMC04LTMuNTktOC04czMuNTktOCA4LTggOCAzLjU5IDggOC0zLjU5IDgtOCA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-circle: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iOSIgY3k9IjkiIHI9IjgiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-clear: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8bWFzayBpZD0iZG9udXRIb2xlIj4KICAgIDxyZWN0IHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0id2hpdGUiIC8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSI4IiBmaWxsPSJibGFjayIvPgogIDwvbWFzaz4KCiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxyZWN0IGhlaWdodD0iMTgiIHdpZHRoPSIyIiB4PSIxMSIgeT0iMyIgdHJhbnNmb3JtPSJyb3RhdGUoMzE1LCAxMiwgMTIpIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIgbWFzaz0idXJsKCNkb251dEhvbGUpIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-close: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1ub25lIGpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIGpwLWljb24zLWhvdmVyIiBmaWxsPSJub25lIj4KICAgIDxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjExIi8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIGpwLWljb24tYWNjZW50Mi1ob3ZlciIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMTkgNi40MUwxNy41OSA1IDEyIDEwLjU5IDYuNDEgNSA1IDYuNDEgMTAuNTkgMTIgNSAxNy41OSA2LjQxIDE5IDEyIDEzLjQxIDE3LjU5IDE5IDE5IDE3LjU5IDEzLjQxIDEyeiIvPgogIDwvZz4KCiAgPGcgY2xhc3M9ImpwLWljb24tbm9uZSBqcC1pY29uLWJ1c3kiIGZpbGw9Im5vbmUiPgogICAgPGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-code-check: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBzaGFwZS1yZW5kZXJpbmc9Imdlb21ldHJpY1ByZWNpc2lvbiI+CiAgICA8cGF0aCBkPSJNNi41OSwzLjQxTDIsOEw2LjU5LDEyLjZMOCwxMS4xOEw0LjgyLDhMOCw0LjgyTDYuNTksMy40MU0xMi40MSwzLjQxTDExLDQuODJMMTQuMTgsOEwxMSwxMS4xOEwxMi40MSwxMi42TDE3LDhMMTIuNDEsMy40MU0yMS41OSwxMS41OUwxMy41LDE5LjY4TDkuODMsMTZMOC40MiwxNy40MUwxMy41LDIyLjVMMjMsMTNMMjEuNTksMTEuNTlaIiAvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-code: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTExLjQgMTguNkw2LjggMTRMMTEuNCA5LjRMMTAgOEw0IDE0TDEwIDIwTDExLjQgMTguNlpNMTYuNiAxOC42TDIxLjIgMTRMMTYuNiA5LjRMMTggOEwyNCAxNEwxOCAyMEwxNi42IDE4LjZWMTguNloiLz4KCTwvZz4KPC9zdmc+Cg==);
  --jp-icon-collapse-all: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTggMmMxIDAgMTEgMCAxMiAwczIgMSAyIDJjMCAxIDAgMTEgMCAxMnMwIDItMiAyQzIwIDE0IDIwIDQgMjAgNFMxMCA0IDYgNGMwLTIgMS0yIDItMnoiIC8+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTE4IDhjMC0xLTEtMi0yLTJTNSA2IDQgNnMtMiAxLTIgMmMwIDEgMCAxMSAwIDEyczEgMiAyIDJjMSAwIDExIDAgMTIgMHMyLTEgMi0yYzAtMSAwLTExIDAtMTJ6bS0yIDB2MTJINFY4eiIgLz4KICAgICAgICA8cGF0aCBkPSJNNiAxM3YyaDh2LTJ6IiAvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-console: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwMCAyMDAiPgogIDxnIGNsYXNzPSJqcC1jb25zb2xlLWljb24tYmFja2dyb3VuZC1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMjg4RDEiPgogICAgPHBhdGggZD0iTTIwIDE5LjhoMTYwdjE1OS45SDIweiIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtY29uc29sZS1pY29uLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIiBmaWxsPSIjZmZmIj4KICAgIDxwYXRoIGQ9Ik0xMDUgMTI3LjNoNDB2MTIuOGgtNDB6TTUxLjEgNzdMNzQgOTkuOWwtMjMuMyAyMy4zIDEwLjUgMTAuNSAyMy4zLTIzLjNMOTUgOTkuOSA4NC41IDg5LjQgNjEuNiA2Ni41eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-copy: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTExLjksMUgzLjJDMi40LDEsMS43LDEuNywxLjcsMi41djEwLjJoMS41VjIuNWg4LjdWMXogTTE0LjEsMy45aC04Yy0wLjgsMC0xLjUsMC43LTEuNSwxLjV2MTAuMmMwLDAuOCwwLjcsMS41LDEuNSwxLjVoOCBjMC44LDAsMS41LTAuNywxLjUtMS41VjUuNEMxNS41LDQuNiwxNC45LDMuOSwxNC4xLDMuOXogTTE0LjEsMTUuNWgtOFY1LjRoOFYxNS41eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-copyright: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDI0IDI0IiBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCI+CiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0xMS44OCw5LjE0YzEuMjgsMC4wNiwxLjYxLDEuMTUsMS42MywxLjY2aDEuNzljLTAuMDgtMS45OC0xLjQ5LTMuMTktMy40NS0zLjE5QzkuNjQsNy42MSw4LDksOCwxMi4xNCBjMCwxLjk0LDAuOTMsNC4yNCwzLjg0LDQuMjRjMi4yMiwwLDMuNDEtMS42NSwzLjQ0LTIuOTVoLTEuNzljLTAuMDMsMC41OS0wLjQ1LDEuMzgtMS42MywxLjQ0QzEwLjU1LDE0LjgzLDEwLDEzLjgxLDEwLDEyLjE0IEMxMCw5LjI1LDExLjI4LDkuMTYsMTEuODgsOS4xNHogTTEyLDJDNi40OCwyLDIsNi40OCwyLDEyczQuNDgsMTAsMTAsMTBzMTAtNC40OCwxMC0xMFMxNy41MiwyLDEyLDJ6IE0xMiwyMGMtNC40MSwwLTgtMy41OS04LTggczMuNTktOCw4LThzOCwzLjU5LDgsOFMxNi40MSwyMCwxMiwyMHoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-cut: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkuNjQgNy42NGMuMjMtLjUuMzYtMS4wNS4zNi0xLjY0IDAtMi4yMS0xLjc5LTQtNC00UzIgMy43OSAyIDZzMS43OSA0IDQgNGMuNTkgMCAxLjE0LS4xMyAxLjY0LS4zNkwxMCAxMmwtMi4zNiAyLjM2QzcuMTQgMTQuMTMgNi41OSAxNCA2IDE0Yy0yLjIxIDAtNCAxLjc5LTQgNHMxLjc5IDQgNCA0IDQtMS43OSA0LTRjMC0uNTktLjEzLTEuMTQtLjM2LTEuNjRMMTIgMTRsNyA3aDN2LTFMOS42NCA3LjY0ek02IDhjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTAgMTJjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTYtNy41Yy0uMjggMC0uNS0uMjItLjUtLjVzLjIyLS41LjUtLjUuNS4yMi41LjUtLjIyLjUtLjUuNXpNMTkgM2wtNiA2IDIgMiA3LTdWM3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-delete: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2cHgiIGhlaWdodD0iMTZweCI+CiAgICA8cGF0aCBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIiAvPgogICAgPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjI2MjYyIiBkPSJNNiAxOWMwIDEuMS45IDIgMiAyaDhjMS4xIDAgMi0uOSAyLTJWN0g2djEyek0xOSA0aC0zLjVsLTEtMWgtNWwtMSAxSDV2MmgxNFY0eiIgLz4KPC9zdmc+Cg==);
  --jp-icon-download: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDloLTRWM0g5djZINWw3IDcgNy03ek01IDE4djJoMTR2LTJINXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-duplicate: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTIuNzk5OTggMC44NzVIOC44OTU4MkM5LjIwMDYxIDAuODc1IDkuNDQ5OTggMS4xMzkxNCA5LjQ0OTk4IDEuNDYxOThDOS40NDk5OCAxLjc4NDgyIDkuMjAwNjEgMi4wNDg5NiA4Ljg5NTgyIDIuMDQ4OTZIMy4zNTQxNUMzLjA0OTM2IDIuMDQ4OTYgMi43OTk5OCAyLjMxMzEgMi43OTk5OCAyLjYzNTk0VjkuNjc5NjlDMi43OTk5OCAxMC4wMDI1IDIuNTUwNjEgMTAuMjY2NyAyLjI0NTgyIDEwLjI2NjdDMS45NDEwMyAxMC4yNjY3IDEuNjkxNjUgMTAuMDAyNSAxLjY5MTY1IDkuNjc5NjlWMi4wNDg5NkMxLjY5MTY1IDEuNDAzMjggMi4xOTA0IDAuODc1IDIuNzk5OTggMC44NzVaTTUuMzY2NjUgMTEuOVY0LjU1SDExLjA4MzNWMTEuOUg1LjM2NjY1Wk00LjE0MTY1IDQuMTQxNjdDNC4xNDE2NSAzLjY5MDYzIDQuNTA3MjggMy4zMjUgNC45NTgzMiAzLjMyNUgxMS40OTE3QzExLjk0MjcgMy4zMjUgMTIuMzA4MyAzLjY5MDYzIDEyLjMwODMgNC4xNDE2N1YxMi4zMDgzQzEyLjMwODMgMTIuNzU5NCAxMS45NDI3IDEzLjEyNSAxMS40OTE3IDEzLjEyNUg0Ljk1ODMyQzQuNTA3MjggMTMuMTI1IDQuMTQxNjUgMTIuNzU5NCA0LjE0MTY1IDEyLjMwODNWNC4xNDE2N1oiIGZpbGw9IiM2MTYxNjEiLz4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNOS40MzU3NCA4LjI2NTA3SDguMzY0MzFWOS4zMzY1QzguMzY0MzEgOS40NTQzNSA4LjI2Nzg4IDkuNTUwNzggOC4xNTAwMiA5LjU1MDc4QzguMDMyMTcgOS41NTA3OCA3LjkzNTc0IDkuNDU0MzUgNy45MzU3NCA5LjMzNjVWOC4yNjUwN0g2Ljg2NDMxQzYuNzQ2NDUgOC4yNjUwNyA2LjY1MDAyIDguMTY4NjQgNi42NTAwMiA4LjA1MDc4QzYuNjUwMDIgNy45MzI5MiA2Ljc0NjQ1IDcuODM2NSA2Ljg2NDMxIDcuODM2NUg3LjkzNTc0VjYuNzY1MDdDNy45MzU3NCA2LjY0NzIxIDguMDMyMTcgNi41NTA3OCA4LjE1MDAyIDYuNTUwNzhDOC4yNjc4OCA2LjU1MDc4IDguMzY0MzEgNi42NDcyMSA4LjM2NDMxIDYuNzY1MDdWNy44MzY1SDkuNDM1NzRDOS41NTM2IDcuODM2NSA5LjY1MDAyIDcuOTMyOTIgOS42NTAwMiA4LjA1MDc4QzkuNjUwMDIgOC4xNjg2NCA5LjU1MzYgOC4yNjUwNyA5LjQzNTc0IDguMjY1MDdaIiBmaWxsPSIjNjE2MTYxIiBzdHJva2U9IiM2MTYxNjEiIHN0cm9rZS13aWR0aD0iMC41Ii8+Cjwvc3ZnPgo=);
  --jp-icon-edit: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMgMTcuMjVWMjFoMy43NUwxNy44MSA5Ljk0bC0zLjc1LTMuNzVMMyAxNy4yNXpNMjAuNzEgNy4wNGMuMzktLjM5LjM5LTEuMDIgMC0xLjQxbC0yLjM0LTIuMzRjLS4zOS0uMzktMS4wMi0uMzktMS40MSAwbC0xLjgzIDEuODMgMy43NSAzLjc1IDEuODMtMS44M3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-ellipses: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iNSIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxOSIgY3k9IjEyIiByPSIyIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-error: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjE5IiByPSIyIi8+PHBhdGggZD0iTTEwIDNoNHYxMmgtNHoiLz48L2c+CjxwYXRoIGZpbGw9Im5vbmUiIGQ9Ik0wIDBoMjR2MjRIMHoiLz4KPC9zdmc+Cg==);
  --jp-icon-expand-all: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTggMmMxIDAgMTEgMCAxMiAwczIgMSAyIDJjMCAxIDAgMTEgMCAxMnMwIDItMiAyQzIwIDE0IDIwIDQgMjAgNFMxMCA0IDYgNGMwLTIgMS0yIDItMnoiIC8+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTE4IDhjMC0xLTEtMi0yLTJTNSA2IDQgNnMtMiAxLTIgMmMwIDEgMCAxMSAwIDEyczEgMiAyIDJjMSAwIDExIDAgMTIgMHMyLTEgMi0yYzAtMSAwLTExIDAtMTJ6bS0yIDB2MTJINFY4eiIgLz4KICAgICAgICA8cGF0aCBkPSJNMTEgMTBIOXYzSDZ2MmgzdjNoMnYtM2gzdi0yaC0zeiIgLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-extension: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwLjUgMTFIMTlWN2MwLTEuMS0uOS0yLTItMmgtNFYzLjVDMTMgMi4xMiAxMS44OCAxIDEwLjUgMVM4IDIuMTIgOCAzLjVWNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAydjMuOEgzLjVjMS40OSAwIDIuNyAxLjIxIDIuNyAyLjdzLTEuMjEgMi43LTIuNyAyLjdIMlYyMGMwIDEuMS45IDIgMiAyaDMuOHYtMS41YzAtMS40OSAxLjIxLTIuNyAyLjctMi43IDEuNDkgMCAyLjcgMS4yMSAyLjcgMi43VjIySDE3YzEuMSAwIDItLjkgMi0ydi00aDEuNWMxLjM4IDAgMi41LTEuMTIgMi41LTIuNVMyMS44OCAxMSAyMC41IDExeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-fast-forward: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTQgMThsOC41LTZMNCA2djEyem05LTEydjEybDguNS02TDEzIDZ6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-file-upload: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkgMTZoNnYtNmg0bC03LTctNyA3aDR6bS00IDJoMTR2Mkg1eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-file: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuMyA4LjJsLTUuNS01LjVjLS4zLS4zLS43LS41LTEuMi0uNUgzLjljLS44LjEtMS42LjktMS42IDEuOHYxNC4xYzAgLjkuNyAxLjYgMS42IDEuNmgxNC4yYy45IDAgMS42LS43IDEuNi0xLjZWOS40Yy4xLS41LS4xLS45LS40LTEuMnptLTUuOC0zLjNsMy40IDMuNmgtMy40VjQuOXptMy45IDEyLjdINC43Yy0uMSAwLS4yIDAtLjItLjJWNC43YzAtLjIuMS0uMy4yLS4zaDcuMnY0LjRzMCAuOC4zIDEuMWMuMy4zIDEuMS4zIDEuMS4zaDQuM3Y3LjJzLS4xLjItLjIuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-filter-dot: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTE0LDEyVjE5Ljg4QzE0LjA0LDIwLjE4IDEzLjk0LDIwLjUgMTMuNzEsMjAuNzFDMTMuMzIsMjEuMSAxMi42OSwyMS4xIDEyLjMsMjAuNzFMMTAuMjksMTguN0MxMC4wNiwxOC40NyA5Ljk2LDE4LjE2IDEwLDE3Ljg3VjEySDkuOTdMNC4yMSw0LjYyQzMuODcsNC4xOSAzLjk1LDMuNTYgNC4zOCwzLjIyQzQuNTcsMy4wOCA0Ljc4LDMgNSwzVjNIMTlWM0MxOS4yMiwzIDE5LjQzLDMuMDggMTkuNjIsMy4yMkMyMC4wNSwzLjU2IDIwLjEzLDQuMTkgMTkuNzksNC42MkwxNC4wMywxMkgxNFoiIC8+CiAgPC9nPgogIDxnIGNsYXNzPSJqcC1pY29uLWRvdCIgZmlsbD0iI0ZGRiI+CiAgICA8Y2lyY2xlIGN4PSIxOCIgY3k9IjE3IiByPSIzIj48L2NpcmNsZT4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-filter-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEwIDE4aDR2LTJoLTR2MnpNMyA2djJoMThWNkgzem0zIDdoMTJ2LTJINnYyeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-filter: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTE0LDEyVjE5Ljg4QzE0LjA0LDIwLjE4IDEzLjk0LDIwLjUgMTMuNzEsMjAuNzFDMTMuMzIsMjEuMSAxMi42OSwyMS4xIDEyLjMsMjAuNzFMMTAuMjksMTguN0MxMC4wNiwxOC40NyA5Ljk2LDE4LjE2IDEwLDE3Ljg3VjEySDkuOTdMNC4yMSw0LjYyQzMuODcsNC4xOSAzLjk1LDMuNTYgNC4zOCwzLjIyQzQuNTcsMy4wOCA0Ljc4LDMgNSwzVjNIMTlWM0MxOS4yMiwzIDE5LjQzLDMuMDggMTkuNjIsMy4yMkMyMC4wNSwzLjU2IDIwLjEzLDQuMTkgMTkuNzksNC42MkwxNC4wMywxMkgxNFoiIC8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-folder-favorite: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjRweCIgdmlld0JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjRweCIgZmlsbD0iIzAwMDAwMCI+CiAgPHBhdGggZD0iTTAgMGgyNHYyNEgwVjB6IiBmaWxsPSJub25lIi8+PHBhdGggY2xhc3M9ImpwLWljb24zIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzYxNjE2MSIgZD0iTTIwIDZoLThsLTItMkg0Yy0xLjEgMC0yIC45LTIgMnYxMmMwIDEuMS45IDIgMiAyaDE2YzEuMSAwIDItLjkgMi0yVjhjMC0xLjEtLjktMi0yLTJ6bS0yLjA2IDExTDE1IDE1LjI4IDEyLjA2IDE3bC43OC0zLjMzLTIuNTktMi4yNCAzLjQxLS4yOUwxNSA4bDEuMzQgMy4xNCAzLjQxLjI5LTIuNTkgMi4yNC43OCAzLjMzeiIvPgo8L3N2Zz4K);
  --jp-icon-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY4YzAtMS4xLS45LTItMi0yaC04bC0yLTJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-home: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjRweCIgdmlld0JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjRweCIgZmlsbD0iIzAwMDAwMCI+CiAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPjxwYXRoIGNsYXNzPSJqcC1pY29uMyBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xMCAyMHYtNmg0djZoNXYtOGgzTDEyIDMgMiAxMmgzdjh6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-html5: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uMCBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMDAiIGQ9Ik0xMDguNCAwaDIzdjIyLjhoMjEuMlYwaDIzdjY5aC0yM1Y0NmgtMjF2MjNoLTIzLjJNMjA2IDIzaC0yMC4zVjBoNjMuN3YyM0gyMjl2NDZoLTIzbTUzLjUtNjloMjQuMWwxNC44IDI0LjNMMzEzLjIgMGgyNC4xdjY5aC0yM1YzNC44bC0xNi4xIDI0LjgtMTYuMS0yNC44VjY5aC0yMi42bTg5LjItNjloMjN2NDYuMmgzMi42VjY5aC01NS42Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI2U0NGQyNiIgZD0iTTEwNy42IDQ3MWwtMzMtMzcwLjRoMzYyLjhsLTMzIDM3MC4yTDI1NS43IDUxMiIvPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNmMTY1MjkiIGQ9Ik0yNTYgNDgwLjVWMTMxaDE0OC4zTDM3NiA0NDciLz4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNlYmViZWIiIGQ9Ik0xNDIgMTc2LjNoMTE0djQ1LjRoLTY0LjJsNC4yIDQ2LjVoNjB2NDUuM0gxNTQuNG0yIDIyLjhIMjAybDMuMiAzNi4zIDUwLjggMTMuNnY0Ny40bC05My4yLTI2Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIiBmaWxsPSIjZmZmIiBkPSJNMzY5LjYgMTc2LjNIMjU1Ljh2NDUuNGgxMDkuNm0tNC4xIDQ2LjVIMjU1Ljh2NDUuNGg1NmwtNS4zIDU5LTUwLjcgMTMuNnY0Ny4ybDkzLTI1LjgiLz4KPC9zdmc+Cg==);
  --jp-icon-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1icmFuZDQganAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNGRkYiIGQ9Ik0yLjIgMi4yaDE3LjV2MTcuNUgyLjJ6Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzNGNTFCNSIgZD0iTTIuMiAyLjJ2MTcuNWgxNy41bC4xLTE3LjVIMi4yem0xMi4xIDIuMmMxLjIgMCAyLjIgMSAyLjIgMi4ycy0xIDIuMi0yLjIgMi4yLTIuMi0xLTIuMi0yLjIgMS0yLjIgMi4yLTIuMnpNNC40IDE3LjZsMy4zLTguOCAzLjMgNi42IDIuMi0zLjIgNC40IDUuNEg0LjR6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-info: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUwLjk3OCA1MC45NzgiPgoJPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KCQk8cGF0aCBkPSJNNDMuNTIsNy40NThDMzguNzExLDIuNjQ4LDMyLjMwNywwLDI1LjQ4OSwwQzE4LjY3LDAsMTIuMjY2LDIuNjQ4LDcuNDU4LDcuNDU4CgkJCWMtOS45NDMsOS45NDEtOS45NDMsMjYuMTE5LDAsMzYuMDYyYzQuODA5LDQuODA5LDExLjIxMiw3LjQ1NiwxOC4wMzEsNy40NThjMCwwLDAuMDAxLDAsMC4wMDIsMAoJCQljNi44MTYsMCwxMy4yMjEtMi42NDgsMTguMDI5LTcuNDU4YzQuODA5LTQuODA5LDcuNDU3LTExLjIxMiw3LjQ1Ny0xOC4wM0M1MC45NzcsMTguNjcsNDguMzI4LDEyLjI2Niw0My41Miw3LjQ1OHoKCQkJIE00Mi4xMDYsNDIuMTA1Yy00LjQzMiw0LjQzMS0xMC4zMzIsNi44NzItMTYuNjE1LDYuODcyaC0wLjAwMmMtNi4yODUtMC4wMDEtMTIuMTg3LTIuNDQxLTE2LjYxNy02Ljg3MgoJCQljLTkuMTYyLTkuMTYzLTkuMTYyLTI0LjA3MSwwLTMzLjIzM0MxMy4zMDMsNC40NCwxOS4yMDQsMiwyNS40ODksMmM2LjI4NCwwLDEyLjE4NiwyLjQ0LDE2LjYxNyw2Ljg3MgoJCQljNC40MzEsNC40MzEsNi44NzEsMTAuMzMyLDYuODcxLDE2LjYxN0M0OC45NzcsMzEuNzcyLDQ2LjUzNiwzNy42NzUsNDIuMTA2LDQyLjEwNXoiLz4KCQk8cGF0aCBkPSJNMjMuNTc4LDMyLjIxOGMtMC4wMjMtMS43MzQsMC4xNDMtMy4wNTksMC40OTYtMy45NzJjMC4zNTMtMC45MTMsMS4xMS0xLjk5NywyLjI3Mi0zLjI1MwoJCQljMC40NjgtMC41MzYsMC45MjMtMS4wNjIsMS4zNjctMS41NzVjMC42MjYtMC43NTMsMS4xMDQtMS40NzgsMS40MzYtMi4xNzVjMC4zMzEtMC43MDcsMC40OTUtMS41NDEsMC40OTUtMi41CgkJCWMwLTEuMDk2LTAuMjYtMi4wODgtMC43NzktMi45NzljLTAuNTY1LTAuODc5LTEuNTAxLTEuMzM2LTIuODA2LTEuMzY5Yy0xLjgwMiwwLjA1Ny0yLjk4NSwwLjY2Ny0zLjU1LDEuODMyCgkJCWMtMC4zMDEsMC41MzUtMC41MDMsMS4xNDEtMC42MDcsMS44MTRjLTAuMTM5LDAuNzA3LTAuMjA3LDEuNDMyLTAuMjA3LDIuMTc0aC0yLjkzN2MtMC4wOTEtMi4yMDgsMC40MDctNC4xMTQsMS40OTMtNS43MTkKCQkJYzEuMDYyLTEuNjQsMi44NTUtMi40ODEsNS4zNzgtMi41MjdjMi4xNiwwLjAyMywzLjg3NCwwLjYwOCw1LjE0MSwxLjc1OGMxLjI3OCwxLjE2LDEuOTI5LDIuNzY0LDEuOTUsNC44MTEKCQkJYzAsMS4xNDItMC4xMzcsMi4xMTEtMC40MSwyLjkxMWMtMC4zMDksMC44NDUtMC43MzEsMS41OTMtMS4yNjgsMi4yNDNjLTAuNDkyLDAuNjUtMS4wNjgsMS4zMTgtMS43MywyLjAwMgoJCQljLTAuNjUsMC42OTctMS4zMTMsMS40NzktMS45ODcsMi4zNDZjLTAuMjM5LDAuMzc3LTAuNDI5LDAuNzc3LTAuNTY1LDEuMTk5Yy0wLjE2LDAuOTU5LTAuMjE3LDEuOTUxLTAuMTcxLDIuOTc5CgkJCUMyNi41ODksMzIuMjE4LDIzLjU3OCwzMi4yMTgsMjMuNTc4LDMyLjIxOHogTTIzLjU3OCwzOC4yMnYtMy40ODRoMy4wNzZ2My40ODRIMjMuNTc4eiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-inspector: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaW5zcGVjdG9yLWljb24tY29sb3IganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY2YzAtMS4xLS45LTItMi0yem0tNSAxNEg0di00aDExdjR6bTAtNUg0VjloMTF2NHptNSA1aC00VjloNHY5eiIvPgo8L3N2Zz4K);
  --jp-icon-json: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtanNvbi1pY29uLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI0Y5QTgyNSI+CiAgICA8cGF0aCBkPSJNMjAuMiAxMS44Yy0xLjYgMC0xLjcuNS0xLjcgMSAwIC40LjEuOS4xIDEuMy4xLjUuMS45LjEgMS4zIDAgMS43LTEuNCAyLjMtMy41IDIuM2gtLjl2LTEuOWguNWMxLjEgMCAxLjQgMCAxLjQtLjggMC0uMyAwLS42LS4xLTEgMC0uNC0uMS0uOC0uMS0xLjIgMC0xLjMgMC0xLjggMS4zLTItMS4zLS4yLTEuMy0uNy0xLjMtMiAwLS40LjEtLjguMS0xLjIuMS0uNC4xLS43LjEtMSAwLS44LS40LS43LTEuNC0uOGgtLjVWNC4xaC45YzIuMiAwIDMuNS43IDMuNSAyLjMgMCAuNC0uMS45LS4xIDEuMy0uMS41LS4xLjktLjEgMS4zIDAgLjUuMiAxIDEuNyAxdjEuOHpNMS44IDEwLjFjMS42IDAgMS43LS41IDEuNy0xIDAtLjQtLjEtLjktLjEtMS4zLS4xLS41LS4xLS45LS4xLTEuMyAwLTEuNiAxLjQtMi4zIDMuNS0yLjNoLjl2MS45aC0uNWMtMSAwLTEuNCAwLTEuNC44IDAgLjMgMCAuNi4xIDEgMCAuMi4xLjYuMSAxIDAgMS4zIDAgMS44LTEuMyAyQzYgMTEuMiA2IDExLjcgNiAxM2MwIC40LS4xLjgtLjEgMS4yLS4xLjMtLjEuNy0uMSAxIDAgLjguMy44IDEuNC44aC41djEuOWgtLjljLTIuMSAwLTMuNS0uNi0zLjUtMi4zIDAtLjQuMS0uOS4xLTEuMy4xLS41LjEtLjkuMS0xLjMgMC0uNS0uMi0xLTEuNy0xdi0xLjl6Ii8+CiAgICA8Y2lyY2xlIGN4PSIxMSIgY3k9IjEzLjgiIHI9IjIuMSIvPgogICAgPGNpcmNsZSBjeD0iMTEiIGN5PSI4LjIiIHI9IjIuMSIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-julia: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDMyNSAzMDAiPgogIDxnIGNsYXNzPSJqcC1icmFuZDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjY2IzYzMzIj4KICAgIDxwYXRoIGQ9Ik0gMTUwLjg5ODQzOCAyMjUgQyAxNTAuODk4NDM4IDI2Ni40MjE4NzUgMTE3LjMyMDMxMiAzMDAgNzUuODk4NDM4IDMwMCBDIDM0LjQ3NjU2MiAzMDAgMC44OTg0MzggMjY2LjQyMTg3NSAwLjg5ODQzOCAyMjUgQyAwLjg5ODQzOCAxODMuNTc4MTI1IDM0LjQ3NjU2MiAxNTAgNzUuODk4NDM4IDE1MCBDIDExNy4zMjAzMTIgMTUwIDE1MC44OTg0MzggMTgzLjU3ODEyNSAxNTAuODk4NDM4IDIyNSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzM4OTgyNiI+CiAgICA8cGF0aCBkPSJNIDIzNy41IDc1IEMgMjM3LjUgMTE2LjQyMTg3NSAyMDMuOTIxODc1IDE1MCAxNjIuNSAxNTAgQyAxMjEuMDc4MTI1IDE1MCA4Ny41IDExNi40MjE4NzUgODcuNSA3NSBDIDg3LjUgMzMuNTc4MTI1IDEyMS4wNzgxMjUgMCAxNjIuNSAwIEMgMjAzLjkyMTg3NSAwIDIzNy41IDMzLjU3ODEyNSAyMzcuNSA3NSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzk1NThiMiI+CiAgICA8cGF0aCBkPSJNIDMyNC4xMDE1NjIgMjI1IEMgMzI0LjEwMTU2MiAyNjYuNDIxODc1IDI5MC41MjM0MzggMzAwIDI0OS4xMDE1NjIgMzAwIEMgMjA3LjY3OTY4OCAzMDAgMTc0LjEwMTU2MiAyNjYuNDIxODc1IDE3NC4xMDE1NjIgMjI1IEMgMTc0LjEwMTU2MiAxODMuNTc4MTI1IDIwNy42Nzk2ODggMTUwIDI0OS4xMDE1NjIgMTUwIEMgMjkwLjUyMzQzOCAxNTAgMzI0LjEwMTU2MiAxODMuNTc4MTI1IDMyNC4xMDE1NjIgMjI1Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-jupyter-favicon: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUyIiBoZWlnaHQ9IjE2NSIgdmlld0JveD0iMCAwIDE1MiAxNjUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgPGcgY2xhc3M9ImpwLWp1cHl0ZXItaWNvbi1jb2xvciIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA3ODk0NywgMTEwLjU4MjkyNykiIGQ9Ik03NS45NDIyODQyLDI5LjU4MDQ1NjEgQzQzLjMwMjM5NDcsMjkuNTgwNDU2MSAxNC43OTY3ODMyLDE3LjY1MzQ2MzQgMCwwIEM1LjUxMDgzMjExLDE1Ljg0MDY4MjkgMTUuNzgxNTM4OSwyOS41NjY3NzMyIDI5LjM5MDQ5NDcsMzkuMjc4NDE3MSBDNDIuOTk5Nyw0OC45ODk4NTM3IDU5LjI3MzcsNTQuMjA2NzgwNSA3NS45NjA1Nzg5LDU0LjIwNjc4MDUgQzkyLjY0NzQ1NzksNTQuMjA2NzgwNSAxMDguOTIxNDU4LDQ4Ljk4OTg1MzcgMTIyLjUzMDY2MywzOS4yNzg0MTcxIEMxMzYuMTM5NDUzLDI5LjU2Njc3MzIgMTQ2LjQxMDI4NCwxNS44NDA2ODI5IDE1MS45MjExNTgsMCBDMTM3LjA4Nzg2OCwxNy42NTM0NjM0IDEwOC41ODI1ODksMjkuNTgwNDU2MSA3NS45NDIyODQyLDI5LjU4MDQ1NjEgTDc1Ljk0MjI4NDIsMjkuNTgwNDU2MSBaIiAvPgogICAgPHBhdGggdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMzczNjgsIDAuNzA0ODc4KSIgZD0iTTc1Ljk3ODQ1NzksMjQuNjI2NDA3MyBDMTA4LjYxODc2MywyNC42MjY0MDczIDEzNy4xMjQ0NTgsMzYuNTUzNDQxNSAxNTEuOTIxMTU4LDU0LjIwNjc4MDUgQzE0Ni40MTAyODQsMzguMzY2MjIyIDEzNi4xMzk0NTMsMjQuNjQwMTMxNyAxMjIuNTMwNjYzLDE0LjkyODQ4NzggQzEwOC45MjE0NTgsNS4yMTY4NDM5IDkyLjY0NzQ1NzksMCA3NS45NjA1Nzg5LDAgQzU5LjI3MzcsMCA0Mi45OTk3LDUuMjE2ODQzOSAyOS4zOTA0OTQ3LDE0LjkyODQ4NzggQzE1Ljc4MTUzODksMjQuNjQwMTMxNyA1LjUxMDgzMjExLDM4LjM2NjIyMiAwLDU0LjIwNjc4MDUgQzE0LjgzMzA4MTYsMzYuNTg5OTI5MyA0My4zMzg1Njg0LDI0LjYyNjQwNzMgNzUuOTc4NDU3OSwyNC42MjY0MDczIEw3NS45Nzg0NTc5LDI0LjYyNjQwNzMgWiIgLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-jupyter: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzkiIGhlaWdodD0iNTEiIHZpZXdCb3g9IjAgMCAzOSA1MSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTYzOCAtMjI4MSkiPgogICAgIDxnIGNsYXNzPSJqcC1qdXB5dGVyLWljb24tY29sb3IiIGZpbGw9IiNGMzc3MjYiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5Ljc0IDIzMTEuOTgpIiBkPSJNIDE4LjI2NDYgNy4xMzQxMUMgMTAuNDE0NSA3LjEzNDExIDMuNTU4NzIgNC4yNTc2IDAgMEMgMS4zMjUzOSAzLjgyMDQgMy43OTU1NiA3LjEzMDgxIDcuMDY4NiA5LjQ3MzAzQyAxMC4zNDE3IDExLjgxNTIgMTQuMjU1NyAxMy4wNzM0IDE4LjI2OSAxMy4wNzM0QyAyMi4yODIzIDEzLjA3MzQgMjYuMTk2MyAxMS44MTUyIDI5LjQ2OTQgOS40NzMwM0MgMzIuNzQyNCA3LjEzMDgxIDM1LjIxMjYgMy44MjA0IDM2LjUzOCAwQyAzMi45NzA1IDQuMjU3NiAyNi4xMTQ4IDcuMTM0MTEgMTguMjY0NiA3LjEzNDExWiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5LjczIDIyODUuNDgpIiBkPSJNIDE4LjI3MzMgNS45MzkzMUMgMjYuMTIzNSA1LjkzOTMxIDMyLjk3OTMgOC44MTU4MyAzNi41MzggMTMuMDczNEMgMzUuMjEyNiA5LjI1MzAzIDMyLjc0MjQgNS45NDI2MiAyOS40Njk0IDMuNjAwNEMgMjYuMTk2MyAxLjI1ODE4IDIyLjI4MjMgMCAxOC4yNjkgMEMgMTQuMjU1NyAwIDEwLjM0MTcgMS4yNTgxOCA3LjA2ODYgMy42MDA0QyAzLjc5NTU2IDUuOTQyNjIgMS4zMjUzOSA5LjI1MzAzIDAgMTMuMDczNEMgMy41Njc0NSA4LjgyNDYzIDEwLjQyMzIgNS45MzkzMSAxOC4yNzMzIDUuOTM5MzFaIi8+CiAgICA8L2c+CiAgICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjY5LjMgMjI4MS4zMSkiIGQ9Ik0gNS44OTM1MyAyLjg0NEMgNS45MTg4OSAzLjQzMTY1IDUuNzcwODUgNC4wMTM2NyA1LjQ2ODE1IDQuNTE2NDVDIDUuMTY1NDUgNS4wMTkyMiA0LjcyMTY4IDUuNDIwMTUgNC4xOTI5OSA1LjY2ODUxQyAzLjY2NDMgNS45MTY4OCAzLjA3NDQ0IDYuMDAxNTEgMi40OTgwNSA1LjkxMTcxQyAxLjkyMTY2IDUuODIxOSAxLjM4NDYzIDUuNTYxNyAwLjk1NDg5OCA1LjE2NDAxQyAwLjUyNTE3IDQuNzY2MzMgMC4yMjIwNTYgNC4yNDkwMyAwLjA4MzkwMzcgMy42Nzc1N0MgLTAuMDU0MjQ4MyAzLjEwNjExIC0wLjAyMTIzIDIuNTA2MTcgMC4xNzg3ODEgMS45NTM2NEMgMC4zNzg3OTMgMS40MDExIDAuNzM2ODA5IDAuOTIwODE3IDEuMjA3NTQgMC41NzM1MzhDIDEuNjc4MjYgMC4yMjYyNTkgMi4yNDA1NSAwLjAyNzU5MTkgMi44MjMyNiAwLjAwMjY3MjI5QyAzLjYwMzg5IC0wLjAzMDcxMTUgNC4zNjU3MyAwLjI0OTc4OSA0Ljk0MTQyIDAuNzgyNTUxQyA1LjUxNzExIDEuMzE1MzEgNS44NTk1NiAyLjA1Njc2IDUuODkzNTMgMi44NDRaIi8+CiAgICAgIDxwYXRoIHRyYW5zZm9ybT0idHJhbnNsYXRlKDE2MzkuOCAyMzIzLjgxKSIgZD0iTSA3LjQyNzg5IDMuNTgzMzhDIDcuNDYwMDggNC4zMjQzIDcuMjczNTUgNS4wNTgxOSA2Ljg5MTkzIDUuNjkyMTNDIDYuNTEwMzEgNi4zMjYwNyA1Ljk1MDc1IDYuODMxNTYgNS4yODQxMSA3LjE0NDZDIDQuNjE3NDcgNy40NTc2MyAzLjg3MzcxIDcuNTY0MTQgMy4xNDcwMiA3LjQ1MDYzQyAyLjQyMDMyIDcuMzM3MTIgMS43NDMzNiA3LjAwODcgMS4yMDE4NCA2LjUwNjk1QyAwLjY2MDMyOCA2LjAwNTIgMC4yNzg2MSA1LjM1MjY4IDAuMTA1MDE3IDQuNjMyMDJDIC0wLjA2ODU3NTcgMy45MTEzNSAtMC4wMjYyMzYxIDMuMTU0OTQgMC4yMjY2NzUgMi40NTg1NkMgMC40Nzk1ODcgMS43NjIxNyAwLjkzMTY5NyAxLjE1NzEzIDEuNTI1NzYgMC43MjAwMzNDIDIuMTE5ODMgMC4yODI5MzUgMi44MjkxNCAwLjAzMzQzOTUgMy41NjM4OSAwLjAwMzEzMzQ0QyA0LjU0NjY3IC0wLjAzNzQwMzMgNS41MDUyOSAwLjMxNjcwNiA2LjIyOTYxIDAuOTg3ODM1QyA2Ljk1MzkzIDEuNjU4OTYgNy4zODQ4NCAyLjU5MjM1IDcuNDI3ODkgMy41ODMzOEwgNy40Mjc4OSAzLjU4MzM4WiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM4LjM2IDIyODYuMDYpIiBkPSJNIDIuMjc0NzEgNC4zOTYyOUMgMS44NDM2MyA0LjQxNTA4IDEuNDE2NzEgNC4zMDQ0NSAxLjA0Nzk5IDQuMDc4NDNDIDAuNjc5MjY4IDMuODUyNCAwLjM4NTMyOCAzLjUyMTE0IDAuMjAzMzcxIDMuMTI2NTZDIDAuMDIxNDEzNiAyLjczMTk4IC0wLjA0MDM3OTggMi4yOTE4MyAwLjAyNTgxMTYgMS44NjE4MUMgMC4wOTIwMDMxIDEuNDMxOCAwLjI4MzIwNCAxLjAzMTI2IDAuNTc1MjEzIDAuNzEwODgzQyAwLjg2NzIyMiAwLjM5MDUxIDEuMjQ2OTEgMC4xNjQ3MDggMS42NjYyMiAwLjA2MjA1OTJDIDIuMDg1NTMgLTAuMDQwNTg5NyAyLjUyNTYxIC0wLjAxNTQ3MTQgMi45MzA3NiAwLjEzNDIzNUMgMy4zMzU5MSAwLjI4Mzk0MSAzLjY4NzkyIDAuNTUxNTA1IDMuOTQyMjIgMC45MDMwNkMgNC4xOTY1MiAxLjI1NDYyIDQuMzQxNjkgMS42NzQzNiA0LjM1OTM1IDIuMTA5MTZDIDQuMzgyOTkgMi42OTEwNyA0LjE3Njc4IDMuMjU4NjkgMy43ODU5NyAzLjY4NzQ2QyAzLjM5NTE2IDQuMTE2MjQgMi44NTE2NiA0LjM3MTE2IDIuMjc0NzEgNC4zOTYyOUwgMi4yNzQ3MSA0LjM5NjI5WiIvPgogICAgPC9nPgogIDwvZz4+Cjwvc3ZnPgo=);
  --jp-icon-jupyterlab-wordmark: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIHZpZXdCb3g9IjAgMCAxODYwLjggNDc1Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0RTRFNEUiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQ4MC4xMzY0MDEsIDY0LjI3MTQ5MykiPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMDAwMDAsIDU4Ljg3NTU2NikiPgogICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA4NzYwMywgMC4xNDAyOTQpIj4KICAgICAgICA8cGF0aCBkPSJNLTQyNi45LDE2OS44YzAsNDguNy0zLjcsNjQuNy0xMy42LDc2LjRjLTEwLjgsMTAtMjUsMTUuNS0zOS43LDE1LjVsMy43LDI5IGMyMi44LDAuMyw0NC44LTcuOSw2MS45LTIzLjFjMTcuOC0xOC41LDI0LTQ0LjEsMjQtODMuM1YwSC00Mjd2MTcwLjFMLTQyNi45LDE2OS44TC00MjYuOSwxNjkuOHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTU1LjA0NTI5NiwgNTYuODM3MTA0KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuNTYyNDUzLCAxLjc5OTg0MikiPgogICAgICAgIDxwYXRoIGQ9Ik0tMzEyLDE0OGMwLDIxLDAsMzkuNSwxLjcsNTUuNGgtMzEuOGwtMi4xLTMzLjNoLTAuOGMtNi43LDExLjYtMTYuNCwyMS4zLTI4LDI3LjkgYy0xMS42LDYuNi0yNC44LDEwLTM4LjIsOS44Yy0zMS40LDAtNjktMTcuNy02OS04OVYwaDM2LjR2MTEyLjdjMCwzOC43LDExLjYsNjQuNyw0NC42LDY0LjdjMTAuMy0wLjIsMjAuNC0zLjUsMjguOS05LjQgYzguNS01LjksMTUuMS0xNC4zLDE4LjktMjMuOWMyLjItNi4xLDMuMy0xMi41LDMuMy0xOC45VjAuMmgzNi40VjE0OEgtMzEyTC0zMTIsMTQ4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzOTAuMDEzMzIyLCA1My40Nzk2MzgpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS43MDY0NTgsIDAuMjMxNDI1KSI+CiAgICAgICAgPHBhdGggZD0iTS00NzguNiw3MS40YzAtMjYtMC44LTQ3LTEuNy02Ni43aDMyLjdsMS43LDM0LjhoMC44YzcuMS0xMi41LDE3LjUtMjIuOCwzMC4xLTI5LjcgYzEyLjUtNywyNi43LTEwLjMsNDEtOS44YzQ4LjMsMCw4NC43LDQxLjcsODQuNywxMDMuM2MwLDczLjEtNDMuNywxMDkuMi05MSwxMDkuMmMtMTIuMSwwLjUtMjQuMi0yLjItMzUtNy44IGMtMTAuOC01LjYtMTkuOS0xMy45LTI2LjYtMjQuMmgtMC44VjI5MWgtMzZ2LTIyMEwtNDc4LjYsNzEuNEwtNDc4LjYsNzEuNHogTS00NDIuNiwxMjUuNmMwLjEsNS4xLDAuNiwxMC4xLDEuNywxNS4xIGMzLDEyLjMsOS45LDIzLjMsMTkuOCwzMS4xYzkuOSw3LjgsMjIuMSwxMi4xLDM0LjcsMTIuMWMzOC41LDAsNjAuNy0zMS45LDYwLjctNzguNWMwLTQwLjctMjEuMS03NS42LTU5LjUtNzUuNiBjLTEyLjksMC40LTI1LjMsNS4xLTM1LjMsMTMuNGMtOS45LDguMy0xNi45LDE5LjctMTkuNiwzMi40Yy0xLjUsNC45LTIuMywxMC0yLjUsMTUuMVYxMjUuNkwtNDQyLjYsMTI1LjZMLTQ0Mi42LDEyNS42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg2MDYuNzQwNzI2LCA1Ni44MzcxMDQpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC43NTEyMjYsIDEuOTg5Mjk5KSI+CiAgICAgICAgPHBhdGggZD0iTS00NDAuOCwwbDQzLjcsMTIwLjFjNC41LDEzLjQsOS41LDI5LjQsMTIuOCw0MS43aDAuOGMzLjctMTIuMiw3LjktMjcuNywxMi44LTQyLjQgbDM5LjctMTE5LjJoMzguNUwtMzQ2LjksMTQ1Yy0yNiw2OS43LTQzLjcsMTA1LjQtNjguNiwxMjcuMmMtMTIuNSwxMS43LTI3LjksMjAtNDQuNiwyMy45bC05LjEtMzEuMSBjMTEuNy0zLjksMjIuNS0xMC4xLDMxLjgtMTguMWMxMy4yLTExLjEsMjMuNy0yNS4yLDMwLjYtNDEuMmMxLjUtMi44LDIuNS01LjcsMi45LTguOGMtMC4zLTMuMy0xLjItNi42LTIuNS05LjdMLTQ4MC4yLDAuMSBoMzkuN0wtNDQwLjgsMEwtNDQwLjgsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoODIyLjc0ODEwNCwgMC4wMDAwMDApIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS40NjQwNTAsIDAuMzc4OTE0KSI+CiAgICAgICAgPHBhdGggZD0iTS00MTMuNywwdjU4LjNoNTJ2MjguMmgtNTJWMTk2YzAsMjUsNywzOS41LDI3LjMsMzkuNWM3LjEsMC4xLDE0LjItMC43LDIxLjEtMi41IGwxLjcsMjcuN2MtMTAuMywzLjctMjEuMyw1LjQtMzIuMiw1Yy03LjMsMC40LTE0LjYtMC43LTIxLjMtMy40Yy02LjgtMi43LTEyLjktNi44LTE3LjktMTIuMWMtMTAuMy0xMC45LTE0LjEtMjktMTQuMS01Mi45IFY4Ni41aC0zMVY1OC4zaDMxVjkuNkwtNDEzLjcsMEwtNDEzLjcsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOTc0LjQzMzI4NiwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAuOTkwMDM0LCAwLjYxMDMzOSkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDQ1LjgsMTEzYzAuOCw1MCwzMi4yLDcwLjYsNjguNiw3MC42YzE5LDAuNiwzNy45LTMsNTUuMy0xMC41bDYuMiwyNi40IGMtMjAuOSw4LjktNDMuNSwxMy4xLTY2LjIsMTIuNmMtNjEuNSwwLTk4LjMtNDEuMi05OC4zLTEwMi41Qy00ODAuMiw0OC4yLTQ0NC43LDAtMzg2LjUsMGM2NS4yLDAsODIuNyw1OC4zLDgyLjcsOTUuNyBjLTAuMSw1LjgtMC41LDExLjUtMS4yLDE3LjJoLTE0MC42SC00NDUuOEwtNDQ1LjgsMTEzeiBNLTMzOS4yLDg2LjZjMC40LTIzLjUtOS41LTYwLjEtNTAuNC02MC4xIGMtMzYuOCwwLTUyLjgsMzQuNC01NS43LDYwLjFILTMzOS4yTC0zMzkuMiw4Ni42TC0zMzkuMiw4Ni42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjAxLjk2MTA1OCwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuMTc5NjQwLCAwLjcwNTA2OCkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDc4LjYsNjhjMC0yMy45LTAuNC00NC41LTEuNy02My40aDMxLjhsMS4yLDM5LjloMS43YzkuMS0yNy4zLDMxLTQ0LjUsNTUuMy00NC41IGMzLjUtMC4xLDcsMC40LDEwLjMsMS4ydjM0LjhjLTQuMS0wLjktOC4yLTEuMy0xMi40LTEuMmMtMjUuNiwwLTQzLjcsMTkuNy00OC43LDQ3LjRjLTEsNS43LTEuNiwxMS41LTEuNywxNy4ydjEwOC4zaC0zNlY2OCBMLTQ3OC42LDY4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCBkPSJNMTM1Mi4zLDMyNi4yaDM3VjI4aC0zN1YzMjYuMnogTTE2MDQuOCwzMjYuMmMtMi41LTEzLjktMy40LTMxLjEtMy40LTQ4Ljd2LTc2IGMwLTQwLjctMTUuMS04My4xLTc3LjMtODMuMWMtMjUuNiwwLTUwLDcuMS02Ni44LDE4LjFsOC40LDI0LjRjMTQuMy05LjIsMzQtMTUuMSw1My0xNS4xYzQxLjYsMCw0Ni4yLDMwLjIsNDYuMiw0N3Y0LjIgYy03OC42LTAuNC0xMjIuMywyNi41LTEyMi4zLDc1LjZjMCwyOS40LDIxLDU4LjQsNjIuMiw1OC40YzI5LDAsNTAuOS0xNC4zLDYyLjItMzAuMmgxLjNsMi45LDI1LjZIMTYwNC44eiBNMTU2NS43LDI1Ny43IGMwLDMuOC0wLjgsOC0yLjEsMTEuOGMtNS45LDE3LjItMjIuNywzNC00OS4yLDM0Yy0xOC45LDAtMzQuOS0xMS4zLTM0LjktMzUuM2MwLTM5LjUsNDUuOC00Ni42LDg2LjItNDUuOFYyNTcuN3ogTTE2OTguNSwzMjYuMiBsMS43LTMzLjZoMS4zYzE1LjEsMjYuOSwzOC43LDM4LjIsNjguMSwzOC4yYzQ1LjQsMCw5MS4yLTM2LjEsOTEuMi0xMDguOGMwLjQtNjEuNy0zNS4zLTEwMy43LTg1LjctMTAzLjcgYy0zMi44LDAtNTYuMywxNC43LTY5LjMsMzcuNGgtMC44VjI4aC0zNi42djI0NS43YzAsMTguMS0wLjgsMzguNi0xLjcsNTIuNUgxNjk4LjV6IE0xNzA0LjgsMjA4LjJjMC01LjksMS4zLTEwLjksMi4xLTE1LjEgYzcuNi0yOC4xLDMxLjEtNDUuNCw1Ni4zLTQ1LjRjMzkuNSwwLDYwLjUsMzQuOSw2MC41LDc1LjZjMCw0Ni42LTIzLjEsNzguMS02MS44LDc4LjFjLTI2LjksMC00OC4zLTE3LjYtNTUuNS00My4zIGMtMC44LTQuMi0xLjctOC44LTEuNy0xMy40VjIwOC4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgZmlsbD0iIzYxNjE2MSIgZD0iTTE1IDlIOXY2aDZWOXptLTIgNGgtMnYtMmgydjJ6bTgtMlY5aC0yVjdjMC0xLjEtLjktMi0yLTJoLTJWM2gtMnYyaC0yVjNIOXYySDdjLTEuMSAwLTIgLjktMiAydjJIM3YyaDJ2MkgzdjJoMnYyYzAgMS4xLjkgMiAyIDJoMnYyaDJ2LTJoMnYyaDJ2LTJoMmMxLjEgMCAyLS45IDItMnYtMmgydi0yaC0ydi0yaDJ6bS00IDZIN1Y3aDEwdjEweiIvPgo8L3N2Zz4K);
  --jp-icon-keyboard: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMTdjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY3YzAtMS4xLS45LTItMi0yem0tOSAzaDJ2MmgtMlY4em0wIDNoMnYyaC0ydi0yek04IDhoMnYySDhWOHptMCAzaDJ2Mkg4di0yem0tMSAySDV2LTJoMnYyem0wLTNINVY4aDJ2MnptOSA3SDh2LTJoOHYyem0wLTRoLTJ2LTJoMnYyem0wLTNoLTJWOGgydjJ6bTMgM2gtMnYtMmgydjJ6bTAtM2gtMlY4aDJ2MnoiLz4KPC9zdmc+Cg==);
  --jp-icon-launch: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMzIgMzIiIHdpZHRoPSIzMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0yNiwyOEg2YTIuMDAyNywyLjAwMjcsMCwwLDEtMi0yVjZBMi4wMDI3LDIuMDAyNywwLDAsMSw2LDRIMTZWNkg2VjI2SDI2VjE2aDJWMjZBMi4wMDI3LDIuMDAyNywwLDAsMSwyNiwyOFoiLz4KICAgIDxwb2x5Z29uIHBvaW50cz0iMjAgMiAyMCA0IDI2LjU4NiA0IDE4IDEyLjU4NiAxOS40MTQgMTQgMjggNS40MTQgMjggMTIgMzAgMTIgMzAgMiAyMCAyIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-launcher: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkgMTlINVY1aDdWM0g1YTIgMiAwIDAwLTIgMnYxNGEyIDIgMCAwMDIgMmgxNGMxLjEgMCAyLS45IDItMnYtN2gtMnY3ek0xNCAzdjJoMy41OWwtOS44MyA5LjgzIDEuNDEgMS40MUwxOSA2LjQxVjEwaDJWM2gtN3oiLz4KPC9zdmc+Cg==);
  --jp-icon-line-form: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGZpbGw9IndoaXRlIiBkPSJNNS44OCA0LjEyTDEzLjc2IDEybC03Ljg4IDcuODhMOCAyMmwxMC0xMEw4IDJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-link: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMuOSAxMmMwLTEuNzEgMS4zOS0zLjEgMy4xLTMuMWg0VjdIN2MtMi43NiAwLTUgMi4yNC01IDVzMi4yNCA1IDUgNWg0di0xLjlIN2MtMS43MSAwLTMuMS0xLjM5LTMuMS0zLjF6TTggMTNoOHYtMkg4djJ6bTktNmgtNHYxLjloNGMxLjcxIDAgMy4xIDEuMzkgMy4xIDMuMXMtMS4zOSAzLjEtMy4xIDMuMWgtNFYxN2g0YzIuNzYgMCA1LTIuMjQgNS01cy0yLjI0LTUtNS01eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xOSA1djE0SDVWNWgxNG0xLjEtMkgzLjljLS41IDAtLjkuNC0uOS45djE2LjJjMCAuNC40LjkuOS45aDE2LjJjLjQgMCAuOS0uNS45LS45VjMuOWMwLS41LS41LS45LS45LS45ek0xMSA3aDZ2MmgtNlY3em0wIDRoNnYyaC02di0yem0wIDRoNnYyaC02ek03IDdoMnYySDd6bTAgNGgydjJIN3ptMCA0aDJ2Mkg3eiIvPgo8L3N2Zz4K);
  --jp-icon-markdown: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjN0IxRkEyIiBkPSJNNSAxNC45aDEybC02LjEgNnptOS40LTYuOGMwLTEuMy0uMS0yLjktLjEtNC41LS40IDEuNC0uOSAyLjktMS4zIDQuM2wtMS4zIDQuM2gtMkw4LjUgNy45Yy0uNC0xLjMtLjctMi45LTEtNC4zLS4xIDEuNi0uMSAzLjItLjIgNC42TDcgMTIuNEg0LjhsLjctMTFoMy4zTDEwIDVjLjQgMS4yLjcgMi43IDEgMy45LjMtMS4yLjctMi42IDEtMy45bDEuMi0zLjdoMy4zbC42IDExaC0yLjRsLS4zLTQuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-move-down: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNMTIuNDcxIDcuNTI4OTlDMTIuNzYzMiA3LjIzNjg0IDEyLjc2MzIgNi43NjMxNiAxMi40NzEgNi40NzEwMVY2LjQ3MTAxQzEyLjE3OSA2LjE3OTA1IDExLjcwNTcgNi4xNzg4NCAxMS40MTM1IDYuNDcwNTRMNy43NSAxMC4xMjc1VjEuNzVDNy43NSAxLjMzNTc5IDcuNDE0MjEgMSA3IDFWMUM2LjU4NTc5IDEgNi4yNSAxLjMzNTc5IDYuMjUgMS43NVYxMC4xMjc1TDIuNTk3MjYgNi40NjgyMkMyLjMwMzM4IDYuMTczODEgMS44MjY0MSA2LjE3MzU5IDEuNTMyMjYgNi40Njc3NFY2LjQ2Nzc0QzEuMjM4MyA2Ljc2MTcgMS4yMzgzIDcuMjM4MyAxLjUzMjI2IDcuNTMyMjZMNi4yOTI4OSAxMi4yOTI5QzYuNjgzNDIgMTIuNjgzNCA3LjMxNjU4IDEyLjY4MzQgNy43MDcxMSAxMi4yOTI5TDEyLjQ3MSA3LjUyODk5WiIgZmlsbD0iIzYxNjE2MSIvPgo8L3N2Zz4K);
  --jp-icon-move-up: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNMS41Mjg5OSA2LjQ3MTAxQzEuMjM2ODQgNi43NjMxNiAxLjIzNjg0IDcuMjM2ODQgMS41Mjg5OSA3LjUyODk5VjcuNTI4OTlDMS44MjA5NSA3LjgyMDk1IDIuMjk0MjYgNy44MjExNiAyLjU4NjQ5IDcuNTI5NDZMNi4yNSAzLjg3MjVWMTIuMjVDNi4yNSAxMi42NjQyIDYuNTg1NzkgMTMgNyAxM1YxM0M3LjQxNDIxIDEzIDcuNzUgMTIuNjY0MiA3Ljc1IDEyLjI1VjMuODcyNUwxMS40MDI3IDcuNTMxNzhDMTEuNjk2NiA3LjgyNjE5IDEyLjE3MzYgNy44MjY0MSAxMi40Njc3IDcuNTMyMjZWNy41MzIyNkMxMi43NjE3IDcuMjM4MyAxMi43NjE3IDYuNzYxNyAxMi40Njc3IDYuNDY3NzRMNy43MDcxMSAxLjcwNzExQzcuMzE2NTggMS4zMTY1OCA2LjY4MzQyIDEuMzE2NTggNi4yOTI4OSAxLjcwNzExTDEuNTI4OTkgNi40NzEwMVoiIGZpbGw9IiM2MTYxNjEiLz4KPC9zdmc+Cg==);
  --jp-icon-new-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwIDZoLThsLTItMkg0Yy0xLjExIDAtMS45OS44OS0xLjk5IDJMMiAxOGMwIDEuMTEuODkgMiAyIDJoMTZjMS4xMSAwIDItLjg5IDItMlY4YzAtMS4xMS0uODktMi0yLTJ6bS0xIDhoLTN2M2gtMnYtM2gtM3YtMmgzVjloMnYzaDN2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-not-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI1IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMTkgMTcuMTg0NCAyLjk2OTY4IDE0LjMwMzIgMS44NjA5NCAxMS40NDA5WiIvPgogICAgPHBhdGggY2xhc3M9ImpwLWljb24yIiBzdHJva2U9IiMzMzMzMzMiIHN0cm9rZS13aWR0aD0iMiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOS4zMTU5MiA5LjMyMDMxKSIgZD0iTTcuMzY4NDIgMEwwIDcuMzY0NzkiLz4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDkuMzE1OTIgMTYuNjgzNikgc2NhbGUoMSAtMSkiIGQ9Ik03LjM2ODQyIDBMMCA3LjM2NDc5Ii8+Cjwvc3ZnPgo=);
  --jp-icon-notebook: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtbm90ZWJvb2staWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNFRjZDMDAiPgogICAgPHBhdGggZD0iTTE4LjcgMy4zdjE1LjRIMy4zVjMuM2gxNS40bTEuNS0xLjVIMS44djE4LjNoMTguM2wuMS0xOC4zeiIvPgogICAgPHBhdGggZD0iTTE2LjUgMTYuNWwtNS40LTQuMy01LjYgNC4zdi0xMWgxMXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-numbering: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTQgMTlINlYxOS41SDVWMjAuNUg2VjIxSDRWMjJIN1YxOEg0VjE5Wk01IDEwSDZWNkg0VjdINVYxMFpNNCAxM0g1LjhMNCAxNS4xVjE2SDdWMTVINS4yTDcgMTIuOVYxMkg0VjEzWk05IDdWOUgyM1Y3SDlaTTkgMjFIMjNWMTlIOVYyMVpNOSAxNUgyM1YxM0g5VjE1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-offline-bolt: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDIuMDJjLTUuNTEgMC05Ljk4IDQuNDctOS45OCA5Ljk4czQuNDcgOS45OCA5Ljk4IDkuOTggOS45OC00LjQ3IDkuOTgtOS45OFMxNy41MSAyLjAyIDEyIDIuMDJ6TTExLjQ4IDIwdi02LjI2SDhMMTMgNHY2LjI2aDMuMzVMMTEuNDggMjB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-palette: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE4IDEzVjIwSDRWNkg5LjAyQzkuMDcgNS4yOSA5LjI0IDQuNjIgOS41IDRINEMyLjkgNCAyIDQuOSAyIDZWMjBDMiAyMS4xIDIuOSAyMiA0IDIySDE4QzE5LjEgMjIgMjAgMjEuMSAyMCAyMFYxNUwxOCAxM1pNMTkuMyA4Ljg5QzE5Ljc0IDguMTkgMjAgNy4zOCAyMCA2LjVDMjAgNC4wMSAxNy45OSAyIDE1LjUgMkMxMy4wMSAyIDExIDQuMDEgMTEgNi41QzExIDguOTkgMTMuMDEgMTEgMTUuNDkgMTFDMTYuMzcgMTEgMTcuMTkgMTAuNzQgMTcuODggMTAuM0wyMSAxMy40MkwyMi40MiAxMkwxOS4zIDguODlaTTE1LjUgOUMxNC4xMiA5IDEzIDcuODggMTMgNi41QzEzIDUuMTIgMTQuMTIgNCAxNS41IDRDMTYuODggNCAxOCA1LjEyIDE4IDYuNUMxOCA3Ljg4IDE2Ljg4IDkgMTUuNSA5WiIvPgogICAgPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00IDZIOS4wMTg5NEM5LjAwNjM5IDYuMTY1MDIgOSA2LjMzMTc2IDkgNi41QzkgOC44MTU3NyAxMC4yMTEgMTAuODQ4NyAxMi4wMzQzIDEySDlWMTRIMTZWMTIuOTgxMUMxNi41NzAzIDEyLjkzNzcgMTcuMTIgMTIuODIwNyAxNy42Mzk2IDEyLjYzOTZMMTggMTNWMjBINFY2Wk04IDhINlYxMEg4VjhaTTYgMTJIOFYxNEg2VjEyWk04IDE2SDZWMThIOFYxNlpNOSAxNkgxNlYxOEg5VjE2WiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-paste: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE5IDJoLTQuMThDMTQuNC44NCAxMy4zIDAgMTIgMGMtMS4zIDAtMi40Ljg0LTIuODIgMkg1Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjRjMC0xLjEtLjktMi0yLTJ6bS03IDBjLjU1IDAgMSAuNDUgMSAxcy0uNDUgMS0xIDEtMS0uNDUtMS0xIC40NS0xIDEtMXptNyAxOEg1VjRoMnYzaDEwVjRoMnYxNnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-pdf: url(data:image/svg+xml;base64,PHN2ZwogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMiAyMiIgd2lkdGg9IjE2Ij4KICAgIDxwYXRoIHRyYW5zZm9ybT0icm90YXRlKDQ1KSIgY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI0ZGMkEyQSIKICAgICAgIGQ9Im0gMjIuMzQ0MzY5LC0zLjAxNjM2NDIgaCA1LjYzODYwNCB2IDEuNTc5MjQzMyBoIC0zLjU0OTIyNyB2IDEuNTA4NjkyOTkgaCAzLjMzNzU3NiBWIDEuNjUwODE1NCBoIC0zLjMzNzU3NiB2IDMuNDM1MjYxMyBoIC0yLjA4OTM3NyB6IG0gLTcuMTM2NDQ0LDEuNTc5MjQzMyB2IDQuOTQzOTU0MyBoIDAuNzQ4OTIgcSAxLjI4MDc2MSwwIDEuOTUzNzAzLC0wLjYzNDk1MzUgMC42NzgzNjksLTAuNjM0OTUzNSAwLjY3ODM2OSwtMS44NDUxNjQxIDAsLTEuMjA0NzgzNTUgLTAuNjcyOTQyLC0xLjgzNDMxMDExIC0wLjY3Mjk0MiwtMC42Mjk1MjY1OSAtMS45NTkxMywtMC42Mjk1MjY1OSB6IG0gLTIuMDg5Mzc3LC0xLjU3OTI0MzMgaCAyLjIwMzM0MyBxIDEuODQ1MTY0LDAgMi43NDYwMzksMC4yNjU5MjA3IDAuOTA2MzAxLDAuMjYwNDkzNyAxLjU1MjEwOCwwLjg5MDAyMDMgMC41Njk4MywwLjU0ODEyMjMgMC44NDY2MDUsMS4yNjQ0ODAwNiAwLjI3Njc3NCwwLjcxNjM1NzgxIDAuMjc2Nzc0LDEuNjIyNjU4OTQgMCwwLjkxNzE1NTEgLTAuMjc2Nzc0LDEuNjM4OTM5OSAtMC4yNzY3NzUsMC43MTYzNTc4IC0wLjg0NjYwNSwxLjI2NDQ4IC0wLjY1MTIzNCwwLjYyOTUyNjYgLTEuNTYyOTYyLDAuODk1NDQ3MyAtMC45MTE3MjgsMC4yNjA0OTM3IC0yLjczNTE4NSwwLjI2MDQ5MzcgaCAtMi4yMDMzNDMgeiBtIC04LjE0NTg1NjUsMCBoIDMuNDY3ODIzIHEgMS41NDY2ODE2LDAgMi4zNzE1Nzg1LDAuNjg5MjIzIDAuODMwMzI0LDAuNjgzNzk2MSAwLjgzMDMyNCwxLjk1MzcwMzE0IDAsMS4yNzUzMzM5NyAtMC44MzAzMjQsMS45NjQ1NTcwNiBRIDkuOTg3MTk2MSwyLjI3NDkxNSA4LjQ0MDUxNDUsMi4yNzQ5MTUgSCA3LjA2MjA2ODQgViA1LjA4NjA3NjcgSCA0Ljk3MjY5MTUgWiBtIDIuMDg5Mzc2OSwxLjUxNDExOTkgdiAyLjI2MzAzOTQzIGggMS4xNTU5NDEgcSAwLjYwNzgxODgsMCAwLjkzODg2MjksLTAuMjkzMDU1NDcgMC4zMzEwNDQxLC0wLjI5ODQ4MjQxIDAuMzMxMDQ0MSwtMC44NDExNzc3MiAwLC0wLjU0MjY5NTMxIC0wLjMzMTA0NDEsLTAuODM1NzUwNzQgLTAuMzMxMDQ0MSwtMC4yOTMwNTU1IC0wLjkzODg2MjksLTAuMjkzMDU1NSB6IgovPgo8L3N2Zz4K);
  --jp-icon-python: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iLTEwIC0xMCAxMzEuMTYxMzYxNjk0MzM1OTQgMTMyLjM4ODk5OTkzODk2NDg0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMzA2OTk4IiBkPSJNIDU0LjkxODc4NSw5LjE5Mjc0MjFlLTQgQyA1MC4zMzUxMzIsMC4wMjIyMTcyNyA0NS45NTc4NDYsMC40MTMxMzY5NyA0Mi4xMDYyODUsMS4wOTQ2NjkzIDMwLjc2MDA2OSwzLjA5OTE3MzEgMjguNzAwMDM2LDcuMjk0NzcxNCAyOC43MDAwMzUsMTUuMDMyMTY5IHYgMTAuMjE4NzUgaCAyNi44MTI1IHYgMy40MDYyNSBoIC0yNi44MTI1IC0xMC4wNjI1IGMgLTcuNzkyNDU5LDAgLTE0LjYxNTc1ODgsNC42ODM3MTcgLTE2Ljc0OTk5OTgsMTMuNTkzNzUgLTIuNDYxODE5OTgsMTAuMjEyOTY2IC0yLjU3MTAxNTA4LDE2LjU4NjAyMyAwLDI3LjI1IDEuOTA1OTI4Myw3LjkzNzg1MiA2LjQ1NzU0MzIsMTMuNTkzNzQ4IDE0LjI0OTk5OTgsMTMuNTkzNzUgaCA5LjIxODc1IHYgLTEyLjI1IGMgMCwtOC44NDk5MDIgNy42NTcxNDQsLTE2LjY1NjI0OCAxNi43NSwtMTYuNjU2MjUgaCAyNi43ODEyNSBjIDcuNDU0OTUxLDAgMTMuNDA2MjUzLC02LjEzODE2NCAxMy40MDYyNSwtMTMuNjI1IHYgLTI1LjUzMTI1IGMgMCwtNy4yNjYzMzg2IC02LjEyOTk4LC0xMi43MjQ3NzcxIC0xMy40MDYyNSwtMTMuOTM3NDk5NyBDIDY0LjI4MTU0OCwwLjMyNzk0Mzk3IDU5LjUwMjQzOCwtMC4wMjAzNzkwMyA1NC45MTg3ODUsOS4xOTI3NDIxZS00IFogbSAtMTQuNSw4LjIxODc1MDEyNTc5IGMgMi43Njk1NDcsMCA1LjAzMTI1LDIuMjk4NjQ1NiA1LjAzMTI1LDUuMTI0OTk5NiAtMmUtNiwyLjgxNjMzNiAtMi4yNjE3MDMsNS4wOTM3NSAtNS4wMzEyNSw1LjA5Mzc1IC0yLjc3OTQ3NiwtMWUtNiAtNS4wMzEyNSwtMi4yNzc0MTUgLTUuMDMxMjUsLTUuMDkzNzUgLTEwZS03LC0yLjgyNjM1MyAyLjI1MTc3NCwtNS4xMjQ5OTk2IDUuMDMxMjUsLTUuMTI0OTk5NiB6Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI2ZmZDQzYiIgZD0ibSA4NS42Mzc1MzUsMjguNjU3MTY5IHYgMTEuOTA2MjUgYyAwLDkuMjMwNzU1IC03LjgyNTg5NSwxNi45OTk5OTkgLTE2Ljc1LDE3IGggLTI2Ljc4MTI1IGMgLTcuMzM1ODMzLDAgLTEzLjQwNjI0OSw2LjI3ODQ4MyAtMTMuNDA2MjUsMTMuNjI1IHYgMjUuNTMxMjQ3IGMgMCw3LjI2NjM0NCA2LjMxODU4OCwxMS41NDAzMjQgMTMuNDA2MjUsMTMuNjI1MDA0IDguNDg3MzMxLDIuNDk1NjEgMTYuNjI2MjM3LDIuOTQ2NjMgMjYuNzgxMjUsMCA2Ljc1MDE1NSwtMS45NTQzOSAxMy40MDYyNTMsLTUuODg3NjEgMTMuNDA2MjUsLTEzLjYyNTAwNCBWIDg2LjUwMDkxOSBoIC0yNi43ODEyNSB2IC0zLjQwNjI1IGggMjYuNzgxMjUgMTMuNDA2MjU0IGMgNy43OTI0NjEsMCAxMC42OTYyNTEsLTUuNDM1NDA4IDEzLjQwNjI0MSwtMTMuNTkzNzUgMi43OTkzMywtOC4zOTg4ODYgMi42ODAyMiwtMTYuNDc1Nzc2IDAsLTI3LjI1IC0xLjkyNTc4LC03Ljc1NzQ0MSAtNS42MDM4NywtMTMuNTkzNzUgLTEzLjQwNjI0MSwtMTMuNTkzNzUgeiBtIC0xNS4wNjI1LDY0LjY1NjI1IGMgMi43Nzk0NzgsM2UtNiA1LjAzMTI1LDIuMjc3NDE3IDUuMDMxMjUsNS4wOTM3NDcgLTJlLTYsMi44MjYzNTQgLTIuMjUxNzc1LDUuMTI1MDA0IC01LjAzMTI1LDUuMTI1MDA0IC0yLjc2OTU1LDAgLTUuMDMxMjUsLTIuMjk4NjUgLTUuMDMxMjUsLTUuMTI1MDA0IDJlLTYsLTIuODE2MzMgMi4yNjE2OTcsLTUuMDkzNzQ3IDUuMDMxMjUsLTUuMDkzNzQ3IHoiLz4KPC9zdmc+Cg==);
  --jp-icon-r-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjE5NkYzIiBkPSJNNC40IDIuNWMxLjItLjEgMi45LS4zIDQuOS0uMyAyLjUgMCA0LjEuNCA1LjIgMS4zIDEgLjcgMS41IDEuOSAxLjUgMy41IDAgMi0xLjQgMy41LTIuOSA0LjEgMS4yLjQgMS43IDEuNiAyLjIgMyAuNiAxLjkgMSAzLjkgMS4zIDQuNmgtMy44Yy0uMy0uNC0uOC0xLjctMS4yLTMuN3MtMS4yLTIuNi0yLjYtMi42aC0uOXY2LjRINC40VjIuNXptMy43IDYuOWgxLjRjMS45IDAgMi45LS45IDIuOS0yLjNzLTEtMi4zLTIuOC0yLjNjLS43IDAtMS4zIDAtMS42LjJ2NC41aC4xdi0uMXoiLz4KPC9zdmc+Cg==);
  --jp-icon-react: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMTUwIDE1MCA1NDEuOSAyOTUuMyI+CiAgPGcgY2xhc3M9ImpwLWljb24tYnJhbmQyIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzYxREFGQiI+CiAgICA8cGF0aCBkPSJNNjY2LjMgMjk2LjVjMC0zMi41LTQwLjctNjMuMy0xMDMuMS04Mi40IDE0LjQtNjMuNiA4LTExNC4yLTIwLjItMTMwLjQtNi41LTMuOC0xNC4xLTUuNi0yMi40LTUuNnYyMi4zYzQuNiAwIDguMy45IDExLjQgMi42IDEzLjYgNy44IDE5LjUgMzcuNSAxNC45IDc1LjctMS4xIDkuNC0yLjkgMTkuMy01LjEgMjkuNC0xOS42LTQuOC00MS04LjUtNjMuNS0xMC45LTEzLjUtMTguNS0yNy41LTM1LjMtNDEuNi01MCAzMi42LTMwLjMgNjMuMi00Ni45IDg0LTQ2LjlWNzhjLTI3LjUgMC02My41IDE5LjYtOTkuOSA1My42LTM2LjQtMzMuOC03Mi40LTUzLjItOTkuOS01My4ydjIyLjNjMjAuNyAwIDUxLjQgMTYuNSA4NCA0Ni42LTE0IDE0LjctMjggMzEuNC00MS4zIDQ5LjktMjIuNiAyLjQtNDQgNi4xLTYzLjYgMTEtMi4zLTEwLTQtMTkuNy01LjItMjktNC43LTM4LjIgMS4xLTY3LjkgMTQuNi03NS44IDMtMS44IDYuOS0yLjYgMTEuNS0yLjZWNzguNWMtOC40IDAtMTYgMS44LTIyLjYgNS42LTI4LjEgMTYuMi0zNC40IDY2LjctMTkuOSAxMzAuMS02Mi4yIDE5LjItMTAyLjcgNDkuOS0xMDIuNyA4Mi4zIDAgMzIuNSA0MC43IDYzLjMgMTAzLjEgODIuNC0xNC40IDYzLjYtOCAxMTQuMiAyMC4yIDEzMC40IDYuNSAzLjggMTQuMSA1LjYgMjIuNSA1LjYgMjcuNSAwIDYzLjUtMTkuNiA5OS45LTUzLjYgMzYuNCAzMy44IDcyLjQgNTMuMiA5OS45IDUzLjIgOC40IDAgMTYtMS44IDIyLjYtNS42IDI4LjEtMTYuMiAzNC40LTY2LjcgMTkuOS0xMzAuMSA2Mi0xOS4xIDEwMi41LTQ5LjkgMTAyLjUtODIuM3ptLTEzMC4yLTY2LjdjLTMuNyAxMi45LTguMyAyNi4yLTEzLjUgMzkuNS00LjEtOC04LjQtMTYtMTMuMS0yNC00LjYtOC05LjUtMTUuOC0xNC40LTIzLjQgMTQuMiAyLjEgMjcuOSA0LjcgNDEgNy45em0tNDUuOCAxMDYuNWMtNy44IDEzLjUtMTUuOCAyNi4zLTI0LjEgMzguMi0xNC45IDEuMy0zMCAyLTQ1LjIgMi0xNS4xIDAtMzAuMi0uNy00NS0xLjktOC4zLTExLjktMTYuNC0yNC42LTI0LjItMzgtNy42LTEzLjEtMTQuNS0yNi40LTIwLjgtMzkuOCA2LjItMTMuNCAxMy4yLTI2LjggMjAuNy0zOS45IDcuOC0xMy41IDE1LjgtMjYuMyAyNC4xLTM4LjIgMTQuOS0xLjMgMzAtMiA0NS4yLTIgMTUuMSAwIDMwLjIuNyA0NSAxLjkgOC4zIDExLjkgMTYuNCAyNC42IDI0LjIgMzggNy42IDEzLjEgMTQuNSAyNi40IDIwLjggMzkuOC02LjMgMTMuNC0xMy4yIDI2LjgtMjAuNyAzOS45em0zMi4zLTEzYzUuNCAxMy40IDEwIDI2LjggMTMuOCAzOS44LTEzLjEgMy4yLTI2LjkgNS45LTQxLjIgOCA0LjktNy43IDkuOC0xNS42IDE0LjQtMjMuNyA0LjYtOCA4LjktMTYuMSAxMy0yNC4xek00MjEuMiA0MzBjLTkuMy05LjYtMTguNi0yMC4zLTI3LjgtMzIgOSAuNCAxOC4yLjcgMjcuNS43IDkuNCAwIDE4LjctLjIgMjcuOC0uNy05IDExLjctMTguMyAyMi40LTI3LjUgMzJ6bS03NC40LTU4LjljLTE0LjItMi4xLTI3LjktNC43LTQxLTcuOSAzLjctMTIuOSA4LjMtMjYuMiAxMy41LTM5LjUgNC4xIDggOC40IDE2IDEzLjEgMjQgNC43IDggOS41IDE1LjggMTQuNCAyMy40ek00MjAuNyAxNjNjOS4zIDkuNiAxOC42IDIwLjMgMjcuOCAzMi05LS40LTE4LjItLjctMjcuNS0uNy05LjQgMC0xOC43LjItMjcuOC43IDktMTEuNyAxOC4zLTIyLjQgMjcuNS0zMnptLTc0IDU4LjljLTQuOSA3LjctOS44IDE1LjYtMTQuNCAyMy43LTQuNiA4LTguOSAxNi0xMyAyNC01LjQtMTMuNC0xMC0yNi44LTEzLjgtMzkuOCAxMy4xLTMuMSAyNi45LTUuOCA0MS4yLTcuOXptLTkwLjUgMTI1LjJjLTM1LjQtMTUuMS01OC4zLTM0LjktNTguMy01MC42IDAtMTUuNyAyMi45LTM1LjYgNTguMy01MC42IDguNi0zLjcgMTgtNyAyNy43LTEwLjEgNS43IDE5LjYgMTMuMiA0MCAyMi41IDYwLjktOS4yIDIwLjgtMTYuNiA0MS4xLTIyLjIgNjAuNi05LjktMy4xLTE5LjMtNi41LTI4LTEwLjJ6TTMxMCA0OTBjLTEzLjYtNy44LTE5LjUtMzcuNS0xNC45LTc1LjcgMS4xLTkuNCAyLjktMTkuMyA1LjEtMjkuNCAxOS42IDQuOCA0MSA4LjUgNjMuNSAxMC45IDEzLjUgMTguNSAyNy41IDM1LjMgNDEuNiA1MC0zMi42IDMwLjMtNjMuMiA0Ni45LTg0IDQ2LjktNC41LS4xLTguMy0xLTExLjMtMi43em0yMzcuMi03Ni4yYzQuNyAzOC4yLTEuMSA2Ny45LTE0LjYgNzUuOC0zIDEuOC02LjkgMi42LTExLjUgMi42LTIwLjcgMC01MS40LTE2LjUtODQtNDYuNiAxNC0xNC43IDI4LTMxLjQgNDEuMy00OS45IDIyLjYtMi40IDQ0LTYuMSA2My42LTExIDIuMyAxMC4xIDQuMSAxOS44IDUuMiAyOS4xem0zOC41LTY2LjdjLTguNiAzLjctMTggNy0yNy43IDEwLjEtNS43LTE5LjYtMTMuMi00MC0yMi41LTYwLjkgOS4yLTIwLjggMTYuNi00MS4xIDIyLjItNjAuNiA5LjkgMy4xIDE5LjMgNi41IDI4LjEgMTAuMiAzNS40IDE1LjEgNTguMyAzNC45IDU4LjMgNTAuNi0uMSAxNS43LTIzIDM1LjYtNTguNCA1MC42ek0zMjAuOCA3OC40eiIvPgogICAgPGNpcmNsZSBjeD0iNDIwLjkiIGN5PSIyOTYuNSIgcj0iNDUuNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-redo: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIi8+PHBhdGggZD0iTTE4LjQgMTAuNkMxNi41NSA4Ljk5IDE0LjE1IDggMTEuNSA4Yy00LjY1IDAtOC41OCAzLjAzLTkuOTYgNy4yMkwzLjkgMTZjMS4wNS0zLjE5IDQuMDUtNS41IDcuNi01LjUgMS45NSAwIDMuNzMuNzIgNS4xMiAxLjg4TDEzIDE2aDlWN2wtMy42IDMuNnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-refresh: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTkgMTMuNWMtMi40OSAwLTQuNS0yLjAxLTQuNS00LjVTNi41MSA0LjUgOSA0LjVjMS4yNCAwIDIuMzYuNTIgMy4xNyAxLjMzTDEwIDhoNVYzbC0xLjc2IDEuNzZDMTIuMTUgMy42OCAxMC42NiAzIDkgMyA1LjY5IDMgMy4wMSA1LjY5IDMuMDEgOVM1LjY5IDE1IDkgMTVjMi45NyAwIDUuNDMtMi4xNiA1LjktNWgtMS41MmMtLjQ2IDItMi4yNCAzLjUtNC4zOCAzLjV6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-regex: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi1hY2NlbnQyIiBmaWxsPSIjRkZGIj4KICAgIDxjaXJjbGUgY2xhc3M9InN0MiIgY3g9IjUuNSIgY3k9IjE0LjUiIHI9IjEuNSIvPgogICAgPHJlY3QgeD0iMTIiIHk9IjQiIGNsYXNzPSJzdDIiIHdpZHRoPSIxIiBoZWlnaHQ9IjgiLz4KICAgIDxyZWN0IHg9IjguNSIgeT0iNy41IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjg2NiAtMC41IDAuNSAwLjg2NiAtMi4zMjU1IDcuMzIxOSkiIGNsYXNzPSJzdDIiIHdpZHRoPSI4IiBoZWlnaHQ9IjEiLz4KICAgIDxyZWN0IHg9IjEyIiB5PSI0IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjUgLTAuODY2IDAuODY2IDAuNSAtMC42Nzc5IDE0LjgyNTIpIiBjbGFzcz0ic3QyIiB3aWR0aD0iMSIgaGVpZ2h0PSI4Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-run: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTggNXYxNGwxMS03eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-running: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMjU2IDhDMTE5IDggOCAxMTkgOCAyNTZzMTExIDI0OCAyNDggMjQ4IDI0OC0xMTEgMjQ4LTI0OFMzOTMgOCAyNTYgOHptOTYgMzI4YzAgOC44LTcuMiAxNi0xNiAxNkgxNzZjLTguOCAwLTE2LTcuMi0xNi0xNlYxNzZjMC04LjggNy4yLTE2IDE2LTE2aDE2MGM4LjggMCAxNiA3LjIgMTYgMTZ2MTYweiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-save: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE3IDNINWMtMS4xMSAwLTIgLjktMiAydjE0YzAgMS4xLjg5IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjdsLTQtNHptLTUgMTZjLTEuNjYgMC0zLTEuMzQtMy0zczEuMzQtMyAzLTMgMyAxLjM0IDMgMy0xLjM0IDMtMyAzem0zLTEwSDVWNWgxMHY0eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-search: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjEsMTAuOWgtMC43bC0wLjItMC4yYzAuOC0wLjksMS4zLTIuMiwxLjMtMy41YzAtMy0yLjQtNS40LTUuNC01LjRTMS44LDQuMiwxLjgsNy4xczIuNCw1LjQsNS40LDUuNCBjMS4zLDAsMi41LTAuNSwzLjUtMS4zbDAuMiwwLjJ2MC43bDQuMSw0LjFsMS4yLTEuMkwxMi4xLDEwLjl6IE03LjEsMTAuOWMtMi4xLDAtMy43LTEuNy0zLjctMy43czEuNy0zLjcsMy43LTMuN3MzLjcsMS43LDMuNywzLjcgUzkuMiwxMC45LDcuMSwxMC45eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-settings: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuNDMgMTIuOThjLjA0LS4zMi4wNy0uNjQuMDctLjk4cy0uMDMtLjY2LS4wNy0uOThsMi4xMS0xLjY1Yy4xOS0uMTUuMjQtLjQyLjEyLS42NGwtMi0zLjQ2Yy0uMTItLjIyLS4zOS0uMy0uNjEtLjIybC0yLjQ5IDFjLS41Mi0uNC0xLjA4LS43My0xLjY5LS45OGwtLjM4LTIuNjVBLjQ4OC40ODggMCAwMDE0IDJoLTRjLS4yNSAwLS40Ni4xOC0uNDkuNDJsLS4zOCAyLjY1Yy0uNjEuMjUtMS4xNy41OS0xLjY5Ljk4bC0yLjQ5LTFjLS4yMy0uMDktLjQ5IDAtLjYxLjIybC0yIDMuNDZjLS4xMy4yMi0uMDcuNDkuMTIuNjRsMi4xMSAxLjY1Yy0uMDQuMzItLjA3LjY1LS4wNy45OHMuMDMuNjYuMDcuOThsLTIuMTEgMS42NWMtLjE5LjE1LS4yNC40Mi0uMTIuNjRsMiAzLjQ2Yy4xMi4yMi4zOS4zLjYxLjIybDIuNDktMWMuNTIuNCAxLjA4LjczIDEuNjkuOThsLjM4IDIuNjVjLjAzLjI0LjI0LjQyLjQ5LjQyaDRjLjI1IDAgLjQ2LS4xOC40OS0uNDJsLjM4LTIuNjVjLjYxLS4yNSAxLjE3LS41OSAxLjY5LS45OGwyLjQ5IDFjLjIzLjA5LjQ5IDAgLjYxLS4yMmwyLTMuNDZjLjEyLS4yMi4wNy0uNDktLjEyLS42NGwtMi4xMS0xLjY1ek0xMiAxNS41Yy0xLjkzIDAtMy41LTEuNTctMy41LTMuNXMxLjU3LTMuNSAzLjUtMy41IDMuNSAxLjU3IDMuNSAzLjUtMS41NyAzLjUtMy41IDMuNXoiLz4KPC9zdmc+Cg==);
  --jp-icon-share: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTSAxOCAyIEMgMTYuMzU0OTkgMiAxNSAzLjM1NDk5MDQgMTUgNSBDIDE1IDUuMTkwOTUyOSAxNS4wMjE3OTEgNS4zNzcxMjI0IDE1LjA1NjY0MSA1LjU1ODU5MzggTCA3LjkyMTg3NSA5LjcyMDcwMzEgQyA3LjM5ODUzOTkgOS4yNzc4NTM5IDYuNzMyMDc3MSA5IDYgOSBDIDQuMzU0OTkwNCA5IDMgMTAuMzU0OTkgMyAxMiBDIDMgMTMuNjQ1MDEgNC4zNTQ5OTA0IDE1IDYgMTUgQyA2LjczMjA3NzEgMTUgNy4zOTg1Mzk5IDE0LjcyMjE0NiA3LjkyMTg3NSAxNC4yNzkyOTcgTCAxNS4wNTY2NDEgMTguNDM5NDUzIEMgMTUuMDIxNTU1IDE4LjYyMTUxNCAxNSAxOC44MDgzODYgMTUgMTkgQyAxNSAyMC42NDUwMSAxNi4zNTQ5OSAyMiAxOCAyMiBDIDE5LjY0NTAxIDIyIDIxIDIwLjY0NTAxIDIxIDE5IEMgMjEgMTcuMzU0OTkgMTkuNjQ1MDEgMTYgMTggMTYgQyAxNy4yNjc0OCAxNiAxNi42MDE1OTMgMTYuMjc5MzI4IDE2LjA3ODEyNSAxNi43MjI2NTYgTCA4Ljk0MzM1OTQgMTIuNTU4NTk0IEMgOC45NzgyMDk1IDEyLjM3NzEyMiA5IDEyLjE5MDk1MyA5IDEyIEMgOSAxMS44MDkwNDcgOC45NzgyMDk1IDExLjYyMjg3OCA4Ljk0MzM1OTQgMTEuNDQxNDA2IEwgMTYuMDc4MTI1IDcuMjc5Mjk2OSBDIDE2LjYwMTQ2IDcuNzIyMTQ2MSAxNy4yNjc5MjMgOCAxOCA4IEMgMTkuNjQ1MDEgOCAyMSA2LjY0NTAwOTYgMjEgNSBDIDIxIDMuMzU0OTkwNCAxOS42NDUwMSAyIDE4IDIgeiBNIDE4IDQgQyAxOC41NjQxMjkgNCAxOSA0LjQzNTg3MDYgMTkgNSBDIDE5IDUuNTY0MTI5NCAxOC41NjQxMjkgNiAxOCA2IEMgMTcuNDM1ODcxIDYgMTcgNS41NjQxMjk0IDE3IDUgQyAxNyA0LjQzNTg3MDYgMTcuNDM1ODcxIDQgMTggNCB6IE0gNiAxMSBDIDYuNTY0MTI5NCAxMSA3IDExLjQzNTg3MSA3IDEyIEMgNyAxMi41NjQxMjkgNi41NjQxMjk0IDEzIDYgMTMgQyA1LjQzNTg3MDYgMTMgNSAxMi41NjQxMjkgNSAxMiBDIDUgMTEuNDM1ODcxIDUuNDM1ODcwNiAxMSA2IDExIHogTSAxOCAxOCBDIDE4LjU2NDEyOSAxOCAxOSAxOC40MzU4NzEgMTkgMTkgQyAxOSAxOS41NjQxMjkgMTguNTY0MTI5IDIwIDE4IDIwIEMgMTcuNDM1ODcxIDIwIDE3IDE5LjU2NDEyOSAxNyAxOSBDIDE3IDE4LjQzNTg3MSAxNy40MzU4NzEgMTggMTggMTggeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-spreadsheet: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNENBRjUwIiBkPSJNMi4yIDIuMnYxNy42aDE3LjZWMi4ySDIuMnptMTUuNCA3LjdoLTUuNVY0LjRoNS41djUuNXpNOS45IDQuNHY1LjVINC40VjQuNGg1LjV6bS01LjUgNy43aDUuNXY1LjVINC40di01LjV6bTcuNyA1LjV2LTUuNWg1LjV2NS41aC01LjV6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-stop: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik02IDZoMTJ2MTJINnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tab: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIxIDNIM2MtMS4xIDAtMiAuOS0yIDJ2MTRjMCAxLjEuOSAyIDIgMmgxOGMxLjEgMCAyLS45IDItMlY1YzAtMS4xLS45LTItMi0yem0wIDE2SDNWNWgxMHY0aDh2MTB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-table-rows: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMSw4SDNWNGgxOFY4eiBNMjEsMTBIM3Y0aDE4VjEweiBNMjEsMTZIM3Y0aDE4VjE2eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-tag: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgiIGhlaWdodD0iMjgiIHZpZXdCb3g9IjAgMCA0MyAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTI4LjgzMzIgMTIuMzM0TDMyLjk5OTggMTYuNTAwN0wzNy4xNjY1IDEyLjMzNEgyOC44MzMyWiIvPgoJCTxwYXRoIGQ9Ik0xNi4yMDk1IDIxLjYxMDRDMTUuNjg3MyAyMi4xMjk5IDE0Ljg0NDMgMjIuMTI5OSAxNC4zMjQ4IDIxLjYxMDRMNi45ODI5IDE0LjcyNDVDNi41NzI0IDE0LjMzOTQgNi4wODMxMyAxMy42MDk4IDYuMDQ3ODYgMTMuMDQ4MkM1Ljk1MzQ3IDExLjUyODggNi4wMjAwMiA4LjYxOTQ0IDYuMDY2MjEgNy4wNzY5NUM2LjA4MjgxIDYuNTE0NzcgNi41NTU0OCA2LjA0MzQ3IDcuMTE4MDQgNi4wMzA1NUM5LjA4ODYzIDUuOTg0NzMgMTMuMjYzOCA1LjkzNTc5IDEzLjY1MTggNi4zMjQyNUwyMS43MzY5IDEzLjYzOUMyMi4yNTYgMTQuMTU4NSAyMS43ODUxIDE1LjQ3MjQgMjEuMjYyIDE1Ljk5NDZMMTYuMjA5NSAyMS42MTA0Wk05Ljc3NTg1IDguMjY1QzkuMzM1NTEgNy44MjU2NiA4LjYyMzUxIDcuODI1NjYgOC4xODI4IDguMjY1QzcuNzQzNDYgOC43MDU3MSA3Ljc0MzQ2IDkuNDE3MzMgOC4xODI4IDkuODU2NjdDOC42MjM4MiAxMC4yOTY0IDkuMzM1ODIgMTAuMjk2NCA5Ljc3NTg1IDkuODU2NjdDMTAuMjE1NiA5LjQxNzMzIDEwLjIxNTYgOC43MDUzMyA5Ljc3NTg1IDguMjY1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-terminal: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0IiA+CiAgICA8cmVjdCBjbGFzcz0ianAtdGVybWluYWwtaWNvbi1iYWNrZ3JvdW5kLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZSIgd2lkdGg9IjIwIiBoZWlnaHQ9IjIwIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyIDIpIiBmaWxsPSIjMzMzMzMzIi8+CiAgICA8cGF0aCBjbGFzcz0ianAtdGVybWluYWwtaWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUtaW52ZXJzZSIgZD0iTTUuMDU2NjQgOC43NjE3MkM1LjA1NjY0IDguNTk3NjYgNS4wMzEyNSA4LjQ1MzEyIDQuOTgwNDcgOC4zMjgxMkM0LjkzMzU5IDguMTk5MjIgNC44NTU0NyA4LjA4MjAzIDQuNzQ2MDkgNy45NzY1NkM0LjY0MDYyIDcuODcxMDkgNC41IDcuNzc1MzkgNC4zMjQyMiA3LjY4OTQ1QzQuMTUyMzQgNy41OTk2MSAzLjk0MzM2IDcuNTExNzIgMy42OTcyNyA3LjQyNTc4QzMuMzAyNzMgNy4yODUxNiAyLjk0MzM2IDcuMTM2NzIgMi42MTkxNCA2Ljk4MDQ3QzIuMjk0OTIgNi44MjQyMiAyLjAxNzU4IDYuNjQyNTggMS43ODcxMSA2LjQzNTU1QzEuNTYwNTUgNi4yMjg1MiAxLjM4NDc3IDUuOTg4MjggMS4yNTk3NyA1LjcxNDg0QzEuMTM0NzcgNS40Mzc1IDEuMDcyMjcgNS4xMDkzOCAxLjA3MjI3IDQuNzMwNDdDMS4wNzIyNyA0LjM5ODQ0IDEuMTI4OTEgNC4wOTU3IDEuMjQyMTkgMy44MjIyN0MxLjM1NTQ3IDMuNTQ0OTIgMS41MTU2MiAzLjMwNDY5IDEuNzIyNjYgMy4xMDE1NkMxLjkyOTY5IDIuODk4NDQgMi4xNzk2OSAyLjczNDM3IDIuNDcyNjYgMi42MDkzOEMyLjc2NTYyIDIuNDg0MzggMy4wOTE4IDIuNDA0MyAzLjQ1MTE3IDIuMzY5MTRWMS4xMDkzOEg0LjM4ODY3VjIuMzgwODZDNC43NDAyMyAyLjQyNzczIDUuMDU2NjQgMi41MjM0NCA1LjMzNzg5IDIuNjY3OTdDNS42MTkxNCAyLjgxMjUgNS44NTc0MiAzLjAwMTk1IDYuMDUyNzMgMy4yMzYzM0M2LjI1MTk1IDMuNDY2OCA2LjQwNDMgMy43NDAyMyA2LjUwOTc3IDQuMDU2NjRDNi42MTkxNCA0LjM2OTE0IDYuNjczODMgNC43MjA3IDYuNjczODMgNS4xMTEzM0g1LjA0NDkyQzUuMDQ0OTIgNC42Mzg2NyA0LjkzNzUgNC4yODEyNSA0LjcyMjY2IDQuMDM5MDZDNC41MDc4MSAzLjc5Mjk3IDQuMjE2OCAzLjY2OTkyIDMuODQ5NjEgMy42Njk5MkMzLjY1MDM5IDMuNjY5OTIgMy40NzY1NiAzLjY5NzI3IDMuMzI4MTIgMy43NTE5NUMzLjE4MzU5IDMuODAyNzMgMy4wNjQ0NSAzLjg3Njk1IDIuOTcwNyAzLjk3NDYxQzIuODc2OTUgNC4wNjgzNiAyLjgwNjY0IDQuMTc5NjkgMi43NTk3NyA0LjMwODU5QzIuNzE2OCA0LjQzNzUgMi42OTUzMSA0LjU3ODEyIDIuNjk1MzEgNC43MzA0N0MyLjY5NTMxIDQuODgyODEgMi43MTY4IDUuMDE5NTMgMi43NTk3NyA1LjE0MDYyQzIuODA2NjQgNS4yNTc4MSAyLjg4MjgxIDUuMzY3MTkgMi45ODgyOCA1LjQ2ODc1QzMuMDk3NjYgNS41NzAzMSAzLjI0MDIzIDUuNjY3OTcgMy40MTYwMiA1Ljc2MTcyQzMuNTkxOCA1Ljg1MTU2IDMuODEwNTUgNS45NDMzNiA0LjA3MjI3IDYuMDM3MTFDNC40NjY4IDYuMTg1NTUgNC44MjQyMiA2LjMzOTg0IDUuMTQ0NTMgNi41QzUuNDY0ODQgNi42NTYyNSA1LjczODI4IDYuODM5ODQgNS45NjQ4NCA3LjA1MDc4QzYuMTk1MzEgNy4yNTc4MSA2LjM3MTA5IDcuNSA2LjQ5MjE5IDcuNzc3MzRDNi42MTcxOSA4LjA1MDc4IDYuNjc5NjkgOC4zNzUgNi42Nzk2OSA4Ljc1QzYuNjc5NjkgOS4wOTM3NSA2LjYyMzA1IDkuNDA0MyA2LjUwOTc3IDkuNjgxNjRDNi4zOTY0OCA5Ljk1NTA4IDYuMjM0MzggMTAuMTkxNCA2LjAyMzQ0IDEwLjM5MDZDNS44MTI1IDEwLjU4OTggNS41NTg1OSAxMC43NSA1LjI2MTcyIDEwLjg3MTFDNC45NjQ4NCAxMC45ODgzIDQuNjMyODEgMTEuMDY0NSA0LjI2NTYyIDExLjA5OTZWMTIuMjQ4SDMuMzMzOThWMTEuMDk5NkMzLjAwMTk1IDExLjA2ODQgMi42Nzk2OSAxMC45OTYxIDIuMzY3MTkgMTAuODgyOEMyLjA1NDY5IDEwLjc2NTYgMS43NzczNCAxMC41OTc3IDEuNTM1MTYgMTAuMzc4OUMxLjI5Njg4IDEwLjE2MDIgMS4xMDU0NyA5Ljg4NDc3IDAuOTYwOTM4IDkuNTUyNzNDMC44MTY0MDYgOS4yMTY4IDAuNzQ0MTQxIDguODE0NDUgMC43NDQxNDEgOC4zNDU3SDIuMzc4OTFDMi4zNzg5MSA4LjYyNjk1IDIuNDE5OTIgOC44NjMyOCAyLjUwMTk1IDkuMDU0NjlDMi41ODM5OCA5LjI0MjE5IDIuNjg5NDUgOS4zOTI1OCAyLjgxODM2IDkuNTA1ODZDMi45NTExNyA5LjYxNTIzIDMuMTAxNTYgOS42OTMzNiAzLjI2OTUzIDkuNzQwMjNDMy40Mzc1IDkuNzg3MTEgMy42MDkzOCA5LjgxMDU1IDMuNzg1MTYgOS44MTA1NUM0LjIwMzEyIDkuODEwNTUgNC41MTk1MyA5LjcxMjg5IDQuNzM0MzggOS41MTc1OEM0Ljk0OTIyIDkuMzIyMjcgNS4wNTY2NCA5LjA3MDMxIDUuMDU2NjQgOC43NjE3MlpNMTMuNDE4IDEyLjI3MTVIOC4wNzQyMlYxMUgxMy40MThWMTIuMjcxNVoiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMuOTUyNjQgNikiIGZpbGw9IndoaXRlIi8+Cjwvc3ZnPgo=);
  --jp-icon-text-editor: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtdGV4dC1lZGl0b3ItaWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xNSAxNUgzdjJoMTJ2LTJ6bTAtOEgzdjJoMTJWN3pNMyAxM2gxOHYtMkgzdjJ6bTAgOGgxOHYtMkgzdjJ6TTMgM3YyaDE4VjNIM3oiLz4KPC9zdmc+Cg==);
  --jp-icon-toc: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik03LDVIMjFWN0g3VjVNNywxM1YxMUgyMVYxM0g3TTQsNC41QTEuNSwxLjUgMCAwLDEgNS41LDZBMS41LDEuNSAwIDAsMSA0LDcuNUExLjUsMS41IDAgMCwxIDIuNSw2QTEuNSwxLjUgMCAwLDEgNCw0LjVNNCwxMC41QTEuNSwxLjUgMCAwLDEgNS41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMy41QTEuNSwxLjUgMCAwLDEgMi41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMC41TTcsMTlWMTdIMjFWMTlIN000LDE2LjVBMS41LDEuNSAwIDAsMSA1LjUsMThBMS41LDEuNSAwIDAsMSA0LDE5LjVBMS41LDEuNSAwIDAsMSAyLjUsMThBMS41LDEuNSAwIDAsMSA0LDE2LjVaIiAvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tree-view: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMiAxMVYzaC03djNIOVYzSDJ2OGg3VjhoMnYxMGg0djNoN3YtOGgtN3YzaC0yVjhoMnYzeiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMiAxNy4xODQ0IDIuOTY5NjggMTQuMzAzMiAxLjg2MDk0IDExLjQ0MDlaIi8+CiAgICA8cGF0aCBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiMzMzMzMzMiIHN0cm9rZT0iIzMzMzMzMyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOCA5Ljg2NzE5KSIgZD0iTTIuODYwMTUgNC44NjUzNUwwLjcyNjU0OSAyLjk5OTU5TDAgMy42MzA0NUwyLjg2MDE1IDYuMTMxNTdMOCAwLjYzMDg3Mkw3LjI3ODU3IDBMMi44NjAxNSA0Ljg2NTM1WiIvPgo8L3N2Zz4K);
  --jp-icon-undo: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjUgOGMtMi42NSAwLTUuMDUuOTktNi45IDIuNkwyIDd2OWg5bC0zLjYyLTMuNjJjMS4zOS0xLjE2IDMuMTYtMS44OCA1LjEyLTEuODggMy41NCAwIDYuNTUgMi4zMSA3LjYgNS41bDIuMzctLjc4QzIxLjA4IDExLjAzIDE3LjE1IDggMTIuNSA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-user: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE2IDdhNCA0IDAgMTEtOCAwIDQgNCAwIDAxOCAwek0xMiAxNGE3IDcgMCAwMC03IDdoMTRhNyA3IDAgMDAtNy03eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-users: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZlcnNpb249IjEuMSIgdmlld0JveD0iMCAwIDM2IDI0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogPGcgY2xhc3M9ImpwLWljb24zIiB0cmFuc2Zvcm09Im1hdHJpeCgxLjczMjcgMCAwIDEuNzMyNyAtMy42MjgyIC4wOTk1NzcpIiBmaWxsPSIjNjE2MTYxIj4KICA8cGF0aCB0cmFuc2Zvcm09Im1hdHJpeCgxLjUsMCwwLDEuNSwwLC02KSIgZD0ibTEyLjE4NiA3LjUwOThjLTEuMDUzNSAwLTEuOTc1NyAwLjU2NjUtMi40Nzg1IDEuNDEwMiAwLjc1MDYxIDAuMzEyNzcgMS4zOTc0IDAuODI2NDggMS44NzMgMS40NzI3aDMuNDg2M2MwLTEuNTkyLTEuMjg4OS0yLjg4MjgtMi44ODA5LTIuODgyOHoiLz4KICA8cGF0aCBkPSJtMjAuNDY1IDIuMzg5NWEyLjE4ODUgMi4xODg1IDAgMCAxLTIuMTg4NCAyLjE4ODUgMi4xODg1IDIuMTg4NSAwIDAgMS0yLjE4ODUtMi4xODg1IDIuMTg4NSAyLjE4ODUgMCAwIDEgMi4xODg1LTIuMTg4NSAyLjE4ODUgMi4xODg1IDAgMCAxIDIuMTg4NCAyLjE4ODV6Ii8+CiAgPHBhdGggdHJhbnNmb3JtPSJtYXRyaXgoMS41LDAsMCwxLjUsMCwtNikiIGQ9Im0zLjU4OTggOC40MjE5Yy0xLjExMjYgMC0yLjAxMzcgMC45MDExMS0yLjAxMzcgMi4wMTM3aDIuODE0NWMwLjI2Nzk3LTAuMzczMDkgMC41OTA3LTAuNzA0MzUgMC45NTg5OC0wLjk3ODUyLTAuMzQ0MzMtMC42MTY4OC0xLjAwMzEtMS4wMzUyLTEuNzU5OC0xLjAzNTJ6Ii8+CiAgPHBhdGggZD0ibTYuOTE1NCA0LjYyM2ExLjUyOTQgMS41Mjk0IDAgMCAxLTEuNTI5NCAxLjUyOTQgMS41Mjk0IDEuNTI5NCAwIDAgMS0xLjUyOTQtMS41Mjk0IDEuNTI5NCAxLjUyOTQgMCAwIDEgMS41Mjk0LTEuNTI5NCAxLjUyOTQgMS41Mjk0IDAgMCAxIDEuNTI5NCAxLjUyOTR6Ii8+CiAgPHBhdGggZD0ibTYuMTM1IDEzLjUzNWMwLTMuMjM5MiAyLjYyNTktNS44NjUgNS44NjUtNS44NjUgMy4yMzkyIDAgNS44NjUgMi42MjU5IDUuODY1IDUuODY1eiIvPgogIDxjaXJjbGUgY3g9IjEyIiBjeT0iMy43Njg1IiByPSIyLjk2ODUiLz4KIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-vega: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbjEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjEyMTIxIj4KICAgIDxwYXRoIGQ9Ik0xMC42IDUuNGwyLjItMy4ySDIuMnY3LjNsNC02LjZ6Ii8+CiAgICA8cGF0aCBkPSJNMTUuOCAyLjJsLTQuNCA2LjZMNyA2LjNsLTQuOCA4djUuNWgxNy42VjIuMmgtNHptLTcgMTUuNEg1LjV2LTQuNGgzLjN2NC40em00LjQgMEg5LjhWOS44aDMuNHY3Ljh6bTQuNCAwaC0zLjRWNi41aDMuNHYxMS4xeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-word: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KIDxnIGNsYXNzPSJqcC1pY29uMiIgZmlsbD0iIzQxNDE0MSI+CiAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiA8L2c+CiA8ZyBjbGFzcz0ianAtaWNvbi1hY2NlbnQyIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSguNDMgLjA0MDEpIiBmaWxsPSIjZmZmIj4KICA8cGF0aCBkPSJtNC4xNCA4Ljc2cTAuMDY4Mi0xLjg5IDIuNDItMS44OSAxLjE2IDAgMS42OCAwLjQyIDAuNTY3IDAuNDEgMC41NjcgMS4xNnYzLjQ3cTAgMC40NjIgMC41MTQgMC40NjIgMC4xMDMgMCAwLjItMC4wMjMxdjAuNzE0cS0wLjM5OSAwLjEwMy0wLjY1MSAwLjEwMy0wLjQ1MiAwLTAuNjkzLTAuMjItMC4yMzEtMC4yLTAuMjg0LTAuNjYyLTAuOTU2IDAuODcyLTIgMC44NzItMC45MDMgMC0xLjQ3LTAuNDcyLTAuNTI1LTAuNDcyLTAuNTI1LTEuMjYgMC0wLjI2MiAwLjA0NTItMC40NzIgMC4wNTY3LTAuMjIgMC4xMTYtMC4zNzggMC4wNjgyLTAuMTY4IDAuMjMxLTAuMzA0IDAuMTU4LTAuMTQ3IDAuMjYyLTAuMjQyIDAuMTE2LTAuMDkxNCAwLjM2OC0wLjE2OCAwLjI2Mi0wLjA5MTQgMC4zOTktMC4xMjYgMC4xMzYtMC4wNDUyIDAuNDcyLTAuMTAzIDAuMzM2LTAuMDU3OCAwLjUwNC0wLjA3OTggMC4xNTgtMC4wMjMxIDAuNTY3LTAuMDc5OCAwLjU1Ni0wLjA2ODIgMC43NzctMC4yMjEgMC4yMi0wLjE1MiAwLjIyLTAuNDQxdi0wLjI1MnEwLTAuNDMtMC4zNTctMC42NjItMC4zMzYtMC4yMzEtMC45NzYtMC4yMzEtMC42NjIgMC0wLjk5OCAwLjI2Mi0wLjMzNiAwLjI1Mi0wLjM5OSAwLjc5OHptMS44OSAzLjY4cTAuNzg4IDAgMS4yNi0wLjQxIDAuNTA0LTAuNDIgMC41MDQtMC45MDN2LTEuMDVxLTAuMjg0IDAuMTM2LTAuODYxIDAuMjMxLTAuNTY3IDAuMDkxNC0wLjk4NyAwLjE1OC0wLjQyIDAuMDY4Mi0wLjc2NiAwLjMyNi0wLjMzNiAwLjI1Mi0wLjMzNiAwLjcwNHQwLjMwNCAwLjcwNCAwLjg2MSAwLjI1MnoiIHN0cm9rZS13aWR0aD0iMS4wNSIvPgogIDxwYXRoIGQ9Im0xMCA0LjU2aDAuOTQ1djMuMTVxMC42NTEtMC45NzYgMS44OS0wLjk3NiAxLjE2IDAgMS44OSAwLjg0IDAuNjgyIDAuODQgMC42ODIgMi4zMSAwIDEuNDctMC43MDQgMi40Mi0wLjcwNCAwLjg4Mi0xLjg5IDAuODgyLTEuMjYgMC0xLjg5LTEuMDJ2MC43NjZoLTAuODV6bTIuNjIgMy4wNHEtMC43NDYgMC0xLjE2IDAuNjQtMC40NTIgMC42My0wLjQ1MiAxLjY4IDAgMS4wNSAwLjQ1MiAxLjY4dDEuMTYgMC42M3EwLjc3NyAwIDEuMjYtMC42MyAwLjQ5NC0wLjY0IDAuNDk0LTEuNjggMC0xLjA1LTAuNDcyLTEuNjgtMC40NjItMC42NC0xLjI2LTAuNjR6IiBzdHJva2Utd2lkdGg9IjEuMDUiLz4KICA8cGF0aCBkPSJtMi43MyAxNS44IDEzLjYgMC4wMDgxYzAuMDA2OSAwIDAtMi42IDAtMi42IDAtMC4wMDc4LTEuMTUgMC0xLjE1IDAtMC4wMDY5IDAtMC4wMDgzIDEuNS0wLjAwODMgMS41LTJlLTMgLTAuMDAxNC0xMS4zLTAuMDAxNC0xMS4zLTAuMDAxNGwtMC4wMDU5Mi0xLjVjMC0wLjAwNzgtMS4xNyAwLjAwMTMtMS4xNyAwLjAwMTN6IiBzdHJva2Utd2lkdGg9Ii45NzUiLz4KIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-yaml: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1jb250cmFzdDIganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjRDgxQjYwIj4KICAgIDxwYXRoIGQ9Ik03LjIgMTguNnYtNS40TDMgNS42aDMuM2wxLjQgMy4xYy4zLjkuNiAxLjYgMSAyLjUuMy0uOC42LTEuNiAxLTIuNWwxLjQtMy4xaDMuNGwtNC40IDcuNnY1LjVsLTIuOS0uMXoiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxNi41IiByPSIyLjEiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxMSIgcj0iMi4xIi8+CiAgPC9nPgo8L3N2Zz4K);
}

/* Icon CSS class declarations */

.jp-AddAboveIcon {
  background-image: var(--jp-icon-add-above);
}

.jp-AddBelowIcon {
  background-image: var(--jp-icon-add-below);
}

.jp-AddIcon {
  background-image: var(--jp-icon-add);
}

.jp-BellIcon {
  background-image: var(--jp-icon-bell);
}

.jp-BugDotIcon {
  background-image: var(--jp-icon-bug-dot);
}

.jp-BugIcon {
  background-image: var(--jp-icon-bug);
}

.jp-BuildIcon {
  background-image: var(--jp-icon-build);
}

.jp-CaretDownEmptyIcon {
  background-image: var(--jp-icon-caret-down-empty);
}

.jp-CaretDownEmptyThinIcon {
  background-image: var(--jp-icon-caret-down-empty-thin);
}

.jp-CaretDownIcon {
  background-image: var(--jp-icon-caret-down);
}

.jp-CaretLeftIcon {
  background-image: var(--jp-icon-caret-left);
}

.jp-CaretRightIcon {
  background-image: var(--jp-icon-caret-right);
}

.jp-CaretUpEmptyThinIcon {
  background-image: var(--jp-icon-caret-up-empty-thin);
}

.jp-CaretUpIcon {
  background-image: var(--jp-icon-caret-up);
}

.jp-CaseSensitiveIcon {
  background-image: var(--jp-icon-case-sensitive);
}

.jp-CheckIcon {
  background-image: var(--jp-icon-check);
}

.jp-CircleEmptyIcon {
  background-image: var(--jp-icon-circle-empty);
}

.jp-CircleIcon {
  background-image: var(--jp-icon-circle);
}

.jp-ClearIcon {
  background-image: var(--jp-icon-clear);
}

.jp-CloseIcon {
  background-image: var(--jp-icon-close);
}

.jp-CodeCheckIcon {
  background-image: var(--jp-icon-code-check);
}

.jp-CodeIcon {
  background-image: var(--jp-icon-code);
}

.jp-CollapseAllIcon {
  background-image: var(--jp-icon-collapse-all);
}

.jp-ConsoleIcon {
  background-image: var(--jp-icon-console);
}

.jp-CopyIcon {
  background-image: var(--jp-icon-copy);
}

.jp-CopyrightIcon {
  background-image: var(--jp-icon-copyright);
}

.jp-CutIcon {
  background-image: var(--jp-icon-cut);
}

.jp-DeleteIcon {
  background-image: var(--jp-icon-delete);
}

.jp-DownloadIcon {
  background-image: var(--jp-icon-download);
}

.jp-DuplicateIcon {
  background-image: var(--jp-icon-duplicate);
}

.jp-EditIcon {
  background-image: var(--jp-icon-edit);
}

.jp-EllipsesIcon {
  background-image: var(--jp-icon-ellipses);
}

.jp-ErrorIcon {
  background-image: var(--jp-icon-error);
}

.jp-ExpandAllIcon {
  background-image: var(--jp-icon-expand-all);
}

.jp-ExtensionIcon {
  background-image: var(--jp-icon-extension);
}

.jp-FastForwardIcon {
  background-image: var(--jp-icon-fast-forward);
}

.jp-FileIcon {
  background-image: var(--jp-icon-file);
}

.jp-FileUploadIcon {
  background-image: var(--jp-icon-file-upload);
}

.jp-FilterDotIcon {
  background-image: var(--jp-icon-filter-dot);
}

.jp-FilterIcon {
  background-image: var(--jp-icon-filter);
}

.jp-FilterListIcon {
  background-image: var(--jp-icon-filter-list);
}

.jp-FolderFavoriteIcon {
  background-image: var(--jp-icon-folder-favorite);
}

.jp-FolderIcon {
  background-image: var(--jp-icon-folder);
}

.jp-HomeIcon {
  background-image: var(--jp-icon-home);
}

.jp-Html5Icon {
  background-image: var(--jp-icon-html5);
}

.jp-ImageIcon {
  background-image: var(--jp-icon-image);
}

.jp-InfoIcon {
  background-image: var(--jp-icon-info);
}

.jp-InspectorIcon {
  background-image: var(--jp-icon-inspector);
}

.jp-JsonIcon {
  background-image: var(--jp-icon-json);
}

.jp-JuliaIcon {
  background-image: var(--jp-icon-julia);
}

.jp-JupyterFaviconIcon {
  background-image: var(--jp-icon-jupyter-favicon);
}

.jp-JupyterIcon {
  background-image: var(--jp-icon-jupyter);
}

.jp-JupyterlabWordmarkIcon {
  background-image: var(--jp-icon-jupyterlab-wordmark);
}

.jp-KernelIcon {
  background-image: var(--jp-icon-kernel);
}

.jp-KeyboardIcon {
  background-image: var(--jp-icon-keyboard);
}

.jp-LaunchIcon {
  background-image: var(--jp-icon-launch);
}

.jp-LauncherIcon {
  background-image: var(--jp-icon-launcher);
}

.jp-LineFormIcon {
  background-image: var(--jp-icon-line-form);
}

.jp-LinkIcon {
  background-image: var(--jp-icon-link);
}

.jp-ListIcon {
  background-image: var(--jp-icon-list);
}

.jp-MarkdownIcon {
  background-image: var(--jp-icon-markdown);
}

.jp-MoveDownIcon {
  background-image: var(--jp-icon-move-down);
}

.jp-MoveUpIcon {
  background-image: var(--jp-icon-move-up);
}

.jp-NewFolderIcon {
  background-image: var(--jp-icon-new-folder);
}

.jp-NotTrustedIcon {
  background-image: var(--jp-icon-not-trusted);
}

.jp-NotebookIcon {
  background-image: var(--jp-icon-notebook);
}

.jp-NumberingIcon {
  background-image: var(--jp-icon-numbering);
}

.jp-OfflineBoltIcon {
  background-image: var(--jp-icon-offline-bolt);
}

.jp-PaletteIcon {
  background-image: var(--jp-icon-palette);
}

.jp-PasteIcon {
  background-image: var(--jp-icon-paste);
}

.jp-PdfIcon {
  background-image: var(--jp-icon-pdf);
}

.jp-PythonIcon {
  background-image: var(--jp-icon-python);
}

.jp-RKernelIcon {
  background-image: var(--jp-icon-r-kernel);
}

.jp-ReactIcon {
  background-image: var(--jp-icon-react);
}

.jp-RedoIcon {
  background-image: var(--jp-icon-redo);
}

.jp-RefreshIcon {
  background-image: var(--jp-icon-refresh);
}

.jp-RegexIcon {
  background-image: var(--jp-icon-regex);
}

.jp-RunIcon {
  background-image: var(--jp-icon-run);
}

.jp-RunningIcon {
  background-image: var(--jp-icon-running);
}

.jp-SaveIcon {
  background-image: var(--jp-icon-save);
}

.jp-SearchIcon {
  background-image: var(--jp-icon-search);
}

.jp-SettingsIcon {
  background-image: var(--jp-icon-settings);
}

.jp-ShareIcon {
  background-image: var(--jp-icon-share);
}

.jp-SpreadsheetIcon {
  background-image: var(--jp-icon-spreadsheet);
}

.jp-StopIcon {
  background-image: var(--jp-icon-stop);
}

.jp-TabIcon {
  background-image: var(--jp-icon-tab);
}

.jp-TableRowsIcon {
  background-image: var(--jp-icon-table-rows);
}

.jp-TagIcon {
  background-image: var(--jp-icon-tag);
}

.jp-TerminalIcon {
  background-image: var(--jp-icon-terminal);
}

.jp-TextEditorIcon {
  background-image: var(--jp-icon-text-editor);
}

.jp-TocIcon {
  background-image: var(--jp-icon-toc);
}

.jp-TreeViewIcon {
  background-image: var(--jp-icon-tree-view);
}

.jp-TrustedIcon {
  background-image: var(--jp-icon-trusted);
}

.jp-UndoIcon {
  background-image: var(--jp-icon-undo);
}

.jp-UserIcon {
  background-image: var(--jp-icon-user);
}

.jp-UsersIcon {
  background-image: var(--jp-icon-users);
}

.jp-VegaIcon {
  background-image: var(--jp-icon-vega);
}

.jp-WordIcon {
  background-image: var(--jp-icon-word);
}

.jp-YamlIcon {
  background-image: var(--jp-icon-yaml);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

.jp-Icon,
.jp-MaterialIcon {
  background-position: center;
  background-repeat: no-repeat;
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-cover {
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

/**
 * (DEPRECATED) Support for specific CSS icon sizes
 */

.jp-Icon-16 {
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-18 {
  background-size: 18px;
  min-width: 18px;
  min-height: 18px;
}

.jp-Icon-20 {
  background-size: 20px;
  min-width: 20px;
  min-height: 20px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.lm-TabBar .lm-TabBar-addButton {
  align-items: center;
  display: flex;
  padding: 4px;
  padding-bottom: 5px;
  margin-right: 1px;
  background-color: var(--jp-layout-color2);
}

.lm-TabBar .lm-TabBar-addButton:hover {
  background-color: var(--jp-layout-color1);
}

.lm-DockPanel-tabBar .lm-TabBar-tab {
  width: var(--jp-private-horizontal-tab-width);
}

.lm-DockPanel-tabBar .lm-TabBar-content {
  flex: unset;
}

.lm-DockPanel-tabBar[data-orientation='horizontal'] {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for icons as inline SVG HTMLElements
 */

/* recolor the primary elements of an icon */
.jp-icon0[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon1[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon2[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon3[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/* recolor the accent elements of an icon */
.jp-icon-accent0[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-accent1[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-accent2[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-accent3[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-accent4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-accent0[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-accent1[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-accent2[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-accent3[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-accent4[stroke] {
  stroke: var(--jp-layout-color4);
}

/* set the color of an icon to transparent */
.jp-icon-none[fill] {
  fill: none;
}

.jp-icon-none[stroke] {
  stroke: none;
}

/* brand icon colors. Same for light and dark */
.jp-icon-brand0[fill] {
  fill: var(--jp-brand-color0);
}

.jp-icon-brand1[fill] {
  fill: var(--jp-brand-color1);
}

.jp-icon-brand2[fill] {
  fill: var(--jp-brand-color2);
}

.jp-icon-brand3[fill] {
  fill: var(--jp-brand-color3);
}

.jp-icon-brand4[fill] {
  fill: var(--jp-brand-color4);
}

.jp-icon-brand0[stroke] {
  stroke: var(--jp-brand-color0);
}

.jp-icon-brand1[stroke] {
  stroke: var(--jp-brand-color1);
}

.jp-icon-brand2[stroke] {
  stroke: var(--jp-brand-color2);
}

.jp-icon-brand3[stroke] {
  stroke: var(--jp-brand-color3);
}

.jp-icon-brand4[stroke] {
  stroke: var(--jp-brand-color4);
}

/* warn icon colors. Same for light and dark */
.jp-icon-warn0[fill] {
  fill: var(--jp-warn-color0);
}

.jp-icon-warn1[fill] {
  fill: var(--jp-warn-color1);
}

.jp-icon-warn2[fill] {
  fill: var(--jp-warn-color2);
}

.jp-icon-warn3[fill] {
  fill: var(--jp-warn-color3);
}

.jp-icon-warn0[stroke] {
  stroke: var(--jp-warn-color0);
}

.jp-icon-warn1[stroke] {
  stroke: var(--jp-warn-color1);
}

.jp-icon-warn2[stroke] {
  stroke: var(--jp-warn-color2);
}

.jp-icon-warn3[stroke] {
  stroke: var(--jp-warn-color3);
}

/* icon colors that contrast well with each other and most backgrounds */
.jp-icon-contrast0[fill] {
  fill: var(--jp-icon-contrast-color0);
}

.jp-icon-contrast1[fill] {
  fill: var(--jp-icon-contrast-color1);
}

.jp-icon-contrast2[fill] {
  fill: var(--jp-icon-contrast-color2);
}

.jp-icon-contrast3[fill] {
  fill: var(--jp-icon-contrast-color3);
}

.jp-icon-contrast0[stroke] {
  stroke: var(--jp-icon-contrast-color0);
}

.jp-icon-contrast1[stroke] {
  stroke: var(--jp-icon-contrast-color1);
}

.jp-icon-contrast2[stroke] {
  stroke: var(--jp-icon-contrast-color2);
}

.jp-icon-contrast3[stroke] {
  stroke: var(--jp-icon-contrast-color3);
}

.jp-icon-dot[fill] {
  fill: var(--jp-warn-color0);
}

.jp-jupyter-icon-color[fill] {
  fill: var(--jp-jupyter-icon-color, var(--jp-warn-color0));
}

.jp-notebook-icon-color[fill] {
  fill: var(--jp-notebook-icon-color, var(--jp-warn-color0));
}

.jp-json-icon-color[fill] {
  fill: var(--jp-json-icon-color, var(--jp-warn-color1));
}

.jp-console-icon-color[fill] {
  fill: var(--jp-console-icon-color, white);
}

.jp-console-icon-background-color[fill] {
  fill: var(--jp-console-icon-background-color, var(--jp-brand-color1));
}

.jp-terminal-icon-color[fill] {
  fill: var(--jp-terminal-icon-color, var(--jp-layout-color2));
}

.jp-terminal-icon-background-color[fill] {
  fill: var(
    --jp-terminal-icon-background-color,
    var(--jp-inverse-layout-color2)
  );
}

.jp-text-editor-icon-color[fill] {
  fill: var(--jp-text-editor-icon-color, var(--jp-inverse-layout-color3));
}

.jp-inspector-icon-color[fill] {
  fill: var(--jp-inspector-icon-color, var(--jp-inverse-layout-color3));
}

/* CSS for icons in selected filebrowser listing items */
.jp-DirListing-item.jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}

.jp-DirListing-item.jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* stylelint-disable selector-max-class, selector-max-compound-selectors */

/**
* TODO: come up with non css-hack solution for showing the busy icon on top
*  of the close icon
* CSS for complex behavior of close icon of tabs in the main area tabbar
*/
.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon3[fill] {
  fill: none;
}

.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: var(--jp-inverse-layout-color3);
}

/* stylelint-enable selector-max-class, selector-max-compound-selectors */

/* CSS for icons in status bar */
#jp-main-statusbar .jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}

#jp-main-statusbar .jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* special handling for splash icon CSS. While the theme CSS reloads during
   splash, the splash icon can loose theming. To prevent that, we set a
   default for its color variable */
:root {
  --jp-warn-color0: var(--md-orange-700);
}

/* not sure what to do with this one, used in filebrowser listing */
.jp-DragIcon {
  margin-right: 4px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for alt colors for icons as inline SVG HTMLElements
 */

/* alt recolor the primary elements of an icon */
.jp-icon-alt .jp-icon0[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-alt .jp-icon1[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-alt .jp-icon2[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-alt .jp-icon3[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-alt .jp-icon4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-alt .jp-icon0[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-alt .jp-icon1[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-alt .jp-icon2[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-alt .jp-icon3[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-alt .jp-icon4[stroke] {
  stroke: var(--jp-layout-color4);
}

/* alt recolor the accent elements of an icon */
.jp-icon-alt .jp-icon-accent0[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon-alt .jp-icon-accent1[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon-alt .jp-icon-accent2[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon-alt .jp-icon-accent3[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon-alt .jp-icon-accent4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-alt .jp-icon-accent0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon-alt .jp-icon-accent1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon-alt .jp-icon-accent2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon-alt .jp-icon-accent3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon-alt .jp-icon-accent4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-icon-hoverShow:not(:hover) .jp-icon-hoverShow-content {
  display: none !important;
}

/**
 * Support for hover colors for icons as inline SVG HTMLElements
 */

/**
 * regular colors
 */

/* recolor the primary elements of an icon */
.jp-icon-hover :hover .jp-icon0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon-hover :hover .jp-icon1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon-hover :hover .jp-icon2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon-hover :hover .jp-icon3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon-hover :hover .jp-icon4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon-hover :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon-hover :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon-hover :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon-hover :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/* recolor the accent elements of an icon */
.jp-icon-hover :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-hover :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-hover :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-hover :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-hover :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-hover :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-hover :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-hover :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-hover :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* set the color of an icon to transparent */
.jp-icon-hover :hover .jp-icon-none-hover[fill] {
  fill: none;
}

.jp-icon-hover :hover .jp-icon-none-hover[stroke] {
  stroke: none;
}

/**
 * inverse colors
 */

/* inverse recolor the primary elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* inverse recolor the accent elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-IFrame {
  width: 100%;
  height: 100%;
}

.jp-IFrame > iframe {
  border: none;
}

/*
When drag events occur, `lm-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-IFrame {
  position: relative;
}

body.lm-mod-override-cursor .jp-IFrame::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-HoverBox {
  position: fixed;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-FormGroup-content fieldset {
  border: none;
  padding: 0;
  min-width: 0;
  width: 100%;
}

/* stylelint-disable selector-max-type */

.jp-FormGroup-content fieldset .jp-inputFieldWrapper input,
.jp-FormGroup-content fieldset .jp-inputFieldWrapper select,
.jp-FormGroup-content fieldset .jp-inputFieldWrapper textarea {
  font-size: var(--jp-content-font-size2);
  border-color: var(--jp-input-border-color);
  border-style: solid;
  border-radius: var(--jp-border-radius);
  border-width: 1px;
  padding: 6px 8px;
  background: none;
  color: var(--jp-ui-font-color0);
  height: inherit;
}

.jp-FormGroup-content fieldset input[type='checkbox'] {
  position: relative;
  top: 2px;
  margin-left: 0;
}

.jp-FormGroup-content button.jp-mod-styled {
  cursor: pointer;
}

.jp-FormGroup-content .checkbox label {
  cursor: pointer;
  font-size: var(--jp-content-font-size1);
}

.jp-FormGroup-content .jp-root > fieldset > legend {
  display: none;
}

.jp-FormGroup-content .jp-root > fieldset > p {
  display: none;
}

/** copy of `input.jp-mod-styled:focus` style */
.jp-FormGroup-content fieldset input:focus,
.jp-FormGroup-content fieldset select:focus {
  -moz-outline-radius: unset;
  outline: var(--jp-border-width) solid var(--md-blue-500);
  outline-offset: -1px;
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-FormGroup-content fieldset input:hover:not(:focus),
.jp-FormGroup-content fieldset select:hover:not(:focus) {
  background-color: var(--jp-border-color2);
}

/* stylelint-enable selector-max-type */

.jp-FormGroup-content .checkbox .field-description {
  /* Disable default description field for checkbox:
   because other widgets do not have description fields,
   we add descriptions to each widget on the field level.
  */
  display: none;
}

.jp-FormGroup-content #root__description {
  display: none;
}

.jp-FormGroup-content .jp-modifiedIndicator {
  width: 5px;
  background-color: var(--jp-brand-color2);
  margin-top: 0;
  margin-left: calc(var(--jp-private-settingeditor-modifier-indent) * -1);
  flex-shrink: 0;
}

.jp-FormGroup-content .jp-modifiedIndicator.jp-errorIndicator {
  background-color: var(--jp-error-color0);
  margin-right: 0.5em;
}

/* RJSF ARRAY style */

.jp-arrayFieldWrapper legend {
  font-size: var(--jp-content-font-size2);
  color: var(--jp-ui-font-color0);
  flex-basis: 100%;
  padding: 4px 0;
  font-weight: var(--jp-content-heading-font-weight);
  border-bottom: 1px solid var(--jp-border-color2);
}

.jp-arrayFieldWrapper .field-description {
  padding: 4px 0;
  white-space: pre-wrap;
}

.jp-arrayFieldWrapper .array-item {
  width: 100%;
  border: 1px solid var(--jp-border-color2);
  border-radius: 4px;
  margin: 4px;
}

.jp-ArrayOperations {
  display: flex;
  margin-left: 8px;
}

.jp-ArrayOperationsButton {
  margin: 2px;
}

.jp-ArrayOperationsButton .jp-icon3[fill] {
  fill: var(--jp-ui-font-color0);
}

button.jp-ArrayOperationsButton.jp-mod-styled:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}

/* RJSF form validation error */

.jp-FormGroup-content .validationErrors {
  color: var(--jp-error-color0);
}

/* Hide panel level error as duplicated the field level error */
.jp-FormGroup-content .panel.errors {
  display: none;
}

/* RJSF normal content (settings-editor) */

.jp-FormGroup-contentNormal {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}

.jp-FormGroup-contentNormal .jp-FormGroup-contentItem {
  margin-left: 7px;
  color: var(--jp-ui-font-color0);
}

.jp-FormGroup-contentNormal .jp-FormGroup-description {
  flex-basis: 100%;
  padding: 4px 7px;
}

.jp-FormGroup-contentNormal .jp-FormGroup-default {
  flex-basis: 100%;
  padding: 4px 7px;
}

.jp-FormGroup-contentNormal .jp-FormGroup-fieldLabel {
  font-size: var(--jp-content-font-size1);
  font-weight: normal;
  min-width: 120px;
}

.jp-FormGroup-contentNormal fieldset:not(:first-child) {
  margin-left: 7px;
}

.jp-FormGroup-contentNormal .field-array-of-string .array-item {
  /* Display `jp-ArrayOperations` buttons side-by-side with content except
    for small screens where flex-wrap will place them one below the other.
  */
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}

.jp-FormGroup-contentNormal .jp-objectFieldWrapper .form-group {
  padding: 2px 8px 2px var(--jp-private-settingeditor-modifier-indent);
  margin-top: 2px;
}

/* RJSF compact content (metadata-form) */

.jp-FormGroup-content.jp-FormGroup-contentCompact {
  width: 100%;
}

.jp-FormGroup-contentCompact .form-group {
  display: flex;
  padding: 0.5em 0.2em 0.5em 0;
}

.jp-FormGroup-contentCompact
  .jp-FormGroup-compactTitle
  .jp-FormGroup-description {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color2);
}

.jp-FormGroup-contentCompact .jp-FormGroup-fieldLabel {
  padding-bottom: 0.3em;
}

.jp-FormGroup-contentCompact .jp-inputFieldWrapper .form-control {
  width: 100%;
  box-sizing: border-box;
}

.jp-FormGroup-contentCompact .jp-arrayFieldWrapper .jp-FormGroup-compactTitle {
  padding-bottom: 7px;
}

.jp-FormGroup-contentCompact
  .jp-objectFieldWrapper
  .jp-objectFieldWrapper
  .form-group {
  padding: 2px 8px 2px var(--jp-private-settingeditor-modifier-indent);
  margin-top: 2px;
}

.jp-FormGroup-contentCompact ul.error-detail {
  margin-block-start: 0.5em;
  margin-block-end: 0.5em;
  padding-inline-start: 1em;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-SidePanel {
  display: flex;
  flex-direction: column;
  min-width: var(--jp-sidebar-min-width);
  overflow-y: auto;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  font-size: var(--jp-ui-font-size1);
}

.jp-SidePanel-header {
  flex: 0 0 auto;
  display: flex;
  border-bottom: var(--jp-border-width) solid var(--jp-border-color2);
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin: 0;
  padding: 2px;
  text-transform: uppercase;
}

.jp-SidePanel-toolbar {
  flex: 0 0 auto;
}

.jp-SidePanel-content {
  flex: 1 1 auto;
}

.jp-SidePanel-toolbar,
.jp-AccordionPanel-toolbar {
  height: var(--jp-private-toolbar-height);
}

.jp-SidePanel-toolbar.jp-Toolbar-micro {
  display: none;
}

.lm-AccordionPanel .jp-AccordionPanel-title {
  box-sizing: border-box;
  line-height: 25px;
  margin: 0;
  display: flex;
  align-items: center;
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  font-size: var(--jp-ui-font-size0);
}

.jp-AccordionPanel-title {
  cursor: pointer;
  user-select: none;
  -moz-user-select: none;
  -webkit-user-select: none;
  text-transform: uppercase;
}

.lm-AccordionPanel[data-orientation='horizontal'] > .jp-AccordionPanel-title {
  /* Title is rotated for horizontal accordion panel using CSS */
  display: block;
  transform-origin: top left;
  transform: rotate(-90deg) translate(-100%);
}

.jp-AccordionPanel-title .lm-AccordionPanel-titleLabel {
  user-select: none;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}

.jp-AccordionPanel-title .lm-AccordionPanel-titleCollapser {
  transform: rotate(-90deg);
  margin: auto 0;
  height: 16px;
}

.jp-AccordionPanel-title.lm-mod-expanded .lm-AccordionPanel-titleCollapser {
  transform: rotate(0deg);
}

.lm-AccordionPanel .jp-AccordionPanel-toolbar {
  background: none;
  box-shadow: none;
  border: none;
  margin-left: auto;
}

.lm-AccordionPanel .lm-SplitPanel-handle:hover {
  background: var(--jp-layout-color3);
}

.jp-text-truncated {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Spinner {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-layout-color0);
  outline: none;
}

.jp-SpinnerContent {
  font-size: 10px;
  margin: 50px auto;
  text-indent: -9999em;
  width: 3em;
  height: 3em;
  border-radius: 50%;
  background: var(--jp-brand-color3);
  background: linear-gradient(
    to right,
    #f37626 10%,
    rgba(255, 255, 255, 0) 42%
  );
  position: relative;
  animation: load3 1s infinite linear, fadeIn 1s;
}

.jp-SpinnerContent::before {
  width: 50%;
  height: 50%;
  background: #f37626;
  border-radius: 100% 0 0;
  position: absolute;
  top: 0;
  left: 0;
  content: '';
}

.jp-SpinnerContent::after {
  background: var(--jp-layout-color0);
  width: 75%;
  height: 75%;
  border-radius: 50%;
  content: '';
  margin: auto;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

@keyframes load3 {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

button.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: none;
  box-sizing: border-box;
  text-align: center;
  line-height: 32px;
  height: 32px;
  padding: 0 12px;
  letter-spacing: 0.8px;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input.jp-mod-styled {
  background: var(--jp-input-background);
  height: 28px;
  box-sizing: border-box;
  border: var(--jp-border-width) solid var(--jp-border-color1);
  padding-left: 7px;
  padding-right: 7px;
  font-size: var(--jp-ui-font-size2);
  color: var(--jp-ui-font-color0);
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input[type='checkbox'].jp-mod-styled {
  appearance: checkbox;
  -webkit-appearance: checkbox;
  -moz-appearance: checkbox;
  height: auto;
}

input.jp-mod-styled:focus {
  border: var(--jp-border-width) solid var(--md-blue-500);
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-select-wrapper {
  display: flex;
  position: relative;
  flex-direction: column;
  padding: 1px;
  background-color: var(--jp-layout-color1);
  box-sizing: border-box;
  margin-bottom: 12px;
}

.jp-select-wrapper:not(.multiple) {
  height: 28px;
}

.jp-select-wrapper.jp-mod-focused select.jp-mod-styled {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-input-active-background);
}

select.jp-mod-styled:hover {
  cursor: pointer;
  color: var(--jp-ui-font-color0);
  background-color: var(--jp-input-hover-background);
  box-shadow: inset 0 0 1px rgba(0, 0, 0, 0.5);
}

select.jp-mod-styled {
  flex: 1 1 auto;
  width: 100%;
  font-size: var(--jp-ui-font-size2);
  background: var(--jp-input-background);
  color: var(--jp-ui-font-color0);
  padding: 0 25px 0 8px;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

select.jp-mod-styled:not([multiple]) {
  height: 32px;
}

select.jp-mod-styled[multiple] {
  max-height: 200px;
  overflow-y: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-switch {
  display: flex;
  align-items: center;
  padding-left: 4px;
  padding-right: 4px;
  font-size: var(--jp-ui-font-size1);
  background-color: transparent;
  color: var(--jp-ui-font-color1);
  border: none;
  height: 20px;
}

.jp-switch:hover {
  background-color: var(--jp-layout-color2);
}

.jp-switch-label {
  margin-right: 5px;
  font-family: var(--jp-ui-font-family);
}

.jp-switch-track {
  cursor: pointer;
  background-color: var(--jp-switch-color, var(--jp-border-color1));
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 34px;
  height: 16px;
  width: 35px;
  position: relative;
}

.jp-switch-track::before {
  content: '';
  position: absolute;
  height: 10px;
  width: 10px;
  margin: 3px;
  left: 0;
  background-color: var(--jp-ui-inverse-font-color1);
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 50%;
}

.jp-switch[aria-checked='true'] .jp-switch-track {
  background-color: var(--jp-switch-true-position-color, var(--jp-warn-color0));
}

.jp-switch[aria-checked='true'] .jp-switch-track::before {
  /* track width (35) - margins (3 + 3) - thumb width (10) */
  left: 19px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

:root {
  --jp-private-toolbar-height: calc(
    28px + var(--jp-border-width)
  ); /* leave 28px for content */
}

.jp-Toolbar {
  color: var(--jp-ui-font-color1);
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  background: var(--jp-toolbar-background);
  min-height: var(--jp-toolbar-micro-height);
  padding: 2px;
  z-index: 8;
  overflow-x: hidden;
}

/* Toolbar items */

.jp-Toolbar > .jp-Toolbar-item.jp-Toolbar-spacer {
  flex-grow: 1;
  flex-shrink: 1;
}

.jp-Toolbar-item.jp-Toolbar-kernelStatus {
  display: inline-block;
  width: 32px;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 16px;
}

.jp-Toolbar > .jp-Toolbar-item {
  flex: 0 0 auto;
  display: flex;
  padding-left: 1px;
  padding-right: 1px;
  font-size: var(--jp-ui-font-size1);
  line-height: var(--jp-private-toolbar-height);
  height: 100%;
}

/* Toolbar buttons */

/* This is the div we use to wrap the react component into a Widget */
div.jp-ToolbarButton {
  color: transparent;
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0;
  margin: 0;
}

button.jp-ToolbarButtonComponent {
  background: var(--jp-layout-color1);
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0 6px;
  margin: 0;
  height: 24px;
  border-radius: var(--jp-border-radius);
  display: flex;
  align-items: center;
  text-align: center;
  font-size: 14px;
  min-width: unset;
  min-height: unset;
}

button.jp-ToolbarButtonComponent:disabled {
  opacity: 0.4;
}

button.jp-ToolbarButtonComponent > span {
  padding: 0;
  flex: 0 0 auto;
}

button.jp-ToolbarButtonComponent .jp-ToolbarButtonComponent-label {
  font-size: var(--jp-ui-font-size1);
  line-height: 100%;
  padding-left: 2px;
  color: var(--jp-ui-font-color1);
  font-family: var(--jp-ui-font-family);
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar.jp-Toolbar-micro {
  padding: 0;
  min-height: 0;
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar {
  border: none;
  box-shadow: none;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-WindowedPanel-outer {
  position: relative;
  overflow-y: auto;
}

.jp-WindowedPanel-inner {
  position: relative;
}

.jp-WindowedPanel-window {
  position: absolute;
  left: 0;
  right: 0;
  overflow: visible;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* Sibling imports */

body {
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
}

/* Disable native link decoration styles everywhere outside of dialog boxes */
a {
  text-decoration: unset;
  color: unset;
}

a:hover {
  text-decoration: unset;
  color: unset;
}

/* Accessibility for links inside dialog box text */
.jp-Dialog-content a {
  text-decoration: revert;
  color: var(--jp-content-link-color);
}

.jp-Dialog-content a:hover {
  text-decoration: revert;
}

/* Styles for ui-components */
.jp-Button {
  color: var(--jp-ui-font-color2);
  border-radius: var(--jp-border-radius);
  padding: 0 12px;
  font-size: var(--jp-ui-font-size1);

  /* Copy from blueprint 3 */
  display: inline-flex;
  flex-direction: row;
  border: none;
  cursor: pointer;
  align-items: center;
  justify-content: center;
  text-align: left;
  vertical-align: middle;
  min-height: 30px;
  min-width: 30px;
}

.jp-Button:disabled {
  cursor: not-allowed;
}

.jp-Button:empty {
  padding: 0 !important;
}

.jp-Button.jp-mod-small {
  min-height: 24px;
  min-width: 24px;
  font-size: 12px;
  padding: 0 7px;
}

/* Use our own theme for hover styles */
.jp-Button.jp-mod-minimal:hover {
  background-color: var(--jp-layout-color2);
}

.jp-Button.jp-mod-minimal {
  background: none;
}

.jp-InputGroup {
  display: block;
  position: relative;
}

.jp-InputGroup input {
  box-sizing: border-box;
  border: none;
  border-radius: 0;
  background-color: transparent;
  color: var(--jp-ui-font-color0);
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
  padding-bottom: 0;
  padding-top: 0;
  padding-left: 10px;
  padding-right: 28px;
  position: relative;
  width: 100%;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  font-size: 14px;
  font-weight: 400;
  height: 30px;
  line-height: 30px;
  outline: none;
  vertical-align: middle;
}

.jp-InputGroup input:focus {
  box-shadow: inset 0 0 0 var(--jp-border-width)
      var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-InputGroup input:disabled {
  cursor: not-allowed;
  resize: block;
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color2);
}

.jp-InputGroup input:disabled ~ span {
  cursor: not-allowed;
  color: var(--jp-ui-font-color2);
}

.jp-InputGroup input::placeholder,
input::placeholder {
  color: var(--jp-ui-font-color2);
}

.jp-InputGroupAction {
  position: absolute;
  bottom: 1px;
  right: 0;
  padding: 6px;
}

.jp-HTMLSelect.jp-DefaultStyle select {
  background-color: initial;
  border: none;
  border-radius: 0;
  box-shadow: none;
  color: var(--jp-ui-font-color0);
  display: block;
  font-size: var(--jp-ui-font-size1);
  font-family: var(--jp-ui-font-family);
  height: 24px;
  line-height: 14px;
  padding: 0 25px 0 10px;
  text-align: left;
  -moz-appearance: none;
  -webkit-appearance: none;
}

.jp-HTMLSelect.jp-DefaultStyle select:disabled {
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color2);
  cursor: not-allowed;
  resize: block;
}

.jp-HTMLSelect.jp-DefaultStyle select:disabled ~ span {
  cursor: not-allowed;
}

/* Use our own theme for hover and option styles */
/* stylelint-disable-next-line selector-max-type */
.jp-HTMLSelect.jp-DefaultStyle select:hover,
.jp-HTMLSelect.jp-DefaultStyle select > option {
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color0);
}

select {
  box-sizing: border-box;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-StatusBar-Widget {
  display: flex;
  align-items: center;
  background: var(--jp-layout-color2);
  min-height: var(--jp-statusbar-height);
  justify-content: space-between;
  padding: 0 10px;
}

.jp-StatusBar-Left {
  display: flex;
  align-items: center;
  flex-direction: row;
}

.jp-StatusBar-Middle {
  display: flex;
  align-items: center;
}

.jp-StatusBar-Right {
  display: flex;
  align-items: center;
  flex-direction: row-reverse;
}

.jp-StatusBar-Item {
  max-height: var(--jp-statusbar-height);
  margin: 0 2px;
  height: var(--jp-statusbar-height);
  white-space: nowrap;
  text-overflow: ellipsis;
  color: var(--jp-ui-font-color1);
  padding: 0 6px;
}

.jp-mod-highlighted:hover {
  background-color: var(--jp-layout-color3);
}

.jp-mod-clicked {
  background-color: var(--jp-brand-color1);
}

.jp-mod-clicked:hover {
  background-color: var(--jp-brand-color0);
}

.jp-mod-clicked .jp-StatusBar-TextItem {
  color: var(--jp-ui-inverse-font-color1);
}

.jp-StatusBar-HoverItem {
  box-shadow: '0px 4px 4px rgba(0, 0, 0, 0.25)';
}

.jp-StatusBar-TextItem {
  font-size: var(--jp-ui-font-size1);
  font-family: var(--jp-ui-font-family);
  line-height: 24px;
  color: var(--jp-ui-font-color1);
}

.jp-StatusBar-GroupItem {
  display: flex;
  align-items: center;
  flex-direction: row;
}

.jp-Statusbar-ProgressCircle svg {
  display: block;
  margin: 0 auto;
  width: 16px;
  height: 24px;
  align-self: normal;
}

.jp-Statusbar-ProgressCircle path {
  fill: var(--jp-inverse-layout-color3);
}

.jp-Statusbar-ProgressBar-progress-bar {
  height: 10px;
  width: 100px;
  border: solid 0.25px var(--jp-brand-color2);
  border-radius: 3px;
  overflow: hidden;
  align-self: center;
}

.jp-Statusbar-ProgressBar-progress-bar > div {
  background-color: var(--jp-brand-color2);
  background-image: linear-gradient(
    -45deg,
    rgba(255, 255, 255, 0.2) 25%,
    transparent 25%,
    transparent 50%,
    rgba(255, 255, 255, 0.2) 50%,
    rgba(255, 255, 255, 0.2) 75%,
    transparent 75%,
    transparent
  );
  background-size: 40px 40px;
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 14px;
  color: #fff;
  text-align: center;
  animation: jp-Statusbar-ExecutionTime-progress-bar 2s linear infinite;
}

.jp-Statusbar-ProgressBar-progress-bar p {
  color: var(--jp-ui-font-color1);
  font-family: var(--jp-ui-font-family);
  font-size: var(--jp-ui-font-size1);
  line-height: 10px;
  width: 100px;
}

@keyframes jp-Statusbar-ExecutionTime-progress-bar {
  0% {
    background-position: 0 0;
  }

  100% {
    background-position: 40px 40px;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-commandpalette-search-height: 28px;
}

/*-----------------------------------------------------------------------------
| Overall styles
|----------------------------------------------------------------------------*/

.lm-CommandPalette {
  padding-bottom: 0;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);

  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Modal variant
|----------------------------------------------------------------------------*/

.jp-ModalCommandPalette {
  position: absolute;
  z-index: 10000;
  top: 38px;
  left: 30%;
  margin: 0;
  padding: 4px;
  width: 40%;
  box-shadow: var(--jp-elevation-z4);
  border-radius: 4px;
  background: var(--jp-layout-color0);
}

.jp-ModalCommandPalette .lm-CommandPalette {
  max-height: 40vh;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-close-icon::after {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-header {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-item {
  margin-left: 4px;
  margin-right: 4px;
}

.jp-ModalCommandPalette
  .lm-CommandPalette
  .lm-CommandPalette-item.lm-mod-disabled {
  display: none;
}

/*-----------------------------------------------------------------------------
| Search
|----------------------------------------------------------------------------*/

.lm-CommandPalette-search {
  padding: 4px;
  background-color: var(--jp-layout-color1);
  z-index: 2;
}

.lm-CommandPalette-wrapper {
  overflow: overlay;
  padding: 0 9px;
  background-color: var(--jp-input-active-background);
  height: 30px;
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
}

.lm-CommandPalette.lm-mod-focused .lm-CommandPalette-wrapper {
  box-shadow: inset 0 0 0 1px var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-SearchIconGroup {
  color: white;
  background-color: var(--jp-brand-color1);
  position: absolute;
  top: 4px;
  right: 4px;
  padding: 5px 5px 1px;
}

.jp-SearchIconGroup svg {
  height: 20px;
  width: 20px;
}

.jp-SearchIconGroup .jp-icon3[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-input {
  background: transparent;
  width: calc(100% - 18px);
  float: left;
  border: none;
  outline: none;
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  line-height: var(--jp-private-commandpalette-search-height);
}

.lm-CommandPalette-input::-webkit-input-placeholder,
.lm-CommandPalette-input::-moz-placeholder,
.lm-CommandPalette-input:-ms-input-placeholder {
  color: var(--jp-ui-font-color2);
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Results
|----------------------------------------------------------------------------*/

.lm-CommandPalette-header:first-child {
  margin-top: 0;
}

.lm-CommandPalette-header {
  border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
  color: var(--jp-ui-font-color1);
  cursor: pointer;
  display: flex;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin-top: 8px;
  padding: 8px 0 8px 12px;
  text-transform: uppercase;
}

.lm-CommandPalette-header.lm-mod-active {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-header > mark {
  background-color: transparent;
  font-weight: bold;
  color: var(--jp-ui-font-color1);
}

.lm-CommandPalette-item {
  padding: 4px 12px 4px 4px;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  font-weight: 400;
  display: flex;
}

.lm-CommandPalette-item.lm-mod-disabled {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item.lm-mod-active {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item.lm-mod-active .lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-inverse-font-color0);
}

.lm-CommandPalette-item.lm-mod-active .jp-icon-selectable[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-item.lm-mod-active:hover:not(.lm-mod-disabled) {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item:hover:not(.lm-mod-active):not(.lm-mod-disabled) {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-itemContent {
  overflow: hidden;
}

.lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.lm-CommandPalette-item.lm-mod-disabled mark {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item .lm-CommandPalette-itemIcon {
  margin: 0 4px 0 0;
  position: relative;
  width: 16px;
  top: 2px;
  flex: 0 0 auto;
}

.lm-CommandPalette-item.lm-mod-disabled .lm-CommandPalette-itemIcon {
  opacity: 0.6;
}

.lm-CommandPalette-item .lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemCaption {
  display: none;
}

.lm-CommandPalette-content {
  background-color: var(--jp-layout-color1);
}

.lm-CommandPalette-content:empty::after {
  content: 'No results';
  margin: auto;
  margin-top: 20px;
  width: 100px;
  display: block;
  font-size: var(--jp-ui-font-size2);
  font-family: var(--jp-ui-font-family);
  font-weight: lighter;
}

.lm-CommandPalette-emptyMessage {
  text-align: center;
  margin-top: 24px;
  line-height: 1.32;
  padding: 0 8px;
  color: var(--jp-content-font-color3);
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Dialog {
  position: absolute;
  z-index: 10000;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  top: 0;
  left: 0;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-dialog-background);
}

.jp-Dialog-content {
  display: flex;
  flex-direction: column;
  margin-left: auto;
  margin-right: auto;
  background: var(--jp-layout-color1);
  padding: 24px 24px 12px;
  min-width: 300px;
  min-height: 150px;
  max-width: 1000px;
  max-height: 500px;
  box-sizing: border-box;
  box-shadow: var(--jp-elevation-z20);
  word-wrap: break-word;
  border-radius: var(--jp-border-radius);

  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color1);
  resize: both;
}

.jp-Dialog-content.jp-Dialog-content-small {
  max-width: 500px;
}

.jp-Dialog-button {
  overflow: visible;
}

button.jp-Dialog-button:focus {
  outline: 1px solid var(--jp-brand-color1);
  outline-offset: 4px;
  -moz-outline-radius: 0;
}

button.jp-Dialog-button:focus::-moz-focus-inner {
  border: 0;
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-accept:focus,
button.jp-Dialog-button.jp-mod-styled.jp-mod-warn:focus,
button.jp-Dialog-button.jp-mod-styled.jp-mod-reject:focus {
  outline-offset: 4px;
  -moz-outline-radius: 0;
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-accept:focus {
  outline: 1px solid var(--jp-accept-color-normal, var(--jp-brand-color1));
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-warn:focus {
  outline: 1px solid var(--jp-warn-color-normal, var(--jp-error-color1));
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-reject:focus {
  outline: 1px solid var(--jp-reject-color-normal, var(--md-grey-600));
}

button.jp-Dialog-close-button {
  padding: 0;
  height: 100%;
  min-width: unset;
  min-height: unset;
}

.jp-Dialog-header {
  display: flex;
  justify-content: space-between;
  flex: 0 0 auto;
  padding-bottom: 12px;
  font-size: var(--jp-ui-font-size3);
  font-weight: 400;
  color: var(--jp-ui-font-color1);
}

.jp-Dialog-body {
  display: flex;
  flex-direction: column;
  flex: 1 1 auto;
  font-size: var(--jp-ui-font-size1);
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  overflow: auto;
}

.jp-Dialog-footer {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
  flex: 0 0 auto;
  margin-left: -12px;
  margin-right: -12px;
  padding: 12px;
}

.jp-Dialog-checkbox {
  padding-right: 5px;
}

.jp-Dialog-checkbox > input:focus-visible {
  outline: 1px solid var(--jp-input-active-border-color);
  outline-offset: 1px;
}

.jp-Dialog-spacer {
  flex: 1 1 auto;
}

.jp-Dialog-title {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.jp-Dialog-body > .jp-select-wrapper {
  width: 100%;
}

.jp-Dialog-body > button {
  padding: 0 16px;
}

.jp-Dialog-body > label {
  line-height: 1.4;
  color: var(--jp-ui-font-color0);
}

.jp-Dialog-button.jp-mod-styled:not(:last-child) {
  margin-right: 12px;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-Input-Boolean-Dialog {
  flex-direction: row-reverse;
  align-items: end;
  width: 100%;
}

.jp-Input-Boolean-Dialog > label {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MainAreaWidget > :focus {
  outline: none;
}

.jp-MainAreaWidget .jp-MainAreaWidget-error {
  padding: 6px;
}

.jp-MainAreaWidget .jp-MainAreaWidget-error > pre {
  width: auto;
  padding: 10px;
  background: var(--jp-error-color3);
  border: var(--jp-border-width) solid var(--jp-error-color1);
  border-radius: var(--jp-border-radius);
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  white-space: pre-wrap;
  word-wrap: break-word;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/**
 * google-material-color v1.2.6
 * https://github.com/danlevan/google-material-color
 */
:root {
  --md-red-50: #ffebee;
  --md-red-100: #ffcdd2;
  --md-red-200: #ef9a9a;
  --md-red-300: #e57373;
  --md-red-400: #ef5350;
  --md-red-500: #f44336;
  --md-red-600: #e53935;
  --md-red-700: #d32f2f;
  --md-red-800: #c62828;
  --md-red-900: #b71c1c;
  --md-red-A100: #ff8a80;
  --md-red-A200: #ff5252;
  --md-red-A400: #ff1744;
  --md-red-A700: #d50000;
  --md-pink-50: #fce4ec;
  --md-pink-100: #f8bbd0;
  --md-pink-200: #f48fb1;
  --md-pink-300: #f06292;
  --md-pink-400: #ec407a;
  --md-pink-500: #e91e63;
  --md-pink-600: #d81b60;
  --md-pink-700: #c2185b;
  --md-pink-800: #ad1457;
  --md-pink-900: #880e4f;
  --md-pink-A100: #ff80ab;
  --md-pink-A200: #ff4081;
  --md-pink-A400: #f50057;
  --md-pink-A700: #c51162;
  --md-purple-50: #f3e5f5;
  --md-purple-100: #e1bee7;
  --md-purple-200: #ce93d8;
  --md-purple-300: #ba68c8;
  --md-purple-400: #ab47bc;
  --md-purple-500: #9c27b0;
  --md-purple-600: #8e24aa;
  --md-purple-700: #7b1fa2;
  --md-purple-800: #6a1b9a;
  --md-purple-900: #4a148c;
  --md-purple-A100: #ea80fc;
  --md-purple-A200: #e040fb;
  --md-purple-A400: #d500f9;
  --md-purple-A700: #a0f;
  --md-deep-purple-50: #ede7f6;
  --md-deep-purple-100: #d1c4e9;
  --md-deep-purple-200: #b39ddb;
  --md-deep-purple-300: #9575cd;
  --md-deep-purple-400: #7e57c2;
  --md-deep-purple-500: #673ab7;
  --md-deep-purple-600: #5e35b1;
  --md-deep-purple-700: #512da8;
  --md-deep-purple-800: #4527a0;
  --md-deep-purple-900: #311b92;
  --md-deep-purple-A100: #b388ff;
  --md-deep-purple-A200: #7c4dff;
  --md-deep-purple-A400: #651fff;
  --md-deep-purple-A700: #6200ea;
  --md-indigo-50: #e8eaf6;
  --md-indigo-100: #c5cae9;
  --md-indigo-200: #9fa8da;
  --md-indigo-300: #7986cb;
  --md-indigo-400: #5c6bc0;
  --md-indigo-500: #3f51b5;
  --md-indigo-600: #3949ab;
  --md-indigo-700: #303f9f;
  --md-indigo-800: #283593;
  --md-indigo-900: #1a237e;
  --md-indigo-A100: #8c9eff;
  --md-indigo-A200: #536dfe;
  --md-indigo-A400: #3d5afe;
  --md-indigo-A700: #304ffe;
  --md-blue-50: #e3f2fd;
  --md-blue-100: #bbdefb;
  --md-blue-200: #90caf9;
  --md-blue-300: #64b5f6;
  --md-blue-400: #42a5f5;
  --md-blue-500: #2196f3;
  --md-blue-600: #1e88e5;
  --md-blue-700: #1976d2;
  --md-blue-800: #1565c0;
  --md-blue-900: #0d47a1;
  --md-blue-A100: #82b1ff;
  --md-blue-A200: #448aff;
  --md-blue-A400: #2979ff;
  --md-blue-A700: #2962ff;
  --md-light-blue-50: #e1f5fe;
  --md-light-blue-100: #b3e5fc;
  --md-light-blue-200: #81d4fa;
  --md-light-blue-300: #4fc3f7;
  --md-light-blue-400: #29b6f6;
  --md-light-blue-500: #03a9f4;
  --md-light-blue-600: #039be5;
  --md-light-blue-700: #0288d1;
  --md-light-blue-800: #0277bd;
  --md-light-blue-900: #01579b;
  --md-light-blue-A100: #80d8ff;
  --md-light-blue-A200: #40c4ff;
  --md-light-blue-A400: #00b0ff;
  --md-light-blue-A700: #0091ea;
  --md-cyan-50: #e0f7fa;
  --md-cyan-100: #b2ebf2;
  --md-cyan-200: #80deea;
  --md-cyan-300: #4dd0e1;
  --md-cyan-400: #26c6da;
  --md-cyan-500: #00bcd4;
  --md-cyan-600: #00acc1;
  --md-cyan-700: #0097a7;
  --md-cyan-800: #00838f;
  --md-cyan-900: #006064;
  --md-cyan-A100: #84ffff;
  --md-cyan-A200: #18ffff;
  --md-cyan-A400: #00e5ff;
  --md-cyan-A700: #00b8d4;
  --md-teal-50: #e0f2f1;
  --md-teal-100: #b2dfdb;
  --md-teal-200: #80cbc4;
  --md-teal-300: #4db6ac;
  --md-teal-400: #26a69a;
  --md-teal-500: #009688;
  --md-teal-600: #00897b;
  --md-teal-700: #00796b;
  --md-teal-800: #00695c;
  --md-teal-900: #004d40;
  --md-teal-A100: #a7ffeb;
  --md-teal-A200: #64ffda;
  --md-teal-A400: #1de9b6;
  --md-teal-A700: #00bfa5;
  --md-green-50: #e8f5e9;
  --md-green-100: #c8e6c9;
  --md-green-200: #a5d6a7;
  --md-green-300: #81c784;
  --md-green-400: #66bb6a;
  --md-green-500: #4caf50;
  --md-green-600: #43a047;
  --md-green-700: #388e3c;
  --md-green-800: #2e7d32;
  --md-green-900: #1b5e20;
  --md-green-A100: #b9f6ca;
  --md-green-A200: #69f0ae;
  --md-green-A400: #00e676;
  --md-green-A700: #00c853;
  --md-light-green-50: #f1f8e9;
  --md-light-green-100: #dcedc8;
  --md-light-green-200: #c5e1a5;
  --md-light-green-300: #aed581;
  --md-light-green-400: #9ccc65;
  --md-light-green-500: #8bc34a;
  --md-light-green-600: #7cb342;
  --md-light-green-700: #689f38;
  --md-light-green-800: #558b2f;
  --md-light-green-900: #33691e;
  --md-light-green-A100: #ccff90;
  --md-light-green-A200: #b2ff59;
  --md-light-green-A400: #76ff03;
  --md-light-green-A700: #64dd17;
  --md-lime-50: #f9fbe7;
  --md-lime-100: #f0f4c3;
  --md-lime-200: #e6ee9c;
  --md-lime-300: #dce775;
  --md-lime-400: #d4e157;
  --md-lime-500: #cddc39;
  --md-lime-600: #c0ca33;
  --md-lime-700: #afb42b;
  --md-lime-800: #9e9d24;
  --md-lime-900: #827717;
  --md-lime-A100: #f4ff81;
  --md-lime-A200: #eeff41;
  --md-lime-A400: #c6ff00;
  --md-lime-A700: #aeea00;
  --md-yellow-50: #fffde7;
  --md-yellow-100: #fff9c4;
  --md-yellow-200: #fff59d;
  --md-yellow-300: #fff176;
  --md-yellow-400: #ffee58;
  --md-yellow-500: #ffeb3b;
  --md-yellow-600: #fdd835;
  --md-yellow-700: #fbc02d;
  --md-yellow-800: #f9a825;
  --md-yellow-900: #f57f17;
  --md-yellow-A100: #ffff8d;
  --md-yellow-A200: #ff0;
  --md-yellow-A400: #ffea00;
  --md-yellow-A700: #ffd600;
  --md-amber-50: #fff8e1;
  --md-amber-100: #ffecb3;
  --md-amber-200: #ffe082;
  --md-amber-300: #ffd54f;
  --md-amber-400: #ffca28;
  --md-amber-500: #ffc107;
  --md-amber-600: #ffb300;
  --md-amber-700: #ffa000;
  --md-amber-800: #ff8f00;
  --md-amber-900: #ff6f00;
  --md-amber-A100: #ffe57f;
  --md-amber-A200: #ffd740;
  --md-amber-A400: #ffc400;
  --md-amber-A700: #ffab00;
  --md-orange-50: #fff3e0;
  --md-orange-100: #ffe0b2;
  --md-orange-200: #ffcc80;
  --md-orange-300: #ffb74d;
  --md-orange-400: #ffa726;
  --md-orange-500: #ff9800;
  --md-orange-600: #fb8c00;
  --md-orange-700: #f57c00;
  --md-orange-800: #ef6c00;
  --md-orange-900: #e65100;
  --md-orange-A100: #ffd180;
  --md-orange-A200: #ffab40;
  --md-orange-A400: #ff9100;
  --md-orange-A700: #ff6d00;
  --md-deep-orange-50: #fbe9e7;
  --md-deep-orange-100: #ffccbc;
  --md-deep-orange-200: #ffab91;
  --md-deep-orange-300: #ff8a65;
  --md-deep-orange-400: #ff7043;
  --md-deep-orange-500: #ff5722;
  --md-deep-orange-600: #f4511e;
  --md-deep-orange-700: #e64a19;
  --md-deep-orange-800: #d84315;
  --md-deep-orange-900: #bf360c;
  --md-deep-orange-A100: #ff9e80;
  --md-deep-orange-A200: #ff6e40;
  --md-deep-orange-A400: #ff3d00;
  --md-deep-orange-A700: #dd2c00;
  --md-brown-50: #efebe9;
  --md-brown-100: #d7ccc8;
  --md-brown-200: #bcaaa4;
  --md-brown-300: #a1887f;
  --md-brown-400: #8d6e63;
  --md-brown-500: #795548;
  --md-brown-600: #6d4c41;
  --md-brown-700: #5d4037;
  --md-brown-800: #4e342e;
  --md-brown-900: #3e2723;
  --md-grey-50: #fafafa;
  --md-grey-100: #f5f5f5;
  --md-grey-200: #eee;
  --md-grey-300: #e0e0e0;
  --md-grey-400: #bdbdbd;
  --md-grey-500: #9e9e9e;
  --md-grey-600: #757575;
  --md-grey-700: #616161;
  --md-grey-800: #424242;
  --md-grey-900: #212121;
  --md-blue-grey-50: #eceff1;
  --md-blue-grey-100: #cfd8dc;
  --md-blue-grey-200: #b0bec5;
  --md-blue-grey-300: #90a4ae;
  --md-blue-grey-400: #78909c;
  --md-blue-grey-500: #607d8b;
  --md-blue-grey-600: #546e7a;
  --md-blue-grey-700: #455a64;
  --md-blue-grey-800: #37474f;
  --md-blue-grey-900: #263238;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| RenderedText
|----------------------------------------------------------------------------*/

:root {
  /* This is the padding value to fill the gaps between lines containing spans with background color. */
  --jp-private-code-span-padding: calc(
    (var(--jp-code-line-height) - 1) * var(--jp-code-font-size) / 2
  );
}

.jp-RenderedText {
  text-align: left;
  padding-left: var(--jp-code-padding);
  line-height: var(--jp-code-line-height);
  font-family: var(--jp-code-font-family);
}

.jp-RenderedText pre,
.jp-RenderedJavaScript pre,
.jp-RenderedHTMLCommon pre {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-code-font-size);
  border: none;
  margin: 0;
  padding: 0;
}

.jp-RenderedText pre a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

.jp-RenderedText pre a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}

.jp-RenderedText pre a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* console foregrounds and backgrounds */
.jp-RenderedText pre .ansi-black-fg {
  color: #3e424d;
}

.jp-RenderedText pre .ansi-red-fg {
  color: #e75c58;
}

.jp-RenderedText pre .ansi-green-fg {
  color: #00a250;
}

.jp-RenderedText pre .ansi-yellow-fg {
  color: #ddb62b;
}

.jp-RenderedText pre .ansi-blue-fg {
  color: #208ffb;
}

.jp-RenderedText pre .ansi-magenta-fg {
  color: #d160c4;
}

.jp-RenderedText pre .ansi-cyan-fg {
  color: #60c6c8;
}

.jp-RenderedText pre .ansi-white-fg {
  color: #c5c1b4;
}

.jp-RenderedText pre .ansi-black-bg {
  background-color: #3e424d;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-red-bg {
  background-color: #e75c58;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-green-bg {
  background-color: #00a250;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-yellow-bg {
  background-color: #ddb62b;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-blue-bg {
  background-color: #208ffb;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-magenta-bg {
  background-color: #d160c4;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-cyan-bg {
  background-color: #60c6c8;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-white-bg {
  background-color: #c5c1b4;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-black-intense-fg {
  color: #282c36;
}

.jp-RenderedText pre .ansi-red-intense-fg {
  color: #b22b31;
}

.jp-RenderedText pre .ansi-green-intense-fg {
  color: #007427;
}

.jp-RenderedText pre .ansi-yellow-intense-fg {
  color: #b27d12;
}

.jp-RenderedText pre .ansi-blue-intense-fg {
  color: #0065ca;
}

.jp-RenderedText pre .ansi-magenta-intense-fg {
  color: #a03196;
}

.jp-RenderedText pre .ansi-cyan-intense-fg {
  color: #258f8f;
}

.jp-RenderedText pre .ansi-white-intense-fg {
  color: #a1a6b2;
}

.jp-RenderedText pre .ansi-black-intense-bg {
  background-color: #282c36;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-red-intense-bg {
  background-color: #b22b31;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-green-intense-bg {
  background-color: #007427;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-yellow-intense-bg {
  background-color: #b27d12;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-blue-intense-bg {
  background-color: #0065ca;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-magenta-intense-bg {
  background-color: #a03196;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-cyan-intense-bg {
  background-color: #258f8f;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-white-intense-bg {
  background-color: #a1a6b2;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-default-inverse-fg {
  color: var(--jp-ui-inverse-font-color0);
}

.jp-RenderedText pre .ansi-default-inverse-bg {
  background-color: var(--jp-inverse-layout-color0);
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-bold {
  font-weight: bold;
}

.jp-RenderedText pre .ansi-underline {
  text-decoration: underline;
}

.jp-RenderedText[data-mime-type='application/vnd.jupyter.stderr'] {
  background: var(--jp-rendermime-error-background);
  padding-top: var(--jp-code-padding);
}

/*-----------------------------------------------------------------------------
| RenderedLatex
|----------------------------------------------------------------------------*/

.jp-RenderedLatex {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);
}

/* Left-justify outputs.*/
.jp-OutputArea-output.jp-RenderedLatex {
  padding: var(--jp-code-padding);
  text-align: left;
}

/*-----------------------------------------------------------------------------
| RenderedHTML
|----------------------------------------------------------------------------*/

.jp-RenderedHTMLCommon {
  color: var(--jp-content-font-color1);
  font-family: var(--jp-content-font-family);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);

  /* Give a bit more R padding on Markdown text to keep line lengths reasonable */
  padding-right: 20px;
}

.jp-RenderedHTMLCommon em {
  font-style: italic;
}

.jp-RenderedHTMLCommon strong {
  font-weight: bold;
}

.jp-RenderedHTMLCommon u {
  text-decoration: underline;
}

.jp-RenderedHTMLCommon a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* Headings */

.jp-RenderedHTMLCommon h1,
.jp-RenderedHTMLCommon h2,
.jp-RenderedHTMLCommon h3,
.jp-RenderedHTMLCommon h4,
.jp-RenderedHTMLCommon h5,
.jp-RenderedHTMLCommon h6 {
  line-height: var(--jp-content-heading-line-height);
  font-weight: var(--jp-content-heading-font-weight);
  font-style: normal;
  margin: var(--jp-content-heading-margin-top) 0
    var(--jp-content-heading-margin-bottom) 0;
}

.jp-RenderedHTMLCommon h1:first-child,
.jp-RenderedHTMLCommon h2:first-child,
.jp-RenderedHTMLCommon h3:first-child,
.jp-RenderedHTMLCommon h4:first-child,
.jp-RenderedHTMLCommon h5:first-child,
.jp-RenderedHTMLCommon h6:first-child {
  margin-top: calc(0.5 * var(--jp-content-heading-margin-top));
}

.jp-RenderedHTMLCommon h1:last-child,
.jp-RenderedHTMLCommon h2:last-child,
.jp-RenderedHTMLCommon h3:last-child,
.jp-RenderedHTMLCommon h4:last-child,
.jp-RenderedHTMLCommon h5:last-child,
.jp-RenderedHTMLCommon h6:last-child {
  margin-bottom: calc(0.5 * var(--jp-content-heading-margin-bottom));
}

.jp-RenderedHTMLCommon h1 {
  font-size: var(--jp-content-font-size5);
}

.jp-RenderedHTMLCommon h2 {
  font-size: var(--jp-content-font-size4);
}

.jp-RenderedHTMLCommon h3 {
  font-size: var(--jp-content-font-size3);
}

.jp-RenderedHTMLCommon h4 {
  font-size: var(--jp-content-font-size2);
}

.jp-RenderedHTMLCommon h5 {
  font-size: var(--jp-content-font-size1);
}

.jp-RenderedHTMLCommon h6 {
  font-size: var(--jp-content-font-size0);
}

/* Lists */

/* stylelint-disable selector-max-type, selector-max-compound-selectors */

.jp-RenderedHTMLCommon ul:not(.list-inline),
.jp-RenderedHTMLCommon ol:not(.list-inline) {
  padding-left: 2em;
}

.jp-RenderedHTMLCommon ul {
  list-style: disc;
}

.jp-RenderedHTMLCommon ul ul {
  list-style: square;
}

.jp-RenderedHTMLCommon ul ul ul {
  list-style: circle;
}

.jp-RenderedHTMLCommon ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol ol {
  list-style: upper-alpha;
}

.jp-RenderedHTMLCommon ol ol ol {
  list-style: lower-alpha;
}

.jp-RenderedHTMLCommon ol ol ol ol {
  list-style: lower-roman;
}

.jp-RenderedHTMLCommon ol ol ol ol ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol,
.jp-RenderedHTMLCommon ul {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon ul ul,
.jp-RenderedHTMLCommon ul ol,
.jp-RenderedHTMLCommon ol ul,
.jp-RenderedHTMLCommon ol ol {
  margin-bottom: 0;
}

/* stylelint-enable selector-max-type, selector-max-compound-selectors */

.jp-RenderedHTMLCommon hr {
  color: var(--jp-border-color2);
  background-color: var(--jp-border-color1);
  margin-top: 1em;
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon > pre {
  margin: 1.5em 2em;
}

.jp-RenderedHTMLCommon pre,
.jp-RenderedHTMLCommon code {
  border: 0;
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  line-height: var(--jp-code-line-height);
  padding: 0;
  white-space: pre-wrap;
}

.jp-RenderedHTMLCommon :not(pre) > code {
  background-color: var(--jp-layout-color2);
  padding: 1px 5px;
}

/* Tables */

.jp-RenderedHTMLCommon table {
  border-collapse: collapse;
  border-spacing: 0;
  border: none;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  table-layout: fixed;
  margin-left: auto;
  margin-bottom: 1em;
  margin-right: auto;
}

.jp-RenderedHTMLCommon thead {
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  vertical-align: bottom;
}

.jp-RenderedHTMLCommon td,
.jp-RenderedHTMLCommon th,
.jp-RenderedHTMLCommon tr {
  vertical-align: middle;
  padding: 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}

.jp-RenderedMarkdown.jp-RenderedHTMLCommon td,
.jp-RenderedMarkdown.jp-RenderedHTMLCommon th {
  max-width: none;
}

:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon td,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon th,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon tr {
  text-align: right;
}

.jp-RenderedHTMLCommon th {
  font-weight: bold;
}

.jp-RenderedHTMLCommon tbody tr:nth-child(odd) {
  background: var(--jp-layout-color0);
}

.jp-RenderedHTMLCommon tbody tr:nth-child(even) {
  background: var(--jp-rendermime-table-row-background);
}

.jp-RenderedHTMLCommon tbody tr:hover {
  background: var(--jp-rendermime-table-row-hover-background);
}

.jp-RenderedHTMLCommon p {
  text-align: left;
  margin: 0;
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon img {
  -moz-force-broken-image-icon: 1;
}

/* Restrict to direct children as other images could be nested in other content. */
.jp-RenderedHTMLCommon > img {
  display: block;
  margin-left: 0;
  margin-right: 0;
  margin-bottom: 1em;
}

/* Change color behind transparent images if they need it... */
[data-jp-theme-light='false'] .jp-RenderedImage img.jp-needs-light-background {
  background-color: var(--jp-inverse-layout-color1);
}

[data-jp-theme-light='true'] .jp-RenderedImage img.jp-needs-dark-background {
  background-color: var(--jp-inverse-layout-color1);
}

.jp-RenderedHTMLCommon img,
.jp-RenderedImage img,
.jp-RenderedHTMLCommon svg,
.jp-RenderedSVG svg {
  max-width: 100%;
  height: auto;
}

.jp-RenderedHTMLCommon img.jp-mod-unconfined,
.jp-RenderedImage img.jp-mod-unconfined,
.jp-RenderedHTMLCommon svg.jp-mod-unconfined,
.jp-RenderedSVG svg.jp-mod-unconfined {
  max-width: none;
}

.jp-RenderedHTMLCommon .alert {
  padding: var(--jp-notebook-padding);
  border: var(--jp-border-width) solid transparent;
  border-radius: var(--jp-border-radius);
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon .alert-info {
  color: var(--jp-info-color0);
  background-color: var(--jp-info-color3);
  border-color: var(--jp-info-color2);
}

.jp-RenderedHTMLCommon .alert-info hr {
  border-color: var(--jp-info-color3);
}

.jp-RenderedHTMLCommon .alert-info > p:last-child,
.jp-RenderedHTMLCommon .alert-info > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-warning {
  color: var(--jp-warn-color0);
  background-color: var(--jp-warn-color3);
  border-color: var(--jp-warn-color2);
}

.jp-RenderedHTMLCommon .alert-warning hr {
  border-color: var(--jp-warn-color3);
}

.jp-RenderedHTMLCommon .alert-warning > p:last-child,
.jp-RenderedHTMLCommon .alert-warning > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-success {
  color: var(--jp-success-color0);
  background-color: var(--jp-success-color3);
  border-color: var(--jp-success-color2);
}

.jp-RenderedHTMLCommon .alert-success hr {
  border-color: var(--jp-success-color3);
}

.jp-RenderedHTMLCommon .alert-success > p:last-child,
.jp-RenderedHTMLCommon .alert-success > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-danger {
  color: var(--jp-error-color0);
  background-color: var(--jp-error-color3);
  border-color: var(--jp-error-color2);
}

.jp-RenderedHTMLCommon .alert-danger hr {
  border-color: var(--jp-error-color3);
}

.jp-RenderedHTMLCommon .alert-danger > p:last-child,
.jp-RenderedHTMLCommon .alert-danger > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon blockquote {
  margin: 1em 2em;
  padding: 0 1em;
  border-left: 5px solid var(--jp-border-color2);
}

a.jp-InternalAnchorLink {
  visibility: hidden;
  margin-left: 8px;
  color: var(--md-blue-800);
}

h1:hover .jp-InternalAnchorLink,
h2:hover .jp-InternalAnchorLink,
h3:hover .jp-InternalAnchorLink,
h4:hover .jp-InternalAnchorLink,
h5:hover .jp-InternalAnchorLink,
h6:hover .jp-InternalAnchorLink {
  visibility: visible;
}

.jp-RenderedHTMLCommon kbd {
  background-color: var(--jp-rendermime-table-row-background);
  border: 1px solid var(--jp-border-color0);
  border-bottom-color: var(--jp-border-color2);
  border-radius: 3px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
  display: inline-block;
  font-size: var(--jp-ui-font-size0);
  line-height: 1em;
  padding: 0.2em 0.5em;
}

/* Most direct children of .jp-RenderedHTMLCommon have a margin-bottom of 1.0.
 * At the bottom of cells this is a bit too much as there is also spacing
 * between cells. Going all the way to 0 gets too tight between markdown and
 * code cells.
 */
.jp-RenderedHTMLCommon > *:last-child {
  margin-bottom: 0.5em;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-cursor-backdrop {
  position: fixed;
  width: 200px;
  height: 200px;
  margin-top: -100px;
  margin-left: -100px;
  will-change: transform;
  z-index: 100;
}

.lm-mod-drag-image {
  will-change: transform;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-lineFormSearch {
  padding: 4px 12px;
  background-color: var(--jp-layout-color2);
  box-shadow: var(--jp-toolbar-box-shadow);
  z-index: 2;
  font-size: var(--jp-ui-font-size1);
}

.jp-lineFormCaption {
  font-size: var(--jp-ui-font-size0);
  line-height: var(--jp-ui-font-size1);
  margin-top: 4px;
  color: var(--jp-ui-font-color0);
}

.jp-baseLineForm {
  border: none;
  border-radius: 0;
  position: absolute;
  background-size: 16px;
  background-repeat: no-repeat;
  background-position: center;
  outline: none;
}

.jp-lineFormButtonContainer {
  top: 4px;
  right: 8px;
  height: 24px;
  padding: 0 12px;
  width: 12px;
}

.jp-lineFormButtonIcon {
  top: 0;
  right: 0;
  background-color: var(--jp-brand-color1);
  height: 100%;
  width: 100%;
  box-sizing: border-box;
  padding: 4px 6px;
}

.jp-lineFormButton {
  top: 0;
  right: 0;
  background-color: transparent;
  height: 100%;
  width: 100%;
  box-sizing: border-box;
}

.jp-lineFormWrapper {
  overflow: hidden;
  padding: 0 8px;
  border: 1px solid var(--jp-border-color0);
  background-color: var(--jp-input-active-background);
  height: 22px;
}

.jp-lineFormWrapperFocusWithin {
  border: var(--jp-border-width) solid var(--md-blue-500);
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-lineFormInput {
  background: transparent;
  width: 200px;
  height: 100%;
  border: none;
  outline: none;
  color: var(--jp-ui-font-color0);
  line-height: 28px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-JSONEditor {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.jp-JSONEditor-host {
  flex: 1 1 auto;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0;
  background: var(--jp-layout-color0);
  min-height: 50px;
  padding: 1px;
}

.jp-JSONEditor.jp-mod-error .jp-JSONEditor-host {
  border-color: red;
  outline-color: red;
}

.jp-JSONEditor-header {
  display: flex;
  flex: 1 0 auto;
  padding: 0 0 0 12px;
}

.jp-JSONEditor-header label {
  flex: 0 0 auto;
}

.jp-JSONEditor-commitButton {
  height: 16px;
  width: 16px;
  background-size: 18px;
  background-repeat: no-repeat;
  background-position: center;
}

.jp-JSONEditor-host.jp-mod-focused {
  background-color: var(--jp-input-active-background);
  border: 1px solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

.jp-Editor.jp-mod-dropTarget {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
.jp-DocumentSearch-input {
  border: none;
  outline: none;
  color: var(--jp-ui-font-color0);
  font-size: var(--jp-ui-font-size1);
  background-color: var(--jp-layout-color0);
  font-family: var(--jp-ui-font-family);
  padding: 2px 1px;
  resize: none;
}

.jp-DocumentSearch-overlay {
  position: absolute;
  background-color: var(--jp-toolbar-background);
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  border-left: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  top: 0;
  right: 0;
  z-index: 7;
  min-width: 405px;
  padding: 2px;
  font-size: var(--jp-ui-font-size1);

  --jp-private-document-search-button-height: 20px;
}

.jp-DocumentSearch-overlay button {
  background-color: var(--jp-toolbar-background);
  outline: 0;
}

.jp-DocumentSearch-overlay button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-overlay button:active {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-overlay-row {
  display: flex;
  align-items: center;
  margin-bottom: 2px;
}

.jp-DocumentSearch-button-content {
  display: inline-block;
  cursor: pointer;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-button-content svg {
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-input-wrapper {
  border: var(--jp-border-width) solid var(--jp-border-color0);
  display: flex;
  background-color: var(--jp-layout-color0);
  margin: 2px;
}

.jp-DocumentSearch-input-wrapper:focus-within {
  border-color: var(--jp-cell-editor-active-border-color);
}

.jp-DocumentSearch-toggle-wrapper,
.jp-DocumentSearch-button-wrapper {
  all: initial;
  overflow: hidden;
  display: inline-block;
  border: none;
  box-sizing: border-box;
}

.jp-DocumentSearch-toggle-wrapper {
  width: 14px;
  height: 14px;
}

.jp-DocumentSearch-button-wrapper {
  width: var(--jp-private-document-search-button-height);
  height: var(--jp-private-document-search-button-height);
}

.jp-DocumentSearch-toggle-wrapper:focus,
.jp-DocumentSearch-button-wrapper:focus {
  outline: var(--jp-border-width) solid
    var(--jp-cell-editor-active-border-color);
  outline-offset: -1px;
}

.jp-DocumentSearch-toggle-wrapper,
.jp-DocumentSearch-button-wrapper,
.jp-DocumentSearch-button-content:focus {
  outline: none;
}

.jp-DocumentSearch-toggle-placeholder {
  width: 5px;
}

.jp-DocumentSearch-input-button::before {
  display: block;
  padding-top: 100%;
}

.jp-DocumentSearch-input-button-off {
  opacity: var(--jp-search-toggle-off-opacity);
}

.jp-DocumentSearch-input-button-off:hover {
  opacity: var(--jp-search-toggle-hover-opacity);
}

.jp-DocumentSearch-input-button-on {
  opacity: var(--jp-search-toggle-on-opacity);
}

.jp-DocumentSearch-index-counter {
  padding-left: 10px;
  padding-right: 10px;
  user-select: none;
  min-width: 35px;
  display: inline-block;
}

.jp-DocumentSearch-up-down-wrapper {
  display: inline-block;
  padding-right: 2px;
  margin-left: auto;
  white-space: nowrap;
}

.jp-DocumentSearch-spacer {
  margin-left: auto;
}

.jp-DocumentSearch-up-down-wrapper button {
  outline: 0;
  border: none;
  width: var(--jp-private-document-search-button-height);
  height: var(--jp-private-document-search-button-height);
  vertical-align: middle;
  margin: 1px 5px 2px;
}

.jp-DocumentSearch-up-down-button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-up-down-button:active {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-filter-button {
  border-radius: var(--jp-border-radius);
}

.jp-DocumentSearch-filter-button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-filter-button-enabled {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-filter-button-enabled:hover {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-search-options {
  padding: 0 8px;
  margin-left: 3px;
  width: 100%;
  display: grid;
  justify-content: start;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  justify-items: stretch;
}

.jp-DocumentSearch-search-filter-disabled {
  color: var(--jp-ui-font-color2);
}

.jp-DocumentSearch-search-filter {
  display: flex;
  align-items: center;
  user-select: none;
}

.jp-DocumentSearch-regex-error {
  color: var(--jp-error-color0);
}

.jp-DocumentSearch-replace-button-wrapper {
  overflow: hidden;
  display: inline-block;
  box-sizing: border-box;
  border: var(--jp-border-width) solid var(--jp-border-color0);
  margin: auto 2px;
  padding: 1px 4px;
  height: calc(var(--jp-private-document-search-button-height) + 2px);
}

.jp-DocumentSearch-replace-button-wrapper:focus {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
}

.jp-DocumentSearch-replace-button {
  display: inline-block;
  text-align: center;
  cursor: pointer;
  box-sizing: border-box;
  color: var(--jp-ui-font-color1);

  /* height - 2 * (padding of wrapper) */
  line-height: calc(var(--jp-private-document-search-button-height) - 2px);
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-replace-button:focus {
  outline: none;
}

.jp-DocumentSearch-replace-wrapper-class {
  margin-left: 14px;
  display: flex;
}

.jp-DocumentSearch-replace-toggle {
  border: none;
  background-color: var(--jp-toolbar-background);
  border-radius: var(--jp-border-radius);
}

.jp-DocumentSearch-replace-toggle:hover {
  background-color: var(--jp-layout-color2);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.cm-editor {
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  border: 0;
  border-radius: 0;
  height: auto;

  /* Changed to auto to autogrow */
}

.cm-editor pre {
  padding: 0 var(--jp-code-padding);
}

.jp-CodeMirrorEditor[data-type='inline'] .cm-dialog {
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
}

.jp-CodeMirrorEditor {
  cursor: text;
}

/* When zoomed out 67% and 33% on a screen of 1440 width x 900 height */
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .jp-CodeMirrorEditor[data-type='inline'] .cm-cursor {
    border-left: var(--jp-code-cursor-width1) solid
      var(--jp-editor-cursor-color);
  }
}

/* When zoomed out less than 33% */
@media screen and (min-width: 4320px) {
  .jp-CodeMirrorEditor[data-type='inline'] .cm-cursor {
    border-left: var(--jp-code-cursor-width2) solid
      var(--jp-editor-cursor-color);
  }
}

.cm-editor.jp-mod-readOnly .cm-cursor {
  display: none;
}

.jp-CollaboratorCursor {
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: none;
  border-bottom: 3px solid;
  background-clip: content-box;
  margin-left: -5px;
  margin-right: -5px;
}

.cm-searching,
.cm-searching span {
  /* `.cm-searching span`: we need to override syntax highlighting */
  background-color: var(--jp-search-unselected-match-background-color);
  color: var(--jp-search-unselected-match-color);
}

.cm-searching::selection,
.cm-searching span::selection {
  background-color: var(--jp-search-unselected-match-background-color);
  color: var(--jp-search-unselected-match-color);
}

.jp-current-match > .cm-searching,
.jp-current-match > .cm-searching span,
.cm-searching > .jp-current-match,
.cm-searching > .jp-current-match span {
  background-color: var(--jp-search-selected-match-background-color);
  color: var(--jp-search-selected-match-color);
}

.jp-current-match > .cm-searching::selection,
.cm-searching > .jp-current-match::selection,
.jp-current-match > .cm-searching span::selection {
  background-color: var(--jp-search-selected-match-background-color);
  color: var(--jp-search-selected-match-color);
}

.cm-trailingspace {
  background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAFCAYAAAB4ka1VAAAAsElEQVQIHQGlAFr/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7+r3zKmT0/+pk9P/7+r3zAAAAAAAAAAABAAAAAAAAAAA6OPzM+/q9wAAAAAA6OPzMwAAAAAAAAAAAgAAAAAAAAAAGR8NiRQaCgAZIA0AGR8NiQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQyoYJ/SY80UAAAAASUVORK5CYII=);
  background-position: center left;
  background-repeat: repeat-x;
}

.jp-CollaboratorCursor-hover {
  position: absolute;
  z-index: 1;
  transform: translateX(-50%);
  color: white;
  border-radius: 3px;
  padding-left: 4px;
  padding-right: 4px;
  padding-top: 1px;
  padding-bottom: 1px;
  text-align: center;
  font-size: var(--jp-ui-font-size1);
  white-space: nowrap;
}

.jp-CodeMirror-ruler {
  border-left: 1px dashed var(--jp-border-color2);
}

/* Styles for shared cursors (remote cursor locations and selected ranges) */
.jp-CodeMirrorEditor .cm-ySelectionCaret {
  position: relative;
  border-left: 1px solid black;
  margin-left: -1px;
  margin-right: -1px;
  box-sizing: border-box;
}

.jp-CodeMirrorEditor .cm-ySelectionCaret > .cm-ySelectionInfo {
  white-space: nowrap;
  position: absolute;
  top: -1.15em;
  padding-bottom: 0.05em;
  left: -1px;
  font-size: 0.95em;
  font-family: var(--jp-ui-font-family);
  font-weight: bold;
  line-height: normal;
  user-select: none;
  color: white;
  padding-left: 2px;
  padding-right: 2px;
  z-index: 101;
  transition: opacity 0.3s ease-in-out;
}

.jp-CodeMirrorEditor .cm-ySelectionInfo {
  transition-delay: 0.7s;
  opacity: 0;
}

.jp-CodeMirrorEditor .cm-ySelectionCaret:hover > .cm-ySelectionInfo {
  opacity: 1;
  transition-delay: 0s;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MimeDocument {
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-filebrowser-button-height: 28px;
  --jp-private-filebrowser-button-width: 48px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-FileBrowser .jp-SidePanel-content {
  display: flex;
  flex-direction: column;
}

.jp-FileBrowser-toolbar.jp-Toolbar {
  flex-wrap: wrap;
  row-gap: 12px;
  border-bottom: none;
  height: auto;
  margin: 8px 12px 0;
  box-shadow: none;
  padding: 0;
  justify-content: flex-start;
}

.jp-FileBrowser-Panel {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
}

.jp-BreadCrumbs {
  flex: 0 0 auto;
  margin: 8px 12px;
}

.jp-BreadCrumbs-item {
  margin: 0 2px;
  padding: 0 2px;
  border-radius: var(--jp-border-radius);
  cursor: pointer;
}

.jp-BreadCrumbs-item:hover {
  background-color: var(--jp-layout-color2);
}

.jp-BreadCrumbs-item:first-child {
  margin-left: 0;
}

.jp-BreadCrumbs-item.jp-mod-dropTarget {
  background-color: var(--jp-brand-color2);
  opacity: 0.7;
}

/*-----------------------------------------------------------------------------
| Buttons
|----------------------------------------------------------------------------*/

.jp-FileBrowser-toolbar > .jp-Toolbar-item {
  flex: 0 0 auto;
  padding-left: 0;
  padding-right: 2px;
  align-items: center;
  height: unset;
}

.jp-FileBrowser-toolbar > .jp-Toolbar-item .jp-ToolbarButtonComponent {
  width: 40px;
}

/*-----------------------------------------------------------------------------
| Other styles
|----------------------------------------------------------------------------*/

.jp-FileDialog.jp-mod-conflict input {
  color: var(--jp-error-color1);
}

.jp-FileDialog .jp-new-name-title {
  margin-top: 12px;
}

.jp-LastModified-hidden {
  display: none;
}

.jp-FileSize-hidden {
  display: none;
}

.jp-FileBrowser .lm-AccordionPanel > h3:first-child {
  display: none;
}

/*-----------------------------------------------------------------------------
| DirListing
|----------------------------------------------------------------------------*/

.jp-DirListing {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
  outline: 0;
}

.jp-DirListing-header {
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  align-items: center;
  overflow: hidden;
  border-top: var(--jp-border-width) solid var(--jp-border-color2);
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  box-shadow: var(--jp-toolbar-box-shadow);
  z-index: 2;
}

.jp-DirListing-headerItem {
  padding: 4px 12px 2px;
  font-weight: 500;
}

.jp-DirListing-headerItem:hover {
  background: var(--jp-layout-color2);
}

.jp-DirListing-headerItem.jp-id-name {
  flex: 1 0 84px;
}

.jp-DirListing-headerItem.jp-id-modified {
  flex: 0 0 112px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
}

.jp-DirListing-headerItem.jp-id-filesize {
  flex: 0 0 75px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
}

.jp-id-narrow {
  display: none;
  flex: 0 0 5px;
  padding: 4px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
  color: var(--jp-border-color2);
}

.jp-DirListing-narrow .jp-id-narrow {
  display: block;
}

.jp-DirListing-narrow .jp-id-modified,
.jp-DirListing-narrow .jp-DirListing-itemModified {
  display: none;
}

.jp-DirListing-headerItem.jp-mod-selected {
  font-weight: 600;
}

/* increase specificity to override bundled default */
.jp-DirListing-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  list-style-type: none;
  overflow: auto;
  background-color: var(--jp-layout-color1);
}

.jp-DirListing-content mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.jp-DirListing-content .jp-DirListing-item.jp-mod-selected mark {
  color: var(--jp-ui-inverse-font-color0);
}

/* Style the directory listing content when a user drops a file to upload */
.jp-DirListing.jp-mod-native-drop .jp-DirListing-content {
  outline: 5px dashed rgba(128, 128, 128, 0.5);
  outline-offset: -10px;
  cursor: copy;
}

.jp-DirListing-item {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 4px 12px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-DirListing-checkboxWrapper {
  /* Increases hit area of checkbox. */
  padding: 4px;
}

.jp-DirListing-header
  .jp-DirListing-checkboxWrapper
  + .jp-DirListing-headerItem {
  padding-left: 4px;
}

.jp-DirListing-content .jp-DirListing-checkboxWrapper {
  position: relative;
  left: -4px;
  margin: -4px 0 -4px -8px;
}

.jp-DirListing-checkboxWrapper.jp-mod-visible {
  visibility: visible;
}

/* For devices that support hovering, hide checkboxes until hovered, selected...
*/
@media (hover: hover) {
  .jp-DirListing-checkboxWrapper {
    visibility: hidden;
  }

  .jp-DirListing-item:hover .jp-DirListing-checkboxWrapper,
  .jp-DirListing-item.jp-mod-selected .jp-DirListing-checkboxWrapper {
    visibility: visible;
  }
}

.jp-DirListing-item[data-is-dot] {
  opacity: 75%;
}

.jp-DirListing-item.jp-mod-selected {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.jp-DirListing-item.jp-mod-dropTarget {
  background: var(--jp-brand-color3);
}

.jp-DirListing-item:hover:not(.jp-mod-selected) {
  background: var(--jp-layout-color2);
}

.jp-DirListing-itemIcon {
  flex: 0 0 20px;
  margin-right: 4px;
}

.jp-DirListing-itemText {
  flex: 1 0 64px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  user-select: none;
}

.jp-DirListing-itemText:focus {
  outline-width: 2px;
  outline-color: var(--jp-inverse-layout-color1);
  outline-style: solid;
  outline-offset: 1px;
}

.jp-DirListing-item.jp-mod-selected .jp-DirListing-itemText:focus {
  outline-color: var(--jp-layout-color1);
}

.jp-DirListing-itemModified {
  flex: 0 0 125px;
  text-align: right;
}

.jp-DirListing-itemFileSize {
  flex: 0 0 90px;
  text-align: right;
}

.jp-DirListing-editor {
  flex: 1 0 64px;
  outline: none;
  border: none;
  color: var(--jp-ui-font-color1);
  background-color: var(--jp-layout-color1);
}

.jp-DirListing-item.jp-mod-running .jp-DirListing-itemIcon::before {
  color: var(--jp-success-color1);
  content: '\25CF';
  font-size: 8px;
  position: absolute;
  left: -8px;
}

.jp-DirListing-item.jp-mod-running.jp-mod-selected
  .jp-DirListing-itemIcon::before {
  color: var(--jp-ui-inverse-font-color1);
}

.jp-DirListing-item.lm-mod-drag-image,
.jp-DirListing-item.jp-mod-selected.lm-mod-drag-image {
  font-size: var(--jp-ui-font-size1);
  padding-left: 4px;
  margin-left: 4px;
  width: 160px;
  background-color: var(--jp-ui-inverse-font-color2);
  box-shadow: var(--jp-elevation-z2);
  border-radius: 0;
  color: var(--jp-ui-font-color1);
  transform: translateX(-40%) translateY(-58%);
}

.jp-Document {
  min-width: 120px;
  min-height: 120px;
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Main OutputArea
| OutputArea has a list of Outputs
|----------------------------------------------------------------------------*/

.jp-OutputArea {
  overflow-y: auto;
}

.jp-OutputArea-child {
  display: table;
  table-layout: fixed;
  width: 100%;
  overflow: hidden;
}

.jp-OutputPrompt {
  width: var(--jp-cell-prompt-width);
  color: var(--jp-cell-outprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
  opacity: var(--jp-cell-prompt-opacity);

  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;

  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-OutputArea-prompt {
  display: table-cell;
  vertical-align: top;
}

.jp-OutputArea-output {
  display: table-cell;
  width: 100%;
  height: auto;
  overflow: auto;
  user-select: text;
  -moz-user-select: text;
  -webkit-user-select: text;
  -ms-user-select: text;
}

.jp-OutputArea .jp-RenderedText {
  padding-left: 1ch;
}

/**
 * Prompt overlay.
 */

.jp-OutputArea-promptOverlay {
  position: absolute;
  top: 0;
  width: var(--jp-cell-prompt-width);
  height: 100%;
  opacity: 0.5;
}

.jp-OutputArea-promptOverlay:hover {
  background: var(--jp-layout-color2);
  box-shadow: inset 0 0 1px var(--jp-inverse-layout-color0);
  cursor: zoom-out;
}

.jp-mod-outputsScrolled .jp-OutputArea-promptOverlay:hover {
  cursor: zoom-in;
}

/**
 * Isolated output.
 */
.jp-OutputArea-output.jp-mod-isolated {
  width: 100%;
  display: block;
}

/*
When drag events occur, `lm-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated {
  position: relative;
}

body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

/* pre */

.jp-OutputArea-output pre {
  border: none;
  margin: 0;
  padding: 0;
  overflow-x: auto;
  overflow-y: auto;
  word-break: break-all;
  word-wrap: break-word;
  white-space: pre-wrap;
}

/* tables */

.jp-OutputArea-output.jp-RenderedHTMLCommon table {
  margin-left: 0;
  margin-right: 0;
}

/* description lists */

.jp-OutputArea-output dl,
.jp-OutputArea-output dt,
.jp-OutputArea-output dd {
  display: block;
}

.jp-OutputArea-output dl {
  width: 100%;
  overflow: hidden;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dt {
  font-weight: bold;
  float: left;
  width: 20%;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dd {
  float: left;
  width: 80%;
  padding: 0;
  margin: 0;
}

.jp-TrimmedOutputs pre {
  background: var(--jp-layout-color3);
  font-size: calc(var(--jp-code-font-size) * 1.4);
  text-align: center;
  text-transform: uppercase;
}

/* Hide the gutter in case of
 *  - nested output areas (e.g. in the case of output widgets)
 *  - mirrored output areas
 */
.jp-OutputArea .jp-OutputArea .jp-OutputArea-prompt {
  display: none;
}

/* Hide empty lines in the output area, for instance due to cleared widgets */
.jp-OutputArea-prompt:empty {
  padding: 0;
  border: 0;
}

/*-----------------------------------------------------------------------------
| executeResult is added to any Output-result for the display of the object
| returned by a cell
|----------------------------------------------------------------------------*/

.jp-OutputArea-output.jp-OutputArea-executeResult {
  margin-left: 0;
  width: 100%;
}

/* Text output with the Out[] prompt needs a top padding to match the
 * alignment of the Out[] prompt itself.
 */
.jp-OutputArea-executeResult .jp-RenderedText.jp-OutputArea-output {
  padding-top: var(--jp-code-padding);
  border-top: var(--jp-border-width) solid transparent;
}

/*-----------------------------------------------------------------------------
| The Stdin output
|----------------------------------------------------------------------------*/

.jp-Stdin-prompt {
  color: var(--jp-content-font-color0);
  padding-right: var(--jp-code-padding);
  vertical-align: baseline;
  flex: 0 0 auto;
}

.jp-Stdin-input {
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  color: inherit;
  background-color: inherit;
  width: 42%;
  min-width: 200px;

  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;

  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0 0.25em;
  margin: 0 0.25em;
  flex: 0 0 70%;
}

.jp-Stdin-input::placeholder {
  opacity: 0;
}

.jp-Stdin-input:focus {
  box-shadow: none;
}

.jp-Stdin-input:focus::placeholder {
  opacity: 1;
}

/*-----------------------------------------------------------------------------
| Output Area View
|----------------------------------------------------------------------------*/

.jp-LinkedOutputView .jp-OutputArea {
  height: 100%;
  display: block;
}

.jp-LinkedOutputView .jp-OutputArea-output:only-child {
  height: 100%;
}

/*-----------------------------------------------------------------------------
| Printing
|----------------------------------------------------------------------------*/

@media print {
  .jp-OutputArea-child {
    break-inside: avoid-page;
  }
}

/*-----------------------------------------------------------------------------
| Mobile
|----------------------------------------------------------------------------*/
@media only screen and (max-width: 760px) {
  .jp-OutputPrompt {
    display: table-row;
    text-align: left;
  }

  .jp-OutputArea-child .jp-OutputArea-output {
    display: table-row;
    margin-left: var(--jp-notebook-padding);
  }
}

/* Trimmed outputs warning */
.jp-TrimmedOutputs > a {
  margin: 10px;
  text-decoration: none;
  cursor: pointer;
}

.jp-TrimmedOutputs > a:hover {
  text-decoration: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Table of Contents
|----------------------------------------------------------------------------*/

:root {
  --jp-private-toc-active-width: 4px;
}

.jp-TableOfContents {
  display: flex;
  flex-direction: column;
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  height: 100%;
}

.jp-TableOfContents-placeholder {
  text-align: center;
}

.jp-TableOfContents-placeholderContent {
  color: var(--jp-content-font-color2);
  padding: 8px;
}

.jp-TableOfContents-placeholderContent > h3 {
  margin-bottom: var(--jp-content-heading-margin-bottom);
}

.jp-TableOfContents .jp-SidePanel-content {
  overflow-y: auto;
}

.jp-TableOfContents-tree {
  margin: 4px;
}

.jp-TableOfContents ol {
  list-style-type: none;
}

/* stylelint-disable-next-line selector-max-type */
.jp-TableOfContents li > ol {
  /* Align left border with triangle icon center */
  padding-left: 11px;
}

.jp-TableOfContents-content {
  /* left margin for the active heading indicator */
  margin: 0 0 0 var(--jp-private-toc-active-width);
  padding: 0;
  background-color: var(--jp-layout-color1);
}

.jp-tocItem {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-tocItem-heading {
  display: flex;
  cursor: pointer;
}

.jp-tocItem-heading:hover {
  background-color: var(--jp-layout-color2);
}

.jp-tocItem-content {
  display: block;
  padding: 4px 0;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow-x: hidden;
}

.jp-tocItem-collapser {
  height: 20px;
  margin: 2px 2px 0;
  padding: 0;
  background: none;
  border: none;
  cursor: pointer;
}

.jp-tocItem-collapser:hover {
  background-color: var(--jp-layout-color3);
}

/* Active heading indicator */

.jp-tocItem-heading::before {
  content: ' ';
  background: transparent;
  width: var(--jp-private-toc-active-width);
  height: 24px;
  position: absolute;
  left: 0;
  border-radius: var(--jp-border-radius);
}

.jp-tocItem-heading.jp-tocItem-active::before {
  background-color: var(--jp-brand-color1);
}

.jp-tocItem-heading:hover.jp-tocItem-active::before {
  background: var(--jp-brand-color0);
  opacity: 1;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapser {
  flex: 0 0 var(--jp-cell-collapser-width);
  padding: 0;
  margin: 0;
  border: none;
  outline: none;
  background: transparent;
  border-radius: var(--jp-border-radius);
  opacity: 1;
}

.jp-Collapser-child {
  display: block;
  width: 100%;
  box-sizing: border-box;

  /* height: 100% doesn't work because the height of its parent is computed from content */
  position: absolute;
  top: 0;
  bottom: 0;
}

/*-----------------------------------------------------------------------------
| Printing
|----------------------------------------------------------------------------*/

/*
Hiding collapsers in print mode.

Note: input and output wrappers have "display: block" propery in print mode.
*/

@media print {
  .jp-Collapser {
    display: none;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Header/Footer
|----------------------------------------------------------------------------*/

/* Hidden by zero height by default */
.jp-CellHeader,
.jp-CellFooter {
  height: 0;
  width: 100%;
  padding: 0;
  margin: 0;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Input
|----------------------------------------------------------------------------*/

/* All input areas */
.jp-InputArea {
  display: table;
  table-layout: fixed;
  width: 100%;
  overflow: hidden;
}

.jp-InputArea-editor {
  display: table-cell;
  overflow: hidden;
  vertical-align: top;

  /* This is the non-active, default styling */
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  border-radius: 0;
  background: var(--jp-cell-editor-background);
}

.jp-InputPrompt {
  display: table-cell;
  vertical-align: top;
  width: var(--jp-cell-prompt-width);
  color: var(--jp-cell-inprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  opacity: var(--jp-cell-prompt-opacity);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;

  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;

  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/*-----------------------------------------------------------------------------
| Mobile
|----------------------------------------------------------------------------*/
@media only screen and (max-width: 760px) {
  .jp-InputArea-editor {
    display: table-row;
    margin-left: var(--jp-notebook-padding);
  }

  .jp-InputPrompt {
    display: table-row;
    text-align: left;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Placeholder {
  display: table;
  table-layout: fixed;
  width: 100%;
}

.jp-Placeholder-prompt {
  display: table-cell;
  box-sizing: border-box;
}

.jp-Placeholder-content {
  display: table-cell;
  padding: 4px 6px;
  border: 1px solid transparent;
  border-radius: 0;
  background: none;
  box-sizing: border-box;
  cursor: pointer;
}

.jp-Placeholder-contentContainer {
  display: flex;
}

.jp-Placeholder-content:hover,
.jp-InputPlaceholder > .jp-Placeholder-content:hover {
  border-color: var(--jp-layout-color3);
}

.jp-Placeholder-content .jp-MoreHorizIcon {
  width: 32px;
  height: 16px;
  border: 1px solid transparent;
  border-radius: var(--jp-border-radius);
}

.jp-Placeholder-content .jp-MoreHorizIcon:hover {
  border: 1px solid var(--jp-border-color1);
  box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.25);
  background-color: var(--jp-layout-color0);
}

.jp-PlaceholderText {
  white-space: nowrap;
  overflow-x: hidden;
  color: var(--jp-inverse-layout-color3);
  font-family: var(--jp-code-font-family);
}

.jp-InputPlaceholder > .jp-Placeholder-content {
  border-color: var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-cell-scrolling-output-offset: 5px;
}

/*-----------------------------------------------------------------------------
| Cell
|----------------------------------------------------------------------------*/

.jp-Cell {
  padding: var(--jp-cell-padding);
  margin: 0;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Common input/output
|----------------------------------------------------------------------------*/

.jp-Cell-inputWrapper,
.jp-Cell-outputWrapper {
  display: flex;
  flex-direction: row;
  padding: 0;
  margin: 0;

  /* Added to reveal the box-shadow on the input and output collapsers. */
  overflow: visible;
}

/* Only input/output areas inside cells */
.jp-Cell-inputArea,
.jp-Cell-outputArea {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Collapser
|----------------------------------------------------------------------------*/

/* Make the output collapser disappear when there is not output, but do so
 * in a manner that leaves it in the layout and preserves its width.
 */
.jp-Cell.jp-mod-noOutputs .jp-Cell-outputCollapser {
  border: none !important;
  background: transparent !important;
}

.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputCollapser {
  min-height: var(--jp-cell-collapser-min-height);
}

/*-----------------------------------------------------------------------------
| Output
|----------------------------------------------------------------------------*/

/* Put a space between input and output when there IS output */
.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputWrapper {
  margin-top: 5px;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea {
  overflow-y: auto;
  max-height: 24em;
  margin-left: var(--jp-private-cell-scrolling-output-offset);
  resize: vertical;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea[style*='height'] {
  max-height: unset;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea::after {
  content: ' ';
  box-shadow: inset 0 0 6px 2px rgb(0 0 0 / 30%);
  width: 100%;
  height: 100%;
  position: sticky;
  bottom: 0;
  top: 0;
  margin-top: -50%;
  float: left;
  display: block;
  pointer-events: none;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-child {
  padding-top: 6px;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-prompt {
  width: calc(
    var(--jp-cell-prompt-width) - var(--jp-private-cell-scrolling-output-offset)
  );
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-promptOverlay {
  left: calc(-1 * var(--jp-private-cell-scrolling-output-offset));
}

/*-----------------------------------------------------------------------------
| CodeCell
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| MarkdownCell
|----------------------------------------------------------------------------*/

.jp-MarkdownOutput {
  display: table-cell;
  width: 100%;
  margin-top: 0;
  margin-bottom: 0;
  padding-left: var(--jp-code-padding);
}

.jp-MarkdownOutput.jp-RenderedHTMLCommon {
  overflow: auto;
}

/* collapseHeadingButton (show always if hiddenCellsButton is _not_ shown) */
.jp-collapseHeadingButton {
  display: flex;
  min-height: var(--jp-cell-collapser-min-height);
  font-size: var(--jp-code-font-size);
  position: absolute;
  background-color: transparent;
  background-size: 25px;
  background-repeat: no-repeat;
  background-position-x: center;
  background-position-y: top;
  background-image: var(--jp-icon-caret-down);
  right: 0;
  top: 0;
  bottom: 0;
}

.jp-collapseHeadingButton.jp-mod-collapsed {
  background-image: var(--jp-icon-caret-right);
}

/*
 set the container font size to match that of content
 so that the nested collapse buttons have the right size
*/
.jp-MarkdownCell .jp-InputPrompt {
  font-size: var(--jp-content-font-size1);
}

/*
  Align collapseHeadingButton with cell top header
  The font sizes are identical to the ones in packages/rendermime/style/base.css
*/
.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='1'] {
  font-size: var(--jp-content-font-size5);
  background-position-y: calc(0.3 * var(--jp-content-font-size5));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='2'] {
  font-size: var(--jp-content-font-size4);
  background-position-y: calc(0.3 * var(--jp-content-font-size4));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='3'] {
  font-size: var(--jp-content-font-size3);
  background-position-y: calc(0.3 * var(--jp-content-font-size3));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='4'] {
  font-size: var(--jp-content-font-size2);
  background-position-y: calc(0.3 * var(--jp-content-font-size2));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='5'] {
  font-size: var(--jp-content-font-size1);
  background-position-y: top;
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='6'] {
  font-size: var(--jp-content-font-size0);
  background-position-y: top;
}

/* collapseHeadingButton (show only on (hover,active) if hiddenCellsButton is shown) */
.jp-Notebook.jp-mod-showHiddenCellsButton .jp-collapseHeadingButton {
  display: none;
}

.jp-Notebook.jp-mod-showHiddenCellsButton
  :is(.jp-MarkdownCell:hover, .jp-mod-active)
  .jp-collapseHeadingButton {
  display: flex;
}

/* showHiddenCellsButton (only show if jp-mod-showHiddenCellsButton is set, which
is a consequence of the showHiddenCellsButton option in Notebook Settings)*/
.jp-Notebook.jp-mod-showHiddenCellsButton .jp-showHiddenCellsButton {
  margin-left: calc(var(--jp-cell-prompt-width) + 2 * var(--jp-code-padding));
  margin-top: var(--jp-code-padding);
  border: 1px solid var(--jp-border-color2);
  background-color: var(--jp-border-color3) !important;
  color: var(--jp-content-font-color0) !important;
  display: flex;
}

.jp-Notebook.jp-mod-showHiddenCellsButton .jp-showHiddenCellsButton:hover {
  background-color: var(--jp-border-color2) !important;
}

.jp-showHiddenCellsButton {
  display: none;
}

/*-----------------------------------------------------------------------------
| Printing
|----------------------------------------------------------------------------*/

/*
Using block instead of flex to allow the use of the break-inside CSS property for
cell outputs.
*/

@media print {
  .jp-Cell-inputWrapper,
  .jp-Cell-outputWrapper {
    display: block;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-notebook-toolbar-padding: 2px 5px 2px 2px;
}

/*-----------------------------------------------------------------------------

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-NotebookPanel-toolbar {
  padding: var(--jp-notebook-toolbar-padding);

  /* disable paint containment from lumino 2.0 default strict CSS containment */
  contain: style size !important;
}

.jp-Toolbar-item.jp-Notebook-toolbarCellType .jp-select-wrapper.jp-mod-focused {
  border: none;
  box-shadow: none;
}

.jp-Notebook-toolbarCellTypeDropdown select {
  height: 24px;
  font-size: var(--jp-ui-font-size1);
  line-height: 14px;
  border-radius: 0;
  display: block;
}

.jp-Notebook-toolbarCellTypeDropdown span {
  top: 5px !important;
}

.jp-Toolbar-responsive-popup {
  position: absolute;
  height: fit-content;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-end;
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  background: var(--jp-toolbar-background);
  min-height: var(--jp-toolbar-micro-height);
  padding: var(--jp-notebook-toolbar-padding);
  z-index: 1;
  right: 0;
  top: 0;
}

.jp-Toolbar > .jp-Toolbar-responsive-opener {
  margin-left: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-Notebook-ExecutionIndicator {
  position: relative;
  display: inline-block;
  height: 100%;
  z-index: 9997;
}

.jp-Notebook-ExecutionIndicator-tooltip {
  visibility: hidden;
  height: auto;
  width: max-content;
  width: -moz-max-content;
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color1);
  text-align: justify;
  border-radius: 6px;
  padding: 0 5px;
  position: fixed;
  display: table;
}

.jp-Notebook-ExecutionIndicator-tooltip.up {
  transform: translateX(-50%) translateY(-100%) translateY(-32px);
}

.jp-Notebook-ExecutionIndicator-tooltip.down {
  transform: translateX(calc(-100% + 16px)) translateY(5px);
}

.jp-Notebook-ExecutionIndicator-tooltip.hidden {
  display: none;
}

.jp-Notebook-ExecutionIndicator:hover .jp-Notebook-ExecutionIndicator-tooltip {
  visibility: visible;
}

.jp-Notebook-ExecutionIndicator span {
  font-size: var(--jp-ui-font-size1);
  font-family: var(--jp-ui-font-family);
  color: var(--jp-ui-font-color1);
  line-height: 24px;
  display: block;
}

.jp-Notebook-ExecutionIndicator-progress-bar {
  display: flex;
  justify-content: center;
  height: 100%;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*
 * Execution indicator
 */
.jp-tocItem-content::after {
  content: '';

  /* Must be identical to form a circle */
  width: 12px;
  height: 12px;
  background: none;
  border: none;
  position: absolute;
  right: 0;
}

.jp-tocItem-content[data-running='0']::after {
  border-radius: 50%;
  border: var(--jp-border-width) solid var(--jp-inverse-layout-color3);
  background: none;
}

.jp-tocItem-content[data-running='1']::after {
  border-radius: 50%;
  border: var(--jp-border-width) solid var(--jp-inverse-layout-color3);
  background-color: var(--jp-inverse-layout-color3);
}

.jp-tocItem-content[data-running='0'],
.jp-tocItem-content[data-running='1'] {
  margin-right: 12px;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-Notebook-footer {
  height: 27px;
  margin-left: calc(
    var(--jp-cell-prompt-width) + var(--jp-cell-collapser-width) +
      var(--jp-cell-padding)
  );
  width: calc(
    100% -
      (
        var(--jp-cell-prompt-width) + var(--jp-cell-collapser-width) +
          var(--jp-cell-padding) + var(--jp-cell-padding)
      )
  );
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  color: var(--jp-ui-font-color3);
  margin-top: 6px;
  background: none;
  cursor: pointer;
}

.jp-Notebook-footer:focus {
  border-color: var(--jp-cell-editor-active-border-color);
}

/* For devices that support hovering, hide footer until hover */
@media (hover: hover) {
  .jp-Notebook-footer {
    opacity: 0;
  }

  .jp-Notebook-footer:focus,
  .jp-Notebook-footer:hover {
    opacity: 1;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Imports
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-side-by-side-output-size: 1fr;
  --jp-side-by-side-resized-cell: var(--jp-side-by-side-output-size);
  --jp-private-notebook-dragImage-width: 304px;
  --jp-private-notebook-dragImage-height: 36px;
  --jp-private-notebook-selected-color: var(--md-blue-400);
  --jp-private-notebook-active-color: var(--md-green-400);
}

/*-----------------------------------------------------------------------------
| Notebook
|----------------------------------------------------------------------------*/

/* stylelint-disable selector-max-class */

.jp-NotebookPanel {
  display: block;
  height: 100%;
}

.jp-NotebookPanel.jp-Document {
  min-width: 240px;
  min-height: 120px;
}

.jp-Notebook {
  padding: var(--jp-notebook-padding);
  outline: none;
  overflow: auto;
  background: var(--jp-layout-color0);
}

.jp-Notebook.jp-mod-scrollPastEnd::after {
  display: block;
  content: '';
  min-height: var(--jp-notebook-scroll-padding);
}

.jp-MainAreaWidget-ContainStrict .jp-Notebook * {
  contain: strict;
}

.jp-Notebook .jp-Cell {
  overflow: visible;
}

.jp-Notebook .jp-Cell .jp-InputPrompt {
  cursor: move;
}

/*-----------------------------------------------------------------------------
| Notebook state related styling
|
| The notebook and cells each have states, here are the possibilities:
|
| - Notebook
|   - Command
|   - Edit
| - Cell
|   - None
|   - Active (only one can be active)
|   - Selected (the cells actions are applied to)
|   - Multiselected (when multiple selected, the cursor)
|   - No outputs
|----------------------------------------------------------------------------*/

/* Command or edit modes */

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-InputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-OutputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

/* cell is active */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser {
  background: var(--jp-brand-color1);
}

/* cell is dirty */
.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt {
  color: var(--jp-warn-color1);
}

.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt::before {
  color: var(--jp-warn-color1);
  content: '•';
}

.jp-Notebook .jp-Cell.jp-mod-active.jp-mod-dirty .jp-Collapser {
  background: var(--jp-warn-color1);
}

/* collapser is hovered */
.jp-Notebook .jp-Cell .jp-Collapser:hover {
  box-shadow: var(--jp-elevation-z2);
  background: var(--jp-brand-color1);
  opacity: var(--jp-cell-collapser-not-active-hover-opacity);
}

/* cell is active and collapser is hovered */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser:hover {
  background: var(--jp-brand-color0);
  opacity: 1;
}

/* Command mode */

.jp-Notebook.jp-mod-commandMode .jp-Cell.jp-mod-selected {
  background: var(--jp-notebook-multiselected-color);
}

.jp-Notebook.jp-mod-commandMode
  .jp-Cell.jp-mod-active.jp-mod-selected:not(.jp-mod-multiSelected) {
  background: transparent;
}

/* Edit mode */

.jp-Notebook.jp-mod-editMode .jp-Cell.jp-mod-active .jp-InputArea-editor {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-cell-editor-active-background);
}

/*-----------------------------------------------------------------------------
| Notebook drag and drop
|----------------------------------------------------------------------------*/

.jp-Notebook-cell.jp-mod-dropSource {
  opacity: 0.5;
}

.jp-Notebook-cell.jp-mod-dropTarget,
.jp-Notebook.jp-mod-commandMode
  .jp-Notebook-cell.jp-mod-active.jp-mod-selected.jp-mod-dropTarget {
  border-top-color: var(--jp-private-notebook-selected-color);
  border-top-style: solid;
  border-top-width: 2px;
}

.jp-dragImage {
  display: block;
  flex-direction: row;
  width: var(--jp-private-notebook-dragImage-width);
  height: var(--jp-private-notebook-dragImage-height);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background);
  overflow: visible;
}

.jp-dragImage-singlePrompt {
  box-shadow: 2px 2px 4px 0 rgba(0, 0, 0, 0.12);
}

.jp-dragImage .jp-dragImage-content {
  flex: 1 1 auto;
  z-index: 2;
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  line-height: var(--jp-code-line-height);
  padding: var(--jp-code-padding);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background-color);
  color: var(--jp-content-font-color3);
  text-align: left;
  margin: 4px 4px 4px 0;
}

.jp-dragImage .jp-dragImage-prompt {
  flex: 0 0 auto;
  min-width: 36px;
  color: var(--jp-cell-inprompt-font-color);
  padding: var(--jp-code-padding);
  padding-left: 12px;
  font-family: var(--jp-cell-prompt-font-family);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: 1.9;
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
}

.jp-dragImage-multipleBack {
  z-index: -1;
  position: absolute;
  height: 32px;
  width: 300px;
  top: 8px;
  left: 8px;
  background: var(--jp-layout-color2);
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  box-shadow: 2px 2px 4px 0 rgba(0, 0, 0, 0.12);
}

/*-----------------------------------------------------------------------------
| Cell toolbar
|----------------------------------------------------------------------------*/

.jp-NotebookTools {
  display: block;
  min-width: var(--jp-sidebar-min-width);
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);

  /* This is needed so that all font sizing of children done in ems is
    * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  overflow: auto;
}

.jp-ActiveCellTool {
  padding: 12px 0;
  display: flex;
}

.jp-ActiveCellTool-Content {
  flex: 1 1 auto;
}

.jp-ActiveCellTool .jp-ActiveCellTool-CellContent {
  background: var(--jp-cell-editor-background);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  border-radius: 0;
  min-height: 29px;
}

.jp-ActiveCellTool .jp-InputPrompt {
  min-width: calc(var(--jp-cell-prompt-width) * 0.75);
}

.jp-ActiveCellTool-CellContent > pre {
  padding: 5px 4px;
  margin: 0;
  white-space: normal;
}

.jp-MetadataEditorTool {
  flex-direction: column;
  padding: 12px 0;
}

.jp-RankedPanel > :not(:first-child) {
  margin-top: 12px;
}

.jp-KeySelector select.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: var(--jp-border-width) solid var(--jp-border-color1);
}

.jp-KeySelector label,
.jp-MetadataEditorTool label,
.jp-NumberSetter label {
  line-height: 1.4;
}

.jp-NotebookTools .jp-select-wrapper {
  margin-top: 4px;
  margin-bottom: 0;
}

.jp-NumberSetter input {
  width: 100%;
  margin-top: 4px;
}

.jp-NotebookTools .jp-Collapse {
  margin-top: 16px;
}

/*-----------------------------------------------------------------------------
| Presentation Mode (.jp-mod-presentationMode)
|----------------------------------------------------------------------------*/

.jp-mod-presentationMode .jp-Notebook {
  --jp-content-font-size1: var(--jp-content-presentation-font-size1);
  --jp-code-font-size: var(--jp-code-presentation-font-size);
}

.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-InputPrompt,
.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-OutputPrompt {
  flex: 0 0 110px;
}

/*-----------------------------------------------------------------------------
| Side-by-side Mode (.jp-mod-sideBySide)
|----------------------------------------------------------------------------*/
.jp-mod-sideBySide.jp-Notebook .jp-Notebook-cell {
  margin-top: 3em;
  margin-bottom: 3em;
  margin-left: 5%;
  margin-right: 5%;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell {
  display: grid;
  grid-template-columns: minmax(0, 1fr) min-content minmax(
      0,
      var(--jp-side-by-side-output-size)
    );
  grid-template-rows: auto minmax(0, 1fr) auto;
  grid-template-areas:
    'header header header'
    'input handle output'
    'footer footer footer';
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell.jp-mod-resizedCell {
  grid-template-columns: minmax(0, 1fr) min-content minmax(
      0,
      var(--jp-side-by-side-resized-cell)
    );
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellHeader {
  grid-area: header;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-Cell-inputWrapper {
  grid-area: input;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-Cell-outputWrapper {
  /* overwrite the default margin (no vertical separation needed in side by side move */
  margin-top: 0;
  grid-area: output;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellFooter {
  grid-area: footer;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellResizeHandle {
  grid-area: handle;
  user-select: none;
  display: block;
  height: 100%;
  cursor: ew-resize;
  padding: 0 var(--jp-cell-padding);
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellResizeHandle::after {
  content: '';
  display: block;
  background: var(--jp-border-color2);
  height: 100%;
  width: 5px;
}

.jp-mod-sideBySide.jp-Notebook
  .jp-CodeCell.jp-mod-resizedCell
  .jp-CellResizeHandle::after {
  background: var(--jp-border-color0);
}

.jp-CellResizeHandle {
  display: none;
}

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Cell-Placeholder {
  padding-left: 55px;
}

.jp-Cell-Placeholder-wrapper {
  background: #fff;
  border: 1px solid;
  border-color: #e5e6e9 #dfe0e4 #d0d1d5;
  border-radius: 4px;
  -webkit-border-radius: 4px;
  margin: 10px 15px;
}

.jp-Cell-Placeholder-wrapper-inner {
  padding: 15px;
  position: relative;
}

.jp-Cell-Placeholder-wrapper-body {
  background-repeat: repeat;
  background-size: 50% auto;
}

.jp-Cell-Placeholder-wrapper-body div {
  background: #f6f7f8;
  background-image: -webkit-linear-gradient(
    left,
    #f6f7f8 0%,
    #edeef1 20%,
    #f6f7f8 40%,
    #f6f7f8 100%
  );
  background-repeat: no-repeat;
  background-size: 800px 104px;
  height: 104px;
  position: absolute;
  right: 15px;
  left: 15px;
  top: 15px;
}

div.jp-Cell-Placeholder-h1 {
  top: 20px;
  height: 20px;
  left: 15px;
  width: 150px;
}

div.jp-Cell-Placeholder-h2 {
  left: 15px;
  top: 50px;
  height: 10px;
  width: 100px;
}

div.jp-Cell-Placeholder-content-1,
div.jp-Cell-Placeholder-content-2,
div.jp-Cell-Placeholder-content-3 {
  left: 15px;
  right: 15px;
  height: 10px;
}

div.jp-Cell-Placeholder-content-1 {
  top: 100px;
}

div.jp-Cell-Placeholder-content-2 {
  top: 120px;
}

div.jp-Cell-Placeholder-content-3 {
  top: 140px;
}

</style>
<style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
The following CSS variables define the main, public API for styling JupyterLab.
These variables should be used by all plugins wherever possible. In other
words, plugins should not define custom colors, sizes, etc unless absolutely
necessary. This enables users to change the visual theme of JupyterLab
by changing these variables.

Many variables appear in an ordered sequence (0,1,2,3). These sequences
are designed to work well together, so for example, `--jp-border-color1` should
be used with `--jp-layout-color1`. The numbers have the following meanings:

* 0: super-primary, reserved for special emphasis
* 1: primary, most important under normal situations
* 2: secondary, next most important under normal situations
* 3: tertiary, next most important under normal situations

Throughout JupyterLab, we are mostly following principles from Google's
Material Design when selecting colors. We are not, however, following
all of MD as it is not optimized for dense, information rich UIs.
*/

:root {
  /* Elevation
   *
   * We style box-shadows using Material Design's idea of elevation. These particular numbers are taken from here:
   *
   * https://github.com/material-components/material-components-web
   * https://material-components-web.appspot.com/elevation.html
   */

  --jp-shadow-base-lightness: 0;
  --jp-shadow-umbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.2
  );
  --jp-shadow-penumbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.14
  );
  --jp-shadow-ambient-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.12
  );
  --jp-elevation-z0: none;
  --jp-elevation-z1: 0 2px 1px -1px var(--jp-shadow-umbra-color),
    0 1px 1px 0 var(--jp-shadow-penumbra-color),
    0 1px 3px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z2: 0 3px 1px -2px var(--jp-shadow-umbra-color),
    0 2px 2px 0 var(--jp-shadow-penumbra-color),
    0 1px 5px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z4: 0 2px 4px -1px var(--jp-shadow-umbra-color),
    0 4px 5px 0 var(--jp-shadow-penumbra-color),
    0 1px 10px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z6: 0 3px 5px -1px var(--jp-shadow-umbra-color),
    0 6px 10px 0 var(--jp-shadow-penumbra-color),
    0 1px 18px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z8: 0 5px 5px -3px var(--jp-shadow-umbra-color),
    0 8px 10px 1px var(--jp-shadow-penumbra-color),
    0 3px 14px 2px var(--jp-shadow-ambient-color);
  --jp-elevation-z12: 0 7px 8px -4px var(--jp-shadow-umbra-color),
    0 12px 17px 2px var(--jp-shadow-penumbra-color),
    0 5px 22px 4px var(--jp-shadow-ambient-color);
  --jp-elevation-z16: 0 8px 10px -5px var(--jp-shadow-umbra-color),
    0 16px 24px 2px var(--jp-shadow-penumbra-color),
    0 6px 30px 5px var(--jp-shadow-ambient-color);
  --jp-elevation-z20: 0 10px 13px -6px var(--jp-shadow-umbra-color),
    0 20px 31px 3px var(--jp-shadow-penumbra-color),
    0 8px 38px 7px var(--jp-shadow-ambient-color);
  --jp-elevation-z24: 0 11px 15px -7px var(--jp-shadow-umbra-color),
    0 24px 38px 3px var(--jp-shadow-penumbra-color),
    0 9px 46px 8px var(--jp-shadow-ambient-color);

  /* Borders
   *
   * The following variables, specify the visual styling of borders in JupyterLab.
   */

  --jp-border-width: 1px;
  --jp-border-color0: var(--md-grey-400);
  --jp-border-color1: var(--md-grey-400);
  --jp-border-color2: var(--md-grey-300);
  --jp-border-color3: var(--md-grey-200);
  --jp-inverse-border-color: var(--md-grey-600);
  --jp-border-radius: 2px;

  /* UI Fonts
   *
   * The UI font CSS variables are used for the typography all of the JupyterLab
   * user interface elements that are not directly user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-ui-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-ui-font-scale-factor: 1.2;
  --jp-ui-font-size0: 0.83333em;
  --jp-ui-font-size1: 13px; /* Base font size */
  --jp-ui-font-size2: 1.2em;
  --jp-ui-font-size3: 1.44em;
  --jp-ui-font-family: system-ui, -apple-system, blinkmacsystemfont, 'Segoe UI',
    helvetica, arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji',
    'Segoe UI Symbol';

  /*
   * Use these font colors against the corresponding main layout colors.
   * In a light theme, these go from dark to light.
   */

  /* Defaults use Material Design specification */
  --jp-ui-font-color0: rgba(0, 0, 0, 1);
  --jp-ui-font-color1: rgba(0, 0, 0, 0.87);
  --jp-ui-font-color2: rgba(0, 0, 0, 0.54);
  --jp-ui-font-color3: rgba(0, 0, 0, 0.38);

  /*
   * Use these against the brand/accent/warn/error colors.
   * These will typically go from light to darker, in both a dark and light theme.
   */

  --jp-ui-inverse-font-color0: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color1: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color2: rgba(255, 255, 255, 0.7);
  --jp-ui-inverse-font-color3: rgba(255, 255, 255, 0.5);

  /* Content Fonts
   *
   * Content font variables are used for typography of user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-content-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-content-line-height: 1.6;
  --jp-content-font-scale-factor: 1.2;
  --jp-content-font-size0: 0.83333em;
  --jp-content-font-size1: 14px; /* Base font size */
  --jp-content-font-size2: 1.2em;
  --jp-content-font-size3: 1.44em;
  --jp-content-font-size4: 1.728em;
  --jp-content-font-size5: 2.0736em;

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-content-presentation-font-size1: 17px;
  --jp-content-heading-line-height: 1;
  --jp-content-heading-margin-top: 1.2em;
  --jp-content-heading-margin-bottom: 0.8em;
  --jp-content-heading-font-weight: 500;

  /* Defaults use Material Design specification */
  --jp-content-font-color0: rgba(0, 0, 0, 1);
  --jp-content-font-color1: rgba(0, 0, 0, 0.87);
  --jp-content-font-color2: rgba(0, 0, 0, 0.54);
  --jp-content-font-color3: rgba(0, 0, 0, 0.38);
  --jp-content-link-color: var(--md-blue-900);
  --jp-content-font-family: system-ui, -apple-system, blinkmacsystemfont,
    'Segoe UI', helvetica, arial, sans-serif, 'Apple Color Emoji',
    'Segoe UI Emoji', 'Segoe UI Symbol';

  /*
   * Code Fonts
   *
   * Code font variables are used for typography of code and other monospaces content.
   */

  --jp-code-font-size: 13px;
  --jp-code-line-height: 1.3077; /* 17px for 13px base */
  --jp-code-padding: 5px; /* 5px for 13px base, codemirror highlighting needs integer px value */
  --jp-code-font-family-default: menlo, consolas, 'DejaVu Sans Mono', monospace;
  --jp-code-font-family: var(--jp-code-font-family-default);

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-code-presentation-font-size: 16px;

  /* may need to tweak cursor width if you change font size */
  --jp-code-cursor-width0: 1.4px;
  --jp-code-cursor-width1: 2px;
  --jp-code-cursor-width2: 4px;

  /* Layout
   *
   * The following are the main layout colors use in JupyterLab. In a light
   * theme these would go from light to dark.
   */

  --jp-layout-color0: white;
  --jp-layout-color1: white;
  --jp-layout-color2: var(--md-grey-200);
  --jp-layout-color3: var(--md-grey-400);
  --jp-layout-color4: var(--md-grey-600);

  /* Inverse Layout
   *
   * The following are the inverse layout colors use in JupyterLab. In a light
   * theme these would go from dark to light.
   */

  --jp-inverse-layout-color0: #111;
  --jp-inverse-layout-color1: var(--md-grey-900);
  --jp-inverse-layout-color2: var(--md-grey-800);
  --jp-inverse-layout-color3: var(--md-grey-700);
  --jp-inverse-layout-color4: var(--md-grey-600);

  /* Brand/accent */

  --jp-brand-color0: var(--md-blue-900);
  --jp-brand-color1: var(--md-blue-700);
  --jp-brand-color2: var(--md-blue-300);
  --jp-brand-color3: var(--md-blue-100);
  --jp-brand-color4: var(--md-blue-50);
  --jp-accent-color0: var(--md-green-900);
  --jp-accent-color1: var(--md-green-700);
  --jp-accent-color2: var(--md-green-300);
  --jp-accent-color3: var(--md-green-100);

  /* State colors (warn, error, success, info) */

  --jp-warn-color0: var(--md-orange-900);
  --jp-warn-color1: var(--md-orange-700);
  --jp-warn-color2: var(--md-orange-300);
  --jp-warn-color3: var(--md-orange-100);
  --jp-error-color0: var(--md-red-900);
  --jp-error-color1: var(--md-red-700);
  --jp-error-color2: var(--md-red-300);
  --jp-error-color3: var(--md-red-100);
  --jp-success-color0: var(--md-green-900);
  --jp-success-color1: var(--md-green-700);
  --jp-success-color2: var(--md-green-300);
  --jp-success-color3: var(--md-green-100);
  --jp-info-color0: var(--md-cyan-900);
  --jp-info-color1: var(--md-cyan-700);
  --jp-info-color2: var(--md-cyan-300);
  --jp-info-color3: var(--md-cyan-100);

  /* Cell specific styles */

  --jp-cell-padding: 5px;
  --jp-cell-collapser-width: 8px;
  --jp-cell-collapser-min-height: 20px;
  --jp-cell-collapser-not-active-hover-opacity: 0.6;
  --jp-cell-editor-background: var(--md-grey-100);
  --jp-cell-editor-border-color: var(--md-grey-300);
  --jp-cell-editor-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-cell-editor-active-background: var(--jp-layout-color0);
  --jp-cell-editor-active-border-color: var(--jp-brand-color1);
  --jp-cell-prompt-width: 64px;
  --jp-cell-prompt-font-family: var(--jp-code-font-family-default);
  --jp-cell-prompt-letter-spacing: 0;
  --jp-cell-prompt-opacity: 1;
  --jp-cell-prompt-not-active-opacity: 0.5;
  --jp-cell-prompt-not-active-font-color: var(--md-grey-700);

  /* A custom blend of MD grey and blue 600
   * See https://meyerweb.com/eric/tools/color-blend/#546E7A:1E88E5:5:hex */
  --jp-cell-inprompt-font-color: #307fc1;

  /* A custom blend of MD grey and orange 600
   * https://meyerweb.com/eric/tools/color-blend/#546E7A:F4511E:5:hex */
  --jp-cell-outprompt-font-color: #bf5b3d;

  /* Notebook specific styles */

  --jp-notebook-padding: 10px;
  --jp-notebook-select-background: var(--jp-layout-color1);
  --jp-notebook-multiselected-color: var(--md-blue-50);

  /* The scroll padding is calculated to fill enough space at the bottom of the
  notebook to show one single-line cell (with appropriate padding) at the top
  when the notebook is scrolled all the way to the bottom. We also subtract one
  pixel so that no scrollbar appears if we have just one single-line cell in the
  notebook. This padding is to enable a 'scroll past end' feature in a notebook.
  */
  --jp-notebook-scroll-padding: calc(
    100% - var(--jp-code-font-size) * var(--jp-code-line-height) -
      var(--jp-code-padding) - var(--jp-cell-padding) - 1px
  );

  /* Rendermime styles */

  --jp-rendermime-error-background: #fdd;
  --jp-rendermime-table-row-background: var(--md-grey-100);
  --jp-rendermime-table-row-hover-background: var(--md-light-blue-50);

  /* Dialog specific styles */

  --jp-dialog-background: rgba(0, 0, 0, 0.25);

  /* Console specific styles */

  --jp-console-padding: 10px;

  /* Toolbar specific styles */

  --jp-toolbar-border-color: var(--jp-border-color1);
  --jp-toolbar-micro-height: 8px;
  --jp-toolbar-background: var(--jp-layout-color1);
  --jp-toolbar-box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.24);
  --jp-toolbar-header-margin: 4px 4px 0 4px;
  --jp-toolbar-active-background: var(--md-grey-300);

  /* Statusbar specific styles */

  --jp-statusbar-height: 24px;

  /* Input field styles */

  --jp-input-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-input-active-background: var(--jp-layout-color1);
  --jp-input-hover-background: var(--jp-layout-color1);
  --jp-input-background: var(--md-grey-100);
  --jp-input-border-color: var(--jp-inverse-border-color);
  --jp-input-active-border-color: var(--jp-brand-color1);
  --jp-input-active-box-shadow-color: rgba(19, 124, 189, 0.3);

  /* General editor styles */

  --jp-editor-selected-background: #d9d9d9;
  --jp-editor-selected-focused-background: #d7d4f0;
  --jp-editor-cursor-color: var(--jp-ui-font-color0);

  /* Code mirror specific styles */

  --jp-mirror-editor-keyword-color: #008000;
  --jp-mirror-editor-atom-color: #88f;
  --jp-mirror-editor-number-color: #080;
  --jp-mirror-editor-def-color: #00f;
  --jp-mirror-editor-variable-color: var(--md-grey-900);
  --jp-mirror-editor-variable-2-color: rgb(0, 54, 109);
  --jp-mirror-editor-variable-3-color: #085;
  --jp-mirror-editor-punctuation-color: #05a;
  --jp-mirror-editor-property-color: #05a;
  --jp-mirror-editor-operator-color: #a2f;
  --jp-mirror-editor-comment-color: #408080;
  --jp-mirror-editor-string-color: #ba2121;
  --jp-mirror-editor-string-2-color: #708;
  --jp-mirror-editor-meta-color: #a2f;
  --jp-mirror-editor-qualifier-color: #555;
  --jp-mirror-editor-builtin-color: #008000;
  --jp-mirror-editor-bracket-color: #997;
  --jp-mirror-editor-tag-color: #170;
  --jp-mirror-editor-attribute-color: #00c;
  --jp-mirror-editor-header-color: blue;
  --jp-mirror-editor-quote-color: #090;
  --jp-mirror-editor-link-color: #00c;
  --jp-mirror-editor-error-color: #f00;
  --jp-mirror-editor-hr-color: #999;

  /*
    RTC user specific colors.
    These colors are used for the cursor, username in the editor,
    and the icon of the user.
  */

  --jp-collaborator-color1: #ffad8e;
  --jp-collaborator-color2: #dac83d;
  --jp-collaborator-color3: #72dd76;
  --jp-collaborator-color4: #00e4d0;
  --jp-collaborator-color5: #45d4ff;
  --jp-collaborator-color6: #e2b1ff;
  --jp-collaborator-color7: #ff9de6;

  /* Vega extension styles */

  --jp-vega-background: white;

  /* Sidebar-related styles */

  --jp-sidebar-min-width: 250px;

  /* Search-related styles */

  --jp-search-toggle-off-opacity: 0.5;
  --jp-search-toggle-hover-opacity: 0.8;
  --jp-search-toggle-on-opacity: 1;
  --jp-search-selected-match-background-color: rgb(245, 200, 0);
  --jp-search-selected-match-color: black;
  --jp-search-unselected-match-background-color: var(
    --jp-inverse-layout-color0
  );
  --jp-search-unselected-match-color: var(--jp-ui-inverse-font-color0);

  /* Icon colors that work well with light or dark backgrounds */
  --jp-icon-contrast-color0: var(--md-purple-600);
  --jp-icon-contrast-color1: var(--md-green-600);
  --jp-icon-contrast-color2: var(--md-pink-600);
  --jp-icon-contrast-color3: var(--md-blue-600);

  /* Button colors */
  --jp-accept-color-normal: var(--md-blue-700);
  --jp-accept-color-hover: var(--md-blue-800);
  --jp-accept-color-active: var(--md-blue-900);
  --jp-warn-color-normal: var(--md-red-700);
  --jp-warn-color-hover: var(--md-red-800);
  --jp-warn-color-active: var(--md-red-900);
  --jp-reject-color-normal: var(--md-grey-600);
  --jp-reject-color-hover: var(--md-grey-700);
  --jp-reject-color-active: var(--md-grey-800);

  /* File or activity icons and switch semantic variables */
  --jp-jupyter-icon-color: #f37626;
  --jp-notebook-icon-color: #f37626;
  --jp-json-icon-color: var(--md-orange-700);
  --jp-console-icon-background-color: var(--md-blue-700);
  --jp-console-icon-color: white;
  --jp-terminal-icon-background-color: var(--md-grey-800);
  --jp-terminal-icon-color: var(--md-grey-200);
  --jp-text-editor-icon-color: var(--md-grey-700);
  --jp-inspector-icon-color: var(--md-grey-700);
  --jp-switch-color: var(--md-grey-400);
  --jp-switch-true-position-color: var(--md-orange-900);
}
</style>
<style type="text/css">
/* Force rendering true colors when outputing to pdf */
* {
  -webkit-print-color-adjust: exact;
}

/* Misc */
a.anchor-link {
  display: none;
}

/* Input area styling */
.jp-InputArea {
  overflow: hidden;
}

.jp-InputArea-editor {
  overflow: hidden;
}

.cm-editor.cm-s-jupyter .highlight pre {
/* weird, but --jp-code-padding defined to be 5px but 4px horizontal padding is hardcoded for pre.cm-line */
  padding: var(--jp-code-padding) 4px;
  margin: 0;

  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
  color: inherit;

}

.jp-OutputArea-output pre {
  line-height: inherit;
  font-family: inherit;
}

.jp-RenderedText pre {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-code-font-size);
}

/* Hiding the collapser by default */
.jp-Collapser {
  display: none;
}

@page {
    margin: 0.5in; /* Margin for each printed piece of paper */
}

@media print {
  .jp-Cell-inputWrapper,
  .jp-Cell-outputWrapper {
    display: block;
  }
}
</style>
<!-- Load mathjax -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS_CHTML-full,Safe"> </script>
<!-- MathJax configuration -->
<script type="text/x-mathjax-config">
    init_mathjax = function() {
        if (window.MathJax) {
        // MathJax loaded
            MathJax.Hub.Config({
                TeX: {
                    equationNumbers: {
                    autoNumber: "AMS",
                    useLabelIds: true
                    }
                },
                tex2jax: {
                    inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                    displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
                    processEscapes: true,
                    processEnvironments: true
                },
                displayAlign: 'center',
                CommonHTML: {
                    linebreaks: {
                    automatic: true
                    }
                }
            });

            MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
        }
    }
    init_mathjax();
    </script>
<!-- End of mathjax configuration --><script type="module">
  document.addEventListener("DOMContentLoaded", async () => {
    const diagrams = document.querySelectorAll(".jp-Mermaid > pre.mermaid");
    // do not load mermaidjs if not needed
    if (!diagrams.length) {
      return;
    }
    const mermaid = (await import("https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.6.0/mermaid.esm.min.mjs")).default;
    const parser = new DOMParser();

    mermaid.initialize({
      maxTextSize: 100000,
      startOnLoad: false,
      fontFamily: window
        .getComputedStyle(document.body)
        .getPropertyValue("--jp-ui-font-family"),
      theme: document.querySelector("body[data-jp-theme-light='true']")
        ? "default"
        : "dark",
    });

    let _nextMermaidId = 0;

    function makeMermaidImage(svg) {
      const img = document.createElement("img");
      const doc = parser.parseFromString(svg, "image/svg+xml");
      const svgEl = doc.querySelector("svg");
      const { maxWidth } = svgEl?.style || {};
      const firstTitle = doc.querySelector("title");
      const firstDesc = doc.querySelector("desc");

      img.setAttribute("src", `data:image/svg+xml,${encodeURIComponent(svg)}`);
      if (maxWidth) {
        img.width = parseInt(maxWidth);
      }
      if (firstTitle) {
        img.setAttribute("alt", firstTitle.textContent);
      }
      if (firstDesc) {
        const caption = document.createElement("figcaption");
        caption.className = "sr-only";
        caption.textContent = firstDesc.textContent;
        return [img, caption];
      }
      return [img];
    }

    async function makeMermaidError(text) {
      let errorMessage = "";
      try {
        await mermaid.parse(text);
      } catch (err) {
        errorMessage = `${err}`;
      }

      const result = document.createElement("details");
      result.className = 'jp-RenderedMermaid-Details';
      const summary = document.createElement("summary");
      summary.className = 'jp-RenderedMermaid-Summary';
      const pre = document.createElement("pre");
      const code = document.createElement("code");
      code.innerText = text;
      pre.appendChild(code);
      summary.appendChild(pre);
      result.appendChild(summary);

      const warning = document.createElement("pre");
      warning.innerText = errorMessage;
      result.appendChild(warning);
      return [result];
    }

    async function renderOneMarmaid(src) {
      const id = `jp-mermaid-${_nextMermaidId++}`;
      const parent = src.parentNode;
      let raw = src.textContent.trim();
      const el = document.createElement("div");
      el.style.visibility = "hidden";
      document.body.appendChild(el);
      let results = null;
      let output = null;
      try {
        const { svg } = await mermaid.render(id, raw, el);
        results = makeMermaidImage(svg);
        output = document.createElement("figure");
        results.map(output.appendChild, output);
      } catch (err) {
        parent.classList.add("jp-mod-warning");
        results = await makeMermaidError(raw);
        output = results[0];
      } finally {
        el.remove();
      }
      parent.classList.add("jp-RenderedMermaid");
      parent.appendChild(output);
    }

    void Promise.all([...diagrams].map(renderOneMarmaid));
  });
</script>
<style>
  .jp-Mermaid:not(.jp-RenderedMermaid) {
    display: none;
  }

  .jp-RenderedMermaid {
    overflow: auto;
    display: flex;
  }

  .jp-RenderedMermaid.jp-mod-warning {
    width: auto;
    padding: 0.5em;
    margin-top: 0.5em;
    border: var(--jp-border-width) solid var(--jp-warn-color2);
    border-radius: var(--jp-border-radius);
    color: var(--jp-ui-font-color1);
    font-size: var(--jp-ui-font-size1);
    white-space: pre-wrap;
    word-wrap: break-word;
  }

  .jp-RenderedMermaid figure {
    margin: 0;
    overflow: auto;
    max-width: 100%;
  }

  .jp-RenderedMermaid img {
    max-width: 100%;
  }

  .jp-RenderedMermaid-Details > pre {
    margin-top: 1em;
  }

  .jp-RenderedMermaid-Summary {
    color: var(--jp-warn-color2);
  }

  .jp-RenderedMermaid:not(.jp-mod-warning) pre {
    display: none;
  }

  .jp-RenderedMermaid-Summary > pre {
    display: inline-block;
    white-space: normal;
  }
</style>
<!-- End of mermaid configuration --></head>
<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">
<main><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=8ca66cad-91f1-4e0a-bc83-d25ef4174c36">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [40]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">StandardScaler</span>
<span class="kn">from</span> <span class="nn">sklearn.decomposition</span> <span class="kn">import</span> <span class="n">PCA</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>

<span class="c1"># Load the Excel file (update the path as needed)</span>
<span class="n">file_path</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">'D:\Thesis Work\charts\AgERA52.xlsx'</span>
<span class="n">df_modified</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_excel</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="n">sheet_name</span><span class="o">=</span><span class="s1">'Sheet1'</span><span class="p">)</span>

<span class="c1"># Select the numerical variables for PCA</span>
<span class="n">variables_modified</span> <span class="o">=</span> <span class="n">df_modified</span><span class="p">[[</span><span class="s1">'Humidity'</span><span class="p">,</span> <span class="s1">'Solar Radiation'</span><span class="p">,</span> <span class="s1">'Temperature Mean'</span><span class="p">,</span> <span class="s1">'Temperature Max'</span><span class="p">,</span>
                                  <span class="s1">'Temperature Min'</span><span class="p">,</span> <span class="s1">'Wind Speed'</span><span class="p">,</span> <span class="s1">'Precipitation'</span><span class="p">]]</span>

<span class="c1"># Standardize the data</span>
<span class="n">scaler_modified</span> <span class="o">=</span> <span class="n">StandardScaler</span><span class="p">()</span>
<span class="n">scaled_data_modified</span> <span class="o">=</span> <span class="n">scaler_modified</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">variables_modified</span><span class="p">)</span>

<span class="c1"># Perform PCA</span>
<span class="n">pca_modified</span> <span class="o">=</span> <span class="n">PCA</span><span class="p">()</span>
<span class="n">pca_data_modified</span> <span class="o">=</span> <span class="n">pca_modified</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">scaled_data_modified</span><span class="p">)</span>

<span class="c1"># Eigenvalues and PC Values Table</span>
<span class="n">eigenvalues_modified</span> <span class="o">=</span> <span class="n">pca_modified</span><span class="o">.</span><span class="n">explained_variance_</span>
<span class="n">pc_values_modified</span> <span class="o">=</span> <span class="n">pca_data_modified</span>

<span class="c1"># Loading scores (coefficients of the original variables)</span>
<span class="n">loading_scores_modified</span> <span class="o">=</span> <span class="n">pca_modified</span><span class="o">.</span><span class="n">components_</span><span class="o">.</span><span class="n">T</span> <span class="o">*</span> <span class="n">np</span><span class="o">.</span><span class="n">sqrt</span><span class="p">(</span><span class="n">eigenvalues_modified</span><span class="p">)</span>

<span class="c1"># Covariance Matrix</span>
<span class="n">cov_matrix_modified</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">cov</span><span class="p">(</span><span class="n">scaled_data_modified</span><span class="o">.</span><span class="n">T</span><span class="p">)</span>

<span class="c1"># Function to plot a clearer biplot with longer arrows</span>
<span class="k">def</span> <span class="nf">biplot</span><span class="p">(</span><span class="n">score</span><span class="p">,</span> <span class="n">coeff</span><span class="p">,</span> <span class="n">pc_x</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">pc_y</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">labels</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">ax</span><span class="o">=</span><span class="kc">None</span><span class="p">):</span>
    <span class="n">ax</span><span class="o">.</span><span class="n">scatter</span><span class="p">(</span><span class="n">score</span><span class="p">[:,</span> <span class="n">pc_x</span><span class="p">],</span> <span class="n">score</span><span class="p">[:,</span> <span class="n">pc_y</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">'gray'</span><span class="p">,</span> <span class="n">s</span><span class="o">=</span><span class="mi">50</span><span class="p">,</span> <span class="n">alpha</span><span class="o">=</span><span class="mf">0.7</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s2">"PC scores"</span><span class="p">)</span>
    
    <span class="c1"># Plot loadings (blue arrows)</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">coeff</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">0</span><span class="p">]):</span>
        <span class="n">ax</span><span class="o">.</span><span class="n">arrow</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">coeff</span><span class="p">[</span><span class="n">i</span><span class="p">,</span> <span class="n">pc_x</span><span class="p">],</span> <span class="n">coeff</span><span class="p">[</span><span class="n">i</span><span class="p">,</span> <span class="n">pc_y</span><span class="p">],</span> <span class="n">color</span><span class="o">=</span><span class="s1">'blue'</span><span class="p">,</span> <span class="n">alpha</span><span class="o">=</span><span class="mf">0.8</span><span class="p">,</span> 
                 <span class="n">head_width</span><span class="o">=</span><span class="mf">0.2</span><span class="p">,</span> <span class="n">head_length</span><span class="o">=</span><span class="mf">0.5</span><span class="p">,</span> <span class="n">linewidth</span><span class="o">=</span><span class="mf">1.5</span><span class="p">)</span>
        <span class="n">ax</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="n">coeff</span><span class="p">[</span><span class="n">i</span><span class="p">,</span> <span class="n">pc_x</span><span class="p">]</span> <span class="o">*</span> <span class="mf">8.15</span><span class="p">,</span> <span class="n">coeff</span><span class="p">[</span><span class="n">i</span><span class="p">,</span> <span class="n">pc_y</span><span class="p">]</span> <span class="o">*</span> <span class="mf">7.15</span><span class="p">,</span> <span class="n">labels</span><span class="p">[</span><span class="n">i</span><span class="p">],</span> 
                <span class="n">color</span><span class="o">=</span><span class="s1">'blue'</span><span class="p">,</span> <span class="n">ha</span><span class="o">=</span><span class="s1">'center'</span><span class="p">,</span> <span class="n">va</span><span class="o">=</span><span class="s1">'center'</span><span class="p">,</span> <span class="n">fontsize</span><span class="o">=</span><span class="mi">12</span><span class="p">)</span>
    
    <span class="n">ax</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="sa">f</span><span class="s2">"PC</span><span class="si">{</span><span class="n">pc_x</span><span class="o">+</span><span class="mi">1</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
    <span class="n">ax</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="sa">f</span><span class="s2">"PC</span><span class="si">{</span><span class="n">pc_y</span><span class="o">+</span><span class="mi">1</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
    <span class="n">ax</span><span class="o">.</span><span class="n">grid</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span>
    <span class="n">ax</span><span class="o">.</span><span class="n">axhline</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s1">'black'</span><span class="p">,</span> <span class="n">linewidth</span><span class="o">=</span><span class="mf">0.5</span><span class="p">)</span>
    <span class="n">ax</span><span class="o">.</span><span class="n">axvline</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s1">'black'</span><span class="p">,</span> <span class="n">linewidth</span><span class="o">=</span><span class="mf">0.5</span><span class="p">)</span>
    <span class="n">ax</span><span class="o">.</span><span class="n">legend</span><span class="p">()</span>

<span class="c1"># Create subplots for the first three components</span>
<span class="n">fig</span><span class="p">,</span> <span class="n">axes</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">18</span><span class="p">,</span> <span class="mi">6</span><span class="p">))</span>

<span class="c1"># Plot the first two principal components in the first subplot</span>
<span class="n">biplot</span><span class="p">(</span><span class="n">pca_data_modified</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">transpose</span><span class="p">(</span><span class="n">pca_modified</span><span class="o">.</span><span class="n">components_</span><span class="p">),</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="n">labels</span><span class="o">=</span><span class="n">variables_modified</span><span class="o">.</span><span class="n">columns</span><span class="p">,</span> <span class="n">ax</span><span class="o">=</span><span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>

<span class="c1"># Plot PC1 vs PC3 in the second subplot</span>
<span class="n">biplot</span><span class="p">(</span><span class="n">pca_data_modified</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">transpose</span><span class="p">(</span><span class="n">pca_modified</span><span class="o">.</span><span class="n">components_</span><span class="p">),</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="n">labels</span><span class="o">=</span><span class="n">variables_modified</span><span class="o">.</span><span class="n">columns</span><span class="p">,</span> <span class="n">ax</span><span class="o">=</span><span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>

<span class="c1"># Plot PC2 vs PC3 in the third subplot</span>
<span class="n">biplot</span><span class="p">(</span><span class="n">pca_data_modified</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">transpose</span><span class="p">(</span><span class="n">pca_modified</span><span class="o">.</span><span class="n">components_</span><span class="p">),</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="n">labels</span><span class="o">=</span><span class="n">variables_modified</span><span class="o">.</span><span class="n">columns</span><span class="p">,</span> <span class="n">ax</span><span class="o">=</span><span class="n">axes</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>

<span class="n">plt</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>

<span class="c1"># Show tables and the biplot</span>
<span class="n">eigenvalues_table_modified</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">eigenvalues_modified</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="p">[</span><span class="s2">"Eigenvalues"</span><span class="p">])</span>
<span class="n">pc_values_table_modified</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">pc_values_modified</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="p">[</span><span class="sa">f</span><span class="s2">"PC</span><span class="si">{</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">pc_values_modified</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">])])</span>
<span class="n">loading_scores_table_modified</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">loading_scores_modified</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="n">variables_modified</span><span class="o">.</span><span class="n">columns</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="p">[</span><span class="sa">f</span><span class="s2">"PC</span><span class="si">{</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="si">}</span><span class="s2">"</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">loading_scores_modified</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">])])</span>
<span class="n">cov_matrix_table_modified</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">cov_matrix_modified</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="n">variables_modified</span><span class="o">.</span><span class="n">columns</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="n">variables_modified</span><span class="o">.</span><span class="n">columns</span><span class="p">)</span>

<span class="c1"># Print the tables</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">"Eigenvalues and PC Values Table:"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">eigenvalues_table_modified</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">Loading Score Table:"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">loading_scores_table_modified</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">"</span><span class="se">\n</span><span class="s2">Covariance Matrix Table:"</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">cov_matrix_table_modified</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,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pqYm+Xy+rK0QUqmUotGoamtr895b+NOf/rS+973v6aKLLtIHH3ygk046SXPnzlVbW5t+/etf66CDDtIFF1ww4H7/8z//ozlz5mjPPfeU3W7Xn/70J82ePVtlZWU65JBD1NDQoC984Qu68cYbtWDBArW0tMhms+noo4/WRRddpP32209XXXWVTj31VL3wwgv61a9+NehE0fL9739fBxxwgL7xjW/onHPOkc/nU3Nzs5566in98pe/1KOPPqq3335bDQ0NmjFjhpYvX65kMqlddtllok4fpoEbbjC///SnUigkHX649Oij0vz5E//YVuh38cXmGn2zZ5shXTgsXXHF0PctLjZDyyuukI46SorHpcsuky6/vHefz3/erBA87DCppmYCnwgmtaHWUpPM/+HO1/ogQDbMlZgrARi9cDisGTNmFHydVAATb1ubK5WXlzNXAjBhJtN684BE+Dfl1dXVqbW1VcFgUGVlZRl/WFKplILBoLxer2prawsyvuuvv1777LOPbr75Zv36179WMplUdXW1vvjFL+orX/lK1vv4/X5df/31am1tlcPh0H777adHH31UdrtZqPrQQw/pu9/9rk477TR1d3drwYIF+slPfiLJ/KTVgw8+qEsvvVRXXXWV5syZoyuvvDJjUeZs9thjD61cuVI//vGPdfDBByuVSqm6ulqnnnqqJKm8vFwPP/ywLr/8ckUiEdXU1OiBBx7QokWLcneyMOktXWp+DebRRzN/Li2Vbr994H79O4acdto6/f731QM+5Xj33eZXfytWZP48f/7AY0rS8cebX/31DfEk6d13B+7z5S+bX4N54glzPcNvfWvwfTC9TYb1QYCRYK7EXAnAyFiVP/zbDmxb+s+V+ppOc6Xly5czVwIwYXiPBJORLZWtcTVyqqurS2VlZQoGgyotLc24LRKJ6J133tFOO+2koqKiMR2/tbVVjY2NCofD8ng86ZYN0WhUXq9XDQ0NqpnipTnJZFJdXV0qLS1NT9Ymq1xc00KKx+NasmSJVq1aNSEtPZApHo9r+fLlOvbYY6fE+X7zTWn9erPtp88nvfKK2eJ0Kphq53qyi0Qiuvfee2W327Oum1FcXKyenh6Fw2Elk0mdeeaZY/qbONS/oZg+mCuNH3Ol/GK+lD/8+50/oVBITz/9tAKBwJC/m+P9tx25fV0zV9o25HOuZLWolMw2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oea25culF1+ULr987GO6/35p40bp298eeJvNJl122fiOj21X/y4jkvTEE09o5syZBR4ZAGAyYs42tOHmbBdfbNe++479+Mi/bakjWz6x5h+AacEwDEUiERmGUeihZNXa2qply5apqalJiURCdrtdiURCr7/+uiSpvb09b2OxFtSNRCJKJBJZ1x9hQV0AAKavu+6SXnhBeuop6ZxzpAcekA4+WOruzt8YLrlE+stfxnbfvfc2x7/33r3bli+XrrhifGO6/37pppuy3/bCC9J//uf4jg84HA4VFRUxvwYAjAhztuyGm7N99avJ8T0ACoa5Um5R+QdgSstWTVddXa26urpJUxbe0dGhxsZGxWIxVVRUZKyzZwVvq1evVmVlZV7G3NHRoe7uboVCIXV1dcnhcMjv98vv98vj8bCgLgAA09xuuyn9aejDDpMMQ7rqKumvf5XOOGPg/j09UnFxbsdQXT32+5aWSgcckLuxjES+Hw8AAIA52+gdcIAUj0tNTfl9XGAyovIPwJQ1WDVdU1OTli1bptbW1kIPUZLU3NyscDissrKyjOBPUvrncDislpaWCR+Ldc7a29vl9/vT52zLli366KOP1NHRoUAgILfbzYK6AABsI6w3ZdavN1s7+f3Sa69JRx0llZRIRxxh3h6Lma2mamslj0eqqjJbUnV0DDzm/fdLBx5oHsvvl/bcU7rjjt7bly6V5s/PvI/NJn3zm9Jtt0kLF5qPscceTj33XGZvqxUrzH1XrOg91s039x7D+rLaU918s9TQIM2aJfl80u67Sz/9qfnGkOXQQ6W//908B32P0Xds/dtTvf66dOKJ0owZUlGR+Rx/97vMfayxPvCA9OMfS3Pnmm+EfeYz0rp1A88bAADAYCbznG3XXaU//CFzv0LN2a68MjPyYM6GbRWVfwCmpKGq6Xw+n4LBoBobG1VeXl7QAMswDLW3t8vj8QwI/vryeDxqa2tTfX39hJW2ZztnJSUlCoVC6u7uViKRUHd3t/baay/ts88+BH8AAGwj2trM71VV0ltvmW8YnXCCdO650g9+ICUSUjJpvmny3HPS974n1debb7pcdpn5JsyaNZLXax7n0kvNT6WffLJ00UVSWZn5psv69cOPZdkyc12YK6803/S5+eaUbrhhX+27b0Jf/nL2+1xyidn+6s9/Nls9WebMMb+3t0unny7ttJPk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r73MCsK6OvNnyWxRWVcn+XzS/vtLa9Zk3n/pUsnvl954QzriCHO/qirpm980g7K+UinpllukPfc0H2fGDOmLX5Tefjtzv0MPNde3amyU6uvNsO2rXzVv++MfpaOOkubM6R3rD34gfbJcWHpMN99s/nffNqjvviutX2+TlNJ99w0MqGy2zFahl19ubnvlFXOcM2ZI1dWjey5DOe008/sDfZYTCwalhx7qfb799b2uxcV2XXjhmfrznz+nSKQkI6T4178W6je/+YKuvfabuuyy/9bFF39B//EfHQqHzYomn8+n7bbbTo88cpIuu+xCbdpUrrvv/pKuuOK7+ulPv6W//e1QJZPmObIqtpLJpHw+X8Zab5FIRD09PYrFYpOypaBhGIpEIqOuuhppi8HhqgUPOuigIasDJ1s1VrZ1+bKxqjwXLVo0oipJy2jbqxbKwoULR3Td/H7/sK+tXFZ2Wi1Z77nnHt17772655571NjYKEk6+OCDde655+qss87SQQcdpBkzZsjhcIzougAAAAAAAAAAJsaIK/+Gk0xKJ54oPfec9L3vmQHa+vXSZZeZwdqaNWZgZVm7VvrhD6Uf/1gqKzPbZZ58srnt6aela681Q7Dvf98MCt95J/P+8bjZevTcc80gbvVqM6Bav17629969zv3XDNMPP986frrpUBAuvJKc3xr10rbbde770cfSWeeaY7/2mvNykZJam01H+vb3zaDxpYW81gvvig984y5zyWXmGHgn/9stj+1zJkjbd06+vN58snSl78s/dd/9YaMo3kugyktNQPDO+80jyeZQaDdblYF3nRT5v79r+t++yX029+u0D/+cZBuu217XXDBvXK5EkokEtqwoUQLFrTqgAP+T05nVJs2zdQ//nGwXn75M/r61/8sn88nj8ejoiKPkkmH7r//VB166Ns6+eR39a9/leiJJ/bTz39u06WXmo9dV1enpqYmffjhh+lgyGazyTAMdXV1pSu5JkuI1dHRoebmZrW3t6fDl+rqatXV1eU8WBquWnC46sBChF2RiPStb5mB///7f70tZq2xJxKJIe9vVZAecsghkjRklWTfKjWHw5FRqWa1w3Q6naqtrVVtbW3Bgz9Jmjlz5oiu20cffaSmpqZhKwRzUdnZ2tqqxsZGhcPh9HgSiYSamprU2tqqhoYG1dTUaIcddtAOO+yggw46aNjq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9pOIiJY09l4nIiKixYAxCREREdHMGDMRNQeLf0REtOSx9zoREREtBoxJiIiIiGbGmIlo4bHtJxERLRvsvU7UfKdPn8YHPvABrFu3DjabDb29vfjMZz6DVCrV6qUREbUMYxIiEoyViIiqY8xEtHB48o+IiIiIZm1oaAi5XA7f/OY3sWHDBhw7dgwf+tCHEI1G8aUvfanVyyMiIiJqKcZKRERE1Aos/hERERHRrO3btw/79u1Tf1+/fj1OnjyJe+65hwktIiIiWvEYKxEREVErsPhHRERERPMqGAzC6/VW/X4ymUQymVR/D4VCAIB0Oo10Or3g61uO5Lrx+jUHr3fz8Fo3D69188zntebrtTQt5liJ/y9YnPi6LE58XRYnvi6LV6tem5X6XmDxj4iIiIjmzejoKL761a/iy1/+ctXbfPGLX8TnPve5sq8//vjjsNvtC7m8Ze+JJ55o9RJWFF7v5uG1bh5e6+aZj2sdi8XmYSXUTEslVuL/CxYnvi6LE1+XxYmvy+LV7NdmpcZLLP4RERERUZnPfvazFZNOWr/61a+wY8cO9fezZ89i3759eOc734kPfvCDVX/uzjvvxCc+8Qn191AohEsvvRS33HIL3G733Be/AqXTaTzxxBO4+eabYTKZWr2cZS+dTuPv/u7veL2bgO/t5uG1bp75vNZyIoyab7nGSvx/weLE12VxYky4OPG/l8WrVa/NSo2XWPwjIiIiojIf/ehH8Z73vKfmbdauXav+fPbsWdx444249tpr8a1vfavmz1ksFlgslrKvm0wm/nI2R7yGzcXr3Ty81s3Da90883Gt+Vq1znKPlfj/gsWJr8vixNdlceLrsng1+7VZqe8DFv+IiIiIqExHRwc6Ojrquu2ZM2dw4403Yvv27fjOd74DvV6/wKsjIiIiai3GSkRERLSYsfhHRERERLN29uxZ3HDDDbjsssvwpS99CZOTk+p7PT09LVwZERERUesxViIiIqJWYPGPiIiIiGbt8ccfx8jICEZGRrB69eqi7+Xz+RatioiIiGhxYKxERERErcA+A0REREQ0a3fccQfy+XzFf4iIiIhWOsZKRERE1Aos/hEREREREREREREREREtEyz+ERERERERERERERERES0TLP4RERERERERERERERERLRMs/hEREREREREREREREREtEyz+ERERERERERERERER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pxLlOj32WOHr738/im5ntRaumdzu5MlCa9P3vre4DemaNcB119X3PImIiIjmat++fRgfH8fY2BjuuusufP3rX8cnP/lJAIVY6d3vfjeuueYa7N+/vyhW+v73vw8ASCaT6OzsxKc//Wls2bKllU+FiIiIaN7NNVYaHBzEzTffjEcffRSHDx/GjTfeiN///d/HS5VmwxARzTNjqxdARIvTjTcC/+N/FIpUv/gFsH37xTl6e/cCX/4yEAwWvmc0Art2zXyfdnuhEKZlsQCJxMW/T00B3d3lP9vT09j6PZ5x9PefwIMP/gfk88DddwOf+EQHfvKTbXj++efxhS98Ab29/xE6nRXX/VvFbe3atbj55pvx/PMh/OM/Anp9J77yla/g5psLMwC/9rX/ga99rfyxLlwo/HtiovDva66pvCa9/uJzrPacenqA06cbe65EREREs2GxWNDzbwHJe9/7XvziF7/AT37yE/zpn/4pvvCFL+Duu+/GxzW90CVWCgQC6u9f+cpXAADf/va3m75+IiIiooU011jp7rvvLrq/L3zhC3jooYfw05/+FFdffXWzngYRrVAs/hFRRVL8e+qpwj+33Xbxe1LoGxwsfO+aay4WBufK5wOef77863Nph6nTAX/1V8Cdd8aQTvfj3nu/DqfTiTe84RJU2mwVi7nVWgCgowMwGoN4xzv+J/76r/+67PYu18XbAcC//mvhFF81cr+VnhPbfhIREVGr2Gw2pNNp3HvvvXA6nfjzP//zirfzeDzNXRgRERHRIjDXWCmXyyEcDsPr9S7gKomICtj2k4gq2rOn0OrzX/8V+PWvC/PzRFtboeXl975XOKVWT8vPet14IxAOAw8/XPx17VzAWsbHK3/9Zz97CcmkBT5fCsPDw1i/fj10On3Vx9LrC9cAKMzky2TakM/rsWMHyv7p7y/c7s1vLpyCHB0tv438AxRuv2pVYS5hPn/xcV97DXj22fqeJxEREdF8ev755/GDH/wAN910k4qVTCZTq5dFREREtCjMR6z05S9/GdFoFO9617sWaJVERBfx5B8RVeR2A9u2AT/5SaEQJvP+xN69hVaawPwW/97/fuDv/77w77/7O6CvD3j00cI8vXr8+38PBAJAMnkLDh/+Hmy225DJ9CKT+Rh0ujy+9rXV+Pa389D927A9nw/4j/8R+M1vgI0bC4/1T/9U+NpllxXu8z3vAf7iL57DQw/9e3z+88Dv/A5gMgGvv15oe/rWtwJvfzuwdi3w+c8Dn/40MDYG7NtXmJ84MVE4zehwAJ/7XOF6/tf/Cnzwg4Wf+9CHCmv+7Gcbb29KRERENFuPPPIInE4nMpkM0uk03vrWt+KrX/0q/uRP/kTFSkREREQr1XzGSvfddx8++9nP4qGHHkJXV9cCrZiI6CKe/COiqm68sXAy7eqrC8VArb17C98zm4F/G5k3L+x24P/+X+BNbwL+5m+Ad7yjUGT74Q/r+/mPfaxQxDt1ai/0+geRyfwMXu/f421v24BnnzXine9sx8aNGzE6Oop8PoeensJJv+99D7j9duCBB4C//VvgH/7h4n0aDMAVV3wa11zzBH70o0LB7m1vA/7bfyvMMLzyyou3vfPOwmnJU6eAP/mTwmnAT32qcKpPThICwAc+APzP/wkcPw78wR8UioZ/+7fA7/7uvFxGIiIiohndeOONePnll3Hy5EkkEgn86Ec/QldXl4qV0ul0q5dIRERE1DLzFSvdf//9+MAHPoAHHngAb3rTmxZ41UREBbp8Xtt0johoebjjjjsQCATwk5/8pOx7v/zlL/HGN74Rvb2/hdW6GseOFX8/EAiU9We/4YYbsHXr1rJhzURERERLUT2x0t13342Pf/zjZd9nrERERETL3XzFSvfddx/+7M/+DPfddx/e9ra3LeyiiYg02PaTiFacnTt34lOf+hT+v/9vFB0dRhw69CouueQSjIyM4Bvf+AZ27dqlgreXX34ZABCJRDA5OYmXX34ZZrMZmzdvbuEzICIiIlo4Eiv99V//Nc6cOYO3v/3tjJWIiIiI/k29sdJ9992H97///fjKV76CN77xjTh37hwAwGazoa2trcXPgoiWO578I6JlqdYOLXH55edx+nQEBsNW5HI59Pb24h3veAc+9rGPqR1alXq4r1mzBqdPn16YhRMRERE1QT2x0gMPPIB//Md/xEsvvcRYiYiIiFaU+YiVbrjhBhw4cKDs5/7kT/4E3/3udxdu8UREYPGPiIiIiIiIiIiIiIiIaNnQt3oBRERERERERERERERERDQ/WPwjIiIiIiIiIiIiIiIiWiZY/CMiIiIiIiIiIiIiIiJaJlj8IyIiIiIiIiIiIiIiIlomWPwjIiIiIiIiIiIiIiIiWiZY/CMiIiIiIiIiIiIiIiJaJlj8IyIiIiIiIiIiIiIiIlomWPwjIiIiIiIiIiIiIiIiWiZY/CMiIiIiIiIiIiIiIiJaJlj8IyIiIiIiIiIiIiIiIlomWPwjIiIiIiIiIiIiIiIiWiZY/CMiIiIiIiIiIiIiIiJaJv5/Dpegm00cm90AAAAASUVORK5CYII="/>
</div>
</div>
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>Eigenvalues and PC Values Table:
   Eigenvalues
0     4.256845
1     1.426737
2     0.806856
3     0.350529
4     0.166675
5     0.011413
6     0.000889

Loading Score Table:
                       PC1       PC2       PC3       PC4       PC5       PC6  \
Humidity          0.587364  0.713174  0.047798  0.322913 -0.206418  0.008265   
Solar Radiation  -0.890253 -0.233631  0.148381 -0.168228 -0.323992 -0.020623   
Temperature Mean -0.969080  0.166102  0.141742  0.106746  0.063506  0.004912   
Temperature Max  -0.983584  0.118113  0.107603  0.050361  0.021563  0.082158   
Temperature Min  -0.925185  0.248979  0.169037  0.200322  0.109273 -0.063970   
Wind Speed        0.269869 -0.847321  0.285508  0.360313 -0.026079  0.006860   
Precipitation     0.532867  0.205067  0.800498 -0.184580  0.044465  0.002477   

                       PC7  
Humidity         -0.000690  
Solar Radiation   0.000652  
Temperature Mean -0.024518  
Temperature Max   0.011436  
Temperature Min   0.012485  
Wind Speed       -0.000260  
Precipitation     0.000181  

Covariance Matrix Table:
                  Humidity  Solar Radiation  Temperature Mean  \
Humidity          1.002849        -0.670046         -0.422549   
Solar Radiation  -0.670046         1.002849          0.806301   
Temperature Mean -0.422549         0.806301          1.002849   
Temperature Max  -0.475862         0.846866          0.994911   
Temperature Min  -0.316182         0.722786          0.989596   
Wind Speed       -0.310339        -0.052234         -0.324952   
Precipitation     0.428736        -0.386923         -0.385736   

                  Temperature Max  Temperature Min  Wind Speed  Precipitation  
Humidity                -0.475862        -0.316182   -0.310339       0.428736  
Solar Radiation          0.846866         0.722786   -0.052234      -0.386923  
Temperature Mean         0.994911         0.989596   -0.324952      -0.385736  
Temperature Max          1.002849         0.964926   -0.316653      -0.421894  
Temperature Min          0.964926         1.002849   -0.343496      -0.338902  
Wind Speed              -0.316653        -0.343496    1.002849       0.130946  
Precipitation           -0.421894        -0.338902    0.130946       1.002849  
</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=8b24b3b6-bae7-432b-86df-466efa047b22">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span> 
</pre></div>
</div>
</div>
</div>
</div>
</div>
</main>
</body>
</html>
