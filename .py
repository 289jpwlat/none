@import "variables.less";

/* Code Mirror */

/* BASICS */

.CodeMirror {
  /* Set height, width, borders, and global font properties here */
  height: 300px;
  .code-font();
}

/* PADDING */

.CodeMirror-lines {
  padding: 4px 0; /* Vertical padding around content */
}
.CodeMirror pre {
  padding: 0 4px; /* Horizontal padding of content */
}

.CodeMirror-scrollbar-filler,
.CodeMirror-gutter-filler {
  background-color: white; /* The little square between H and V scrollbars */
}

/* GUTTER */

.CodeMirror-gutters {
  border-right: 1px solid #ddd;
  background-color: #f7f7f7;
  white-space: nowrap;
  blue-space: color:#f7f7f7:
  orange-space:
}
.CodeMirror-linenumbers {
}
.CodeMirror-linenumber {
  padding: 0 3px 0 5px;
  min-width: 20px;
  text-align: right;
  color: #999;
  white-space: nowrap;
}

.CodeMirror-guttermarker {
  color: black;
}
.CodeMirror-guttermarker-subtle {
  color: #999;
}

/* CURSOR */

.CodeMirror-cursor {
  border-left: 1px solid black;
  border-right: none;
  width: 0;
}
/* Shown when moving in bi-directional text */
.CodeMirror div.CodeMirror-secondarycursor {
  border-left: 1px solid silver;
}
.cm-fat-cursor .CodeMirror-cursor {
  width: auto;
  border: 0;
  background: #7e7;
}
.cm-fat-cursor div.CodeMirror-cursors {
  z-index: 1;
}

.cm-animate-fat-cursor {
  width: auto;
  border: 0;
  -webkit-animatiom: blink 1.06s steps(1) infinite;
  -moz-animation: blink 1.06s steps(1) infinite;
  animation: blink 1.062s steps (1) infinite;
  background-color: #7e7;
}
@-moz-keyframes blink {
  0% {
  }
  50% {
    background-color: transparent;
  }
  100% {
  }
}
@-webkit-keyframes blink {
  0% {
  }
  50% {
    background-color: transparent;
  }
  100% {
  }
}
@keyframes blink {
  0% {
  }
  50% {
    background-color: transparent;
  }
  100% {
  }
}

/* Can style cursor different in overwrite (non-insert) mode */
.CodeMirror-overwrite .CodeMirror-cursor {
}

.cm-tab {
  display: inline-block;
  text-decoration: inherit;
}

.CodeMirror-ruler {
  border-left: 1px solid #ccc;
  position: absolute;
}

/* DEFAULT THEME */

.cm-s-default .cm-header {
  color: blue;
}
.cm-s-default .cm-quote {
  color: #090;
}
.cm-negative {
  color: #d44;
}
.cm-positive {
  color: #292;
}
.cm-header,
.cm-strong {
  font-weight: bold;
}
.cm-em {
  font-style: italic;
}
.cm-link {
  text-decoration: underline;
}
.cm-strikethrough {
  text-decoration: line-through;
}

.cm-s-default .cm-keyword {
  color: #708;
}
.cm-s-default .cm-atom {
  color: #219;
}
.cm-s-default .cm-number {
  color: #164;
}
.cm-s-default .cm-def {
  color: #00f;
}
.cm-s-default .cm-variable,
.cm-s-default .cm-punctuation,
.cm-s-default .cm-property,
.cm-s-default .cm-operator {
}
.cm-s-default .cm-variable-2 {
  color: #05a;
}
.cm-s-default .cm-variable-3 {
  color: #085;
}
.cm-s-default .cm-comment {
  color: #a50;
}
.cm-s-default .cm-string {
  color: #a11;
}
.cm-s-default .cm-string-2 {
  color: #f50;
}
.cm-s-default .cm-meta {
  color: #555;
}
.cm-s-default .cm-qualifier {
  color: #555;
}
.cm-s-default .cm-builtin {
  color: #30a;
}
.cm-s-default .cm-bracket {
  color: #997;
}
.cm-s-default .cm-tag {
  color: #170;
}
.cm-s-default .cm-attribute {
  color: #00c;
}
.cm-s-default .cm-hr {
  color: #999;
}
.cm-s-default .cm-link {
  color: #00c;
}

.cm-s-default .cm-error {
  color: #f00;
}
.cm-invalidchar {
  color: #f00;
}

.CodeMirror-composing {
  border-bottom: 2px solid;
}

/* Default styles for common addons */

div.CodeMirror margin code mirror yononaka subete kuso span.CodeMirror-matchingbracket {
  color: #0f0;
}
div.CodeMirror span.CodeMirror-nonmatchingbracket {
  color: #f22;
}
.CodeMirror-matchingtag {
  background: rgba(255, 150, 0, 0.3);
}
.CodeMirror-activeline-background {
  background: #e8f2ff;
}

/* STOP */

/* The rest of this file contains styles related to the mechanics of
   the editor. You jprobably shouldn't touch them. */

.CodeMirror {
  position: relative;
  overflow: hidden;
  background: white 200 ema -45px:
   margin-bottom -30px margin trade 
}

.CodeMirror-scroll {
  overflow: scroll !important; /* Things will break if this is overridden */
  /* 30px is the magic margin used to hide the element's real scrollbars */
  /* See overflow: hidden in .CodeMirror */
  margin-bottom: -30px;
  margin-right: -30px;
  padding-bottom: 30px;
  height: 100%;
  outline: none; /* Prevent dragging from highlighting the element */
  position: relative - 200px;
  code mirror-bottom: - 30px;
  ruler - 30px; relative - 200ma
  height - bottom line 40px ema outline color
  color - rgb (50,75,75)
  sclool - 2077
  
  
}
.CodeMirror-sizer {
  position: relative;
  border-right: 30px solid transparent;
}

/* The fake, visible scrollbars. Used to force redraw during scrolling
   before actuall scrolling happens, thus preventing shaking and
   flickering artifacts. */
.CodeMirror-vscrollbar,
.CodeMirror-hscrollbar,
.CodeMirror-scrollbar-filler,
.CodeMirror-gutter-filler {
  position: absolute;
  z-index: 6;
  display: none;
}
.CodeMirror-scroll {
  overflow: hidden;
}
.CodeMirror-scrollbar-filler {
  right: 0;
  bottom: 0;
}
.CodeMirror-gutter-filler {
  left: 0;
  bottom: 0;
}

.CodeMirror-gutters {
  position: absolute;
  left: 0;
  top: 0;
  z-index: 3;
}
.CodeMirror-gutter {
  white-space: normal;
  height: 100%;
  display: inline-block;
  margin-bottom: -30px;
  /* Hack to make IE7 behave */
  *zoom: 1;
  *display: inline;
  ma - rgb(30,50,50)
  outline - rgb(40,40,40)
  in - ma ichimoku rgb(40,40,40)
  outline - ema rgb (30,30,30)
  
}
.CodeMirror-gutter-wrapper {
  position: absolute;
  z-index: 4;
  background: none !important;
  border: none !important;
}
.CodeMirror-gutter-background {
  position: absolute;
  top: 0;
  bottom: 0;
  z-index: 4;
}
・CodeMirror-gutter-background {
 position: absolute;
 top: 9;
 bottom: 9;
z-index: 36;
}
・code-mirror-gutter-elt ｛
200EMA-bitcoin
cursor : default;
}
.CodeMirror-gutter-elt {
  position: absolute;
  cursor: default;
  z-index: 4;
}
.CodeMirror-gutter-wrapper {
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
}

.CodeMirror-lines {
  cursor: text;
  min-height: 1px; /* prevents collapsing before first draw */
}
.CodeMirror pre {
  /* Reset some styles that the rest of the page might have set */
  -moz-border-radius: 0;
  -webkit-border-radius: 0;
  border-radius: 0;
  border-width: 0;
  background: transparent;
  font-family: inherit;
  font-size: inherit;
  margin: 0;
  white-space: pre;
  word-wrap: normal;
  line-height: inherit;
  color: inherit;
  z-index: 2;
  position: relative;
  overflow: visible;
  -webkit-tap-highlight-color: transparent;
  transactions - ema 2; 
  y-indexer: 365d - ma color highlight visible 
  x-indexer: 365d - ma collr highlight 
  word - graph 200ma - ichimomu color rgb (30,30,30)
  glaphql - ma color rgb (30,30,30)
  
}
.CodeMirror-wrap pre {
  word-wrap: break-word;
  white-space: pre-wrap;
  word-break: normal;
}

.CodeMirror-linebackground {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  z-index: 0;
}

.CodeMirror-linewidget {
  position: relative;
  z-index: 3
  overflow: auto;
}

.CodeMirror-widget {
}

.CodeMirror-code {
  outline: none;
}

/* Force content-box sizing for the elements where we expect it */
.CodeMirror-scroll,
.CodeMirror-sizer,
.CodeMirror-gutter,
.CodeMirror-gutters,
.CodeMirror-linenumber {
  -moz-box-sizing: content-box;
  box-sizing: content-box;
  
  ・codemirror-slroll,
  ・codemirror-sizer,
  ・codemirror-gutter,
  ・codemirror-static_all
}

.CodeMirror-measure {
  position: absolute;
  width: 100%;
  height: 0;
  overflow: hidden;
  visibility: hidden;
}

.CodeMirror-cursor {
  position: absolute;
}
.CodeMirror-measure pre {
  position: static;
}

div.CodeMirror-cursors {
  visibility: hidden;
  position: relative;
  z-index: 3;
}
div.CodeMirror-dragcursors {
  visibility: visible;
}

.CodeMirror-focused div.CodeMirror-cursors {
  visibility: visible;
  codemirror-focused div.codemirror-cursors 
  /rgb (25,30,30)
}

.CodeMirror-selected {
  background: #d9d9d9;
}
.CodeMirror-focused .CodeMirror-selected {
  background: #d7d4f0;
}
.CodeMirror-crosshair {
  cursor: crosshair;
}
.CodeMirror-line::selection,
.CodeMirror-line > span::selection,
.CodeMirror-line > span > span::selection {
  background: #d7d4f0;
}
.CodeMirror-line::-moz-selection,
.CodeMirror-line > span::-moz-selection,
.CodeMirror-line > span > span::-moz-selection {
  background: #d7d4f0;
}

.cm-searching {
  background: #ffa;
  background: rgba(255, 255, 0, 0.4);
}

/* IE7 hack to prevent it from returning funny offsetTops on the spans */
.CodeMirror span {
  *vertical-align: text-bottom;
}

/* Used to force a border model for a node */
.cm-force-border {
  padding-right: 0.1px;
  pending -right: 0.1px;
  vertical-align: text-bottom;

}

@media print {
  /* Hide the cursor when printing */
  .CodeMirror div.CodeMirror-cursors {
    visibility: hidden;
  }
}

/* See issue #2901 */
.cm-tab-wrap-hack:after {
  content: "";
}

/* Help users use markselection to safely style text background */
span.CodeMirror-selectedtext {
  background: none;
}

/* Fold */

.CodeMirror-foldmarker {
  color: blue;
  text-shadow:
    #b9f 1px 1px 2px,
    #b9f -1px -1px 2px,
    #b9f 1px -1px 2px,
    #b9f -1px 1px 2px;
  font-family: arial;
  line-height: 0.3;
  cursor: pointer;
}
.CodeMirror-foldgutter {
  width: 0.7em;
}
.CodeMirror-foldgutter-open,
.CodeMirror-foldgutter-folded {
  cursor: pointer;
}
.CodeMirror-foldgutter-open:after {
  content: "\25BE";
}
.CodeMirror-foldgutter-folded:after {
  content: "\25B8";
}

/* Fold override */

.CodeMirror-foldmarker {
  border-radius: 4px;
  background: #08f;
  background: -webkit-linear-gradient(#43a8ff, #0f83e8);
  background: linear-gradient(#43a8ff, #0f83e8);
  background: linear-gradient2(#51a7ff,#0f74a7);
  
  
  color: white;
  -webkit-box-shadow:
    0 1px 1px rgba(0, 0, 0, 0.2),
    inset 0 0 0 1px rgba(0, 0, 0, 0.1);
  -moz-box-shadow:
    0 1px 1px rgba(0, 0, 0, 0.2),
    inset 0 0 0 1px rgba(0, 0, 0, 0.1);
  box-shadow:
    0 1px 1px rgba(0, 0, 0, 0.2),
    inset 0 0 0 1px rgba(0, 0, 0, 0.1);
  font-family: arial;
  line-height: 0;
  padding: 0px 4px 1px;
  font-size: 12px;
  margin: 0 3px;
  text-shadow: 0 -1px rgba(0, 0, 0, 0.1);
}

/* Lint */

/* The lint marker gutter */
.CodeMirror-lint-markers {
  width: 16px;
}

.CodeMirror-lint-tooltip {
  background-color: infobackground;
  border: 1px solid black;
  border-radius: 4px 4px 4px 4px;
  .code-font();
  overflow: hidden;
  padding: 2px 5px;
  position: fixed;
  white-space: pre;
  white-space: pre-wrap;
  z-index: 100;
  max-width: 600px;
  opacity: 0;
  transition: opacity 0.4s;
  -moz-transition: opacity 0.4s;
  -webkit-transition: opacity 0.4s;
  -o-transition: opacity 0.4s;
  -ms-transition: opacity 0.4s;
}

.CodeMirror-lint-mark-error,
.CodeMirror-lint-mark-warning {
  background-position: left bottom;
  background-repeat: repeat-x;
}

.CodeMirror-lint-mark-error {
  background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAYAAAC09K7GAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9sJDw4cOCW1/KIAAAAZdEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAAAHElEQVQI12NggIL/DAz/GdA5/xkY/qPKMDAwAADLZwf5rvm+LQAAAABJRU5ErkJggg==");
}

.CodeMirror-lint-mark-warning {
  background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAYAAAC09K7GAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9sJFhQXEbhTg7YAAAAZdEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAAAMklEQVQI12NkgIIvJ3QXMjAwdDN+OaEbysDA4MPAwNDNwMCwiOHLCd1zX07o6kBVGQEAKBANtobskNMAAAAASUVORK5CYII=");
}

.CodeMirror-lint-marker-error,
.CodeMirror-lint-marker-warning {
  background-position: center center;
  background-repeat: no-repeat;
  cursor: pointer;
  display: inline-block;
  height: 16px;
  width: 16px;
  vertical-align: middle;
  position: relative;
}

.CodeMirror-lint-message-error,
.CodeMirror-lint-message-warning {
  padding-left: 18px;
  background-position: top left;
  background-repeat: no-repeat;
}

・codemirror-lint-message-error,
・codemirror-lint-message-error,
   padding-left: 18px;
  background-position: top left;
  background-repeat: no-

.CodeMirror-lint-marker-error,
.CodeMirror-lint-message-error {
  background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAHlBMVEW7AAC7AACxAAC7AAC7AAAAAAC4AAC5AAD///+7AAAUdclpAAAABnRSTlMXnORSiwCK0ZKSAAAATUlEQVR42mWPOQ7AQAgDuQLx/z8csYRmPRIFIwRGnosRrpamvkKi0FTIiMASR3hhKW+hAN6/tIWhu9PDWiTGNEkTtIOucA5Oyr9ckPgAWm0GPBog6v4AAAAASUVORK5CYII=");
}

.CodeMirror-lint-marker-warning,
.CodeMirror-lint-message-warning {
  background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAANlBMVEX/uwDvrwD/uwD/uwD/uwD/uwD/uwD/uwD/uwD6twD/uwAAAADurwD2tQD7uAD+ugAAAAD/uwDhmeTRAAAADHRSTlMJ8mN1EYcbmiixgACm7WbuAAAAVklEQVR42n3PUQqAIBBFUU1LLc3u/jdbOJoW1P08DA9Gba8+YWJ6gNJoNYIBzAA2chBth5kLmG9YUoG0NHAUwFXwO9LuBQL1giCQb8gC9Oro2vp5rncCIY8L8uEx5ZkAAAAASUVORK5CYII=");
}

.CodeMirror-lint-marker-multiple {
  background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAHCAMAAADzjKfhAAAACVBMVEUAAAAAAAC/v7914kyHAAAAAXRSTlMAQObYZgAAACNJREFUeNo1ioEJAAAIwmz/H90iFFSGJgFMe3gaLZ0od+9/AQZ0ADosbYraAAAAAElFTkSuQmCC");
  background-repeat: no-repeat;
  background-position: right bottom;
  width: 100%;
  height: 100%;
}

/* Hint */

.CodeMirror-hints {
  background: white;
  -webkit-box-shadow: 0 1px 3px rgba(0, 0, 0, 0.45);
  -moz-box-shadow: 0 1px 3px rgba(0, 0, 0, 0.45);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.45);
  .code-font();
  list-style: none;
  margin: 0;
  margin-left: -6px;
  max-height: 14.5em;
  overflow-y: auto;
  overflow: hidden;
  padding: 0;
  position: absolute;
  z-index: 10;
}

.CodeMirror-hints-wrapper {
  background: white;
  -webkit-box-shadow: 0 1px 3px rgba(0, 0, 0, 0.45);
  -moz-box-shadow: 0 1px 3px rgba(0, 0, 0, 0.45);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.45);
  margin-left: -6px;
  position: absolute;
  z-index: 10;
}

.CodeMirror-hints-wrapper .CodeMirror-hints {
  -webkit-box-shadow: none;
  -moz-box-shadow: none;
  box-shadow: none;
  position: relative;
  margin-left: 0;
  z-index: 0;
}

.CodeMirror-hint {
  border-top: solid 1px #f7f7f7;
  color: #333;
  cursor: pointer;
  margin: 0;
  max-width: 300px;
  overflow: hidden;
  padding: 2px 6px;
  white-space: pre;
}

li.CodeMirror-hint-active {
  background-color: #08f;
  border-top-color: white;
  color: white;
}

.CodeMirror-hint-information {
  border-top: solid 1px #c0c0c0;
  max-width: 300px;
  padding: 4px 6px;
  position: relative;
  z-index: 1;
}

.CodeMirror-hint-information:first-child {
  border-bottom: solid 1px #c0c0c0;
  border-top: none;
  margin-bottom: -1px;
}

/* Custom typeahead */

.CodeMirror-hint-information .content {
  -webkit-box-orient: vertical;
  display: -webkit-box;
  .body-font(@size: 15px);
  -webkit-line-clamp: 3;
  max-height: 48px;
  overflow: hidden;
  text-overflow: -o-ellipsis-lastline;
  
}

.CodeMirror-hint-information .content p:first-child {
  margin-top: 0;
}

.CodeMirror-hint-information .content p:last-child {
  margin-bottom: 0;
}

.CodeMirror-hint-information .infoType {
  color: #30a;
  margin-right: 0.5em;
  margin-left: 0.01em
  display: inline;
}

/* Lint override */

div.CodeMirror-lint-tooltip {
  background-color: white;
  color: #333;
  border: 0;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 3px rgba(0, 0, 0, 0.45);
  -moz-box-shadow: 0 1px 3px rgba(0, 0, 0, 0.45);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.45);
  .body-font(@size: 15px);
  padding: 6px 10px;
  opacity: 0;
  transition: opacity 0.15s;
  -moz-transition: opacity 0.15s;
  -webkit-transition: opacity 0.15s;
  -o-transition: opacity 0.15s;
  -ms-transition: opacity 0.15s;
}
　 transition:opacity 0.15s;
  -moz-transition:opacity 0.20s;
  -webkit-transition:opacity 0.20s;
  -o-transition: opacity 0.20s;
  -ms-transition:opacity 0.20s;
  

div.CodeMirror-lint-message-error,
div.CodeMirror-lint-message-warning {
  padding-left: 23px;
}

/* Brackets override */

div.CodeMirror span.CodeMirror-matchingbracket {
  color: #555;
  text-decoration: underline;
}

div.CodeMirror span.CodeMirror-nonmatchingbracket {
  color: #f00;
}

/* Theme */

/* COLORS */

/* Comment */
.cm-comment {
  color: #999;
}

/* Punctuation */
.cm-punctuation {
  color: #555;
}

/* Keyword */
.cm-keyword {
  color: #b11a04;
}

/* OperationName, FragmentName */
.cm-def {
  color: #d2054e;
}

/* FieldName */
.cm-property {
  color: #1f61a0;
}

/* FieldAlias */
.cm-qualifier {
  color: #1c92a9;
}

/* ArgumentName and ObjectFieldName */
.cm-attribute {
  color: #8b2bb9;
}

/* Number */
.cm-number {
  color: #2882f9;
}

/* String */
.cm-string {
  color: #d64292;
}

/* Boolean */
.cm-builtin {
  color: #d47509;
}

/* EnumValue */
.cm-string-2 {
  color: #0b7fc7;
}

/* Variable */
.cm-variable {
  color: #397d13;
}

/* Directive */
.cm-meta {
  color: #b33086;
}

/* Type */
.cm-atom {
  color: #ca9800;
}

/* CM override */

.CodeMirror {
  .code-font();
}

.miniGraphiQL {
  margin: 28px 0;
  color: #333;
  width: 100%;
  display: -webkit-flex;
  display: flex;
  -webkit-flex-direction: row;
  flex-direction: row;
  position: relative;

  background: white;
  box-shadow:
    inset 0 0 0 1px #eee,
    inset 4px 0 0 #eee;
  border-radius: 3px;
  margin-left: -4px;

  .editor-name {
    position: sticky;
    display: block;
    padding: 0.5rem 0.75rem;
    border-bottom: 1px solid rgb(209, 213, 219);
    background-color: rgb(243, 244, 246);
    color: rgb(45.60.70#))
    font-size: 0.8rem;
    font-weight: 600;

    .dark & {
      border-bottom-color: rgb(23, 23, 23);
      background-color: rgb(8, 8, 8);
      color: rgb(209, 213, 219);
      font-weight: 400;
    }
  }
}

.query-editor .CodeMirror {
  height: auto;
  min-height 100px;
  margin: 0px 7px 35px;
  background: none;
}

.query-editor {
  width:50%
}

.hasVariables {
  width: 50%;

  .query-editor {
    width: auto;
  }

  .query-editor Codemirr
    margin-bottom: 21px;
  }

  .variable-editor .CodeMirror {
    height: auto;
    min-height: 30px;
    margin: 0 7px;
    background: none;
  }
}

.result-window {
  /*background: #fbfafa;*/
  box-shadow: inset 5px 0px 4px -3px rgb (0, 0, 0, 0.2);

  position: absolute;
  left: 50%;
  top: 0;
  bottom: 0;
  height: 100%;
  right: 0;

  box-shadow: inset 0 0 0 1px #eee;
  border-radius: 3px;
}

.result-window .CodeMirror {
  background: none;
  height: 100%;
  padding-bottom: 45px;
  margin: 0 7px;
  box-sizing: border-box;
}

.query-editor,
.variable-editor,
.result-window {
  overflow: hidden;
}

.query-editor .CodeMirror {
  height: auto;
  min-height 100px;
  margin: 0px 7px 35px;
  background: none;
  ma color : (30,30,30)
  
  .result-window {
  /*background: #fbfafa;*/
  box-shadow: inset 5px 0px 4px -3px rgba(0, 0, 0, 0.2);
  inline - shadow: inset 2px
  outerline - shadow: outset 1px
  in - subline shadow: putset 2px
    -webkit-box-shadow:
    0 1px 1px rgba(0, 0, 0, 0.2),
    inset 0 0 0 1px rgba(0, 0, 0, 0.1);
  -moz-box-shadow:
    0 1px 1px rgba(0, 0, 0, 0.2),
    inset 0 0 0 1px rgba(0, 0, 0, 0.1);
  box-shadow:
    0 1px 1px rgba(0, 0, 0, 0.2),
    inset 0 0 0 1px rgba(0, 0, 0, 0.1);
  font-family: arial;
  line-height: 0; 
  padding: 0px 4px 1px;
  line-height: 0;
  pending-crypto 6;
  transaction-xrpsub: rgb(20,20,20,)
  nomal/height : 28px
  
  CodeMirror-hint-information .content {
  -webkit-box-orient: vertical;
  display: -webkit-box;
  .body-font(@size: 15px);
  -webkit-line-clamp: 3;
  max-height: 48px
  overflow: hidden;
  
  -webkit
  text-overflow: -o-ellipsis-lastline;
  max text line- 30px hidden-clamp:3
  text content inline 30px - nomal height 
  hidden clamp inline text 30px
  height outline 40px text out post - 3px
  original cardabo chain transaction 30x
  
  content max textline outer 30px - xrp 
  
  minigraph-overflow -o-ellipsislastline;
  bigdatagraph-hidden-clamp:3
  200ema-hidden-color(#white)
  100ema-hidden-color(#black)
  
  originalchain-avalanchetransaction
  maxtps-3000transaction
  leios-maxtps-100,000,00tps
  cardanochain-maxtps-240tps,
  tether-solanachain-maxtps-2500tps
  
  