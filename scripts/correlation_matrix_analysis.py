<!DOCTYPE html>

<html lang="en">
<head><meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title> correlation_matrix</title><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
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
<main><div class="jp-Cell jp-CodeCell jp-Notebook-cell" id="cell-id=6e192dc9-b45e-4e4c-b1ba-455a108c4af8">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [6]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">seaborn</span> <span class="k">as</span> <span class="nn">sns</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>

<span class="c1"># Load the dataset (replace with your file path if necessary)</span>
<span class="n">file_path</span> <span class="o">=</span> <span class="sa">r</span><span class="s2">"D:\Thesis Work\MACHINE LEARNING\PCA_Final_Analysis_Manual.xlsx"</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_excel</span><span class="p">(</span><span class="n">file_path</span><span class="p">,</span> <span class="n">sheet_name</span><span class="o">=</span><span class="s1">'Original Data'</span><span class="p">)</span>

<span class="c1"># Drop the 'Date' column since it's not needed for correlation analysis</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">columns</span><span class="o">=</span><span class="p">[</span><span class="s1">'Date'</span><span class="p">])</span>

<span class="c1"># Calculate the correlation matrix</span>
<span class="n">correlation_matrix</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">corr</span><span class="p">()</span>

<span class="c1"># Plot the heatmap</span>
<span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">8</span><span class="p">))</span>
<span class="n">sns</span><span class="o">.</span><span class="n">heatmap</span><span class="p">(</span><span class="n">correlation_matrix</span><span class="p">,</span> <span class="n">annot</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">cmap</span><span class="o">=</span><span class="s1">'coolwarm'</span><span class="p">,</span> <span class="n">vmin</span><span class="o">=-</span><span class="mi">1</span><span class="p">,</span> <span class="n">vmax</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">linewidths</span><span class="o">=</span><span class="mf">0.5</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">'Correlation Matrix Heatmap'</span><span class="p">)</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
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
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,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18yrevoInFGjRqFXr1548OABpk+fDnt7e9y6datYfmtra7Rt2xaTJk1S7Zp7/fp1PsKFiEiTit0riYiIysvFixeFgQMHCtWrVxf09fUFIyMjwdfXV/jmm2+EuLg4Vb78/Hxh9uzZQu3atQU9PT3B2tpa+OCDD4QHDx6o1de6dWuhTp06xc7zdNfc77//XmM7Ll26JPTp00ewsbER9PT0BDs7O6Ft27bCkiVLVHk07Zr78OFDoWfPnoKFhYVgYmIidOzYUbh69arGXV/nzZsnuLm5CTo6OgIAYdWqVYIgFN81VxAKd7794osvBBcXF0FPT0+wt7cXPvroIyE5OVktn4uLi9ClS5di/WndurXQunVrjX19Fv7dNbc0mna+vXbtmtChQwfBxMREsLCwEHr37i3cv39f486wISEhgoODgyCVStXGr6S2Pz32dPwyMjIET09PwdvbW8jMzFTL9/HHHwt6enrC6dOn/3M/S9rRuCzXRG5urjBu3DjB0dFRkMvlgp+fn7Bt2zaNf6cHDx4UfH19BZlMJgBQ9e/prrnx8fFq+QcOHCgYGRkVa6+ma/y7774TXF1dBZlMJnh5eQnLli1T1atpHBYtWiS4u7sLenp6gqenp7Bu3brSho+ISGtJBEEQKmQGTERERFRFSCQSfPzxx/jll18quilERG8E3iNKREREREREouJElIiIiIiIiETFzYqIiIiIXhHvdCIiejmMiBIREREREb0hjh07hrfffhsODg6QSCTYtm3bC8scPXoUDRs2hFwuR40aNbBkyZJieTZv3gxvb2/IZDJ4e3tj69at5dD6IpyIEhERERERvSEyMzNRv379Mm+OdvfuXXTu3BktW7ZEZGQkvvrqK3z66afYvHmzKk9ERAT69u2L/v3749KlS+jfvz/69OmD06dPl1c3wF1ziYiIiIiI3kASiQRbt25Ft27dSszzxRdfYMeOHYiKilKljRw5EpcuXUJERAQAoG/fvkhLS8PevXtVeTp27AgLCwusX7++XNrOiCgREREREVEFys3NRVpamtorNzf3tdQdERGBoKAgtbS33noL586dg0KhKDXPyZMnX0sbNOFmRUREREREpPV263lU2LnPTnwXU6dOVUubPHkypkyZ8sp1x8bGwtbWVi3N1tYWSqUSCQkJsLe3LzFPbGzsK5+/JJyIUpVSkR8g2qCL4gZydhe/uZ1eD3mXkfhkbmpFN6NK+2WMGbacKajoZlRZPRpLsexgRbeiahvWHpi3g3dVlZfR70j4GVHOejTmgkxNQkJCMGbMGLU0mUz22uqXSCRq75/enflsuqY8z6e9TpyIEhERERGR1pPold+k60VkMtlrnXg+y87OrlhkMy4uDrq6urCysio1z/NR0teJP0kQERERERFVUQEBAThw4IBa2p9//gl/f3/o6emVmqdZs2bl1i5GRImIiIiIiN4QGRkZuH37tur93bt3cfHiRVhaWqJ69eoICQnBo0ePsGbNGgCFO+T+8ssvGDNmDIYNG4aIiAisWLFCbTfczz77DK1atcLs2bMRHByM7du34+DBgzhx4kS59YMTUSIiIiIi0npS3Ypbmvsyzp07h8DAQNX7p/eWDhw4EGFhYYiJicH9+/dVx93c3LBnzx58/vnnWLhwIRwcHLBgwQL07NlTladZs2bYsGEDvv76a0yaNAnu7u7YuHEjmjRpUm794ESUiIiIiIjoDdGmTRvVZkOahIWFFUtr3bo1Lly4UGq9vXr1Qq9evV61eWXGiSgREREREWk9iR63zxETR5uIiIiIiIhExYkoERERERERiYpLc4mIiIiISOu9KZsVVRWMiBIREREREZGoGBElIiIiIiKtJ9FjRFRMjIgSERERERGRqBgRJSIiIiIircd7RMXFiCgRERERERGJihNRIiIiIiIiEhWX5hIRERERkdbjZkXiYkSUiIiIiIiIRMWIKBERERERaT1uViQuRkSJiIiIiIhIVJyIEhERERERkai4NJeIiIiIiLSeRIdLc8XEiCgRERERERGJihFRIiIiIiLSelJGREXFiCgRERERERGJihFRIiIiIiLSehIpI6JiYkSUiIiIiIiIRMWJKBEREREREYmKS3OJiIiIiEjrSXQYoxMTR5uIiIiIiIhExYgoERERERFpPT6+RVyMiBIREREREZGoOBElIiIiIiIiUXFpLhERERERaT0+R1RcjIgSERERERGRqBgRJSIiIiIircfNisTFiCiVWXR0NCQSCS5evFhinvDwcEgkEqSkpAAAwsLCYG5uLkr7iIiIiIjozcCI6Btm0KBBSElJwbZt29TSw8PDERgYiOTk5HKb+Dk7OyMmJgbW1tZlLtO3b1907txZ9X7KlCnYtm1bqZPZqsyyhT9qjB0CMz8fyB1s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JCA/Px+2trZq6ba2toiNjX1hH2NiYrB3715VNPUpT09PhIWFYceOHVi/fj3kcjmaN2+OW7duvdqgloJLc4mIiIiIiCpQSEgIxowZo5Ymk8lKzC+RqC8jFgShWJomYWFhMDc3R7du3dTSmzZtiqZNm6reN2/eHH5+fvj555+xYMGCMvTg5XEiSkREREREWq8i7xGVyWSlTjyfsra2ho6OTrHoZ1xcXLEo6fMEQcDKlSvRv39/6Ovrl5pXKpWiUaNG5RoR5dJcIiIiIiKiN4C+vj4aNmyIAwcOqKUfOHAAzZo1K7Xs0aNHcfv2bQwZMuSF5xEEARcvXoS9vf0rtbc0jIgSERERERG9IcaMGYP+/fvD398fAQEBCA0Nxf379zFy5EgAhct8Hz16hDVr1qiVW7FiBZo0aQIfH59idU6dOhVNmzZFrVq1kJaWhgULFuDixYtYuHBhufWDE1EiIiIiItJ6b8rjW/r27YvExERMmzYNMTEx8PHxwZ49e1S74MbExBR7pmhqaio2b96M+fPna6wzJSUFw4cPR2xsLMzMzODr64tjx46hcePG5dYPTkSJiIiIiIjeIKNGjcKoUaM0HgsLCyuWZmZmhqysrBLr++mnn/DTTz+9ruaVCSeiRERERESk9SRSbp8jJo42ERERERERiYoTUSIiIiIiIhIVl+YSEREREZHWe1M2K6oqJIIgCBXdCCIiIiIioor0YFTPCju386LNFXbuisKIKFUpObuXVHQTqjR5l5HYredR0c2osroobmDrmfyKbkaV1r2xDhKvnqzoZlRZVj7NeA2Xs+6NdfB7REFFN6PK6hMgxa4LyopuRpXW1a/yTj+4WZG4ONpEREREREQkqsr7kwQREREREZFYJLxHVEyMiBIREREREZGoOBElIiIiIiIiUXFpLhERERERaT0+vkVcjIgSERERERGRqBgRJSIiIiIircfHt4iLo01ERERERESi4kSUiIiIiIiIRMWluUREREREpPW4WZG4GBElIiIiIiIiUTEiSkREREREWo+bFYmLo01ERERERESiYkSUiIiIiIi0Hu8RFRcjokRERERERCQqTkSJiIiIiIhIVFyaS0REREREWo9Lc8XFiCgRERERERGJihFRIiIiIiIiPr5FVBxtIiIiIiIiEhUnokRERERERCQqLs0lIiIiIiKtJ5FwsyIxMSJKREREREREomJElIiIiIiItJ6EmxWJiqNNREREREREouJElIiIiIiIiETFpblERERERKT1JFJuViQmRkSJiIiIiIhIVIyIEhERERERcbMiUXG0iYiIiIiISFSMiBIRERERkdbjPaLiYkSUiIiIiIiIRMWJKBEREREREYmKS3OJiIiIiEjrSSSM0YmJo01ERERERESi4kT0Defq6op58+aVOX90dDQkEgkuXrxYLu0ZNGgQunXrVi51ExERERGVG6mk4l5aiEtzX6NBgwZh9erVAABdXV04OzujR48emDp1KoyMjMrlnGfPnn2pup2dnRETEwNra2sAQHh4OAIDA5GcnAxzc/My1xMdHQ03NzdERkaiQYMGqvT58+dDEIQy11OVbPzrEsKOnENCWibc7awwoVtr+NVw0pj3wj+PMH/XcdyNS0ZOngL2lqboFVAP/Vv7qfJsP/M3vtnwZ7GyZ2b/DzI9/tMtiWULf9QYOwRmfj6QO9jgXM9ReLLjUEU3640gCAIObl2IM0c2ITszDc7u9dBt4NewdapVYpmrZw/gyM5QJD65j3ylEtZ21dGy02D4tXhHleef6+dwbPdKPIr+G+kp8ej/2QLU8W8vRpcqlc37DuO37XuRmJwCN2dHfDb4PTTwrq0xb0JyCn4O24Ab/9zDg5gn6N25PUZ/+J5anvBT57Bmy248jHkCZX4+nO1t0e/tjujUppkY3amUeA2XP0EQcGTbQpw7+juyM9PgVKMeug6YBFvHksf473N/4tiuUCQ9uY/8fCWsbF3QvOMgNGgerDH/0V2hOPjHTwjo0B+d3/+qvLpSKQmCgD83L8KpQ5uQlZkGl5r10GPw17BzrllimVOHNuHc8R2IfXgbAODk5o3OfT9D9Zr1VHm+/V8HJCc8Lla2WYd+6PnhpNffEaIy4LfZ16xjx45YtWoVFAoFjh8/jqFDhyIzMxOLFy9Wy6dQKKCnp/fK56tWrdpL5dfR0YGdnd0rn7ckZmZm5VZ3ZbYv8gbmbAvHxJ5t0cDNAX+cvIJRoduw9YsBsLcwLZbfQF8P/Vo0QC0Haxjo6yHyn8eY/sdBGOjroldA0X8cxnJ9bP9ykFpZTkJLp2NkiLTLN/Bw9RY03PRLRTfnjXJ09wqc2LsavYfPhLWdKw5vX4Lls4di3Jw9kBlo/sHLwNgMge+MgI29G3R09RB18Sj+WDYRxqaWqF2vBQBAkZsF++oe8G/VHb8u+EzMLlUaB/86jfmrfsO4Yf1Rz7MWtv0ZjrEz5mLdvBmwq2ZVLL9CoYS5qQkG9uyKDbuK/yAFAKbGxhjYsytcHO2hq6uLv85dxMyFK2BhZoKmvnXLu0uVEq/h8nd8z3Kc3B+G7kMLxzh8xxKs/n4IPpu1t8QxNjQyR+u3R8DavgZ0dfVw42I4tq6YCCNTK9Sq20It78N/ruBc+O+wdfYQozuVzpGdK3B0z2r0GzkD1exdcXDrUiydORRfzN0NeQnjezvqLHybdYZr7QbQ1ZPhyM6VWDprOCZ8vx1mlrYAgNEzNqKgIF9VJvbBbSydORT1m74lSr+INOHS3NdMJpPBzs4Ozs7OeO+99/D+++9j27ZtmDJlCho0aICVK1eiRo0akMlkEAQBqampGD58OGxsbGBqaoq2bdvi0qVLanXu2LED/v7+kMvlsLa2Ro8ePVTHnl+aK5FIsHjxYnTq1AkGBgZwc3PDpk2bVMefXZobHR2NwMBAAICFhQUkEgkGDRoEANi3bx9atGgBc3NzWFlZoWvXrrhz546qHjc3NwCAr68vJBIJ2rRpA6D40tzc3Fx8+umnsLGxgVwuR4sWLXD27FnV8fDwcEgkEhw6dAj+/v4wNDREs2bNcOPGjVf6exDb2qMX0L2JD3o0rYsatlaY0L0N7MxN8PtflzXm93KyQSc/T9S0s4ajpRm6+nuhmYcrLvzzSC2fBBJYmxqpvah08fuP4ebkeYjddqCim/JGEQQBf+1bg8DgEfBp1AF2zrXQZ8QsKPJycDFiV4nl3L0aw8e/PWwc3WFlWx0t3uoPO+faiL55QZXHo34rvNX7M/g06iBGVyqlDTv/xNttW+Gd9q3h6uSA0R++BxsrS2zdf1hjfnsba3w+5H10atMcxoYGGvP4+XiidZOGcHVygJOdDfp2DYK7ixMuX79Vnl2ptHgNlz9BEBDx5xq0ensE6vgHwdapNnoO+w6K3BxcPlXyGLt5NYZ3ww6wcXCHpU11BAQNgK1zbdy7eV4tX25OJv5YOh7dBk+DgWHxH3GrOkEQcGzvWrTvNhz1GneAvXMtvPvRTOTl5SDyr90llvvgkzloHvQuHF29YOtYA32GT4UgFODW1VOqPMamljA1r6Z6XbsQDitbZ7h7NRKja28MiVRaYS9tpJ29FpGBgQEUCgUA4Pbt2/j999+xefNm1T2aXbp0QWxsLPbs2YPz58/Dz88P7dq1Q1JSEgBg9+7d6NGjB7p06YLIyEjVhK00kyZNQs+ePXHp0iV88MEHePfddxEVFVUsn7OzMzZv3gwAuHHjBmJiYjB//nwAQGZmJsaMGYOzZ8/i0KFDkEql6N69OwoKCgAAZ86cAQAcPHgQMTEx2LJli8a2TJgwAZs3b8bq1atx4cIF1KxZE2+99Zaqf09NnDgRP/74I86dOwddXV18+OGHZRneSkGhzEfUwycIqO2ilh7gUR2Xoosvg9Ek6mEcLkU/hr+7+lLerLw8dJy+HB2mLsMny7ch6mHca2s30bOS4h8iPTUBtXyKlnXq6unDzdMf925dLFMdgiDg9t8RiI+JhptH6Z9T2kShUOLGnWg0blBHLb1x/Tq4cuNOCaVejiAIOHf5Gu4/jkUDb+2MJPEaLn/J8Q+RkZqAmj7NVWm6evpw9WyE+7cjy1SHIAi4cy0CCTHRcH1ujHetnY7a9VvDvY52Li9PinuI9JQE1K6rPr7uXv6Ivlm28QWAvNwc5CuVMDTWvEpNqczD+RO70LhND0gk2nlvIlUOXONXjs6cOYPffvsN7dq1AwDk5eVh7dq1quW0hw8fxpUrVxAXFweZTAYA+OGHH7Bt2zb88ccfGD58OGbMmIF+/fph6tSpqnrr169f6nl79+6NoUOHAgCmT5+OAwcO4Oeff8aiRYvU8uno6MDS0hIAYGNjo3aPaM+ePdXyrlixAjY2Nrh27Rp8fHxUfbCysipxqe/TJclhYWHo1KkTAGDZsmU4cOAAVqxYgfHjx6vyzpgxA61btwYAfPnll+jSpQtycnIgl8tL7WtlkJyZjfwCAVYmhmrpViZGSEi/V2rZDlOXITkjG/kFBRj5VlP0aFq0nM7NxhLT+r2FWvbWyMzNxbpjkRj080b8Pu4DuFSzKJe+kPbKSEkAAJiYWaulm5haIzmx9B9UcrLSMfPTNlAqFZBKpQgeOAm16mrnF0lNUtLTkV9QAEsz9QiPpbkZklKuvlLdGZlZCB4+BnkKJXSkEowb1h+N69d5ccEqiNdw+ctILRxjY1P1MTY2tUJKGcb4+8/bQKnMg1QiRdcB36hNaC+f2o3H965h5DebSq6kiktLfXoNqy/XNzGzQpKG+ztLsnv9XJhZ2qCWT4DG41fPHkZOVjoater2n9taVUm0dNOgisKJ6Gu2a9cuGBsbQ6lUQqFQIDg4WDUJdHFxUbun8/z588jIyICVlfoHTnZ2tmoZ7MWLFzFs2LCXakNAQECx9y+7S+6dO3cwadIknDp1CgkJCapI6P379+Hj41PmOhQKBZo3L/qPRk9PD40bNy4Woa1Xr+i+SHt7ewBAXFwcqlevrrHu3Nxc5ObmqqU9ncxXlOd/VBQEoVja81Z90gfZuQpcvheD+btPoLq1OTr5eQIA6rnao56rvSpvA1dH9Ju7DuuPX8SXPQJfd/NJy0T+tRNbV01RvR80dknhH567aAUIkKD0C1lfboRPZ2xBXk4Wbv99Crt/mwNLG2e4ezV+3c1+sz0/tq9hYzdDAzlW/zAVWTm5OHflGhaEbYCDrQ38fDxfue7Kjtdw+bt0cid2rJ6iev/B54X7XWj6/w5lGONR0wrH+J9rp7Bv/WxYVnOGm1djpCbGYM9vszBw3HLo6Vfs/+ViOn9iF/5YPkX1fuiEp+Nb/LPiRdfwU4d3rEDkyT0YNSmsxLE8Hb4Zng1awMzS5r81nOg14UT0NQsMDMTixYuhp6cHBwcHtQ2Jnt/dtqCgAPb29ggPDy9Wz9PopIGB5nuDXtbLLr14++234ezsjGXLlsHBwQEFBQXw8fFBXl5emet4+iVL4wfqc2nPjtPTY08nv5rMmjVLLUoMAJMnT8aXjcpvI6aSWBgZQEcqQUJallp6UkYWrIwNSyhVyMmqcNlMLQdrJGZkYfH+U6qJ6POkUgnqONvifkLKa2k3aTdvv7ZwfmZHxXxF4b/t9JR4mJoX/WCWkZYIY7Pim+k8SyqVwtq2cGm6g4sX4h7/g/Cdy7T+S/xT5iYm0JFKkZSSqpaenJoGS/NX2+BNKpXCyb5wM5LabtVx7+FjrNmySysmoryGy5+nb1s4uReNsVL57xinJsDEvGgSk5meVKYxtvp3jO1dvBAfcwfHdofCzasxHkX/jcy0RCyZ0kuVv6AgH/dunsPpQ79h8vJLkEp1XmfXKoU6DQPhUrNoJZTy31u50lISYGrx7DWcVCxKqsmRXatwaPsyjPxqORxcNC/RT4p/jFtXTmHQmPmv2PoqSsK7FsXEiehrZmRkhJo1S95i+1l+fn6IjY2Frq4uXF1dNeapV68eDh06hMGDB5e5DadOncKAAQPU3vv6+mrMq6+vDwDIzy/aSS0xMRFRUVFYunQpWrZsCQA4ceLEC8s9r2bNmtDX18eJEyfw3nuFjx1QKBQ4d+4cRo8eXeb+aBISEoIxY8aopclkMggHV71Svf+Fnq4OvJxscermPbSrV/R3f+rmfbSp417megRBgEJZ8ngKgoAbj+NR0966xDxEZSUzMFLb4VIQBJiYWeP21Qg4unoDKPzSeff6OXTqO6akajQTBCgVZf/RqqrT09OFh7srzlz6G62bNFSln718DS0bNXit5xIEQKFUvtY6Kytew+VP0xgbm1njzt8n4eBSNMbR188iqM/Yl6pbeGaM3b0D8Mm329WOb10xEdZ2bmjZZWiVnIQCgNzASG0nXEEQYGJujZtXTsLJzQtA4fjeiTqHru+Wfg0f2bkSB7cuxfCQUDi7l7xy7ezRrTA2s4SXb6vX0wmiV8CJaAVq3749AgIC0K1bN8yePRseHh54/Pgx9uzZg27dusHf3x+TJ09Gu3bt4O7ujn79+kGpVGLv3r2YMGFCifVu2rQJ/v7+aNGiBdatW4czZ85gxYoVGvO6uLhAIpFg165d6Ny5MwwMDGBhYQErKyuEhobC3t4e9+/fx5dffqlWzsbGBgYGBti3bx+cnJwgl8uLPbrFyMgIH330EcaPHw9LS0tUr14dc+bMQVZWFoYMGfJKYyeTyTQuxc15pVr/u/6t/TDxt33wdrZFfVd7bI64gpjkdPRuVvhL8vxdJxCXloEZ73UEAGw4cRF2FiZwsym8Rzfy7mOsCT+Pd1s0UNW5ZH8E6rrYw6WaOTJy8vDb8Yu48SgeIT3ait6/N4mOkSGMahYt6TZ0c4JpfU/kJaUi50FMBbascpNIJGjecQCO7AyFlZ0LrG1dcGRnKPT05WgQ0FWVb+OSL2FmYYOO/36xP7IjFE5uPrC0dUa+UoEbl47hwl870G3QN6oyuTmZSHxyX/U+Kf4RHt+LgqGRGcytHcTrZAXq93YQpi1YBi93V/h41MT2A0fxJCER3YIKl9kv/nUT4pNS8M2nRbdi3LxbOGbZOblISUvHzbv3oaerAzdnRwDAmi274OnuBkfbalAo8xFx4TL2Hj2J8cP7i9/BSoDXcPmTSCQICBqAYztDYWXrAitbFxzdFQo9mRz1mhaN8R+hX8DUwhZBvQvH+OiuUDi61oGlTXXkKxW4efkYLp7cgbcHFI6xzMAItk7qz9TV0zeAobF5sfSqTCKRoFWn/ji0fRmq2bvA2s4Fh7aFQl9fDt/mXVT5flsUAjMLG3R593MAhctx9236GR98MgcW1RyQlhIPAJDJDSGTF010CwoKcPboVvi3CoaODqcAVPF4FVYgiUSCPXv2YOLEifjwww8RHx8POzs7tGrVCra2hUut2rRpg02bNmH69On47rvvYGpqilatSv8Va+rUqdiwYQNGjRoFOzs7rFu3Dt7e3hrzOjo6YurUqfjyyy8xePBgDBgwAGFhYdiwYQM+/fRT+Pj4wMPDAwsWLFA9ogUAdHV1sWDBAkybNg3ffPMNWrZsqXGJ8XfffYeCggL0798f6enp8Pf3x/79+2FhUbU22+no64HUrByE/nka8WmZqGlvhYXDusHBsnBzkoT0TMQmp6vyFwgCFuz+C4+SUqErlcLJyhyfdWmh9gzR9OxcTN90EAlpWTA20Ienow1WftIbdV3EX378JjFr6IOAQ2tV771/KHwY+oM1W3B5SEhFNeuN0LrLECjycrA9bBqys9LgXKMehkxYrhYRSUmMgeSZpUt5udnYtnoaUpOeQE9fhmr2NdB35GzUb9pJlefh3b+xbOYg1fvdv80GAPi16IY+I2aWf8cqgfbNmyA1PRMrN+1AYnIqalR3xA9ffQ57m8IVDonJqXiSkKhWZtC4yao/X78TjT+Pn4JdNStsWfIDgMIJ6g+haxCXlAyZvj5cHO0w+bNhaN+8iXgdq2R4DZe/lp2HQpmXi51rpiEnMw1O7vUwcJz6GKcmxkD6zBgrcrOwc+00pCU9gZ6+HNb2bug1fDbqNulcEV2o1ALfHgJFXi42r5yO7Mw0VHevh+FfLVOLnKYkxKjd4nTywAbkKxVYPe9ztbqCeo7CW70+Vr2/dTUCyQkxaNKmB0gzblYkLonwOnZLoEpDIpFg69atas/y1CY5u5dUdBOqNHmXkditp52PhhBDF8UNbD1T8vJsenXdG+sg8erJim5GlWXl04zXcDnr3lgHv0eUvIcCvZo+AVLsuqAdy9srSle/yhsHS5s7usLObTpmXoWdu6JU3iuBiIiIiIhILFJuViQmjjYRERERERGJihHRKoYrrYmIiIiIqLLjRJSIiIiIiLTe88+5p/LFpblEREREREQkKkZEiYiIiIiIuFmRqDjaREREREREJCpGRImIiIiISOtJpLxHVEyMiBIREREREZGoOBElIiIiIiIiUXFpLhERERERkYQxOjFxtImIiIiIiEhUjIgSERERERFxsyJRMSJKRERERET0Blm0aBHc3Nwgl8vRsGFDHD9+vMS84eHhkEgkxV7Xr19Xy7d582Z4e3tDJpPB29sbW7duLdc+cCJKRERERET0hti4cSNGjx6NiRMnIjIyEi1btkSnTp1w//79UsvduHEDMTExqletWrVUxyIiItC3b1/0798fly5dQv/+/dGnTx+cPn263PrBiSgREREREWk9iURaYa+XMXfuXAwZMgRDhw6Fl5cX5s2bB2dnZyxevLjUcjY2NrCzs1O9dHR0VMfmzZuHDh06ICQkBJ6enggJCUG7du0wb968/zKUZcKJKBERERERUQXKzc1FWlqa2is3N7dYvry8PJw/fx5BQUFq6UFBQTh58mSp5/D19YW9vT3atWuHI0eOqB2LiIgoVudbb731wjpfBSeiREREREREUkmFvWbNmgUzMzO116xZs4o1MSEhAfn5+bC1tVVLt7W1RWxsrMZu2dvbIzQ0FJs3b8aWLVvg4eGBdu3a4dixY6o8sbGxL1Xn68Bdc4mIiIiIiCpQSEgIxowZo5Ymk8lKzC+RqO/wKwhCsbSnPDw84OHhoXofEBCABw8e4IcffkCrVq3+U52vAyeiRERERESk9STSilssKpPJSp14PmVtbQ0dHZ1ikcq4uLhiEc3SNG3aFL/++qvqvZ2d3SvX+bK4NJeIiIiIiOgNoK+vj4YNG+LAgQNq6QcOHECzZs3KXE9kZCTs7e1V7wMCAorV+eeff75UnS+LEVEiIiIiIqI3xJgxY9C/f3/4+/sjICAAoaGhuH//PkaOHAmgcJnvo0ePsGbNGgCFO+K6urqiTp06yMvLw6+//orNmzdj8+bNqjo/++wztGrVCrNnz0ZwcDC2b9+OgwcP4sSJE+XWD05EiYiIiIiIyvF+yNepb9++SExMxLRp0xATEwMfHx/s2bMHLi4uAICYmBi1Z4rm5eVh3LhxePToEQwMDFCnTh3s3r0bnTt3VuVp1qwZNmzYgK+//hqTJk2Cu7s7Nm7ciCZNmpRbPzgRJSIiIiIieoOMGjUKo0aN0ngsLCxM7f2ECRMwYcKEF9bZq1cv9OrV63U0r0w4ESUiIiIiIqrAzYq0EUebiIiIiIiIRMWJKBEREREREYmKS3OJiIiIiIjekM2KqgpGRImIiIiIiEhUjIgSEREREZHWk3CzIlFxtImIiIiIiEhUjIgSERERERFJGKMTE0ebiIiIiIiIRMWJKBEREREREYmKS3OJiIiIiIikfHyLmBgRJSIiIiIiIlExIkpERERERFpPws2KRMXRJiIiIiIiIlFxIkpERERERESikgiCIFR0I4iIiIiIiCpSzsY5FXZued8JFXbuisJ7RKlK+WRuakU3oUr7ZYwZtp7Jr+hmVFndG+tgt55HRTejSuuiuIFbd+5VdDOqrFruLrjeO6iim1GleW76E5c6tqroZlRZ9fcdw8NPeld0M6o0p182VXQTqJLgRJSIiIiIiIibFYmKo01ERERERESiYkSUiIiIiIhIIqnoFmgVRkSJiIiIiIhIVJyIEhERERERkai4NJeIiIiIiEjKGJ2YONpEREREREQkKkZEiYiIiIiI+PgWUXG0iYiIiIiISFSciBIREREREZGouDSXiIiIiIhIyueIiokRUSIiIiIiIhIVI6JERERERETcrEhUHG0iIiIiIiISFSeiREREREREJCouzSUiIiIiIpJwsyIxMSJKREREREREomJElIiIiIiISMoYnZg42kRERERERCQqRkSJiIiIiIh4j6ioGBElIiIiIiIiUXEiSkRERERERKLi0lwiIiIiIiIJY3Ri4mgTERERERGRqBgRJSIiIiIi4uNbRMXRJiIiIiIiIlFxIkpERERERESi4tJcIiIiIiIiPkdUVIyIEhERERERkagYESUiIiIiIuLjW0TF0SYiIiIiIiJRMSJKRERERETEe0RFxYgoERERERERiYoTUSIiIiIiIhIVl+YSERERERFJGaMTE0f7FUyZMgUNGjSo6Gb8Z9HR0ZBIJLh48SIAIDw8HBKJBCkpKa9U7+uqh4iIiIiIqiatjojGxcVh0qRJ2Lt3L548eQILCwvUr18fU6ZMQUBAQEU3D0DhZNHNzU313tTUFF5eXpg4cSLefvvt13quZs2aISYmBmZmZmUu06ZNGzRo0ADz5s17pXqqis4BMjSvqw8DuQT3YvKx8XA2YhMLSi1jIAPebi5H/Zp6MJRLkJhagC3HcnDtrhIAINMDuv573NhQgodx+fjjSA7uP8kXo0uViiAIOLh1Ic4c2YTszDQ4u9dDt4Ffw9apVollrp49gCM7Q5H45D7ylUpY21VHy06D4dfiHVWef66f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1RY9GkuReFXzjfD06qx8muHWnXsV3YwqrZa7C3braccjeipCF8UNfg6Xsx6Npdh2Nr+im1FldWukg98jeA2Xpz4BlffpkbfvVNyzrGu6u7040782btyI/v37Y8mSJQgICEBoaCiWLVuGv//+Gy4uLggJCcGjR4+wZs0aAIWPb/Hx8cGIESMwbNgwREREYOTIkVi/fr0q+HPy5Em0atUKM2bMQHBwMLZv346vv/4aJ06cKLbXy+vCiCgREREREWk9AZV3kvysvn37IjExEdOmTUNMTAx8fHywZ88euLgUblgVExOj9lQONzc37NmzB59//jkWLlwIBwcHLFiwQG0FYrNmzbBhwwZ8/fXXmDRpEtzd3bFx48Zym4QCnIhWSffv31ctn9Xk2rVrqF69eonHiYiIiIio8ho1ahRGjRql8VhYWFixtNatW+PChQul1tmrVy/06tWr1DyvEyeiVZCDg4PqWZ8lHS8LrtomIiIiIm0hvOB5rfR6cSJaBenq6qJmzZoV3QwiIiIiIiKN3oyF0ERERERERFRlMCJKRERERERaj0tzxcWIKBEREREREYmKEVEiIiIiItJ6jIiKixFRIiIiIiIiEhUjokREREREpPUYERUXI6JEREREREQkKk5EiYiIiIiISFRcmktERERERFpPELg0V0yMiBIREREREZGoGBElIiIiIiKtx82KxMWIKBEREREREYmKE1EiIiIiIiISFZfmEhERERGR1uPSXHExIkpERERERESiYkSUiIiIiIi0HiOi4mJElIiIiIiIiETFiCgREREREWk9QWBEVEyMiBIREREREZGoOBElIiIiIiIiUXFpLhERERERab0CblYkKkZEiYiIiIiISFSMiBIRERERkdbj41vExYgoERERERERiYoTUSIiIiIiIhIVl+YSEREREZHW43NExcWIKBEREREREYmKEVEiIiIiItJ63KxIXIyIEhERERERkag4ESUiIiIiIiJRcWkuERERERFpPW5WJC5GRImIiIiIiEhUjIgSEREREZHW42ZF4mJElIiIiIiIiETFiCgREREREWk93iMqLokgCEJFN4KIiIiIiKginbmeWmHnbuxpVmHnriiMiFKVsuxgRbegahvWHth6Jr+im1FldW+sg+u9gyq6GVWa56Y/seVMQUU3o8rq0ViK3XoeFd2MKq2L4gb2GHpWdDOq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+x/su1r6OgT0cfq3UcIR1UbyDkOh9cgPR5Cmg7zDUFjdsx7w/Fax7lkP5B1CqQ5ck99nnL6ta99KxpVyH1EiIiIiIiKiimIiWk00adIE2traJT7evjXKx3J1dS31dRYvrp1DEImIiIiIxGL5PWqjSpkjWlV8fX3h6+sr7zBkIigoqMTbwAAodw7p+9i0aROys7NL3GZoWPa9LImIiIiIiCpDtU5EaxMbGxuZvE6dOnVk8jpERERERDWJGLx9iyxxaC4RERERERHJFBNRIiIiIiIikikOzSUiIiIiolqP9xGVLVZEiYiIiIiISKZYESUiIiIiolqvtt5GRV5YESUiIiIiIiKZYkWUiIiIiIhqPVZEZYsVUSIiIiIiIpIpJqJEREREREQkUxyaS0REREREtZ5ILJB3CLUKK6JEREREREQkU6yIEhERERFRrcfFimSLFVEiIiIiIiKSKSaiREREREREJFMcmktERERERLUeh+bKFiuiREREREREJFOsiBIRERERUa0nYkVUplgRJSIiIiIiIpliIkpEREREREQyxaG5RERERERU64nFAnmHUKuwIkpEREREREQyxYooERERERHVerx9i2yxIkpEREREREQyxYooERERERHVerx9i2yxIkpEREREREQyxUSUiIiIiIiIZIpDc4mIiIiIqNbjYkWyxYooERERERERyRQrokREREREVOuxIipbrIgSERERERGRTDERJSIiIiIiIpni0FwiIiIiIqr1eB9R2WJFlIiIiIiIiGSKFVEiIiIiIqr1uFiRbLEiSkRERERERDIlEIuZ+xMRERERUe22/h/5vfaYLvJ7bXnh0FxSKKsP8nuVqjSxtwC7gkXyDkNhubko4Va3L+QdhkL75Nh5HLhWKO8wFFbf1soI0nSQdxgKrXvWAxxRbSTvMBRWj/xwnKzrJO8wFFrn2DvyDoGqCQ7NJSIiIiIiIpliRZSIiIiIiGo9TliULVZEiYiIiIiISKZYESUiIiIiolqPFVHZYkWUiIiIiIiIZIqJKBEREREREckUh+YSEREREVGtJ+LQXJliRZSIiIiIiIhkihVRIiIiIiKq9cRyXa1IIMfXlg9WRImIiIiIiEimWBElIiIiIqJaj7dvkS1WRImIiIiIiEimmIgSERERERGRTHFoLhERERER1XoikbwjqF1YESUiIiIiIiKZYkWU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HBywf/9+qX3T0tKwe/dujBo1qtjzPnnyBPPnz0dISAiioqIQFBSEAQMGoEWLFvjss88qHB8rokREREREVOsp2u1bgKKVbX18fNClSxcAQO/evfHbb79J9QkPD0dqaqpU244dOyAWizF48OBizykUCnHq1CmsWbMGGRkZsLKyQo8ePTB37lwoKytXODYmokRERERERArI0NAQ27ZtK7OPuIS5saNHj8bo0aNL7G9lZYVz5859dGxMRImIiIiIqNYrKSGjqsM5okRERERERCRTTESJiIiIiIhIpjg0l4iIiIiIaj2RAi5WVJ2xIkpEREREREQyxYooERERERHVeop4+5bqjBVRIiIiIiIikilWRImIiIiIqNbj7VtkixVRIiIiIiIikikmokRERERERCRTHJpLRERERES1nlgkkncItQorokRERERERCRTrIgSEREREVGtJ+LtW2SKFVEiIiIiIiKSKSaiREREREREJFMcmktERERERLUe7yMqW6yIEhERERERkUyxIkpERERERLWemIsVyRQrokRERERERCRTTEQJAoEABw4ckNnrBQQEQF9fX2avR0RERERUHrFILLdHbVSlQ3MFAkGZ2z09PREQEFCVIchchw4d0Lx5c6xevVreoUhkZ2fD0tISAoEAcXFx0NDQkNoeHx8PAwODD37+s2fPomPHjtDX10d8fDzU1dUl265evYq2bdsCeDMBfODAgejevfsHv151JRaLcWr//3D1zC5kZ6bBql4z9PGcDbO6DUrd5+61f3D20Aa8fB6NwoICGJvb4HPX4XD+vI+kz9mDG3A35ASS4iOgqqoOmwYt0G3QZJhY2MnisKoVsViMf/b+jsundiMrMw029Zuh/4j/g7lV/VL3uXxqN0IuHERC7GMAQF27xug+cAKs6zeT9Fk4/mu8evGs2L7tvh6Eb0bOrvwDqaa02neBzld9oKynj/z4WKTs3Yy8Jw9K7Gvg/gO0Pu1QrD0/PgbPF00CAKiY14Vuz4EQWtlDxcgUKXs2I+NsUFUeQrUnFotx5sD/EHKu6H2irn0z9Bw2G2Z1Sn+fuBfyD84f3oDk59EoLCyAkZkNPus2HM0/61Ni/3OHN+Dknl/g8rUHug/9qaoOpVqyHj0Y9hO9oGZugoywx7g/dTFeXbpean+bMUNgM2YoNGzqIDsmHk+Wr0Pcn39LtgtUVFBv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"/>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs" id="cell-id=0f3c2a25-29f9-4736-a272-0f4d479bfea0">
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
