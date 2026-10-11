import { jsxs as S, jsx as i, Fragment as re } from "react/jsx-runtime";
import { useState as $, useRef as V, useCallback as me, useEffect as L, useMemo as Pe } from "react";
import { settings as K, extension as Q, INTERNAL_SYSTEM_SLOT as P, Extension as Z, useExtensionContext as ee, defineSave as Ut, method as X } from "@avg-studio/sdk";
const Re = 2, Le = "剧情选项", Ae = {
  width: 1920,
  height: 1080
}, ze = [
  {
    id: "choice-dialog-list",
    refId: "choice-list",
    type: "choice-list",
    name: "选项列表_故事分支",
    rect: {
      x: 500,
      y: 335,
      w: 920,
      h: 410
    },
    anchor: "c",
    style: {
      fontSize: 26,
      fontWeight: 500,
      letterSpacing: 0.4,
      color: "#e8f1f0",
      fill: "transparent",
      borderColor: "transparent",
      borderWidth: 0,
      radius: 14,
      opacity: 100,
      customCss: 'font-family: "Plus Jakarta Sans", "M PLUS Rounded 1c", "PingFang SC", "Hiragino Sans GB", "HarmonyOS Sans", "Microsoft YaHei", -apple-system, BlinkMacSystemFont, sans-serif;'
    },
    animation: {
      enter: {
        preset: "rise",
        durationMs: 420,
        delayMs: 90
      },
      exit: {
        preset: "fade",
        durationMs: 190,
        delayMs: 0
      }
    },
    props: {
      choiceTemplateSchema: "avg.visual-ui.choice/v1",
      direction: "vertical",
      gap: 14,
      bgImage: "",
      previewChoices: [
        "继续追问她",
        "保持沉默",
        "转身离开"
      ],
      previewDisabledIndex: 2
    }
  },
  {
    id: "choice-dialog-item",
    type: "choice-item",
    name: "选项按钮框体_模板",
    rect: {
      x: 504,
      y: 412,
      w: 912,
      h: 76
    },
    anchor: "c",
    style: {
      fill: "rgba(7, 16, 24, 0.86)",
      borderColor: "rgba(127, 212, 200, 0.36)",
      borderWidth: 1,
      radius: 14,
      opacity: 100
    },
    props: {
      choiceListId: "choice-dialog-list",
      hoverSound: "",
      clickSound: "",
      itemImage: "",
      itemHoverImage: "",
      itemPressedImage: "",
      itemDisabledImage: "",
      hoverFill: "rgba(20, 48, 54, 0.94)",
      pressedFill: "rgba(82, 184, 168, 0.24)",
      disabledFill: "rgba(6, 12, 18, 0.58)",
      focusColor: "#7fd4c8"
    }
  },
  {
    id: "choice-dialog-indicator",
    type: "choice-indicator",
    name: "选项强调线_模板",
    rect: {
      x: 505,
      y: 424,
      w: 3,
      h: 52
    },
    anchor: "c",
    style: {
      fill: "#7fd4c8",
      radius: 999,
      opacity: 46,
      customCss: "border-radius: 0 999px 999px 0 !important;"
    },
    props: {
      choiceListId: "choice-dialog-list",
      hoverOpacity: 100,
      pressedOpacity: 100,
      disabledOpacity: 20,
      glow: 14
    }
  },
  {
    id: "choice-dialog-number",
    type: "choice-number",
    name: "选项序号_模板",
    rect: {
      x: 535,
      y: 413,
      w: 34,
      h: 74
    },
    anchor: "c",
    style: {
      fontFamily: '"SFMono-Regular", Consolas, monospace',
      fontSize: 15.08,
      fontWeight: 700,
      letterSpacing: 1.8,
      color: "#7fd4c8",
      opacity: 62,
      textAlign: "left"
    },
    props: {
      choiceListId: "choice-dialog-list",
      numberFormat: "leading-zero",
      numberStart: 1,
      numberPrefix: "",
      numberSuffix: "",
      hoverColor: "#7fd4c8",
      pressedColor: "#7fd4c8",
      disabledColor: "#7fd4c8",
      hoverOpacity: 100,
      pressedOpacity: 100,
      disabledOpacity: 20
    }
  },
  {
    id: "choice-dialog-text",
    type: "choice-text",
    name: "选项正文_模板",
    rect: {
      x: 587,
      y: 413,
      w: 800,
      h: 74
    },
    anchor: "c",
    style: {
      fontFamily: '"PingFang SC", "Microsoft YaHei", sans-serif',
      fontSize: 26,
      fontWeight: 500,
      letterSpacing: 0.4,
      color: "#e8f1f0",
      opacity: 100,
      textAlign: "left"
    },
    props: {
      choiceListId: "choice-dialog-list",
      hoverColor: "#f5fffd",
      pressedColor: "#ffffff",
      disabledColor: "rgba(190, 205, 203, 0.38)",
      lineHeight: 1.45
    }
  }
], Xt = {
  version: Re,
  name: Le,
  canvas: Ae,
  elements: ze
}, qt = /* @__PURE__ */ Object.freeze(/* @__PURE__ */ Object.defineProperty({
  __proto__: null,
  canvas: Ae,
  default: Xt,
  elements: ze,
  name: Le,
  version: Re
}, Symbol.toStringTag, { value: "Module" })), Ee = 2, We = "对话框", Be = {
  width: 1920,
  height: 1080
}, De = [
  {
    id: "dialogue-backdrop",
    refId: "dialogue-backdrop",
    type: "dialogue-backdrop",
    name: "舞台遮罩",
    rect: {
      x: 0,
      y: 0,
      w: 1920,
      h: 1080
    },
    anchor: "c",
    style: {
      fill: "#000000",
      opacity: 0
    },
    props: {}
  },
  {
    id: "dialogue-frame",
    refId: "dialogue-frame",
    type: "dialogue-frame",
    name: "框体背景",
    rect: {
      x: 0,
      y: 880,
      w: 1920,
      h: 200
    },
    anchor: "tl",
    style: {
      fill: "transparent",
      borderColor: "transparent",
      borderWidth: 0,
      radius: 0,
      opacity: 100
    },
    props: {
      runtimeOverride: !0,
      backgroundImage: "",
      backgroundImageFit: "stretch",
      backgroundImagePosition: "center",
      backgroundImageRepeat: "no-repeat",
      linearGradient: {
        enabled: !0,
        angle: 0,
        startColor: "rgba(0,0,0,0.75)",
        endColor: "rgba(0,0,0,0.3)"
      },
      frameDecoration: {
        borderTop: "1px solid rgba(255,255,255,0.12)",
        borderRight: "",
        borderBottom: "",
        borderLeft: "",
        borderRadius: "",
        boxShadow: ""
      }
    }
  },
  {
    id: "dialogue-text",
    refId: "dialogue-text",
    type: "dialogue-text",
    name: "对白文本",
    rect: {
      x: 200,
      y: 900,
      w: 1520,
      h: 180
    },
    anchor: "tl",
    style: {
      fontFamily: "'Source Han Sans', 'PingFang SC', sans-serif",
      fontSize: 30,
      fontWeight: 500,
      color: "#f3ede2",
      letterSpacing: 1.2,
      textAlign: "left",
      opacity: 100
    },
    props: {
      lineHeight: 1.75,
      textShadows: [
        {
          offsetX: 0,
          offsetY: 0,
          blur: 1.5,
          color: "rgba(0,0,0,0.95)"
        },
        {
          offsetX: 0,
          offsetY: 0,
          blur: 3,
          color: "rgba(0,0,0,0.7)"
        },
        {
          offsetX: 1,
          offsetY: 2,
          blur: 4,
          color: "rgba(0,0,0,0.6)"
        }
      ],
      previewText: `有些故事，会从一个看似普通的夜晚开始。
而我们，刚好站在它的入口。`
    }
  },
  {
    id: "dialogue-name",
    refId: "dialogue-name",
    type: "dialogue-name",
    name: "角色名",
    rect: {
      x: 200,
      y: 840,
      w: 384,
      h: 40
    },
    anchor: "tl",
    style: {
      fontFamily: "'Source Han Sans', 'PingFang SC', sans-serif",
      fontSize: 34,
      fontWeight: 600,
      color: "#ffd88a",
      fill: "transparent",
      borderColor: "transparent",
      borderWidth: 0,
      radius: 0,
      letterSpacing: 1.36,
      textAlign: "left",
      opacity: 100
    },
    props: {
      backgroundImage: "",
      backgroundImageFit: "stretch",
      backgroundImagePosition: "center",
      backgroundImageRepeat: "no-repeat",
      linearGradient: {
        enabled: !1,
        angle: 180,
        startColor: "transparent",
        endColor: "transparent"
      },
      frameDecoration: {
        borderTop: "",
        borderRight: "",
        borderBottom: "",
        borderLeft: "",
        borderRadius: "",
        boxShadow: ""
      },
      lineHeight: 1.5,
      textShadows: [
        {
          offsetX: 0,
          offsetY: 0,
          blur: 1.5,
          color: "rgba(0,0,0,0.95)"
        },
        {
          offsetX: 0,
          offsetY: 0,
          blur: 3,
          color: "rgba(0,0,0,0.7)"
        },
        {
          offsetX: 1,
          offsetY: 2,
          blur: 4,
          color: "rgba(0,0,0,0.6)"
        }
      ],
      previewName: "小满"
    }
  },
  {
    id: "dialogue-wait-cursor",
    refId: "dialogue-wait-cursor",
    type: "dialogue-wait-cursor",
    name: "等待提示",
    rect: {
      x: 1546.4,
      y: 965.6,
      w: 28,
      h: 28
    },
    anchor: "tl",
    style: {
      color: "#ffffff",
      opacity: 100
    },
    props: {
      fixedDefaultRect: {
        x: 1546.4,
        y: 965.6,
        w: 28,
        h: 28
      },
      source: "legacy",
      imageAsset: "",
      shape: "diamond",
      accentColor: "#ff3d00",
      animation: "rotate",
      durationMs: 1e3
    }
  }
], je = {
  text_speed: 30
}, Jt = {
  version: Ee,
  name: We,
  canvas: Be,
  elements: De,
  dialogueBehavior: je
}, Kt = /* @__PURE__ */ Object.freeze(/* @__PURE__ */ Object.defineProperty({
  __proto__: null,
  canvas: Be,
  default: Jt,
  dialogueBehavior: je,
  elements: De,
  name: We,
  version: Ee
}, Symbol.toStringTag, { value: "Module" })), He = 2, Ve = "鉴赏界面", Ye = {
  width: 1920,
  height: 1080
}, Ge = {
  enter: {
    preset: "fade",
    durationMs: 320,
    delayMs: 0
  },
  exit: {
    preset: "fade",
    durationMs: 240,
    delayMs: 0
  }
}, Ne = [
  {
    id: "mask",
    type: "rect",
    name: "遮罩",
    rect: {
      x: 0,
      y: 0,
      w: 1920,
      h: 1080
    },
    anchor: "c",
    style: {
      fill: "rgba(7, 10, 8, 0.94)",
      radius: 0,
      backdropBlur: 28,
      opacity: 100,
      customCss: "background-image: radial-gradient(ellipse 70% 65% at 72% -5%, rgba(171,111,36,0.19), transparent 60%), radial-gradient(ellipse 55% 50% at 0% 100%, rgba(70,88,58,0.2), transparent 68%), repeating-linear-gradient(0deg, rgba(226,221,191,0.018) 0 1px, transparent 1px 5px), linear-gradient(135deg, rgba(21,28,21,0.98), rgba(5,8,6,0.98));"
    },
    animation: {
      enter: {
        preset: "fade",
        durationMs: 420,
        delayMs: 0
      },
      exit: {
        preset: "fade",
        durationMs: 220,
        delayMs: 80
      }
    }
  },
  {
    id: "grid-overlay",
    type: "rect",
    name: "装饰_坐标网格",
    rect: {
      x: 0,
      y: 0,
      w: 1920,
      h: 1080
    },
    anchor: "c",
    style: {
      fill: "transparent",
      radius: 0,
      opacity: 100,
      customCss: "background-image: linear-gradient(rgba(227,166,75,0.025) 1px, transparent 1px), linear-gradient(90deg, rgba(227,166,75,0.025) 1px, transparent 1px); background-size: 64px 64px; mask-image: linear-gradient(to bottom, black, transparent 78%);"
    },
    animation: {
      enter: {
        preset: "fade",
        durationMs: 520,
        delayMs: 40
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 40
      }
    }
  },
  {
    id: "eyebrow",
    type: "text",
    name: "文字_档案编号",
    rect: {
      x: 104,
      y: 72,
      w: 680,
      h: 24
    },
    anchor: "tl",
    style: {
      fontSize: 13,
      color: "#e3a64b",
      letterSpacing: 5,
      fontWeight: 700,
      fontFamily: '"JetBrains Mono", "SF Mono", "Menlo", monospace',
      opacity: 100,
      customCss: "text-transform: uppercase; text-shadow: 0 0 14px rgba(227,166,75,0.25);"
    },
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 360,
        delayMs: 70
      },
      exit: {
        preset: "fade",
        durationMs: 140,
        delayMs: 40
      }
    },
    props: {
      text: "ARCHIVE 03 / RECOVERED MATERIALS"
    }
  },
  {
    id: "title",
    type: "text",
    name: "文字_鉴赏档案库",
    rect: {
      x: 100,
      y: 102,
      w: 820,
      h: 72
    },
    anchor: "tl",
    style: {
      fontSize: 50,
      color: "#e7e7da",
      letterSpacing: 2,
      fontWeight: 760,
      fontFamily: '"M PLUS Rounded 1c", "PingFang SC", "Microsoft YaHei", sans-serif',
      opacity: 100,
      customCss: "text-shadow: 0 4px 26px rgba(0,0,0,0.6);"
    },
    animation: {
      enter: {
        preset: "rise",
        durationMs: 440,
        delayMs: 105
      },
      exit: {
        preset: "sink",
        durationMs: 200,
        delayMs: 20
      }
    },
    props: {
      text: "鉴赏档案库"
    }
  },
  {
    id: "status",
    type: "text",
    name: "文字_终端状态",
    rect: {
      x: 1270,
      y: 86,
      w: 470,
      h: 56
    },
    anchor: "tr",
    style: {
      fontSize: 11,
      color: "rgba(215,218,202,0.52)",
      letterSpacing: 3,
      textAlign: "right",
      fontFamily: '"JetBrains Mono", "SF Mono", monospace',
      opacity: 100,
      customCss: "line-height: 1.8;"
    },
    animation: {
      enter: {
        preset: "fade",
        durationMs: 380,
        delayMs: 170
      },
      exit: {
        preset: "fade",
        durationMs: 140,
        delayMs: 0
      }
    },
    props: {
      text: `TERMINAL ONLINE  ●
CLEARANCE / SURVIVOR`
    }
  },
  {
    id: "close-btn",
    type: "button",
    name: "按钮_关闭当前界面",
    rect: {
      x: 1760,
      y: 84,
      w: 52,
      h: 52
    },
    anchor: "tr",
    style: {
      fontSize: 21,
      color: "#e3a64b",
      fill: "rgba(227,166,75,0.055)",
      borderColor: "rgba(227,166,75,0.32)",
      borderWidth: 1,
      radius: 4,
      opacity: 100,
      customCss: "box-shadow: inset 0 0 0 3px rgba(7,10,8,0.8), 0 8px 24px rgba(0,0,0,0.4); transition: background .16s, border-color .16s, transform .16s; &:hover { background: rgba(227,166,75,0.14); border-color: rgba(227,166,75,0.75); transform: rotate(90deg); }"
    },
    animation: {
      enter: {
        preset: "scale",
        durationMs: 300,
        delayMs: 190
      },
      exit: {
        preset: "shrink",
        durationMs: 160,
        delayMs: 0
      }
    },
    props: {
      text: "×"
    },
    events: {
      onClick: {
        type: "ui.close"
      }
    }
  },
  {
    id: "gallery-tabs",
    type: "tabs",
    name: "页签_CG音乐片段",
    rect: {
      x: 100,
      y: 190,
      w: 1040,
      h: 64
    },
    anchor: "t",
    style: {
      fontSize: 17,
      color: "#f0eadb",
      borderColor: "#e3a64b",
      letterSpacing: 3,
      radius: 0,
      opacity: 100,
      customCss: "& [data-visual-ui-tabs-bar] { border-bottom-color: rgba(227,166,75,0.18) !important; }"
    },
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 420,
        delayMs: 180
      },
      exit: {
        preset: "fade",
        durationMs: 180,
        delayMs: 20
      }
    },
    props: {
      tabs: [
        "影像档案",
        "音频信号",
        "剧情记录"
      ],
      activeIndex: 0,
      inactiveColor: "rgba(240,234,219,0.55)",
      gap: 6
    }
  },
  {
    id: "tab-hint",
    type: "text",
    name: "文字_页签提示",
    rect: {
      x: 1260,
      y: 211,
      w: 550,
      h: 28
    },
    anchor: "tr",
    style: {
      fontSize: 10,
      color: "rgba(209,213,197,0.4)",
      letterSpacing: 3,
      textAlign: "right",
      fontFamily: '"JetBrains Mono", monospace',
      opacity: 100
    },
    animation: {
      enter: {
        preset: "fade",
        durationMs: 320,
        delayMs: 240
      },
      exit: {
        preset: "fade",
        durationMs: 140,
        delayMs: 0
      }
    },
    props: {
      text: "SELECT ARCHIVE TYPE / 点击页签切换鉴赏模式"
    }
  },
  {
    id: "cg-gallery",
    type: "cg-gallery",
    name: "智能组件_CG鉴赏",
    rect: {
      x: 100,
      y: 286,
      w: 1712,
      h: 680
    },
    anchor: "c",
    style: {
      radius: 6,
      opacity: 100
    },
    animation: {
      enter: {
        preset: "rise",
        durationMs: 520,
        delayMs: 240
      },
      exit: {
        preset: "sink",
        durationMs: 240,
        delayMs: 0
      }
    },
    props: {
      sharedSource: "ext:avg.internal.default-shell.unlockedShared",
      slotSource: "ext:avg.internal.default-shell.unlockedSlot",
      cols: 4,
      rows: 2,
      gap: 20,
      emptyText: "尚未回收任何影像档案",
      accentColor: "#e3a64b"
    },
    tab: {
      of: "gallery-tabs",
      index: 0
    }
  },
  {
    id: "music-gallery",
    type: "music-gallery",
    name: "智能组件_音乐鉴赏",
    rect: {
      x: 100,
      y: 286,
      w: 1712,
      h: 680
    },
    anchor: "c",
    style: {
      radius: 6,
      opacity: 100
    },
    animation: {
      enter: {
        preset: "rise",
        durationMs: 520,
        delayMs: 240
      },
      exit: {
        preset: "sink",
        durationMs: 240,
        delayMs: 0
      }
    },
    props: {
      sharedSource: "ext:avg.internal.default-shell.unlockedMusicShared",
      slotSource: "ext:avg.internal.default-shell.unlockedMusicSlot",
      emptyText: "尚未截获任何音频信号",
      accentColor: "#e3a64b",
      showArtist: !0,
      showDescription: !0
    },
    tab: {
      of: "gallery-tabs",
      index: 1
    }
  },
  {
    id: "fragment-gallery",
    type: "fragment-gallery",
    name: "智能组件_片段鉴赏",
    rect: {
      x: 100,
      y: 286,
      w: 1712,
      h: 680
    },
    anchor: "c",
    style: {
      radius: 6,
      opacity: 100
    },
    animation: {
      enter: {
        preset: "rise",
        durationMs: 520,
        delayMs: 240
      },
      exit: {
        preset: "sink",
        durationMs: 240,
        delayMs: 0
      }
    },
    props: {
      sharedSource: "ext:avg.internal.default-shell.unlockedFragmentsShared",
      slotSource: "ext:avg.internal.default-shell.unlockedFragmentsSlot",
      cols: 3,
      rows: 2,
      gap: 20,
      emptyText: "尚未解密任何剧情记录",
      accentColor: "#e3a64b",
      showDescription: !0
    },
    tab: {
      of: "gallery-tabs",
      index: 2
    }
  },
  {
    id: "footer-left",
    type: "text",
    name: "文字_底部操作提示",
    rect: {
      x: 102,
      y: 1006,
      w: 680,
      h: 22
    },
    anchor: "bl",
    style: {
      fontSize: 10,
      color: "rgba(211,215,200,0.38)",
      letterSpacing: 2,
      fontFamily: '"JetBrains Mono", monospace',
      opacity: 100
    },
    animation: {
      enter: {
        preset: "fade",
        durationMs: 320,
        delayMs: 360
      },
      exit: {
        preset: "fade",
        durationMs: 120,
        delayMs: 0
      }
    },
    props: {
      text: "ESC / MIDDLE CLICK  返回上一级"
    }
  },
  {
    id: "footer-right",
    type: "text",
    name: "文字_档案权限",
    rect: {
      x: 1230,
      y: 1006,
      w: 580,
      h: 22
    },
    anchor: "br",
    style: {
      fontSize: 10,
      color: "rgba(227,166,75,0.46)",
      letterSpacing: 3,
      textAlign: "right",
      fontFamily: '"JetBrains Mono", monospace',
      opacity: 100
    },
    animation: {
      enter: {
        preset: "fade",
        durationMs: 320,
        delayMs: 390
      },
      exit: {
        preset: "fade",
        durationMs: 120,
        delayMs: 0
      }
    },
    props: {
      text: "PROPERTY OF SHELTER NETWORK / LEVEL 03"
    }
  }
], Qt = {
  version: He,
  name: Ve,
  canvas: Ye,
  transition: Ge,
  elements: Ne
}, Zt = /* @__PURE__ */ Object.freeze(/* @__PURE__ */ Object.defineProperty({
  __proto__: null,
  canvas: Ye,
  default: Qt,
  elements: Ne,
  name: Ve,
  transition: Ge,
  version: He
}, Symbol.toStringTag, { value: "Module" })), Ue = 1, Xe = "历史记录", qe = {
  width: 1920,
  height: 1080
}, Je = {
  exit: {
    preset: "fade",
    durationMs: 280,
    delayMs: 0
  }
}, Ke = [
  {
    id: "mask",
    type: "rect",
    name: "遮罩",
    rect: {
      x: 0,
      y: 0,
      w: 1920,
      h: 1080
    },
    anchor: "c",
    style: {
      fill: "rgba(8, 13, 20, 0.88)",
      radius: 0,
      backdropBlur: 28,
      opacity: 100,
      customCss: "background-image: radial-gradient(ellipse 110% 85% at 18% 0%, rgba(40,70,100,0.36), transparent 58%), linear-gradient(115deg, rgba(127,212,200,0.025), transparent 45%);"
    },
    animation: {
      enter: {
        preset: "fade",
        durationMs: 420,
        delayMs: 0
      },
      exit: {
        preset: "fade",
        durationMs: 260,
        delayMs: 80
      }
    }
  },
  {
    id: "eyebrow",
    type: "text",
    name: "文字_Narrative_Log",
    rect: {
      x: 120,
      y: 96,
      w: 560,
      h: 24
    },
    anchor: "tl",
    style: {
      fontSize: 15,
      color: "#7fd4c8",
      letterSpacing: 5,
      fontFamily: '"JetBrains Mono", "SF Mono", "Menlo", monospace',
      opacity: 100,
      customCss: "text-transform: uppercase; text-shadow: 0 0 12px rgba(127,212,200,0.4);"
    },
    props: {
      text: "Narrative Log"
    },
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 360,
        delayMs: 80
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 60
      }
    }
  },
  {
    id: "title",
    type: "text",
    name: "文字_历史记录",
    rect: {
      x: 118,
      y: 122,
      w: 800,
      h: 80
    },
    anchor: "tl",
    style: {
      fontSize: 56,
      color: "#e8edf2",
      letterSpacing: 2,
      fontFamily: '"M PLUS Rounded 1c", "Plus Jakarta Sans", "PingFang SC", "Microsoft YaHei", sans-serif',
      opacity: 100
    },
    props: {
      text: "历史记录"
    },
    animation: {
      enter: {
        preset: "rise",
        durationMs: 460,
        delayMs: 120
      },
      exit: {
        preset: "sink",
        durationMs: 220,
        delayMs: 40
      }
    }
  },
  {
    id: "title-accent",
    type: "rect",
    name: "玉青短横线",
    rect: {
      x: 120,
      y: 212,
      w: 72,
      h: 4
    },
    anchor: "tl",
    style: {
      fill: "#7fd4c8",
      radius: 999,
      opacity: 100,
      customCss: "background-image: linear-gradient(90deg, #7fd4c8, #5eb8d4); box-shadow: 0 0 14px rgba(94,184,212,0.5);"
    },
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 420,
        delayMs: 190
      },
      exit: {
        preset: "shrink",
        durationMs: 180,
        delayMs: 20
      }
    }
  },
  {
    id: "hint",
    type: "text",
    name: "文字_回看说明",
    rect: {
      x: 1320,
      y: 172,
      w: 360,
      h: 28
    },
    anchor: "tr",
    style: {
      fontSize: 14,
      color: "rgba(232,237,242,0.46)",
      letterSpacing: 2,
      textAlign: "right",
      fontFamily: '"JetBrains Mono", "SF Mono", monospace',
      opacity: 100
    },
    props: {
      text: "SCROLL TO REVIEW  ·  ▶ REPLAY"
    },
    animation: {
      enter: {
        preset: "fade",
        durationMs: 360,
        delayMs: 220
      },
      exit: {
        preset: "fade",
        durationMs: 140,
        delayMs: 0
      }
    }
  },
  {
    id: "close-btn",
    type: "button",
    name: "按钮_关闭当前界面",
    rect: {
      x: 1748,
      y: 118,
      w: 52,
      h: 52
    },
    anchor: "tr",
    style: {
      fontSize: 22,
      color: "#dce8f2",
      fill: "rgba(120, 150, 180, 0.06)",
      borderColor: "rgba(150, 180, 210, 0.14)",
      borderWidth: 1,
      radius: 12,
      backdropBlur: 10,
      opacity: 100,
      customCss: "box-shadow: inset 0 1px 0 rgba(200,225,245,0.06), 0 4px 14px rgba(4,10,18,0.4); transition: transform 180ms cubic-bezier(0.22,1,0.36,1), background 180ms, border-color 180ms, box-shadow 180ms; &:hover { background: rgba(127,212,200,0.12); border-color: rgba(127,212,200,0.55); box-shadow: 0 0 22px rgba(94,184,212,0.3); transform: rotate(90deg); }"
    },
    props: {
      text: "✕"
    },
    events: {
      onClick: {
        type: "ui.close"
      }
    },
    animation: {
      enter: {
        preset: "scale",
        durationMs: 320,
        delayMs: 200
      },
      exit: {
        preset: "shrink",
        durationMs: 180,
        delayMs: 0
      }
    }
  },
  {
    id: "history-list",
    type: "history-list",
    name: "历史记录_对话",
    rect: {
      x: 300,
      y: 264,
      w: 1320,
      h: 718
    },
    anchor: "c",
    style: {
      fontSize: 22,
      color: "#e8edf2",
      fill: "rgba(9, 16, 24, 0.58)",
      borderColor: "rgba(127, 212, 200, 0.22)",
      borderWidth: 1,
      radius: 18,
      letterSpacing: 0.6,
      opacity: 100,
      customCss: "filter: drop-shadow(0 26px 68px rgba(0,0,0,0.26));"
    },
    props: {
      maxEntries: 200,
      gap: 12,
      showSpeaker: !0,
      showVoiceButton: !0,
      showTimeline: !0,
      emptyText: "还没有可以回看的对话",
      accentColor: "#7fd4c8"
    },
    animation: {
      enter: {
        preset: "rise",
        durationMs: 540,
        delayMs: 230
      },
      exit: {
        preset: "sink",
        durationMs: 260,
        delayMs: 0
      }
    }
  }
], er = {
  version: Ue,
  name: Xe,
  canvas: qe,
  transition: Je,
  elements: Ke
}, tr = /* @__PURE__ */ Object.freeze(/* @__PURE__ */ Object.defineProperty({
  __proto__: null,
  canvas: qe,
  default: er,
  elements: Ke,
  name: Xe,
  transition: Je,
  version: Ue
}, Symbol.toStringTag, { value: "Module" })), Qe = 1, Ze = "变量输入对话框", et = {
  width: 1920,
  height: 1080
}, tt = [
  {
    id: "input-dialog-mask",
    type: "rect",
    name: "遮罩",
    rect: {
      x: 0,
      y: 0,
      w: 1920,
      h: 1080
    },
    anchor: "c",
    style: {
      fill: "rgba(3, 8, 13, 0.66)",
      radius: 0,
      backdropBlur: 16,
      opacity: 100,
      customCss: "background-image: radial-gradient(ellipse 70% 70% at 50% 42%, rgba(46,90,96,0.18), transparent 68%);"
    },
    animation: {
      enter: {
        preset: "fade",
        durationMs: 300,
        delayMs: 0
      },
      exit: {
        preset: "fade",
        durationMs: 220,
        delayMs: 60
      }
    }
  },
  {
    id: "input-dialog-standard",
    refId: "input-dialog",
    type: "input-dialog",
    name: "输入对话框_玩家姓名",
    rect: {
      x: 530,
      y: 300,
      w: 860,
      h: 480
    },
    anchor: "c",
    style: {
      fontSize: 24,
      color: "#f4f8f7",
      fill: "rgba(9, 18, 27, 0.96)",
      borderColor: "#7fd4c8",
      borderWidth: 1,
      radius: 18,
      opacity: 100
    },
    animation: {
      enter: {
        preset: "scale",
        durationMs: 380,
        delayMs: 70
      },
      exit: {
        preset: "shrink",
        durationMs: 220,
        delayMs: 0
      }
    },
    props: {
      variable: "playerName",
      valueType: "string",
      title: "请告诉我你的名字",
      description: "这个名字会在接下来的故事中使用。",
      label: "玩家姓名",
      showLabel: !0,
      placeholder: "输入名字",
      defaultValue: "",
      confirmText: "确认",
      requiredText: "请输入名字后再继续",
      required: !0,
      minLength: 0,
      maxLength: 20,
      step: 1,
      dismissible: !1
    }
  }
], rr = {
  version: Qe,
  name: Ze,
  canvas: et,
  elements: tt
}, ar = /* @__PURE__ */ Object.freeze(/* @__PURE__ */ Object.defineProperty({
  __proto__: null,
  canvas: et,
  default: rr,
  elements: tt,
  name: Ze,
  version: Qe
}, Symbol.toStringTag, { value: "Module" })), rt = 2, at = "加载界面", ot = {
  width: 1920,
  height: 1080
}, nt = [
  {
    id: "loading-background",
    type: "rect",
    name: "加载背景",
    rect: {
      x: 0,
      y: 0,
      w: 1920,
      h: 1080
    },
    anchor: "tl",
    style: {
      fill: "rgba(7, 16, 24, 0.96)",
      opacity: 100
    },
    props: {},
    animation: {
      enter: {
        preset: "fade",
        durationMs: 320,
        delayMs: 0
      },
      exit: {
        preset: "fade",
        durationMs: 200,
        delayMs: 20
      }
    }
  },
  {
    id: "loading-title",
    type: "text",
    name: "加载提示",
    rect: {
      x: 600,
      y: 476,
      w: 720,
      h: 64
    },
    anchor: "c",
    style: {
      fontSize: 28,
      fontWeight: 500,
      color: "#e8f1f0",
      textAlign: "center",
      opacity: 100
    },
    props: {
      text: "正在加载资源…"
    },
    animation: {
      enter: {
        preset: "rise",
        durationMs: 320,
        delayMs: 40,
        distancePx: 8
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 0
      }
    }
  },
  {
    id: "loading-progress",
    type: "loading-progress",
    name: "加载进度",
    rect: {
      x: 800,
      y: 540,
      w: 320,
      h: 48
    },
    anchor: "c",
    style: {
      color: "#e8f1f0",
      fontSize: 20,
      radius: 2
    },
    props: {
      showPercentage: !0,
      trackHeight: 4,
      trackColor: "rgba(127,212,200,0.2)",
      fillColor: "#7fd4c8",
      previewPercentage: 50
    },
    animation: {
      enter: {
        preset: "rise",
        durationMs: 320,
        delayMs: 70,
        distancePx: 8
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 0
      }
    }
  }
], or = {
  version: rt,
  name: at,
  canvas: ot,
  elements: nt
}, nr = /* @__PURE__ */ Object.freeze(/* @__PURE__ */ Object.defineProperty({
  __proto__: null,
  canvas: ot,
  default: or,
  elements: nt,
  name: at,
  version: rt
}, Symbol.toStringTag, { value: "Module" })), st = 1, it = "标准消息框", lt = {
  width: 1920,
  height: 1080
}, dt = [
  {
    id: "message-box-mask",
    type: "rect",
    name: "遮罩",
    rect: {
      x: 0,
      y: 0,
      w: 1920,
      h: 1080
    },
    anchor: "c",
    style: {
      fill: "rgba(3, 8, 13, 0.66)",
      radius: 0,
      backdropBlur: 16,
      opacity: 100,
      customCss: "background-image: radial-gradient(ellipse 70% 70% at 50% 42%, rgba(46,90,96,0.18), transparent 68%);"
    },
    animation: {
      enter: {
        preset: "fade",
        durationMs: 300,
        delayMs: 0
      },
      exit: {
        preset: "fade",
        durationMs: 220,
        delayMs: 60
      }
    }
  },
  {
    id: "message-box-standard",
    refId: "message-box",
    type: "message-box",
    name: "消息框_提示",
    rect: {
      x: 560,
      y: 340,
      w: 800,
      h: 400
    },
    anchor: "c",
    style: {
      fontSize: 24,
      color: "#f4f8f7",
      fill: "rgba(9, 18, 27, 0.96)",
      borderColor: "#7fd4c8",
      borderWidth: 1,
      radius: 18,
      opacity: 100
    },
    animation: {
      enter: {
        preset: "rise",
        durationMs: 380,
        delayMs: 70
      },
      exit: {
        preset: "sink",
        durationMs: 220,
        delayMs: 0
      }
    },
    props: {
      mode: "alert",
      title: "提示",
      message: "这里显示需要告诉玩家的消息。",
      confirmText: "知道了",
      cancelText: "取消",
      tone: "info",
      dismissible: !0
    }
  }
], sr = {
  version: st,
  name: it,
  canvas: lt,
  elements: dt
}, ir = /* @__PURE__ */ Object.freeze(/* @__PURE__ */ Object.defineProperty({
  __proto__: null,
  canvas: lt,
  default: sr,
  elements: dt,
  name: it,
  version: st
}, Symbol.toStringTag, { value: "Module" })), ct = 2, pt = "段落 · 电影留白", ut = {
  width: 1920,
  height: 1080
}, ft = [
  {
    id: "background-mask",
    refId: "background-mask",
    type: "background-mask",
    name: "背景遮罩",
    rect: {
      x: 0,
      y: 0,
      w: 1920,
      h: 1080
    },
    anchor: "c",
    style: {
      fill: "#05070d",
      opacity: 66
    }
  },
  {
    id: "paragraph",
    refId: "paragraph",
    type: "paragraph",
    name: "整屏段落",
    rect: {
      x: 400,
      y: 94,
      w: 1120,
      h: 892
    },
    anchor: "t",
    style: {
      fontFamily: "'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif",
      fontSize: 31,
      fontWeight: 500,
      color: "#f7f3ec",
      fill: "transparent",
      borderColor: "transparent",
      borderWidth: 0,
      radius: 0,
      backdropBlur: 0,
      letterSpacing: 1.6,
      textAlign: "left",
      opacity: 100
    },
    props: {
      gap: 32,
      lineHeight: 1.82,
      inactiveColor: "#cbc8c2",
      readBehavior: {
        mode: "dim",
        followMode: "overflow"
      },
      readStyle: {
        color: "#cbc8c2",
        opacity: 62,
        transform: {
          y: -4,
          scale: 100
        },
        transition: {
          preset: "fade-up",
          durationMs: 240,
          delayMs: 0,
          easing: "soft"
        }
      },
      textPadding: {
        top: 48,
        right: 56,
        bottom: 48,
        left: 56
      },
      backgroundImage: "",
      backgroundImageFit: "cover",
      backgroundImagePosition: "center",
      backgroundImageRepeat: "no-repeat",
      linearGradient: {
        enabled: !1,
        angle: 180,
        startColor: "transparent",
        endColor: "transparent"
      },
      frameDecoration: {
        borderTop: "",
        borderRight: "",
        borderBottom: "",
        borderLeft: "",
        borderRadius: "",
        boxShadow: ""
      },
      textShadows: [
        {
          offsetX: 0,
          offsetY: 0,
          blur: 3,
          color: "rgba(0, 0, 0, 0.95)"
        },
        {
          offsetX: 0,
          offsetY: 2,
          blur: 14,
          color: "rgba(0, 0, 0, 0.85)"
        }
      ],
      previewParagraphs: [
        "银幕暗下去以后，远处的海潮才重新有了声音。",
        "我沿着那道微光向前，仿佛正走进故事尚未写完的部分。",
        "直到她在身后叫住我，所有沉默才有了方向。"
      ]
    }
  }
], lr = {
  version: ct,
  name: pt,
  canvas: ut,
  elements: ft
}, dr = /* @__PURE__ */ Object.freeze(/* @__PURE__ */ Object.defineProperty({
  __proto__: null,
  canvas: ut,
  default: lr,
  elements: ft,
  name: pt,
  version: ct
}, Symbol.toStringTag, { value: "Module" })), yt = 2, gt = "段落 · 暮色手账", mt = {
  width: 1920,
  height: 1080
}, bt = [
  {
    id: "background-mask",
    refId: "background-mask",
    type: "background-mask",
    name: "背景遮罩",
    rect: {
      x: 0,
      y: 0,
      w: 1920,
      h: 1080
    },
    anchor: "c",
    style: {
      fill: "#241618",
      opacity: 42
    }
  },
  {
    id: "paragraph",
    refId: "paragraph",
    type: "paragraph",
    name: "整屏段落",
    rect: {
      x: 336,
      y: 72,
      w: 1248,
      h: 936
    },
    anchor: "t",
    style: {
      fontFamily: "'Kaiti SC', STKaiti, KaiTi, 'Songti SC', serif",
      fontSize: 30,
      fontWeight: 400,
      color: "#fff8ef",
      fill: "rgba(68, 43, 39, 0.88)",
      borderColor: "rgba(255, 225, 205, 0.22)",
      borderWidth: 1,
      radius: 32,
      backdropBlur: 12,
      letterSpacing: 1.2,
      textAlign: "left",
      opacity: 100
    },
    props: {
      gap: 30,
      lineHeight: 1.82,
      inactiveColor: "#dcc6b9",
      readBehavior: {
        mode: "dim",
        followMode: "overflow"
      },
      readStyle: {
        color: "#dcc6b9",
        opacity: 74,
        filter: {
          blur: 0.3,
          grayscale: 4,
          brightness: 96
        },
        transform: {
          y: -2,
          scale: 99
        },
        transition: {
          preset: "settle",
          durationMs: 260,
          delayMs: 0,
          easing: "soft"
        }
      },
      textPadding: {
        top: 64,
        right: 72,
        bottom: 64,
        left: 72
      },
      backgroundImage: "",
      backgroundImageFit: "cover",
      backgroundImagePosition: "center",
      backgroundImageRepeat: "no-repeat",
      linearGradient: {
        enabled: !0,
        angle: 150,
        startColor: "rgba(92, 57, 50, 0.92)",
        endColor: "rgba(49, 33, 39, 0.90)"
      },
      frameDecoration: {
        borderTop: "",
        borderRight: "",
        borderBottom: "",
        borderLeft: "",
        borderRadius: "",
        boxShadow: "0 24px 64px rgba(42, 20, 18, 0.32), inset 0 1px 0 rgba(255, 249, 241, 0.12)"
      },
      textShadows: [
        {
          offsetX: 0,
          offsetY: 2,
          blur: 7,
          color: "rgba(45, 24, 20, 0.55)"
        }
      ],
      previewParagraphs: [
        "傍晚的风把窗帘吹得鼓起来，也把厨房里的甜香送到了书桌边。",
        "她在便签背面画了一朵歪歪扭扭的花，然后认真地写下明天见。",
        "门铃响起时，那张便签还被晚风轻轻压在杯沿下。"
      ]
    }
  }
], cr = {
  version: yt,
  name: gt,
  canvas: mt,
  elements: bt
}, pr = /* @__PURE__ */ Object.freeze(/* @__PURE__ */ Object.defineProperty({
  __proto__: null,
  canvas: mt,
  default: cr,
  elements: bt,
  name: gt,
  version: yt
}, Symbol.toStringTag, { value: "Module" })), ht = 2, xt = "段落 · 书页叙事", vt = {
  width: 1920,
  height: 1080
}, St = [
  {
    id: "background-mask",
    refId: "background-mask",
    type: "background-mask",
    name: "背景遮罩",
    rect: {
      x: 0,
      y: 0,
      w: 1920,
      h: 1080
    },
    anchor: "c",
    style: {
      fill: "#1a1410",
      opacity: 36
    }
  },
  {
    id: "paragraph",
    refId: "paragraph",
    type: "paragraph",
    name: "整屏段落",
    rect: {
      x: 320,
      y: 64,
      w: 1280,
      h: 952
    },
    anchor: "t",
    style: {
      fontFamily: "'Songti SC', STSong, SimSun, serif",
      fontSize: 29,
      fontWeight: 400,
      color: "#342b24",
      fill: "rgba(250, 244, 230, 0.96)",
      borderColor: "#d0b98f",
      borderWidth: 1,
      radius: 8,
      backdropBlur: 0,
      letterSpacing: 1.4,
      textAlign: "left",
      opacity: 100
    },
    props: {
      gap: 30,
      lineHeight: 1.9,
      inactiveColor: "#746659",
      readBehavior: {
        mode: "dim",
        followMode: "overflow"
      },
      readStyle: {
        color: "#746659",
        opacity: 82,
        filter: {
          grayscale: 8,
          brightness: 94
        },
        transform: {
          y: 1,
          scale: 99.5
        },
        transition: {
          preset: "settle",
          durationMs: 260,
          delayMs: 0,
          easing: "soft"
        }
      },
      textPadding: {
        top: 68,
        right: 88,
        bottom: 68,
        left: 88
      },
      backgroundImage: "",
      backgroundImageFit: "cover",
      backgroundImagePosition: "center",
      backgroundImageRepeat: "no-repeat",
      linearGradient: {
        enabled: !0,
        angle: 165,
        startColor: "rgba(255, 251, 240, 0.98)",
        endColor: "rgba(237, 224, 200, 0.96)"
      },
      frameDecoration: {
        borderTop: "",
        borderRight: "",
        borderBottom: "",
        borderLeft: "",
        borderRadius: "",
        boxShadow: "0 20px 60px rgba(20, 12, 6, 0.34), inset 0 0 42px rgba(130, 92, 48, 0.10)"
      },
      textShadows: [],
      previewParagraphs: [
        "信纸在窗边压了一夜，边角沾着一点潮湿的月色。",
        "那些没有寄出的句子，如今读来，竟比当时更接近答案。",
        "我翻到最后一页，才发现答案一直藏在落款旁。"
      ]
    }
  }
], ur = {
  version: ht,
  name: xt,
  canvas: vt,
  elements: St
}, fr = /* @__PURE__ */ Object.freeze(/* @__PURE__ */ Object.defineProperty({
  __proto__: null,
  canvas: vt,
  default: ur,
  elements: St,
  name: xt,
  version: ht
}, Symbol.toStringTag, { value: "Module" })), Mt = 2, wt = "段落 · 冷光档案", kt = {
  width: 1920,
  height: 1080
}, _t = [
  {
    id: "background-mask",
    refId: "background-mask",
    type: "background-mask",
    name: "背景遮罩",
    rect: {
      x: 0,
      y: 0,
      w: 1920,
      h: 1080
    },
    anchor: "c",
    style: {
      fill: "#041224",
      opacity: 58
    }
  },
  {
    id: "paragraph",
    refId: "paragraph",
    type: "paragraph",
    name: "整屏段落",
    rect: {
      x: 320,
      y: 72,
      w: 1280,
      h: 936
    },
    anchor: "t",
    style: {
      fontFamily: "'PingFang SC', 'Microsoft YaHei', Arial, sans-serif",
      fontSize: 29,
      fontWeight: 500,
      color: "#eaf7ff",
      fill: "rgba(4, 12, 24, 0.90)",
      borderColor: "rgba(91, 207, 255, 0.18)",
      borderWidth: 1,
      radius: 4,
      backdropBlur: 8,
      letterSpacing: 0.6,
      textAlign: "left",
      opacity: 100
    },
    props: {
      gap: 24,
      lineHeight: 1.68,
      inactiveColor: "#9fb9c8",
      readBehavior: {
        mode: "dim",
        followMode: "overflow"
      },
      readStyle: {
        color: "#9fb9c8",
        opacity: 58,
        filter: {
          grayscale: 18,
          brightness: 84
        },
        transform: {
          x: -4,
          scale: 100
        },
        transition: {
          preset: "settle",
          durationMs: 200,
          delayMs: 0,
          easing: "ease-out"
        }
      },
      textPadding: {
        top: 52,
        right: 68,
        bottom: 52,
        left: 68
      },
      backgroundImage: "",
      backgroundImageFit: "cover",
      backgroundImagePosition: "center",
      backgroundImageRepeat: "no-repeat",
      linearGradient: {
        enabled: !0,
        angle: 180,
        startColor: "rgba(7, 26, 45, 0.95)",
        endColor: "rgba(2, 8, 18, 0.94)"
      },
      frameDecoration: {
        borderTop: "1px solid rgba(91, 207, 255, 0.18)",
        borderRight: "1px solid rgba(91, 207, 255, 0.18)",
        borderBottom: "1px solid rgba(91, 207, 255, 0.18)",
        borderLeft: "3px solid rgba(91, 207, 255, 0.85)",
        borderRadius: "4px",
        boxShadow: "0 0 30px rgba(67, 181, 255, 0.16), inset 0 0 40px rgba(0, 97, 156, 0.08)"
      },
      textShadows: [
        {
          offsetX: 0,
          offsetY: 1,
          blur: 2,
          color: "rgba(0, 0, 0, 0.85)"
        },
        {
          offsetX: 0,
          offsetY: 0,
          blur: 8,
          color: "rgba(81, 194, 255, 0.22)"
        }
      ],
      previewParagraphs: [
        "记录编号 07：城区照明在凌晨三点十七分同时熄灭。",
        "唯一仍在运转的终端，反复显示着同一句尚未解密的留言。",
        "我按下确认键，冷光里终于浮出了一个名字。"
      ]
    }
  }
], yr = {
  version: Mt,
  name: wt,
  canvas: kt,
  elements: _t
}, gr = /* @__PURE__ */ Object.freeze(/* @__PURE__ */ Object.defineProperty({
  __proto__: null,
  canvas: kt,
  default: yr,
  elements: _t,
  name: wt,
  version: Mt
}, Symbol.toStringTag, { value: "Module" })), $t = 2, Ct = "段落", It = {
  width: 1920,
  height: 1080
}, Ft = [
  {
    id: "background-mask",
    refId: "background-mask",
    type: "background-mask",
    name: "背景遮罩",
    rect: {
      x: 0,
      y: 0,
      w: 1920,
      h: 1080
    },
    anchor: "c",
    style: {
      fill: "#000000",
      opacity: 70
    }
  },
  {
    id: "paragraph",
    refId: "paragraph",
    type: "paragraph",
    name: "整屏段落",
    rect: {
      x: 384,
      y: 80,
      w: 1152,
      h: 1e3
    },
    anchor: "t",
    style: {
      fontSize: 28,
      fontWeight: 400,
      color: "#ffffff",
      fill: "transparent",
      borderColor: "transparent",
      borderWidth: 0,
      radius: 0,
      backdropBlur: 0,
      letterSpacing: 0,
      textAlign: "left",
      opacity: 100
    },
    props: {
      layoutMode: "native-fluid",
      gap: 30,
      inactiveColor: "#808080",
      textPadding: {
        top: 0,
        right: 0,
        bottom: 0,
        left: 0
      },
      backgroundImage: "",
      backgroundImageFit: "cover",
      backgroundImagePosition: "center",
      backgroundImageRepeat: "no-repeat",
      linearGradient: {
        enabled: !1,
        angle: 180,
        startColor: "transparent",
        endColor: "transparent"
      },
      frameDecoration: {
        borderTop: "",
        borderRight: "",
        borderBottom: "",
        borderLeft: "",
        borderRadius: "",
        boxShadow: ""
      },
      textShadows: [],
      previewParagraphs: [
        "有些故事，会从一个看似普通的夜晚开始。",
        "而我们，刚好站在它的入口。",
        "那一刻，远处的钟声正好响起。"
      ]
    }
  }
], mr = {
  version: $t,
  name: Ct,
  canvas: It,
  elements: Ft
}, br = /* @__PURE__ */ Object.freeze(/* @__PURE__ */ Object.defineProperty({
  __proto__: null,
  canvas: It,
  default: mr,
  elements: Ft,
  name: Ct,
  version: $t
}, Symbol.toStringTag, { value: "Module" })), Tt = 1, Ot = "存档读档", Pt = {
  width: 1920,
  height: 1080
}, Rt = [
  {
    id: "mask",
    type: "rect",
    name: "遮罩",
    rect: {
      x: 0,
      y: 0,
      w: 1920,
      h: 1080
    },
    anchor: "c",
    style: {
      fill: "rgba(8, 13, 20, 0.86)",
      radius: 0,
      backdropBlur: 28,
      opacity: 100,
      customCss: "background-image: radial-gradient(ellipse 120% 80% at 20% 0%, rgba(40,70,100,0.35), transparent 60%);"
    },
    animation: {
      enter: {
        preset: "fade",
        durationMs: 420,
        delayMs: 0
      },
      exit: {
        preset: "fade",
        durationMs: 260,
        delayMs: 100
      }
    }
  },
  {
    id: "eyebrow",
    type: "text",
    name: "文字_Save",
    rect: {
      x: 120,
      y: 96,
      w: 500,
      h: 24
    },
    anchor: "tl",
    style: {
      fontSize: 15,
      color: "#7fd4c8",
      letterSpacing: 5,
      fontFamily: '"JetBrains Mono", "SF Mono", "Menlo", "Monaco", "Consolas", monospace',
      opacity: 100,
      customCss: "text-transform: uppercase; text-shadow: 0 0 12px rgba(127,212,200,0.4);"
    },
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 360,
        delayMs: 80
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 60
      }
    },
    props: {
      text: "Save / Load"
    }
  },
  {
    id: "title",
    type: "text",
    name: "文字_保存存档",
    rect: {
      x: 118,
      y: 122,
      w: 800,
      h: 80
    },
    anchor: "tl",
    style: {
      fontSize: 56,
      color: "#e8edf2",
      letterSpacing: 2,
      fontFamily: '"M PLUS Rounded 1c", "Plus Jakarta Sans", "PingFang SC", "Hiragino Sans GB", "HarmonyOS Sans", "Microsoft YaHei", -apple-system, BlinkMacSystemFont, sans-serif',
      opacity: 100
    },
    animation: {
      enter: {
        preset: "rise",
        durationMs: 460,
        delayMs: 120
      },
      exit: {
        preset: "sink",
        durationMs: 220,
        delayMs: 40
      }
    },
    props: {
      text: "存档 / 读档"
    }
  },
  {
    id: "title-accent",
    type: "rect",
    name: "玉青短横线",
    rect: {
      x: 120,
      y: 212,
      w: 72,
      h: 4
    },
    anchor: "tl",
    style: {
      fill: "#7fd4c8",
      radius: 999,
      opacity: 100,
      customCss: "background-image: linear-gradient(90deg, #7fd4c8, #5eb8d4); box-shadow: 0 0 14px rgba(94,184,212,0.5);"
    },
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 420,
        delayMs: 190
      },
      exit: {
        preset: "shrink",
        durationMs: 180,
        delayMs: 20
      }
    }
  },
  {
    id: "close-btn",
    type: "button",
    name: "按钮_关闭当前界面",
    rect: {
      x: 1748,
      y: 118,
      w: 52,
      h: 52
    },
    anchor: "tr",
    style: {
      fontSize: 22,
      color: "#dce8f2",
      fill: "rgba(120, 150, 180, 0.06)",
      borderColor: "rgba(150, 180, 210, 0.14)",
      borderWidth: 1,
      radius: 12,
      backdropBlur: 10,
      opacity: 100,
      customCss: "box-shadow: inset 0 1px 0 rgba(200,225,245,0.06), 0 4px 14px rgba(4,10,18,0.4); transition: transform 180ms cubic-bezier(0.22,1,0.36,1), background 180ms, border-color 180ms, box-shadow 180ms; &:hover { background: rgba(127,212,200,0.12); border-color: rgba(127,212,200,0.55); box-shadow: 0 0 22px rgba(94,184,212,0.3); transform: rotate(90deg); }"
    },
    animation: {
      enter: {
        preset: "scale",
        durationMs: 320,
        delayMs: 200
      },
      exit: {
        preset: "shrink",
        durationMs: 180,
        delayMs: 0
      }
    },
    props: {
      text: "✕"
    },
    events: {
      onClick: {
        type: "ui.close"
      }
    }
  },
  {
    id: "save-grid",
    type: "save-grid",
    name: "存档格子",
    rect: {
      x: 120,
      y: 264,
      w: 1680,
      h: 720
    },
    anchor: "c",
    style: {
      radius: 16,
      opacity: 100
    },
    animation: {
      enter: {
        preset: "rise",
        durationMs: 520,
        delayMs: 240
      },
      exit: {
        preset: "sink",
        durationMs: 260,
        delayMs: 0
      }
    },
    props: {
      cols: 3,
      rows: 2,
      gap: 28,
      showTime: !0,
      showText: !0,
      mode: "auto",
      confirmOverwrite: !0,
      totalSlots: 30
    }
  }
], hr = {
  version: Tt,
  name: Ot,
  canvas: Pt,
  elements: Rt
}, xr = /* @__PURE__ */ Object.freeze(/* @__PURE__ */ Object.defineProperty({
  __proto__: null,
  canvas: Pt,
  default: hr,
  elements: Rt,
  name: Ot,
  version: Tt
}, Symbol.toStringTag, { value: "Module" })), Lt = 2, At = "系统设置", zt = {
  width: 1920,
  height: 1080
}, Et = [
  {
    id: "mask",
    type: "rect",
    name: "遮罩",
    rect: {
      x: 0,
      y: 0,
      w: 1920,
      h: 1080
    },
    anchor: "c",
    style: {
      fill: "rgba(8, 13, 20, 0.86)",
      radius: 0,
      backdropBlur: 28,
      opacity: 100,
      customCss: "background-image: radial-gradient(ellipse 120% 80% at 20% 0%, rgba(40,70,100,0.35), transparent 60%);"
    },
    animation: {
      enter: {
        preset: "fade",
        durationMs: 420,
        delayMs: 0
      },
      exit: {
        preset: "fade",
        durationMs: 260,
        delayMs: 100
      }
    }
  },
  {
    id: "eyebrow",
    type: "text",
    name: "文字_Settings",
    rect: {
      x: 120,
      y: 96,
      w: 500,
      h: 24
    },
    anchor: "tl",
    style: {
      fontSize: 15,
      color: "#7fd4c8",
      letterSpacing: 5,
      fontFamily: '"JetBrains Mono", "SF Mono", "Menlo", "Monaco", "Consolas", monospace',
      opacity: 100,
      customCss: "text-transform: uppercase; text-shadow: 0 0 12px rgba(127,212,200,0.4);"
    },
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 360,
        delayMs: 80
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 60
      }
    },
    props: {
      text: "Settings"
    }
  },
  {
    id: "title",
    type: "text",
    name: "文字_系统设置",
    rect: {
      x: 118,
      y: 122,
      w: 800,
      h: 80
    },
    anchor: "tl",
    style: {
      fontSize: 56,
      color: "#e8edf2",
      letterSpacing: 2,
      fontFamily: '"M PLUS Rounded 1c", "Plus Jakarta Sans", "PingFang SC", "Hiragino Sans GB", "HarmonyOS Sans", "Microsoft YaHei", -apple-system, BlinkMacSystemFont, sans-serif',
      opacity: 100
    },
    animation: {
      enter: {
        preset: "rise",
        durationMs: 460,
        delayMs: 120
      },
      exit: {
        preset: "sink",
        durationMs: 220,
        delayMs: 40
      }
    },
    props: {
      text: "系统设置"
    }
  },
  {
    id: "title-accent",
    type: "rect",
    name: "玉青短横线",
    rect: {
      x: 120,
      y: 212,
      w: 72,
      h: 4
    },
    anchor: "t",
    style: {
      fill: "#7fd4c8",
      radius: 999,
      opacity: 100,
      customCss: "background-image: linear-gradient(90deg, #7fd4c8, #5eb8d4); box-shadow: 0 0 14px rgba(94,184,212,0.5);"
    },
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 420,
        delayMs: 190
      },
      exit: {
        preset: "shrink",
        durationMs: 180,
        delayMs: 20
      }
    }
  },
  {
    id: "close-btn",
    type: "button",
    name: "按钮_关闭当前界面",
    rect: {
      x: 1748,
      y: 118,
      w: 52,
      h: 52
    },
    anchor: "tr",
    style: {
      fontSize: 22,
      color: "#dce8f2",
      fill: "rgba(120, 150, 180, 0.06)",
      borderColor: "rgba(150, 180, 210, 0.14)",
      borderWidth: 1,
      radius: 10,
      backdropBlur: 10,
      opacity: 100,
      customCss: "box-shadow: inset 0 1px 0 rgba(200,225,245,0.06), 0 4px 14px rgba(4,10,18,0.4); transition: transform 180ms cubic-bezier(0.22,1,0.36,1), background 180ms, border-color 180ms, box-shadow 180ms; &:hover { background: rgba(127,212,200,0.12); border-color: rgba(127,212,200,0.55); box-shadow: 0 0 22px rgba(94,184,212,0.3); transform: rotate(90deg); }"
    },
    animation: {
      enter: {
        preset: "scale",
        durationMs: 320,
        delayMs: 200
      },
      exit: {
        preset: "shrink",
        durationMs: 180,
        delayMs: 0
      }
    },
    props: {
      text: "✕"
    },
    events: {
      onClick: {
        type: "ui.close"
      }
    }
  },
  {
    id: "settings-tabs",
    type: "tabs",
    name: "页签_设置分组",
    rect: {
      x: 210,
      y: 264,
      w: 1500,
      h: 40
    },
    anchor: "tl",
    style: {
      fontSize: 15,
      color: "#e8edf2",
      radius: 8,
      opacity: 100,
      fontFamily: '"Plus Jakarta Sans", "Noto Sans SC", "PingFang SC", sans-serif'
    },
    animation: {
      enter: {
        preset: "rise",
        durationMs: 380,
        delayMs: 220
      },
      exit: {
        preset: "sink",
        durationMs: 200,
        delayMs: 0
      }
    },
    props: {
      tabs: [
        "音量",
        "文本与播放",
        "显示"
      ],
      activeIndex: 0,
      inactiveColor: "rgba(220,232,242,0.55)",
      gap: 8
    }
  },
  {
    id: "vol-card",
    type: "rect",
    name: "矩形_音量卡片",
    rect: {
      x: 210,
      y: 314,
      w: 1500,
      h: 316
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "rise",
        durationMs: 340,
        delayMs: 80
      },
      exit: {
        preset: "sink",
        durationMs: 200,
        delayMs: 0
      }
    },
    style: {
      fill: "rgba(120,150,180,0.06)",
      radius: 12,
      opacity: 100
    },
    tab: {
      of: "settings-tabs",
      index: 0
    }
  },
  {
    id: "vol-title",
    type: "text",
    name: "文字_音量",
    rect: {
      x: 250,
      y: 334,
      w: 200,
      h: 32
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "fade",
        durationMs: 280,
        delayMs: 130
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 0
      }
    },
    style: {
      fontSize: 20,
      color: "#e8edf2",
      letterSpacing: 4,
      opacity: 100
    },
    props: {
      text: "音量"
    },
    tab: {
      of: "settings-tabs",
      index: 0
    }
  },
  {
    id: "vol-master-label",
    type: "text",
    name: "文字_主音量",
    rect: {
      x: 250,
      y: 382,
      w: 320,
      h: 44
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 300,
        delayMs: 180
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 0
      }
    },
    style: {
      fontSize: 18,
      color: "rgba(220,232,242,0.82)",
      opacity: 100
    },
    props: {
      text: "主音量"
    },
    tab: {
      of: "settings-tabs",
      index: 0
    }
  },
  {
    id: "vol-master-slider",
    type: "slider",
    name: "滑块_主音量",
    rect: {
      x: 630,
      y: 382,
      w: 1040,
      h: 44
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "fade",
        durationMs: 320,
        delayMs: 200
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 0
      }
    },
    style: {
      fontSize: 18,
      opacity: 100
    },
    props: {
      bind: "masterVolume",
      value: 80,
      showValue: !0
    },
    tab: {
      of: "settings-tabs",
      index: 0
    }
  },
  {
    id: "vol-bgm-label",
    type: "text",
    name: "文字_背景音乐",
    rect: {
      x: 250,
      y: 444,
      w: 320,
      h: 44
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 300,
        delayMs: 230
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 0
      }
    },
    style: {
      fontSize: 18,
      color: "rgba(220,232,242,0.82)",
      opacity: 100
    },
    props: {
      text: "背景音乐"
    },
    tab: {
      of: "settings-tabs",
      index: 0
    }
  },
  {
    id: "vol-bgm-slider",
    type: "slider",
    name: "滑块_背景音乐音量",
    rect: {
      x: 630,
      y: 444,
      w: 1040,
      h: 44
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "fade",
        durationMs: 320,
        delayMs: 250
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 0
      }
    },
    style: {
      fontSize: 18,
      opacity: 100
    },
    props: {
      bind: "bgmVolume",
      value: 80,
      showValue: !0
    },
    tab: {
      of: "settings-tabs",
      index: 0
    }
  },
  {
    id: "vol-se-label",
    type: "text",
    name: "文字_音效",
    rect: {
      x: 250,
      y: 506,
      w: 320,
      h: 44
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 300,
        delayMs: 280
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 0
      }
    },
    style: {
      fontSize: 18,
      color: "rgba(220,232,242,0.82)",
      opacity: 100
    },
    props: {
      text: "音效"
    },
    tab: {
      of: "settings-tabs",
      index: 0
    }
  },
  {
    id: "vol-se-slider",
    type: "slider",
    name: "滑块_音效音量",
    rect: {
      x: 630,
      y: 506,
      w: 1040,
      h: 44
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "fade",
        durationMs: 320,
        delayMs: 300
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 0
      }
    },
    style: {
      fontSize: 18,
      opacity: 100
    },
    props: {
      bind: "seVolume",
      value: 80,
      showValue: !0
    },
    tab: {
      of: "settings-tabs",
      index: 0
    }
  },
  {
    id: "vol-voice-label",
    type: "text",
    name: "文字_语音",
    rect: {
      x: 250,
      y: 568,
      w: 320,
      h: 44
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 300,
        delayMs: 330
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 0
      }
    },
    style: {
      fontSize: 18,
      color: "rgba(220,232,242,0.82)",
      opacity: 100
    },
    props: {
      text: "语音"
    },
    tab: {
      of: "settings-tabs",
      index: 0
    }
  },
  {
    id: "vol-voice-slider",
    type: "slider",
    name: "滑块_语音音量",
    rect: {
      x: 630,
      y: 568,
      w: 1040,
      h: 44
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "fade",
        durationMs: 320,
        delayMs: 350
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 0
      }
    },
    style: {
      fontSize: 18,
      opacity: 100
    },
    props: {
      bind: "voiceVolume",
      value: 80,
      showValue: !0
    },
    tab: {
      of: "settings-tabs",
      index: 0
    }
  },
  {
    id: "text-card",
    type: "rect",
    name: "矩形_文本与播放卡片",
    rect: {
      x: 210,
      y: 314,
      w: 1500,
      h: 310
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "rise",
        durationMs: 340,
        delayMs: 80
      },
      exit: {
        preset: "sink",
        durationMs: 200,
        delayMs: 0
      }
    },
    style: {
      fill: "rgba(120,150,180,0.06)",
      radius: 12,
      opacity: 100
    },
    tab: {
      of: "settings-tabs",
      index: 1
    }
  },
  {
    id: "text-title",
    type: "text",
    name: "文字_文本与播放",
    rect: {
      x: 250,
      y: 334,
      w: 240,
      h: 32
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "fade",
        durationMs: 280,
        delayMs: 130
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 0
      }
    },
    style: {
      fontSize: 20,
      color: "#e8edf2",
      letterSpacing: 4,
      opacity: 100
    },
    props: {
      text: "文本与播放"
    },
    tab: {
      of: "settings-tabs",
      index: 1
    }
  },
  {
    id: "speed-label",
    type: "text",
    name: "文字_文字速度",
    rect: {
      x: 250,
      y: 380,
      w: 320,
      h: 44
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 300,
        delayMs: 180
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 0
      }
    },
    style: {
      fontSize: 18,
      color: "rgba(220,232,242,0.82)",
      opacity: 100
    },
    props: {
      text: "文字速度"
    },
    tab: {
      of: "settings-tabs",
      index: 1
    }
  },
  {
    id: "speed-slider",
    type: "slider",
    name: "滑块_文字速度",
    rect: {
      x: 630,
      y: 380,
      w: 1040,
      h: 44
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "fade",
        durationMs: 320,
        delayMs: 200
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 0
      }
    },
    style: {
      fontSize: 18,
      opacity: 100
    },
    props: {
      bind: "textSpeed",
      value: 50,
      showValue: !0
    },
    tab: {
      of: "settings-tabs",
      index: 1
    }
  },
  {
    id: "auto-speed-label",
    type: "text",
    name: "文字_自动模式速度",
    rect: {
      x: 250,
      y: 442,
      w: 320,
      h: 44
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 300,
        delayMs: 230
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 0
      }
    },
    style: {
      fontSize: 18,
      color: "rgba(220,232,242,0.82)",
      opacity: 100
    },
    props: {
      text: "自动模式速度"
    },
    tab: {
      of: "settings-tabs",
      index: 1
    }
  },
  {
    id: "auto-speed-slider",
    type: "slider",
    name: "滑块_自动模式速度",
    rect: {
      x: 630,
      y: 442,
      w: 1040,
      h: 44
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "fade",
        durationMs: 320,
        delayMs: 250
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 0
      }
    },
    style: {
      fontSize: 18,
      opacity: 100
    },
    props: {
      bind: "autoModeTextSpeed",
      value: 50,
      showValue: !0
    },
    tab: {
      of: "settings-tabs",
      index: 1
    }
  },
  {
    id: "skip-label",
    type: "text",
    name: "文字_跳过模式",
    rect: {
      x: 250,
      y: 504,
      w: 320,
      h: 44
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 300,
        delayMs: 280
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 0
      }
    },
    style: {
      fontSize: 18,
      color: "rgba(220,232,242,0.82)",
      opacity: 100
    },
    props: {
      text: "跳过模式"
    },
    tab: {
      of: "settings-tabs",
      index: 1
    }
  },
  {
    id: "skip-select",
    type: "select",
    name: "下拉_跳过模式",
    rect: {
      x: 630,
      y: 502,
      w: 320,
      h: 48
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "fade",
        durationMs: 320,
        delayMs: 300
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 0
      }
    },
    style: {
      fontSize: 18,
      color: "#e8edf2",
      radius: 6,
      opacity: 100
    },
    props: {
      options: [
        "仅跳过已读",
        "跳过全部"
      ],
      value: 0,
      bind: "skipMode"
    },
    tab: {
      of: "settings-tabs",
      index: 1
    }
  },
  {
    id: "stopvoice-label",
    type: "text",
    name: "文字_下句中断语音",
    rect: {
      x: 250,
      y: 562,
      w: 320,
      h: 44
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 300,
        delayMs: 330
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 0
      }
    },
    style: {
      fontSize: 18,
      color: "rgba(220,232,242,0.82)",
      opacity: 100
    },
    props: {
      text: "下句中断语音"
    },
    tab: {
      of: "settings-tabs",
      index: 1
    }
  },
  {
    id: "stopvoice-switch",
    type: "switch",
    name: "开关_下句中断语音",
    rect: {
      x: 630,
      y: 560,
      w: 96,
      h: 48
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "scale",
        durationMs: 280,
        delayMs: 350
      },
      exit: {
        preset: "shrink",
        durationMs: 160,
        delayMs: 0
      }
    },
    style: {
      opacity: 100
    },
    props: {
      bind: "stopVoiceOnNextDialogue",
      value: !0
    },
    tab: {
      of: "settings-tabs",
      index: 1
    }
  },
  {
    id: "display-card",
    type: "rect",
    name: "矩形_显示卡片",
    refId: "display-card",
    rect: {
      x: 210,
      y: 314,
      w: 1500,
      h: 120
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "rise",
        durationMs: 340,
        delayMs: 80
      },
      exit: {
        preset: "sink",
        durationMs: 200,
        delayMs: 0
      }
    },
    style: {
      fill: "rgba(120,150,180,0.06)",
      radius: 12,
      opacity: 100
    },
    tab: {
      of: "settings-tabs",
      index: 2
    }
  },
  {
    id: "display-title",
    type: "text",
    name: "文字_显示",
    refId: "display-title",
    rect: {
      x: 250,
      y: 332,
      w: 200,
      h: 30
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "fade",
        durationMs: 280,
        delayMs: 130
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 0
      }
    },
    style: {
      fontSize: 20,
      color: "#e8edf2",
      letterSpacing: 4,
      opacity: 100
    },
    props: {
      text: "显示"
    },
    tab: {
      of: "settings-tabs",
      index: 2
    }
  },
  {
    id: "display-label",
    type: "text",
    name: "文字_全屏",
    refId: "display-label",
    rect: {
      x: 250,
      y: 376,
      w: 320,
      h: 44
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 300,
        delayMs: 180
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 0
      }
    },
    style: {
      fontSize: 18,
      color: "rgba(220,232,242,0.82)",
      opacity: 100
    },
    props: {
      text: "全屏"
    },
    tab: {
      of: "settings-tabs",
      index: 2
    }
  },
  {
    id: "display-switch",
    type: "switch",
    name: "开关_全屏",
    refId: "display-switch",
    rect: {
      x: 630,
      y: 374,
      w: 96,
      h: 48
    },
    anchor: "t",
    animation: {
      enter: {
        preset: "scale",
        durationMs: 280,
        delayMs: 200
      },
      exit: {
        preset: "shrink",
        durationMs: 160,
        delayMs: 0
      }
    },
    style: {
      opacity: 100
    },
    props: {
      bind: "fullscreen",
      value: !1
    },
    tab: {
      of: "settings-tabs",
      index: 2
    }
  },
  {
    id: "reset-btn",
    type: "button",
    name: "按钮_恢复默认",
    refId: "reset-btn",
    rect: {
      x: 210,
      y: 1014,
      w: 168,
      h: 52
    },
    anchor: "b",
    animation: {
      enter: {
        preset: "scale",
        durationMs: 300,
        delayMs: 300
      },
      exit: {
        preset: "shrink",
        durationMs: 180,
        delayMs: 0
      }
    },
    style: {
      fontSize: 18,
      color: "rgba(220,232,242,0.85)",
      fill: "rgba(120,150,180,0.06)",
      borderColor: "rgba(220,232,242,0.25)",
      borderWidth: 1,
      radius: 6,
      letterSpacing: 4,
      opacity: 100
    },
    props: {
      text: "恢复默认"
    },
    events: {
      onClick: {
        type: "config.reset"
      }
    }
  },
  {
    id: "button-mrvvgpma-1",
    type: "button",
    name: "按钮_退出游戏",
    rect: {
      x: 1350,
      y: 1014,
      w: 168,
      h: 52
    },
    anchor: "b",
    style: {
      fontSize: 18,
      color: "rgba(220,232,242,0.85)",
      fill: "rgba(120,150,180,0.06)",
      borderColor: "rgba(220,232,242,0.25)",
      borderWidth: 1,
      radius: 6,
      letterSpacing: 4,
      opacity: 100
    },
    animation: {
      enter: {
        preset: "scale",
        durationMs: 300,
        delayMs: 300
      },
      exit: {
        preset: "shrink",
        durationMs: 180,
        delayMs: 0
      }
    },
    props: {
      text: "退出游戏"
    },
    events: {
      onClick: {
        type: "system.exit"
      }
    }
  },
  {
    id: "button-mrvvhi2h-2",
    type: "button",
    name: "按钮_返回标题",
    rect: {
      x: 1542,
      y: 1014,
      w: 168,
      h: 52
    },
    anchor: "b",
    style: {
      fontSize: 18,
      color: "rgba(220,232,242,0.85)",
      fill: "rgba(120,150,180,0.06)",
      borderColor: "rgba(220,232,242,0.25)",
      borderWidth: 1,
      radius: 6,
      letterSpacing: 4,
      opacity: 100
    },
    animation: {
      enter: {
        preset: "scale",
        durationMs: 300,
        delayMs: 300
      },
      exit: {
        preset: "shrink",
        durationMs: 180,
        delayMs: 0
      }
    },
    props: {
      text: "返回标题画面"
    },
    events: {
      onClick: {
        type: "system.openSlot",
        slot: "title"
      }
    }
  }
], vr = {
  version: Lt,
  name: At,
  canvas: zt,
  elements: Et
}, Sr = /* @__PURE__ */ Object.freeze(/* @__PURE__ */ Object.defineProperty({
  __proto__: null,
  canvas: zt,
  default: vr,
  elements: Et,
  name: At,
  version: Lt
}, Symbol.toStringTag, { value: "Module" })), Wt = 1, Bt = "标题画面", Dt = {
  width: 1920,
  height: 1080
}, jt = [
  {
    id: "vignette",
    type: "rect",
    name: "矩形_暗角遮罩",
    rect: {
      x: 0,
      y: 0,
      w: 1920,
      h: 1080
    },
    anchor: "c",
    style: {
      fill: "transparent",
      radius: 0,
      opacity: 100,
      customCss: "background: radial-gradient(ellipse 70% 80% at 0% 50%, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0) 55%), radial-gradient(ellipse 80% 60% at 100% 100%, rgba(0,0,0,0.50) 0%, rgba(0,0,0,0) 60%), linear-gradient(180deg, rgba(0,0,0,0.18) 0%, rgba(0,0,0,0) 22%, rgba(0,0,0,0) 78%, rgba(0,0,0,0.22) 100%); pointer-events: none;"
    },
    animation: {
      enter: {
        preset: "fade",
        durationMs: 600,
        delayMs: 0
      },
      exit: {
        preset: "fade",
        durationMs: 260,
        delayMs: 160
      }
    }
  },
  {
    id: "top-line",
    type: "line",
    name: "线条_顶部细线",
    rect: {
      x: 48,
      y: 40,
      w: 1824,
      h: 12
    },
    anchor: "t",
    style: {
      color: "rgba(255,255,255,0.14)",
      opacity: 60
    },
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 500,
        delayMs: 60
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 100
      }
    },
    props: {
      thickness: 1,
      lineStyle: "solid"
    }
  },
  {
    id: "version-tag",
    type: "text",
    name: "文字_版本号",
    rect: {
      x: 1536,
      y: 56,
      w: 320,
      h: 24
    },
    anchor: "tr",
    style: {
      fontSize: 10,
      color: "rgba(245,245,247,0.38)",
      letterSpacing: 6,
      textAlign: "right",
      opacity: 100,
      customCss: 'text-transform: uppercase; font-family: "JetBrains Mono", "SF Mono", "Menlo", "Monaco", "Consolas", monospace;'
    },
    animation: {
      enter: {
        preset: "fade",
        durationMs: 320,
        delayMs: 140
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 100
      }
    },
    props: {
      text: "AVG · ENGINE"
    }
  },
  {
    id: "studio-tag",
    type: "text",
    name: "文字_工作室标签",
    rect: {
      x: 80,
      y: 984,
      w: 400,
      h: 24
    },
    anchor: "bl",
    style: {
      fontSize: 10,
      color: "#d4a574",
      letterSpacing: 7,
      opacity: 100,
      customCss: 'text-transform: uppercase; font-family: "JetBrains Mono", "SF Mono", "Menlo", "Monaco", "Consolas", monospace;'
    },
    animation: {
      enter: {
        preset: "fade",
        durationMs: 360,
        delayMs: 220
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 80
      }
    },
    props: {
      text: "— LetsGal Studio"
    }
  },
  {
    id: "copyright",
    type: "text",
    name: "文字_版权",
    rect: {
      x: 1536,
      y: 984,
      w: 320,
      h: 24
    },
    anchor: "br",
    style: {
      fontSize: 10,
      color: "rgba(245,245,247,0.38)",
      letterSpacing: 4,
      textAlign: "right",
      opacity: 70,
      customCss: 'text-transform: uppercase; font-family: "JetBrains Mono", "SF Mono", "Menlo", "Monaco", "Consolas", monospace;'
    },
    animation: {
      enter: {
        preset: "fade",
        durationMs: 360,
        delayMs: 260
      },
      exit: {
        preset: "fade",
        durationMs: 160,
        delayMs: 80
      }
    },
    props: {
      text: "© 2026"
    }
  },
  {
    id: "menu-num-1",
    type: "text",
    name: "文字_编号01",
    rect: {
      x: 96,
      y: 424,
      w: 32,
      h: 32
    },
    anchor: "l",
    style: {
      fontSize: 14,
      color: "rgba(245,245,247,0.38)",
      letterSpacing: 3,
      fontWeight: 600,
      opacity: 100,
      customCss: 'font-family: "JetBrains Mono", "SF Mono", "Menlo", "Monaco", "Consolas", monospace;'
    },
    animation: {
      enter: {
        preset: "fade",
        durationMs: 260,
        delayMs: 180
      },
      exit: {
        preset: "fade",
        durationMs: 140,
        delayMs: 80
      }
    },
    props: {
      text: "01"
    }
  },
  {
    id: "menu-start",
    type: "button",
    name: "按钮_开始游戏",
    rect: {
      x: 144,
      y: 400,
      w: 520,
      h: 80
    },
    anchor: "l",
    style: {
      fontSize: 56,
      color: "#f5f5f7",
      fill: "transparent",
      borderWidth: 0,
      fontWeight: 600,
      letterSpacing: 1,
      textAlign: "left",
      opacity: 100,
      customCss: 'font-family: "Plus Jakarta Sans", "M PLUS Rounded 1c", "PingFang SC", "Hiragino Sans GB", "HarmonyOS Sans", "Microsoft YaHei", -apple-system, BlinkMacSystemFont, sans-serif; justify-content: flex-start; text-shadow: 0 2px 24px rgba(0,0,0,0.8); transition: color .18s cubic-bezier(0.22,1,0.36,1), transform .18s cubic-bezier(0.22,1,0.36,1); &:hover { color: #d4a574; transform: translateX(10px); }'
    },
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 420,
        delayMs: 200
      },
      exit: {
        preset: "slide-left",
        durationMs: 200,
        delayMs: 80
      }
    },
    props: {
      text: "开始游戏"
    },
    events: {
      onClick: {
        type: "system.newGame"
      }
    }
  },
  {
    id: "menu-num-2",
    type: "text",
    name: "文字_编号02",
    rect: {
      x: 96,
      y: 520,
      w: 32,
      h: 32
    },
    anchor: "l",
    style: {
      fontSize: 14,
      color: "rgba(245,245,247,0.38)",
      letterSpacing: 3,
      fontWeight: 600,
      opacity: 100,
      customCss: 'font-family: "JetBrains Mono", "SF Mono", "Menlo", "Monaco", "Consolas", monospace;'
    },
    animation: {
      enter: {
        preset: "fade",
        durationMs: 260,
        delayMs: 250
      },
      exit: {
        preset: "fade",
        durationMs: 140,
        delayMs: 60
      }
    },
    props: {
      text: "02"
    }
  },
  {
    id: "menu-load",
    type: "button",
    name: "按钮_读取存档",
    rect: {
      x: 144,
      y: 496,
      w: 520,
      h: 80
    },
    anchor: "l",
    style: {
      fontSize: 56,
      color: "#f5f5f7",
      fill: "transparent",
      borderWidth: 0,
      fontWeight: 600,
      letterSpacing: 1,
      textAlign: "left",
      opacity: 100,
      customCss: 'font-family: "Plus Jakarta Sans", "M PLUS Rounded 1c", "PingFang SC", "Hiragino Sans GB", "HarmonyOS Sans", "Microsoft YaHei", -apple-system, BlinkMacSystemFont, sans-serif; justify-content: flex-start; text-shadow: 0 2px 24px rgba(0,0,0,0.8); transition: color .18s cubic-bezier(0.22,1,0.36,1), transform .18s cubic-bezier(0.22,1,0.36,1); &:hover { color: #d4a574; transform: translateX(10px); }'
    },
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 420,
        delayMs: 270
      },
      exit: {
        preset: "slide-left",
        durationMs: 200,
        delayMs: 60
      }
    },
    props: {
      text: "读取存档"
    },
    events: {
      onClick: {
        type: "system.openSlot",
        slot: "load"
      }
    }
  },
  {
    id: "menu-num-3",
    type: "text",
    name: "文字_编号03",
    rect: {
      x: 96,
      y: 616,
      w: 32,
      h: 32
    },
    anchor: "l",
    style: {
      fontSize: 14,
      color: "rgba(245,245,247,0.38)",
      letterSpacing: 3,
      fontWeight: 600,
      opacity: 100,
      customCss: 'font-family: "JetBrains Mono", "SF Mono", "Menlo", "Monaco", "Consolas", monospace;'
    },
    animation: {
      enter: {
        preset: "fade",
        durationMs: 260,
        delayMs: 320
      },
      exit: {
        preset: "fade",
        durationMs: 140,
        delayMs: 40
      }
    },
    props: {
      text: "03"
    }
  },
  {
    id: "menu-gallery",
    type: "button",
    name: "按钮_鉴赏",
    rect: {
      x: 144,
      y: 592,
      w: 520,
      h: 80
    },
    anchor: "l",
    style: {
      fontSize: 56,
      color: "#f5f5f7",
      fill: "transparent",
      borderWidth: 0,
      fontWeight: 600,
      letterSpacing: 1,
      textAlign: "left",
      opacity: 100,
      customCss: 'font-family: "Plus Jakarta Sans", "M PLUS Rounded 1c", "PingFang SC", "Hiragino Sans GB", "HarmonyOS Sans", "Microsoft YaHei", -apple-system, BlinkMacSystemFont, sans-serif; justify-content: flex-start; text-shadow: 0 2px 24px rgba(0,0,0,0.8); transition: color .18s cubic-bezier(0.22,1,0.36,1), transform .18s cubic-bezier(0.22,1,0.36,1); &:hover { color: #d4a574; transform: translateX(10px); }'
    },
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 420,
        delayMs: 340
      },
      exit: {
        preset: "slide-left",
        durationMs: 200,
        delayMs: 40
      }
    },
    props: {
      text: "鉴赏"
    },
    events: {
      onClick: {
        type: "system.openSlot",
        slot: "gallery"
      }
    }
  },
  {
    id: "menu-num-4",
    type: "text",
    name: "文字_编号04",
    rect: {
      x: 96,
      y: 712,
      w: 32,
      h: 32
    },
    anchor: "l",
    style: {
      fontSize: 14,
      color: "rgba(245,245,247,0.38)",
      letterSpacing: 3,
      fontWeight: 600,
      opacity: 100,
      customCss: 'font-family: "JetBrains Mono", "SF Mono", "Menlo", "Monaco", "Consolas", monospace;'
    },
    animation: {
      enter: {
        preset: "fade",
        durationMs: 260,
        delayMs: 390
      },
      exit: {
        preset: "fade",
        durationMs: 140,
        delayMs: 20
      }
    },
    props: {
      text: "04"
    }
  },
  {
    id: "menu-settings",
    type: "button",
    name: "按钮_设置",
    rect: {
      x: 144,
      y: 688,
      w: 520,
      h: 80
    },
    anchor: "l",
    style: {
      fontSize: 56,
      color: "#f5f5f7",
      fill: "transparent",
      borderWidth: 0,
      fontWeight: 600,
      letterSpacing: 1,
      textAlign: "left",
      opacity: 100,
      customCss: 'font-family: "Plus Jakarta Sans", "M PLUS Rounded 1c", "PingFang SC", "Hiragino Sans GB", "HarmonyOS Sans", "Microsoft YaHei", -apple-system, BlinkMacSystemFont, sans-serif; justify-content: flex-start; text-shadow: 0 2px 24px rgba(0,0,0,0.8); transition: color .18s cubic-bezier(0.22,1,0.36,1), transform .18s cubic-bezier(0.22,1,0.36,1); &:hover { color: #d4a574; transform: translateX(10px); }'
    },
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 420,
        delayMs: 410
      },
      exit: {
        preset: "slide-left",
        durationMs: 200,
        delayMs: 20
      }
    },
    props: {
      text: "设置"
    },
    events: {
      onClick: {
        type: "system.openSlot",
        slot: "settings"
      }
    }
  },
  {
    id: "menu-num-5",
    type: "text",
    name: "文字_编号05",
    rect: {
      x: 96,
      y: 808,
      w: 32,
      h: 32
    },
    anchor: "l",
    style: {
      fontSize: 14,
      color: "rgba(245,245,247,0.38)",
      letterSpacing: 3,
      fontWeight: 600,
      opacity: 100,
      customCss: 'font-family: "JetBrains Mono", "SF Mono", "Menlo", "Monaco", "Consolas", monospace;'
    },
    animation: {
      enter: {
        preset: "fade",
        durationMs: 260,
        delayMs: 460
      },
      exit: {
        preset: "fade",
        durationMs: 140,
        delayMs: 0
      }
    },
    props: {
      text: "05"
    }
  },
  {
    id: "menu-exit",
    type: "button",
    name: "按钮_退出",
    rect: {
      x: 144,
      y: 784,
      w: 520,
      h: 80
    },
    anchor: "l",
    style: {
      fontSize: 56,
      color: "#f5f5f7",
      fill: "transparent",
      borderWidth: 0,
      fontWeight: 600,
      letterSpacing: 1,
      textAlign: "left",
      opacity: 100,
      customCss: 'font-family: "Plus Jakarta Sans", "M PLUS Rounded 1c", "PingFang SC", "Hiragino Sans GB", "HarmonyOS Sans", "Microsoft YaHei", -apple-system, BlinkMacSystemFont, sans-serif; justify-content: flex-start; text-shadow: 0 2px 24px rgba(0,0,0,0.8); transition: color .18s cubic-bezier(0.22,1,0.36,1), transform .18s cubic-bezier(0.22,1,0.36,1); &:hover { color: #d4a574; transform: translateX(10px); }'
    },
    animation: {
      enter: {
        preset: "slide-left",
        durationMs: 420,
        delayMs: 480
      },
      exit: {
        preset: "slide-left",
        durationMs: 200,
        delayMs: 0
      }
    },
    props: {
      text: "退出"
    },
    events: {
      onClick: {
        type: "system.exit"
      }
    }
  }
], Mr = {
  version: Wt,
  name: Bt,
  canvas: Dt,
  elements: jt
}, wr = /* @__PURE__ */ Object.freeze(/* @__PURE__ */ Object.defineProperty({
  __proto__: null,
  canvas: Dt,
  default: Mr,
  elements: jt,
  name: Bt,
  version: Wt
}, Symbol.toStringTag, { value: "Module" })), Ht = 1, Vt = {
  width: 1920,
  height: 1080
}, Yt = [
  {
    id: "toolbar",
    type: "rect",
    rect: {
      x: 210,
      y: 1027,
      w: 1500,
      h: 48
    },
    anchor: "b",
    name: "工具栏底图",
    style: {
      fontSize: 18,
      color: "#e8edf2",
      fill: "transparent",
      borderColor: "rgba(127, 212, 200, 0.28)",
      borderWidth: 0,
      radius: 27,
      letterSpacing: 1,
      opacity: 100
    },
    animation: {
      enter: {
        preset: "rise",
        durationMs: 420,
        delayMs: 30
      },
      exit: {
        preset: "sink",
        durationMs: 220,
        delayMs: 0
      }
    },
    props: {
      toolbarBackdrop: !0,
      toolbarOriginId: "toolbar"
    }
  },
  {
    id: "toolbar-part-0",
    type: "rect",
    name: "顶部强调线",
    rect: {
      x: 771.2582781456954,
      y: 1027,
      w: 377.4834437086093,
      h: 1.170731707317073
    },
    anchor: "b",
    style: {
      fill: "rgba(127,212,200,.7)",
      opacity: 100
    },
    props: {
      __smartTemplateRole: "toolbar-accent",
      toolbarOriginId: "toolbar"
    },
    events: {},
    animation: {
      enter: {
        preset: "rise",
        durationMs: 420,
        delayMs: 30
      },
      exit: {
        preset: "sink",
        durationMs: 220,
        delayMs: 0
      }
    }
  },
  {
    id: "toolbar-part-1",
    type: "button",
    name: "跳过按钮",
    rect: {
      x: 237.81456953642385,
      y: 1032.8536585365853,
      w: 160.485651214128,
      h: 37.46341463414634
    },
    hidden: !1,
    props: {
      __smartTemplateRole: "toolbar-button",
      toolbarAction: "skip",
      toolbarLabel: "跳过",
      toolbarOriginId: "toolbar",
      toolbarStandalone: !0,
      accentColor: "#7fd4c8"
    },
    children: [
      {
        id: "toolbar-part-1-0",
        type: "rect",
        name: "跳过按钮",
        rect: {
          x: 0,
          y: 0,
          w: 160.485651214128,
          h: 37.46341463414634
        },
        anchor: "c",
        style: {
          fill: "transparent",
          borderColor: "transparent",
          borderWidth: 1,
          radius: 17,
          color: "#e8edf2",
          opacity: 100
        },
        props: {
          text: "",
          __smartTemplateAction: "skip",
          __smartTemplateRole: "toolbar-surface"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-1-1",
        type: "text",
        name: "跳过图标",
        rect: {
          x: 28.587196467991163,
          y: 10.536585365853657,
          w: 27.81456953642384,
          h: 16.390243902439025
        },
        anchor: "c",
        style: {
          fontSize: 24,
          color: "#e8edf2",
          textAlign: "center",
          opacity: 100
        },
        props: {
          text: "»",
          __smartTemplateRole: "toolbar-icon"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-1-2",
        type: "text",
        name: "跳过文字",
        rect: {
          x: 62.362030905077255,
          y: 9.951219512195122,
          w: 69.5364238410596,
          h: 17.560975609756095
        },
        anchor: "c",
        style: {
          fontSize: 18,
          fontWeight: 400,
          color: "#e8edf2",
          letterSpacing: 2,
          textAlign: "center",
          opacity: 100
        },
        props: {
          text: "跳过",
          __smartTemplateRole: "toolbar-label"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-1-3",
        type: "rect",
        name: "跳过分隔线",
        rect: {
          x: 159.4922737306843,
          y: 8.780487804878048,
          w: 0.9933774834437086,
          h: 18.73170731707317
        },
        anchor: "c",
        style: {
          fill: "rgba(170,210,204,.28)",
          opacity: 100
        },
        props: {
          __smartTemplateRole: "toolbar-separator"
        },
        events: {},
        hidden: !1
      }
    ],
    anchor: "b",
    animation: {
      enter: {
        preset: "rise",
        durationMs: 420,
        delayMs: 30
      },
      exit: {
        preset: "sink",
        durationMs: 220,
        delayMs: 0
      }
    },
    style: {
      opacity: 100
    }
  },
  {
    id: "toolbar-part-2",
    type: "button",
    name: "自动按钮",
    rect: {
      x: 398.30022075055183,
      y: 1032.8536585365853,
      w: 160.485651214128,
      h: 37.46341463414634
    },
    hidden: !1,
    props: {
      __smartTemplateRole: "toolbar-button",
      toolbarAction: "auto",
      toolbarLabel: "自动",
      toolbarOriginId: "toolbar",
      toolbarStandalone: !0,
      accentColor: "#7fd4c8"
    },
    children: [
      {
        id: "toolbar-part-2-0",
        type: "rect",
        name: "自动按钮",
        rect: {
          x: 0,
          y: 0,
          w: 160.485651214128,
          h: 37.46341463414634
        },
        anchor: "c",
        style: {
          fill: "transparent",
          borderColor: "transparent",
          borderWidth: 1,
          radius: 17,
          color: "#e8edf2",
          opacity: 100
        },
        props: {
          text: "",
          __smartTemplateAction: "auto",
          __smartTemplateRole: "toolbar-surface"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-2-1",
        type: "text",
        name: "自动图标",
        rect: {
          x: 28.587196467991163,
          y: 10.536585365853657,
          w: 27.81456953642384,
          h: 16.390243902439025
        },
        anchor: "c",
        style: {
          fontSize: 24,
          color: "#e8edf2",
          textAlign: "center",
          opacity: 100
        },
        props: {
          text: "A",
          __smartTemplateRole: "toolbar-icon"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-2-2",
        type: "text",
        name: "自动文字",
        rect: {
          x: 62.362030905077255,
          y: 9.951219512195122,
          w: 69.5364238410596,
          h: 17.560975609756095
        },
        anchor: "c",
        style: {
          fontSize: 18,
          fontWeight: 400,
          color: "#e8edf2",
          letterSpacing: 2,
          textAlign: "center",
          opacity: 100
        },
        props: {
          text: "自动",
          __smartTemplateRole: "toolbar-label"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-2-3",
        type: "rect",
        name: "自动分隔线",
        rect: {
          x: 159.4922737306843,
          y: 8.780487804878048,
          w: 0.9933774834437086,
          h: 18.73170731707317
        },
        anchor: "c",
        style: {
          fill: "rgba(170,210,204,.28)",
          opacity: 100
        },
        props: {
          __smartTemplateRole: "toolbar-separator"
        },
        events: {},
        hidden: !1
      }
    ],
    anchor: "b",
    animation: {
      enter: {
        preset: "rise",
        durationMs: 420,
        delayMs: 30
      },
      exit: {
        preset: "sink",
        durationMs: 220,
        delayMs: 0
      }
    },
    style: {
      opacity: 100
    }
  },
  {
    id: "toolbar-part-3",
    type: "button",
    name: "存档按钮",
    rect: {
      x: 558.7858719646799,
      y: 1032.8536585365853,
      w: 160.485651214128,
      h: 37.46341463414634
    },
    hidden: !1,
    props: {
      __smartTemplateRole: "toolbar-button",
      toolbarAction: "save",
      toolbarLabel: "存档",
      toolbarOriginId: "toolbar",
      toolbarStandalone: !0,
      accentColor: "#7fd4c8"
    },
    children: [
      {
        id: "toolbar-part-3-0",
        type: "rect",
        name: "存档按钮",
        rect: {
          x: 0,
          y: 0,
          w: 160.485651214128,
          h: 37.46341463414634
        },
        anchor: "c",
        style: {
          fill: "transparent",
          borderColor: "transparent",
          borderWidth: 1,
          radius: 17,
          color: "#e8edf2",
          opacity: 100
        },
        props: {
          text: "",
          __smartTemplateAction: "save",
          __smartTemplateRole: "toolbar-surface"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-3-1",
        type: "text",
        name: "存档图标",
        rect: {
          x: 28.587196467991163,
          y: 10.536585365853657,
          w: 27.81456953642384,
          h: 16.390243902439025
        },
        anchor: "c",
        style: {
          fontSize: 24,
          color: "#e8edf2",
          textAlign: "center",
          opacity: 100
        },
        props: {
          text: "S",
          __smartTemplateRole: "toolbar-icon"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-3-2",
        type: "text",
        name: "存档文字",
        rect: {
          x: 62.362030905077255,
          y: 9.951219512195122,
          w: 69.5364238410596,
          h: 17.560975609756095
        },
        anchor: "c",
        style: {
          fontSize: 18,
          fontWeight: 400,
          color: "#e8edf2",
          letterSpacing: 2,
          textAlign: "center",
          opacity: 100
        },
        props: {
          text: "存档",
          __smartTemplateRole: "toolbar-label"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-3-3",
        type: "rect",
        name: "存档分隔线",
        rect: {
          x: 159.4922737306843,
          y: 8.780487804878048,
          w: 0.9933774834437086,
          h: 18.73170731707317
        },
        anchor: "c",
        style: {
          fill: "rgba(170,210,204,.28)",
          opacity: 100
        },
        props: {
          __smartTemplateRole: "toolbar-separator"
        },
        events: {},
        hidden: !1
      }
    ],
    anchor: "b",
    animation: {
      enter: {
        preset: "rise",
        durationMs: 420,
        delayMs: 30
      },
      exit: {
        preset: "sink",
        durationMs: 220,
        delayMs: 0
      }
    },
    style: {
      opacity: 100
    }
  },
  {
    id: "toolbar-part-4",
    type: "button",
    name: "读档按钮",
    rect: {
      x: 719.2715231788079,
      y: 1032.8536585365853,
      w: 160.485651214128,
      h: 37.46341463414634
    },
    hidden: !1,
    props: {
      __smartTemplateRole: "toolbar-button",
      toolbarAction: "load",
      toolbarLabel: "读档",
      toolbarOriginId: "toolbar",
      toolbarStandalone: !0,
      accentColor: "#7fd4c8"
    },
    children: [
      {
        id: "toolbar-part-4-0",
        type: "rect",
        name: "读档按钮",
        rect: {
          x: 0,
          y: 0,
          w: 160.485651214128,
          h: 37.46341463414634
        },
        anchor: "c",
        style: {
          fill: "transparent",
          borderColor: "transparent",
          borderWidth: 1,
          radius: 17,
          color: "#e8edf2",
          opacity: 100
        },
        props: {
          text: "",
          __smartTemplateAction: "load",
          __smartTemplateRole: "toolbar-surface"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-4-1",
        type: "text",
        name: "读档图标",
        rect: {
          x: 28.587196467991106,
          y: 10.536585365853657,
          w: 27.81456953642384,
          h: 16.390243902439025
        },
        anchor: "c",
        style: {
          fontSize: 24,
          color: "#e8edf2",
          textAlign: "center",
          opacity: 100
        },
        props: {
          text: "L",
          __smartTemplateRole: "toolbar-icon"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-4-2",
        type: "text",
        name: "读档文字",
        rect: {
          x: 62.3620309050772,
          y: 9.951219512195122,
          w: 69.5364238410596,
          h: 17.560975609756095
        },
        anchor: "c",
        style: {
          fontSize: 18,
          fontWeight: 400,
          color: "#e8edf2",
          letterSpacing: 2,
          textAlign: "center",
          opacity: 100
        },
        props: {
          text: "读档",
          __smartTemplateRole: "toolbar-label"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-4-3",
        type: "rect",
        name: "读档分隔线",
        rect: {
          x: 159.4922737306843,
          y: 8.780487804878048,
          w: 0.9933774834437086,
          h: 18.73170731707317
        },
        anchor: "c",
        style: {
          fill: "rgba(170,210,204,.28)",
          opacity: 100
        },
        props: {
          __smartTemplateRole: "toolbar-separator"
        },
        events: {},
        hidden: !1
      }
    ],
    anchor: "b",
    animation: {
      enter: {
        preset: "rise",
        durationMs: 420,
        delayMs: 30
      },
      exit: {
        preset: "sink",
        durationMs: 220,
        delayMs: 0
      }
    },
    style: {
      opacity: 100
    }
  },
  {
    id: "toolbar-part-5",
    type: "button",
    name: "快存按钮",
    rect: {
      x: 879.7571743929359,
      y: 1032.8536585365853,
      w: 160.485651214128,
      h: 37.46341463414634
    },
    hidden: !1,
    props: {
      __smartTemplateRole: "toolbar-button",
      toolbarAction: "quickSave",
      toolbarLabel: "快存",
      toolbarOriginId: "toolbar",
      toolbarStandalone: !0,
      accentColor: "#7fd4c8"
    },
    children: [
      {
        id: "toolbar-part-5-0",
        type: "rect",
        name: "快存按钮",
        rect: {
          x: 0,
          y: 0,
          w: 160.485651214128,
          h: 37.46341463414634
        },
        anchor: "c",
        style: {
          fill: "transparent",
          borderColor: "transparent",
          borderWidth: 1,
          radius: 17,
          color: "#e8edf2",
          opacity: 100
        },
        props: {
          text: "",
          __smartTemplateAction: "quickSave",
          __smartTemplateRole: "toolbar-surface"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-5-1",
        type: "text",
        name: "快存图标",
        rect: {
          x: 28.58719646799122,
          y: 10.536585365853657,
          w: 27.81456953642384,
          h: 16.390243902439025
        },
        anchor: "c",
        style: {
          fontSize: 24,
          color: "#e8edf2",
          textAlign: "center",
          opacity: 100
        },
        props: {
          text: "QS",
          __smartTemplateRole: "toolbar-icon"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-5-2",
        type: "text",
        name: "快存文字",
        rect: {
          x: 62.36203090507731,
          y: 9.951219512195122,
          w: 69.5364238410596,
          h: 17.560975609756095
        },
        anchor: "c",
        style: {
          fontSize: 18,
          fontWeight: 400,
          color: "#e8edf2",
          letterSpacing: 2,
          textAlign: "center",
          opacity: 100
        },
        props: {
          text: "快存",
          __smartTemplateRole: "toolbar-label"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-5-3",
        type: "rect",
        name: "快存分隔线",
        rect: {
          x: 159.4922737306843,
          y: 8.780487804878048,
          w: 0.9933774834437086,
          h: 18.73170731707317
        },
        anchor: "c",
        style: {
          fill: "rgba(170,210,204,.28)",
          opacity: 100
        },
        props: {
          __smartTemplateRole: "toolbar-separator"
        },
        events: {},
        hidden: !1
      }
    ],
    anchor: "b",
    animation: {
      enter: {
        preset: "rise",
        durationMs: 420,
        delayMs: 30
      },
      exit: {
        preset: "sink",
        durationMs: 220,
        delayMs: 0
      }
    },
    style: {
      opacity: 100
    }
  },
  {
    id: "toolbar-part-6",
    type: "button",
    name: "快读按钮",
    rect: {
      x: 1040.2428256070639,
      y: 1032.8536585365853,
      w: 160.485651214128,
      h: 37.46341463414634
    },
    hidden: !1,
    props: {
      __smartTemplateRole: "toolbar-button",
      toolbarAction: "quickLoad",
      toolbarLabel: "快读",
      toolbarOriginId: "toolbar",
      toolbarStandalone: !0,
      accentColor: "#7fd4c8"
    },
    children: [
      {
        id: "toolbar-part-6-0",
        type: "rect",
        name: "快读按钮",
        rect: {
          x: 0,
          y: 0,
          w: 160.485651214128,
          h: 37.46341463414634
        },
        anchor: "c",
        style: {
          fill: "transparent",
          borderColor: "transparent",
          borderWidth: 1,
          radius: 17,
          color: "#e8edf2",
          opacity: 100
        },
        props: {
          text: "",
          __smartTemplateAction: "quickLoad",
          __smartTemplateRole: "toolbar-surface"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-6-1",
        type: "text",
        name: "快读图标",
        rect: {
          x: 28.587196467991106,
          y: 10.536585365853657,
          w: 27.81456953642384,
          h: 16.390243902439025
        },
        anchor: "c",
        style: {
          fontSize: 24,
          color: "#e8edf2",
          textAlign: "center",
          opacity: 100
        },
        props: {
          text: "QL",
          __smartTemplateRole: "toolbar-icon"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-6-2",
        type: "text",
        name: "快读文字",
        rect: {
          x: 62.3620309050772,
          y: 9.951219512195122,
          w: 69.5364238410596,
          h: 17.560975609756095
        },
        anchor: "c",
        style: {
          fontSize: 18,
          fontWeight: 400,
          color: "#e8edf2",
          letterSpacing: 2,
          textAlign: "center",
          opacity: 100
        },
        props: {
          text: "快读",
          __smartTemplateRole: "toolbar-label"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-6-3",
        type: "rect",
        name: "快读分隔线",
        rect: {
          x: 159.4922737306843,
          y: 8.780487804878048,
          w: 0.9933774834437086,
          h: 18.73170731707317
        },
        anchor: "c",
        style: {
          fill: "rgba(170,210,204,.28)",
          opacity: 100
        },
        props: {
          __smartTemplateRole: "toolbar-separator"
        },
        events: {},
        hidden: !1
      }
    ],
    anchor: "b",
    animation: {
      enter: {
        preset: "rise",
        durationMs: 420,
        delayMs: 30
      },
      exit: {
        preset: "sink",
        durationMs: 220,
        delayMs: 0
      }
    },
    style: {
      opacity: 100
    }
  },
  {
    id: "toolbar-part-7",
    type: "button",
    name: "历史按钮",
    rect: {
      x: 1200.728476821192,
      y: 1032.8536585365853,
      w: 160.485651214128,
      h: 37.46341463414634
    },
    hidden: !1,
    props: {
      __smartTemplateRole: "toolbar-button",
      toolbarAction: "history",
      toolbarLabel: "历史",
      toolbarOriginId: "toolbar",
      toolbarStandalone: !0,
      accentColor: "#7fd4c8"
    },
    children: [
      {
        id: "toolbar-part-7-0",
        type: "rect",
        name: "历史按钮",
        rect: {
          x: 0,
          y: 0,
          w: 160.485651214128,
          h: 37.46341463414634
        },
        anchor: "c",
        style: {
          fill: "transparent",
          borderColor: "transparent",
          borderWidth: 1,
          radius: 17,
          color: "#e8edf2",
          opacity: 100
        },
        props: {
          text: "",
          __smartTemplateAction: "history",
          __smartTemplateRole: "toolbar-surface"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-7-1",
        type: "text",
        name: "历史图标",
        rect: {
          x: 28.58719646799122,
          y: 10.536585365853657,
          w: 27.81456953642384,
          h: 16.390243902439025
        },
        anchor: "c",
        style: {
          fontSize: 24,
          color: "#e8edf2",
          textAlign: "center",
          opacity: 100
        },
        props: {
          text: "↺",
          __smartTemplateRole: "toolbar-icon"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-7-2",
        type: "text",
        name: "历史文字",
        rect: {
          x: 62.36203090507731,
          y: 9.951219512195122,
          w: 69.5364238410596,
          h: 17.560975609756095
        },
        anchor: "c",
        style: {
          fontSize: 18,
          fontWeight: 400,
          color: "#e8edf2",
          letterSpacing: 2,
          textAlign: "center",
          opacity: 100
        },
        props: {
          text: "历史",
          __smartTemplateRole: "toolbar-label"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-7-3",
        type: "rect",
        name: "历史分隔线",
        rect: {
          x: 159.4922737306842,
          y: 8.780487804878048,
          w: 0.9933774834437086,
          h: 18.73170731707317
        },
        anchor: "c",
        style: {
          fill: "rgba(170,210,204,.28)",
          opacity: 100
        },
        props: {
          __smartTemplateRole: "toolbar-separator"
        },
        events: {},
        hidden: !1
      }
    ],
    anchor: "b",
    animation: {
      enter: {
        preset: "rise",
        durationMs: 420,
        delayMs: 30
      },
      exit: {
        preset: "sink",
        durationMs: 220,
        delayMs: 0
      }
    },
    style: {
      opacity: 100
    }
  },
  {
    id: "toolbar-part-8",
    type: "button",
    name: "设置按钮",
    rect: {
      x: 1361.2141280353198,
      y: 1032.8536585365853,
      w: 160.485651214128,
      h: 37.46341463414634
    },
    hidden: !1,
    props: {
      __smartTemplateRole: "toolbar-button",
      toolbarAction: "settings",
      toolbarLabel: "设置",
      toolbarOriginId: "toolbar",
      toolbarStandalone: !0,
      accentColor: "#7fd4c8"
    },
    children: [
      {
        id: "toolbar-part-8-0",
        type: "rect",
        name: "设置按钮",
        rect: {
          x: 0,
          y: 0,
          w: 160.485651214128,
          h: 37.46341463414634
        },
        anchor: "c",
        style: {
          fill: "transparent",
          borderColor: "transparent",
          borderWidth: 1,
          radius: 17,
          color: "#e8edf2",
          opacity: 100
        },
        props: {
          text: "",
          __smartTemplateAction: "settings",
          __smartTemplateRole: "toolbar-surface"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-8-1",
        type: "text",
        name: "设置图标",
        rect: {
          x: 28.58719646799122,
          y: 10.536585365853657,
          w: 27.81456953642384,
          h: 16.390243902439025
        },
        anchor: "c",
        style: {
          fontSize: 24,
          color: "#e8edf2",
          textAlign: "center",
          opacity: 100
        },
        props: {
          text: "◇",
          __smartTemplateRole: "toolbar-icon"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-8-2",
        type: "text",
        name: "设置文字",
        rect: {
          x: 62.36203090507731,
          y: 9.951219512195122,
          w: 69.5364238410596,
          h: 17.560975609756095
        },
        anchor: "c",
        style: {
          fontSize: 18,
          fontWeight: 400,
          color: "#e8edf2",
          letterSpacing: 2,
          textAlign: "center",
          opacity: 100
        },
        props: {
          text: "设置",
          __smartTemplateRole: "toolbar-label"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-8-3",
        type: "rect",
        name: "设置分隔线",
        rect: {
          x: 159.49227373068442,
          y: 8.780487804878048,
          w: 0.9933774834437086,
          h: 18.73170731707317
        },
        anchor: "c",
        style: {
          fill: "rgba(170,210,204,.28)",
          opacity: 100
        },
        props: {
          __smartTemplateRole: "toolbar-separator"
        },
        events: {},
        hidden: !1
      }
    ],
    anchor: "b",
    animation: {
      enter: {
        preset: "rise",
        durationMs: 420,
        delayMs: 30
      },
      exit: {
        preset: "sink",
        durationMs: 220,
        delayMs: 0
      }
    },
    style: {
      opacity: 100
    }
  },
  {
    id: "toolbar-part-9",
    type: "button",
    name: "隐藏按钮",
    rect: {
      x: 1521.699779249448,
      y: 1032.8536585365853,
      w: 160.485651214128,
      h: 37.46341463414634
    },
    hidden: !1,
    props: {
      __smartTemplateRole: "toolbar-button",
      toolbarAction: "hide",
      toolbarLabel: "隐藏",
      toolbarOriginId: "toolbar",
      toolbarStandalone: !0,
      accentColor: "#7fd4c8"
    },
    children: [
      {
        id: "toolbar-part-9-0",
        type: "rect",
        name: "隐藏按钮",
        rect: {
          x: 0,
          y: 0,
          w: 160.485651214128,
          h: 37.46341463414634
        },
        anchor: "c",
        style: {
          fill: "transparent",
          borderColor: "transparent",
          borderWidth: 1,
          radius: 17,
          color: "#e8edf2",
          opacity: 100
        },
        props: {
          text: "",
          __smartTemplateAction: "hide",
          __smartTemplateRole: "toolbar-surface"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-9-1",
        type: "text",
        name: "隐藏图标",
        rect: {
          x: 28.58719646799122,
          y: 10.536585365853657,
          w: 27.81456953642384,
          h: 16.390243902439025
        },
        anchor: "c",
        style: {
          fontSize: 24,
          color: "#e8edf2",
          textAlign: "center",
          opacity: 100
        },
        props: {
          text: "—",
          __smartTemplateRole: "toolbar-icon"
        },
        events: {},
        hidden: !1
      },
      {
        id: "toolbar-part-9-2",
        type: "text",
        name: "隐藏文字",
        rect: {
          x: 62.36203090507731,
          y: 9.951219512195122,
          w: 69.5364238410596,
          h: 17.560975609756095
        },
        anchor: "c",
        style: {
          fontSize: 18,
          fontWeight: 400,
          color: "#e8edf2",
          letterSpacing: 2,
          textAlign: "center",
          opacity: 100
        },
        props: {
          text: "隐藏",
          __smartTemplateRole: "toolbar-label"
        },
        events: {},
        hidden: !1
      }
    ],
    anchor: "b",
    animation: {
      enter: {
        preset: "rise",
        durationMs: 420,
        delayMs: 30
      },
      exit: {
        preset: "sink",
        durationMs: 220,
        delayMs: 0
      }
    },
    style: {
      opacity: 100
    }
  }
], Gt = "对话工具栏", kr = {
  version: Ht,
  canvas: Vt,
  elements: Yt,
  name: Gt
}, _r = /* @__PURE__ */ Object.freeze(/* @__PURE__ */ Object.defineProperty({
  __proto__: null,
  canvas: Vt,
  default: kr,
  elements: Yt,
  name: Gt,
  version: Ht
}, Symbol.toStringTag, { value: "Module" })), ke = {
  id: "avg.internal.default-shell",
  name: "默认游戏壳",
  description: "标题/存档/历史/设置/工具栏及剧情选项、标准输入、消息弹层一体的默认游戏 UI。每个 UI 子模块都可单独替换。",
  author: "LetsGal Studio",
  version: "1.0.0",
  // 跟用户扩展同形态:vite build 出 dist/index.mjs,加载方按 manifest.entry 找。
  // 历史上(2026-05 前)这里写的是 "<internal>",当时 default-shell 走 TS
  // 源码直接 import 进 Studio renderer bundle 的路径;2026-05-15 全栈统一后
  // 走真正的 ESM bundle 加载链路,entry 也跟着规范化。
  entry: "dist/index.mjs",
  // SDK 契约当前停在 1.x(src/sdk/constants.ts 的 SDK_VERSION = "1.0.0");
  // 历史上这里误写成 ">=2.0.0",2026-06 加载时兼容校验落地前理顺为 1.x 声明。
  sdkVersion: ">=1.0.0",
  // 2026-05 Internal Extension Points:DefaultShell 是引擎内置兜底扩展,
  // 不可禁用、不可卸载。仅 avg.internal.* namespace 可声明 builtin: true。
  // 详见 /docs/plans/2026-05-14-internal-extension-points-design.md §5.1
  builtin: !0,
  contributes: {
    dialogueBoxStyles: [
      {
        id: "landing",
        name: "默认对话框",
        description: "LetsGal 的唯一系统对话框基线。项目未选择其它扩展样式时使用。",
        visualUI: "dialogue-box",
        dialogueBox: {}
      }
    ]
  }
  // 静态 manifest.actions 字段已在 2026-05 设计中废弃,扩展贡献的 action
  // 通过 onRegister 阶段调 ctx.input.registerAction(...) 注册即可。
}, t = {
  // ---- color ----
  bgOverlay: "rgba(11, 13, 16, 0.82)",
  bgOverlayStrong: "rgba(11, 13, 16, 0.92)",
  bgSurface: "rgba(255, 255, 255, 0.04)",
  bgElevated: "rgba(255, 255, 255, 0.07)",
  bgSunken: "rgba(0, 0, 0, 0.28)",
  borderSubtle: "rgba(255, 255, 255, 0.08)",
  borderRegular: "rgba(255, 255, 255, 0.14)",
  borderStrong: "rgba(255, 255, 255, 0.24)",
  borderAccent: "rgba(212, 165, 116, 0.55)",
  textPrimary: "#f5f5f7",
  textMuted: "rgba(245, 245, 247, 0.62)",
  textFaint: "rgba(245, 245, 247, 0.38)",
  textOnAccent: "#1a1410",
  accent: "#d4a574",
  accentSoft: "rgba(212, 165, 116, 0.16)",
  accentGlow: "rgba(212, 165, 116, 0.32)",
  danger: "#e0635a",
  // ---- typography ----
  // 风格:现代圆润黑体(geometric rounded sans),不要衬线/宋体
  // - fontDisplay  : 大字标题用,粗+圆润,系统圆润字体优先
  // - fontUI       : 正文/按钮用,中粗黑体
  // - fontMono     : 数字/timestamp,等宽
  fontDisplay: '"Plus Jakarta Sans", "M PLUS Rounded 1c", "PingFang SC", "Hiragino Sans GB", "HarmonyOS Sans", "Microsoft YaHei", -apple-system, BlinkMacSystemFont, sans-serif',
  fontUI: '"Plus Jakarta Sans", "Noto Sans SC", "PingFang SC", "Hiragino Sans GB", "HarmonyOS Sans", "Microsoft YaHei", -apple-system, BlinkMacSystemFont, "Helvetica Neue", sans-serif',
  fontMono: '"JetBrains Mono", "SF Mono", "Menlo", "Monaco", "Consolas", monospace',
  // ---- motion ----
  // quint-out 是公认最 silky 的 UI 缓动之一
  easeOut: "cubic-bezier(0.22, 1, 0.36, 1)",
  easeIn: "cubic-bezier(0.64, 0, 0.78, 0)",
  // 2026-05 提速:从 180/280/420 收紧到 140/220/320。
  // 原值整体偏慢一档,玩家反馈"重、迟钝"。新值与 Vercel/Linear 这类
  // 现代 UI 的节奏对齐,同时保留 quint-out 的丝滑感。
  durFast: 140,
  durBase: 220,
  durSlow: 320,
  // ---- spacing & radius ----
  radiusSm: 6,
  radiusMd: 10,
  radiusLg: 16,
  radiusPill: 999
}, _e = "avg-default-shell-shared-style";
function $r() {
  if (typeof document > "u" || document.getElementById(_e)) return;
  const e = document.createElement("style");
  e.id = _e, e.textContent = `
    /* overlay:只动 opacity,backdrop-filter 用 inline 写死避免合成层重建闪烁 */
    @keyframes avg-overlay-in {
      from { opacity: 0; }
      to   { opacity: 1; }
    }
    @keyframes avg-overlay-out {
      from { opacity: 1; }
      to   { opacity: 0; }
    }
    @keyframes avg-content-rise {
      from { opacity: 0; transform: translateY(14px); }
      to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes avg-content-fall {
      from { opacity: 1; transform: translateY(0); }
      to   { opacity: 0; transform: translateY(8px); }
    }
    @keyframes avg-stagger-rise {
      from { opacity: 0; transform: translateY(10px); }
      to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes avg-title-reveal {
      from {
        opacity: 0;
        transform: translateY(18px);
        letter-spacing: 0.04em;
        filter: blur(6px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
        letter-spacing: 0.02em;
        filter: blur(0);
      }
    }
    @keyframes avg-page-slide-in-right {
      from { opacity: 0; transform: translateX(24px); }
      to   { opacity: 1; transform: translateX(0); }
    }
    @keyframes avg-page-slide-in-left {
      from { opacity: 0; transform: translateX(-24px); }
      to   { opacity: 1; transform: translateX(0); }
    }
    @keyframes avg-pulse-glow {
      0%, 100% { box-shadow: 0 0 0 0 rgba(212, 165, 116, 0); }
      50%      { box-shadow: 0 0 0 6px rgba(212, 165, 116, 0.06); }
    }
    @keyframes avg-row-rise {
      from { opacity: 0; transform: translateY(12px) scale(0.98); }
      to   { opacity: 1; transform: translateY(0) scale(1); }
    }
    @keyframes avg-card-rise {
      from { opacity: 0; transform: translateY(20px) scale(0.96); filter: blur(4px); }
      to   { opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }
    }
    @keyframes avg-header-slide {
      from { opacity: 0; transform: translateX(-16px); filter: blur(4px); }
      to   { opacity: 1; transform: translateX(0); filter: blur(0); }
    }
    @keyframes avg-line-expand {
      from { transform: scaleX(0); opacity: 0; }
      to   { transform: scaleX(1); opacity: 1; }
    }
    /* 工具栏按钮 active 态呼吸:用于标注当前处于 auto/skip 模式。
       双 keyframe 周期 2.4s,opacity + box-shadow 同步呼吸,
       动效柔和不抢戏。 */
    @keyframes avg-toolbar-active-breath {
      0%, 100% {
        opacity: 0.85;
        box-shadow: 0 0 0 0 rgba(212, 165, 116, 0.0);
      }
      50% {
        opacity: 1;
        box-shadow: 0 0 18px 2px rgba(212, 165, 116, 0.35);
      }
    }

    .avg-shell-scrollbar::-webkit-scrollbar { width: 8px; height: 8px; }
    .avg-shell-scrollbar::-webkit-scrollbar-track { background: transparent; }
    .avg-shell-scrollbar::-webkit-scrollbar-thumb {
      background: rgba(255, 255, 255, 0.08);
      border-radius: 999px;
      transition: background 220ms cubic-bezier(0.22, 1, 0.36, 1);
    }
    .avg-shell-scrollbar::-webkit-scrollbar-thumb:hover {
      background: rgba(255, 255, 255, 0.18);
    }

    @media (prefers-reduced-motion: reduce) {
      [class*="avg-anim"] { animation: none !important; }
    }
  `, document.head.appendChild(e);
}
$r();
async function G(e) {
  try {
    await e;
  } catch (r) {
    if (!Cr(r)) throw r;
  }
}
function Cr(e) {
  if (!e || typeof e != "object") return !1;
  const r = e;
  return r.name === "AbortError" && typeof r.message == "string" && (r.message === "Engine 已销毁" || r.message.startsWith("Engine 已销毁，"));
}
function H() {
  const [e, r] = $(!1), a = V(0), n = V(null), o = me(() => {
    if (n.current !== null) return;
    const l = Date.now() - a.current, u = 80;
    l >= u ? r(!1) : n.current = window.setTimeout(() => {
      n.current = null, r(!1);
    }, u - l);
  }, []), s = me(() => {
    n.current !== null && (window.clearTimeout(n.current), n.current = null), a.current = Date.now(), r(!0);
  }, []);
  return L(() => {
    if (!e) return;
    const l = () => o();
    return window.addEventListener("pointerup", l), window.addEventListener("pointercancel", l), () => {
      window.removeEventListener("pointerup", l), window.removeEventListener("pointercancel", l);
    };
  }, [e, o]), {
    pressed: e,
    handlers: {
      onPointerDown: s,
      onPointerLeave: o
    }
  };
}
var Ir = Object.defineProperty, Fr = Object.getOwnPropertyDescriptor, Tr = (e, r, a) => r in e ? Ir(e, r, { enumerable: !0, configurable: !0, writable: !0, value: a }) : e[r] = a, Or = (e, r, a, n) => {
  for (var o = n > 1 ? void 0 : n ? Fr(r, a) : r, s = e.length - 1, l; s >= 0; s--)
    (l = e[s]) && (o = l(o) || o);
  return o;
}, Pr = (e, r, a) => Tr(e, r + "", a);
const Rr = [
  { key: "start", settingKey: "startLabel", defaultLabel: "开始游戏" },
  { key: "load", settingKey: "loadLabel", defaultLabel: "读取存档" },
  { key: "gallery", settingKey: "galleryLabel", defaultLabel: "鉴赏" },
  { key: "settings", settingKey: "settingsLabel", defaultLabel: "设置" },
  { key: "exit", settingKey: "exitLabel", defaultLabel: "退出" }
], Lr = () => {
  const e = ee(), r = e.settings.get("showGallery") ?? !0, a = Rr.filter(
    (d) => d.key !== "gallery" || r
  ).map((d) => {
    const m = (e.settings.get(d.settingKey) ?? "").trim();
    return { key: d.key, label: m || d.defaultLabel };
  }), [n, o] = $(!1), [s, l] = $(null), u = (d) => {
    o(!0), window.setTimeout(d, t.durBase);
  }, c = (d) => {
    d === "start" ? u(() => e.ui.hide("title-screen")) : d === "load" ? G(
      e.system.invoke(P.Load, {
        mode: "load",
        source: "title"
      })
    ) : d === "gallery" ? G(
      e.system.invoke(P.Gallery)
    ) : d === "settings" ? G(
      e.system.invoke(P.Settings)
    ) : d === "exit" && u(() => e.game.exit());
  }, [g, b] = $(!1);
  L(() => {
    const d = requestAnimationFrame(() => b(!0));
    return () => cancelAnimationFrame(d);
  }, []);
  const f = g && !n;
  return /* @__PURE__ */ S(
    "div",
    {
      style: {
        position: "absolute",
        inset: 0,
        backgroundColor: "transparent",
        color: t.textPrimary,
        fontFamily: t.fontUI,
        overflow: "hidden",
        opacity: f ? 1 : 0,
        transition: `opacity ${t.durBase}ms ${t.easeOut}`
      },
      children: [
        /* @__PURE__ */ i(
          "div",
          {
            style: {
              position: "absolute",
              inset: 0,
              background: `
            radial-gradient(ellipse 70% 80% at 0% 50%, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0) 55%),
            radial-gradient(ellipse 80% 60% at 100% 100%, rgba(0,0,0,0.50) 0%, rgba(0,0,0,0) 60%),
            linear-gradient(180deg, rgba(0,0,0,0.18) 0%, rgba(0,0,0,0) 22%, rgba(0,0,0,0) 78%, rgba(0,0,0,0.22) 100%)
          `,
              pointerEvents: "none",
              opacity: f ? 1 : 0,
              transition: `opacity ${t.durSlow}ms ${t.easeOut}`
            }
          }
        ),
        /* @__PURE__ */ i(
          "div",
          {
            style: {
              position: "absolute",
              top: 40,
              left: "50%",
              height: 1,
              background: `linear-gradient(90deg, transparent 0%, ${t.borderRegular} 30%, ${t.borderRegular} 70%, transparent 100%)`,
              width: f ? "calc(100% - 96px)" : 0,
              transform: "translateX(-50%)",
              transition: `width ${t.durSlow}ms ${t.easeOut} 50ms`,
              opacity: 0.6
            }
          }
        ),
        /* @__PURE__ */ i(
          "div",
          {
            style: {
              position: "absolute",
              top: 56,
              right: 64,
              fontFamily: t.fontMono,
              fontSize: 10,
              letterSpacing: "0.32em",
              textTransform: "uppercase",
              color: t.textFaint,
              opacity: f ? 1 : 0,
              transition: `opacity ${t.durSlow}ms ${t.easeOut} 140ms`
            },
            children: "AVG · ENGINE"
          }
        ),
        /* @__PURE__ */ i(
          "div",
          {
            style: {
              position: "absolute",
              bottom: 48,
              left: 80,
              fontFamily: t.fontMono,
              fontSize: 10,
              letterSpacing: "0.40em",
              textTransform: "uppercase",
              color: t.accent,
              opacity: f ? 1 : 0,
              transform: f ? "translateY(0)" : "translateY(6px)",
              transition: `all ${t.durSlow}ms ${t.easeOut} 130ms`
            },
            children: "— LetsGal Studio"
          }
        ),
        /* @__PURE__ */ S(
          "div",
          {
            style: {
              position: "absolute",
              bottom: 48,
              right: 64,
              fontFamily: t.fontMono,
              fontSize: 10,
              letterSpacing: "0.24em",
              textTransform: "uppercase",
              color: t.textFaint,
              opacity: f ? 0.7 : 0,
              transition: `opacity ${t.durSlow}ms ${t.easeOut} 160ms`
            },
            children: [
              "© ",
              (/* @__PURE__ */ new Date()).getFullYear()
            ]
          }
        ),
        /* @__PURE__ */ i(
          "nav",
          {
            "aria-label": "主菜单",
            style: {
              position: "absolute",
              left: 96,
              top: "50%",
              transform: "translateY(-50%)",
              display: "flex",
              flexDirection: "column",
              gap: 8
            },
            children: a.map((d, m) => /* @__PURE__ */ i(
              Ar,
              {
                index: m,
                label: d.label,
                isHover: s === d.key,
                isOtherHover: s !== null && s !== d.key,
                visible: f,
                onMouseEnter: () => l(d.key),
                onMouseLeave: () => l(null),
                onClick: () => c(d.key)
              },
              d.key
            ))
          }
        )
      ]
    }
  );
}, Ar = ({
  index: e,
  label: r,
  isHover: a,
  isOtherHover: n,
  visible: o,
  onMouseEnter: s,
  onMouseLeave: l,
  onClick: u
}) => {
  const c = H(), g = o ? c.pressed ? 4 : a ? 10 : 0 : -16;
  return /* @__PURE__ */ S(
    "button",
    {
      onMouseEnter: s,
      onMouseLeave: (b) => {
        l(), c.handlers.onPointerLeave(b);
      },
      onPointerDown: c.handlers.onPointerDown,
      onClick: u,
      style: {
        position: "relative",
        appearance: "none",
        background: "transparent",
        border: "none",
        color: c.pressed || a ? t.accent : t.textPrimary,
        fontFamily: t.fontDisplay,
        fontSize: "clamp(36px, 4.2vw, 56px)",
        fontWeight: 600,
        lineHeight: 1.15,
        letterSpacing: "0.01em",
        padding: "12px 0 12px 96px",
        textAlign: "left",
        cursor: "default",
        textShadow: "0 2px 24px rgba(0,0,0,0.8)",
        opacity: o ? n ? 0.4 : 1 : 0,
        transform: `translateX(${g}px) scale(${c.pressed ? 0.985 : 1})`,
        transformOrigin: "left center",
        filter: c.pressed ? "brightness(1.1)" : "brightness(1)",
        transition: `color ${t.durFast}ms ${t.easeOut}, transform ${t.durFast}ms ${t.easeOut}, opacity ${t.durBase}ms ${t.easeOut}, filter ${t.durFast}ms ${t.easeOut}`,
        animation: o ? `avg-stagger-rise ${t.durSlow}ms ${t.easeOut} ${360 + e * 55}ms both` : "none",
        whiteSpace: "nowrap",
        userSelect: "none"
      },
      children: [
        /* @__PURE__ */ i(
          "span",
          {
            "aria-hidden": !0,
            style: {
              position: "absolute",
              left: 0,
              top: "50%",
              transform: "translateY(-50%)",
              fontFamily: t.fontMono,
              fontSize: 14,
              letterSpacing: "0.18em",
              color: a ? t.accent : t.textFaint,
              fontWeight: 600,
              transition: `color ${t.durBase}ms ${t.easeOut}`,
              fontVariantNumeric: "tabular-nums"
            },
            children: String(e + 1).padStart(2, "0")
          }
        ),
        /* @__PURE__ */ i(
          "span",
          {
            "aria-hidden": !0,
            style: {
              position: "absolute",
              left: 36,
              top: "50%",
              height: 2,
              background: t.accent,
              width: a ? 52 : 0,
              transform: "translateY(-50%)",
              transition: `width ${t.durBase}ms ${t.easeOut}`,
              boxShadow: a ? `0 0 12px ${t.accentGlow}` : "none",
              borderRadius: 999
            }
          }
        ),
        r
      ]
    }
  );
};
let be = class extends Z {
  render() {
    return { component: Lr, props: {} };
  }
};
Pr(be, "settings", K((e) => ({
  startLabel: e.string("「开始游戏」按钮文本").default("开始游戏"),
  loadLabel: e.string("「读取存档」按钮文本").default("读取存档"),
  showGallery: e.boolean("显示「鉴赏」菜单项").default(!0),
  galleryLabel: e.string("「鉴赏」按钮文本").default("鉴赏").enabledWhen("showGallery"),
  settingsLabel: e.string("「设置」按钮文本").default("设置"),
  exitLabel: e.string("「退出」按钮文本").default("退出")
})));
be = Or([
  Q({
    id: "title-screen",
    label: "标题画面",
    exposeUI: !1,
    // 1.6.0 起只导出 ui/title-screen.json,React 版不再进入 UI 列表
    // 2026-05 Internal Extension Points §6.1:声明本 UI 实现哪些系统槽位。
    supportsSlot: P.Title
  })
], be);
function A(e) {
  const [r, a] = $(!1), n = e.delay ?? 0, o = e.duration ?? t.durSlow;
  return L(() => {
    const l = window.setTimeout(() => a(!0), n);
    return () => window.clearTimeout(l);
  }, [n]), r ? {
    opacity: 1,
    transform: "none",
    filter: "none",
    transition: `opacity ${o}ms ${t.easeOut}, transform ${o}ms ${t.easeOut}, filter ${o}ms ${t.easeOut}`
  } : {
    ...e.hidden,
    transition: "none"
  };
}
function le(e) {
  const [r, a] = $(!1);
  return L(() => {
    const n = window.setTimeout(() => a(!0), 0);
    return () => window.clearTimeout(n);
  }, []), e === "exit" ? {
    opacity: 0,
    transition: `opacity ${t.durFast}ms ${t.easeIn}`
  } : r ? {
    opacity: 1,
    transition: `opacity ${t.durBase}ms ${t.easeOut}`
  } : { opacity: 0, transition: "none" };
}
function de(e, r, a = t.durFast) {
  const [n, o] = $("shown"), s = me(() => {
    o((l) => l === "exit" ? l : "exit"), window.setTimeout(() => {
      e.ui.hide(r);
    }, a);
  }, [e, r, a]);
  return { phase: n, requestClose: s };
}
const ce = ({ eyebrow: e, title: r, rightSlot: a }) => {
  const n = A({
    hidden: { opacity: 0, transform: "translateX(-16px)" },
    delay: 40
  }), o = A({
    hidden: { opacity: 0, transform: "scaleX(0)" },
    delay: 180
  }), s = A({
    hidden: { opacity: 0, transform: "translateY(10px)" },
    delay: 120
  });
  return /* @__PURE__ */ S(
    "header",
    {
      style: {
        padding: "48px 80px 32px",
        display: "flex",
        alignItems: "flex-end",
        gap: 24
      },
      children: [
        /* @__PURE__ */ S("div", { style: n, children: [
          /* @__PURE__ */ i(
            "div",
            {
              style: {
                fontFamily: t.fontMono,
                fontSize: 11,
                letterSpacing: "0.36em",
                textTransform: "uppercase",
                color: t.accent,
                marginBottom: 12,
                fontWeight: 600
              },
              children: e
            }
          ),
          /* @__PURE__ */ i(
            "h2",
            {
              style: {
                fontFamily: t.fontDisplay,
                fontSize: "clamp(40px, 4.4vw, 60px)",
                fontWeight: 700,
                margin: 0,
                letterSpacing: "0.005em",
                lineHeight: 1.05
              },
              children: r
            }
          ),
          /* @__PURE__ */ i(
            "div",
            {
              style: {
                marginTop: 16,
                width: 64,
                height: 3,
                background: t.accent,
                borderRadius: 999,
                transformOrigin: "left center",
                boxShadow: `0 0 12px ${t.accentGlow}`,
                ...o
              }
            }
          )
        ] }),
        /* @__PURE__ */ i(
          "div",
          {
            style: {
              marginLeft: "auto",
              display: "flex",
              alignItems: "center",
              gap: 12,
              ...s
            },
            children: a
          }
        )
      ]
    }
  );
}, zr = ({ onClick: e, children: r }) => {
  const [a, n] = $(!1), o = H();
  return /* @__PURE__ */ i(
    "button",
    {
      onClick: e,
      onMouseEnter: () => n(!0),
      onMouseLeave: (s) => {
        n(!1), o.handlers.onPointerLeave(s);
      },
      onPointerDown: o.handlers.onPointerDown,
      style: {
        appearance: "none",
        background: a ? t.bgElevated : t.bgSurface,
        border: `1px solid ${a ? t.borderRegular : t.borderSubtle}`,
        borderRadius: t.radiusSm,
        height: 44,
        padding: "0 22px",
        color: t.textPrimary,
        fontFamily: t.fontUI,
        fontSize: 14,
        fontWeight: 600,
        letterSpacing: "0.04em",
        cursor: "default",
        transform: o.pressed ? "scale(0.96)" : a ? "translateY(-1px)" : "translateY(0)",
        transition: `background ${t.durFast}ms ${t.easeOut}, border-color ${t.durFast}ms ${t.easeOut}, transform ${t.durFast}ms ${t.easeOut}`
      },
      children: r
    }
  );
}, ae = ({ onClick: e }) => {
  const [r, a] = $(!1), n = H();
  return /* @__PURE__ */ i(
    "button",
    {
      onClick: e,
      onMouseEnter: () => a(!0),
      onMouseLeave: (o) => {
        a(!1), n.handlers.onPointerLeave(o);
      },
      onPointerDown: n.handlers.onPointerDown,
      "aria-label": "关闭",
      style: {
        appearance: "none",
        background: r ? t.bgElevated : t.bgSurface,
        border: `1px solid ${r ? t.borderRegular : t.borderSubtle}`,
        borderRadius: t.radiusSm,
        width: 44,
        height: 44,
        color: t.textPrimary,
        cursor: "default",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        transform: n.pressed ? "scale(0.92) rotate(90deg)" : r ? "rotate(90deg)" : "rotate(0)",
        transition: `background ${t.durFast}ms ${t.easeOut}, border-color ${t.durFast}ms ${t.easeOut}, transform ${t.durFast}ms ${t.easeOut}`
      },
      children: /* @__PURE__ */ i("svg", { width: "16", height: "16", viewBox: "0 0 16 16", "aria-hidden": !0, children: /* @__PURE__ */ i(
        "path",
        {
          d: "M3 3l10 10M13 3L3 13",
          stroke: "currentColor",
          strokeWidth: "1.8",
          strokeLinecap: "round"
        }
      ) })
    }
  );
};
function U(e) {
  if (!e || typeof e != "object") return e;
  if (Array.isArray(e)) {
    const n = e.map(U);
    return n.every((o, s) => o === e[s]) ? e : n;
  }
  const r = Object.entries(e), a = r.filter(([, n]) => n !== void 0).map(([n, o]) => [n, U(o)]);
  return a.length === r.length && a.every(([n, o], s) => n === r[s][0] && o === r[s][1]) ? e : Object.fromEntries(a);
}
function Er(e) {
  if (typeof e != "string" || !e.trim()) return [];
  let r;
  try {
    r = JSON.parse(e);
  } catch {
    return [];
  }
  if (!Array.isArray(r)) return [];
  const a = [];
  for (const n of r) {
    if (!n || typeof n != "object") continue;
    const o = n;
    if (typeof o.assetPath != "string" || !o.assetPath.trim())
      continue;
    const s = o.particle && typeof o.particle == "object" ? o.particle : void 0;
    a.push(U({
      assetPath: o.assetPath,
      ...o.kind === "particle" ? {
        kind: "particle",
        particle: {
          preset: typeof (s == null ? void 0 : s.preset) == "string" ? s.preset : "LIGHT_SNOW",
          optionsJson: typeof (s == null ? void 0 : s.optionsJson) == "string" ? s.optionsJson : ""
        }
      } : {},
      distance: typeof o.distance == "number" ? o.distance : void 0,
      offset: typeof o.offset == "string" ? o.offset : void 0,
      name: typeof o.name == "string" ? o.name : void 0,
      depthMapPath: typeof o.depthMapPath == "string" && o.depthMapPath.trim() ? o.depthMapPath.trim() : void 0,
      normalMapPath: typeof o.normalMapPath == "string" && o.normalMapPath.trim() ? o.normalMapPath.trim() : void 0,
      normalStrength: typeof o.normalStrength == "number" && Number.isFinite(o.normalStrength) ? Math.min(2, Math.max(0, o.normalStrength)) : void 0,
      depthStrength: typeof o.depthStrength == "number" && Number.isFinite(o.depthStrength) ? Math.min(2, Math.max(0, o.depthStrength)) : void 0,
      invertDepth: typeof o.invertDepth == "boolean" ? o.invertDepth : void 0,
      flipNormalY: typeof o.flipNormalY == "boolean" ? o.flipNormalY : void 0
    }));
  }
  return a;
}
function Wr(e) {
  if (typeof e != "string" || !e.trim()) return;
  let r;
  try {
    r = JSON.parse(e);
  } catch {
    return;
  }
  if (!r || typeof r != "object" || Array.isArray(r))
    return;
  const a = r, n = Array.isArray(a.position) ? a.position : [], o = (u, c) => {
    const g = Number(u);
    return Number.isFinite(g) ? g : c;
  }, s = (u, c, g) => Math.min(g, Math.max(c, u)), l = typeof a.color == "string" && /^#[0-9a-f]{6}$/i.test(a.color) ? a.color.toLowerCase() : "#ffd6a0";
  return {
    enabled: a.enabled !== !1,
    ambient: s(o(a.ambient, 0.35), 0, 1),
    intensity: s(o(a.intensity, 1.2), 0, 4),
    color: l,
    position: [
      s(o(n[0], 0.7), 0, 1),
      s(o(n[1], 0.25), 0, 1),
      s(o(n[2], 0.8), 0.05, 2)
    ]
  };
}
function ie(e) {
  if (!e || typeof e.entryId != "string" || !e.entryId || typeof e.sceneId != "string" || !e.sceneId || !Array.isArray(e.layers) || e.layers.length === 0) return !1;
  for (const r of e.layers)
    if (!r || typeof r.assetPath != "string" || !r.assetPath) return !1;
  return !0;
}
function he(e) {
  return !e || typeof e.entryId != "string" || !e.entryId.trim() || typeof e.title != "string" || !e.title.trim() ? !1 : typeof e.audioUri == "string" && e.audioUri.trim().length > 0;
}
function xe(e) {
  return !e || typeof e.entryId != "string" || !e.entryId.trim() || typeof e.title != "string" || !e.title.trim() ? !1 : typeof e.fragmentId == "string" && e.fragmentId.trim().length > 0;
}
function E(e) {
  return typeof e != "string" ? void 0 : e.trim() || void 0;
}
function Br(e) {
  const r = typeof e.customTitle == "string" ? e.customTitle.trim() : "", a = typeof e.sceneName == "string" ? e.sceneName.trim() : "";
  return r || a || e.sceneId;
}
function Dr(e) {
  for (const r of e)
    if (r && r.kind !== "particle" && typeof r.assetPath == "string" && r.assetPath.trim())
      return r.assetPath;
  return "";
}
var jr = Object.defineProperty, Hr = Object.getOwnPropertyDescriptor, Vr = (e, r, a) => r in e ? jr(e, r, { enumerable: !0, configurable: !0, writable: !0, value: a }) : e[r] = a, Yr = (e, r, a, n) => {
  for (var o = n > 1 ? void 0 : n ? Hr(r, a) : r, s = e.length - 1, l; s >= 0; s--)
    (l = e[s]) && (o = l(o) || o);
  return o;
}, Y = (e, r, a) => Vr(e, typeof r != "symbol" ? r + "" : r, a);
const Gr = [
  "unlockedShared",
  "unlockedSlot",
  "unlockedMusicShared",
  "unlockedMusicSlot",
  "unlockedFragmentsShared",
  "unlockedFragmentsSlot"
], Nr = "gallery-screen", Ur = `${ke.id}.unlockedShared`, Xr = `${ke.id}.unlockedSlot`;
function qr(e) {
  const [r] = e.variables.useValue(Ur), [a] = e.variables.useValue(Xr), n = r ?? [], o = a ?? [], s = /* @__PURE__ */ new Set(), l = [];
  for (const u of [...n, ...o])
    ie(u) && (s.has(u.entryId) || (s.add(u.entryId), l.push(u)));
  return l;
}
const Jr = () => {
  const e = ee(), r = qr(e), { phase: a, requestClose: n } = de(e, Nr), [o, s] = $(null);
  L(() => {
    if (o) return;
    const b = (d) => {
      d.key === "Escape" && n();
    }, f = (d) => {
      d.button === 1 && (d.preventDefault(), n());
    };
    return window.addEventListener("keydown", b), window.addEventListener("auxclick", f), () => {
      window.removeEventListener("keydown", b), window.removeEventListener("auxclick", f);
    };
  }, [o, n]);
  const l = (b) => {
    b.preventDefault(), !o && n();
  }, u = le(a), c = A({
    hidden: { opacity: 0, transform: "translateY(14px)" },
    delay: 180
  }), g = 12;
  return /* @__PURE__ */ S(
    "div",
    {
      onContextMenu: l,
      style: {
        position: "absolute",
        inset: 0,
        background: t.bgOverlayStrong,
        backdropFilter: "blur(28px)",
        WebkitBackdropFilter: "blur(28px)",
        color: t.textPrimary,
        fontFamily: t.fontUI,
        display: "flex",
        flexDirection: "column",
        willChange: "opacity",
        ...u
      },
      children: [
        /* @__PURE__ */ i(
          ce,
          {
            eyebrow: "Gallery",
            title: "鉴赏室",
            phase: a,
            rightSlot: /* @__PURE__ */ S(re, { children: [
              /* @__PURE__ */ S(
                "span",
                {
                  style: {
                    fontFamily: t.fontMono,
                    fontSize: 14,
                    color: t.textMuted,
                    fontWeight: 600,
                    fontVariantNumeric: "tabular-nums",
                    marginRight: 4
                  },
                  children: [
                    r.length,
                    " 张"
                  ]
                }
              ),
              /* @__PURE__ */ i(ae, { onClick: n })
            ] })
          }
        ),
        /* @__PURE__ */ i(
          "div",
          {
            className: "avg-shell-scrollbar",
            style: {
              flex: 1,
              overflowY: "auto",
              padding: "24px 80px 80px"
            },
            children: /* @__PURE__ */ i("div", { style: { maxWidth: 1160, margin: "0 auto" }, children: r.length === 0 ? /* @__PURE__ */ i(
              "div",
              {
                style: {
                  textAlign: "center",
                  marginTop: 100,
                  fontFamily: t.fontDisplay,
                  fontSize: 22,
                  color: t.textFaint,
                  fontWeight: 500,
                  ...c
                },
                children: "还没有解锁任何鉴赏内容"
              }
            ) : /* @__PURE__ */ i(
              "div",
              {
                style: {
                  display: "grid",
                  gridTemplateColumns: "repeat(auto-fill, minmax(240px, 1fr))",
                  gap: 20
                },
                children: r.map((b, f) => /* @__PURE__ */ i(
                  Kr,
                  {
                    entry: b,
                    ctx: e,
                    animationDelay: 140 + Math.min(f, g) * 36,
                    onOpen: () => s(b)
                  },
                  b.entryId
                ))
              }
            ) })
          }
        ),
        o && /* @__PURE__ */ i(
          Zr,
          {
            entry: o,
            ctx: e,
            onClose: () => s(null)
          }
        )
      ]
    }
  );
}, Kr = ({ entry: e, ctx: r, animationDelay: a, onOpen: n }) => {
  const [o, s] = $(!1), l = H(), u = A({
    hidden: { opacity: 0, transform: "translateY(16px) scale(0.97)" },
    delay: a
  });
  return /* @__PURE__ */ i("div", { style: u, children: /* @__PURE__ */ S(
    "div",
    {
      onClick: n,
      onMouseEnter: () => s(!0),
      onMouseLeave: () => {
        s(!1), l.handlers.onPointerLeave();
      },
      onPointerDown: l.handlers.onPointerDown,
      role: "button",
      "aria-label": e.title,
      style: {
        position: "relative",
        aspectRatio: "16 / 9",
        borderRadius: t.radiusMd,
        overflow: "hidden",
        background: t.bgSunken,
        border: `1px solid ${o ? t.borderAccent : t.borderSubtle}`,
        cursor: "default",
        transform: l.pressed ? "scale(0.97)" : o ? "translateY(-2px)" : "translateY(0)",
        boxShadow: o ? `0 8px 28px rgba(0, 0, 0, 0.4), 0 0 16px ${t.accentGlow}` : "0 2px 10px rgba(0, 0, 0, 0.25)",
        transition: `border-color ${t.durFast}ms ${t.easeOut}, transform ${t.durFast}ms ${t.easeOut}, box-shadow ${t.durBase}ms ${t.easeOut}`
      },
      children: [
        /* @__PURE__ */ i(
          Qr,
          {
            layers: e.layers,
            ctx: r,
            hover: o,
            alt: e.title
          }
        ),
        /* @__PURE__ */ i(
          "div",
          {
            style: {
              position: "absolute",
              left: 0,
              right: 0,
              bottom: 0,
              padding: "26px 12px 10px",
              background: "linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.72) 100%)",
              fontSize: 13,
              fontWeight: 600,
              letterSpacing: "0.02em",
              color: o ? t.accent : t.textPrimary,
              whiteSpace: "nowrap",
              overflow: "hidden",
              textOverflow: "ellipsis",
              transition: `color ${t.durFast}ms ${t.easeOut}`
            },
            children: e.title
          }
        )
      ]
    }
  ) });
}, Qr = ({ layers: e, ctx: r, hover: a, alt: n }) => /* @__PURE__ */ i(
  "div",
  {
    style: {
      position: "absolute",
      inset: 0,
      transform: a ? "scale(1.05)" : "scale(1)",
      transition: `transform ${t.durSlow}ms ${t.easeOut}`
    },
    children: e.map((o, s) => {
      const l = r.asset.resolve(o.assetPath).url;
      return /* @__PURE__ */ i(
        "img",
        {
          src: l,
          alt: s === 0 ? n : "",
          draggable: !1,
          style: {
            position: "absolute",
            inset: 0,
            width: "100%",
            height: "100%",
            objectFit: "cover",
            display: "block"
          }
        },
        `${s}-${o.assetPath}`
      );
    })
  }
), Zr = ({ entry: e, ctx: r, onClose: a }) => {
  const n = A({
    hidden: { opacity: 0 },
    duration: t.durBase
  }), o = A({
    hidden: { opacity: 0, transform: "scale(0.96) translateY(10px)" },
    delay: 40
  }), s = V(null), [l, u] = $(null), [c, g] = $(!1), b = V(null), f = t.durBase, d = () => {
    c || (g(!0), b.current = window.setTimeout(() => {
      a();
    }, f));
  };
  return L(() => () => {
    b.current != null && clearTimeout(b.current);
  }, []), L(() => {
    const m = (v) => {
      v.key === "Escape" && d();
    }, y = (v) => {
      v.button === 1 && (v.preventDefault(), d());
    };
    return window.addEventListener("keydown", m), window.addEventListener("auxclick", y), () => {
      window.removeEventListener("keydown", m), window.removeEventListener("auxclick", y);
    };
  }, []), L(() => {
    if (!s.current) return;
    const m = s.current;
    let y = null, v = !1;
    const k = new AbortController();
    return (async () => {
      try {
        const _ = await r.sceneRender.mount(m, e.layers, {
          // 场景图按 AVG 常规呈现 = 铺满容器、超出裁掉(cover),
          // contain 会留黑边导致用户看到"显示不全"
          displayType: "cover",
          ...e.lighting ? { lighting: e.lighting } : {},
          signal: k.signal
        });
        if (v) {
          _.dispose();
          return;
        }
        y = _;
      } catch (_) {
        if (v || _ instanceof Error && _.name === "AbortError")
          return;
        console.error("[gallery] 大图临时引擎渲染失败:", _), u(
          _ instanceof Error ? _.message : "场景渲染失败"
        );
      }
    })(), () => {
      v = !0, k.abort(), y == null || y.dispose();
    };
  }, [r.sceneRender, e.layers, e.lighting]), /* @__PURE__ */ S(
    "div",
    {
      onClick: d,
      onContextMenu: (m) => {
        m.preventDefault(), m.stopPropagation(), d();
      },
      style: {
        position: "absolute",
        inset: 0,
        zIndex: 20,
        background: "rgba(0, 0, 0, 0.88)",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        // 关闭态:整层 fade out,覆盖引擎 destroy 的中间态白闪
        ...c ? {
          opacity: 0,
          transition: `opacity ${f}ms ${t.easeOut}`,
          pointerEvents: "none"
        } : n
      },
      children: [
        /* @__PURE__ */ S(
          "div",
          {
            onClick: (m) => m.stopPropagation(),
            style: {
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              maxWidth: "88%",
              ...c ? {
                // 关闭态:figure 一并下沉淡出,跟 enter 动画对称
                opacity: 0,
                transform: "scale(0.96) translateY(10px)",
                transition: `opacity ${f}ms ${t.easeOut}, transform ${f}ms ${t.easeOut}`
              } : o
            },
            children: [
              /* @__PURE__ */ i(
                "div",
                {
                  ref: s,
                  style: {
                    position: "relative",
                    width: "min(88vw, 1280px)",
                    aspectRatio: "16 / 9",
                    maxHeight: "72vh",
                    borderRadius: t.radiusLg,
                    border: `1px solid ${t.borderSubtle}`,
                    boxShadow: "0 24px 80px rgba(0, 0, 0, 0.6)",
                    background: "#000",
                    overflow: "hidden"
                  },
                  children: l && /* @__PURE__ */ S(
                    "div",
                    {
                      style: {
                        position: "absolute",
                        inset: 0,
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "center",
                        color: t.textMuted,
                        fontSize: 14,
                        padding: 24,
                        textAlign: "center"
                      },
                      children: [
                        "场景渲染失败:",
                        l
                      ]
                    }
                  )
                }
              ),
              /* @__PURE__ */ i(
                "div",
                {
                  style: {
                    marginTop: 20,
                    fontFamily: t.fontDisplay,
                    fontSize: 20,
                    fontWeight: 600,
                    letterSpacing: "0.01em",
                    textAlign: "center"
                  },
                  children: e.title
                }
              )
            ]
          }
        ),
        /* @__PURE__ */ i(
          "div",
          {
            onClick: (m) => m.stopPropagation(),
            style: { position: "absolute", top: 28, right: 32 },
            children: /* @__PURE__ */ i(ae, { onClick: d })
          }
        )
      ]
    }
  );
};
let j = class extends Z {
  static onRegister(e) {
    const r = e.variables, a = () => {
      for (const n of Gr) {
        const o = `${ke.id}.${n}`, s = r.get(o);
        if (!Array.isArray(s)) continue;
        const l = U(s);
        l !== s && r.set(o, l);
      }
    };
    a(), e.subscribe("runtime:started", a), e.subscribe("archive:changed", a);
  }
  render() {
    return { component: Jr, props: {} };
  }
};
Y(j, "saveSchema", Ut({
  unlockedShared: {
    type: "list",
    persistence: "shared",
    default: []
  },
  unlockedSlot: {
    type: "list",
    persistence: "slot",
    default: []
  },
  unlockedMusicShared: {
    type: "list",
    persistence: "shared",
    default: []
  },
  unlockedMusicSlot: {
    type: "list",
    persistence: "slot",
    default: []
  },
  unlockedFragmentsShared: {
    type: "list",
    persistence: "shared",
    default: []
  },
  unlockedFragmentsSlot: {
    type: "list",
    persistence: "slot",
    default: []
  }
}));
Y(j, "settings", K((e) => ({
  unlockScope: e.enum("解锁记录范围", ["shared", "slot"]).labels({ shared: "全局共享(跨存档)", slot: "跟随存档" }).default("shared").describe(
    "新解锁的鉴赏条目记到哪里:全局共享 = 任意周目解锁全局可见;跟随存档 = 只在当前存档可见。已解锁条目不受切换影响。"
  )
})));
Y(j, "addToGallery", X({
  id: "add-to-gallery",
  title: "加入鉴赏",
  description: "把一个场景解锁到鉴赏室,玩家可在鉴赏界面查看",
  schema: {
    // scene 字段值是 sceneId 字符串;Inspector 选场景时同步把 layers 快照
    // 写进兄弟字段 _sceneLayers、场景名写进 _sceneName(都是内部兄弟字段)。
    scene: { type: "scene", label: "鉴赏场景", required: !0 },
    // 选填:不填时缺省用场景名称(而非 sceneId)。
    title: { type: "string", label: "标题(选填,默认用场景名)" }
  },
  run(e, r) {
    const a = typeof r.scene == "string" ? r.scene.trim() : "";
    if (!a) {
      console.warn("[gallery] 「加入鉴赏」缺少场景,已跳过:", r);
      return;
    }
    const n = a, o = this.save, s = e.settings.get("unlockScope") ?? "shared", l = o.get("unlockedShared") ?? [], u = o.get("unlockedSlot") ?? [];
    if ([...l, ...u].some((v) => (v == null ? void 0 : v.entryId) === n)) return;
    const g = r._sceneLayers, b = Er(
      typeof g == "string" ? g : void 0
    );
    if (b.length === 0) {
      console.warn(
        "[gallery] 「加入鉴赏」layers 快照缺失或为空,已跳过:",
        { sceneId: a }
      );
      return;
    }
    const f = r, d = Wr(
      typeof f._sceneLighting == "string" ? f._sceneLighting : void 0
    ), m = Br({
      customTitle: f.title,
      sceneName: f._sceneName,
      sceneId: a
    }), y = {
      entryId: n,
      title: m,
      sceneId: a,
      layers: b,
      ...d ? { lighting: d } : {},
      // 拍平一张顶层封面,供可视化「数据列表」版鉴赏墙绑图(它取不到嵌套 layers)
      coverImage: Dr(b)
    };
    s === "slot" ? o.set("unlockedSlot", [...u.filter(ie), y]) : o.set("unlockedShared", [...l.filter(ie), y]);
  }
}));
Y(j, "removeFromGallery", X({
  id: "remove-from-gallery",
  title: "移除鉴赏",
  description: "从鉴赏室移除指定场景对应的条目(两个记录桶都会找)",
  schema: {
    scene: { type: "scene", label: "鉴赏场景", required: !0 }
  },
  run(e, r) {
    const a = typeof r.scene == "string" ? r.scene.trim() : "";
    if (!a) {
      console.warn("[gallery] 「移除鉴赏」缺少场景,已跳过");
      return;
    }
    const n = this.save, o = (s) => ie(s) && s.sceneId !== a;
    n.set(
      "unlockedShared",
      (n.get("unlockedShared") ?? []).filter(o)
    ), n.set(
      "unlockedSlot",
      (n.get("unlockedSlot") ?? []).filter(o)
    );
  }
}));
Y(j, "addMusicToGallery", X({
  id: "add-music-to-gallery",
  title: "加入音乐鉴赏",
  description: "解锁一首音乐，玩家可在鉴赏界面试听",
  schema: {
    audio: {
      type: "asset",
      assetType: "audio",
      label: "音乐资源",
      required: !0
    },
    title: { type: "string", label: "曲名（选填）" },
    artist: { type: "string", label: "作者（选填）" },
    description: {
      type: "string",
      label: "曲目说明（选填）",
      multiline: !0
    }
  },
  run(e, r) {
    var f;
    const a = E(r.audio);
    if (!a) {
      console.warn("[gallery] 「加入音乐鉴赏」缺少音乐资源，已跳过");
      return;
    }
    const n = E(r.title) ?? ((f = a.split(/[\\/]/).pop()) == null ? void 0 : f.replace(/\.[^.]+$/, "")) ?? a, o = U({
      entryId: a,
      title: n,
      audioUri: a,
      artist: E(r.artist),
      description: E(r.description)
    }), s = this.save, l = s.get("unlockedMusicShared") ?? [], u = s.get("unlockedMusicSlot") ?? [], c = l.some(
      (d) => (d == null ? void 0 : d.entryId) === o.entryId
    ), g = u.some((d) => (d == null ? void 0 : d.entryId) === o.entryId);
    if (c || g) {
      c && s.set(
        "unlockedMusicShared",
        l.map(
          (d) => (d == null ? void 0 : d.entryId) === o.entryId ? o : d
        )
      ), g && s.set(
        "unlockedMusicSlot",
        u.map(
          (d) => (d == null ? void 0 : d.entryId) === o.entryId ? o : d
        )
      );
      return;
    }
    (e.settings.get("unlockScope") ?? "shared") === "slot" ? s.set("unlockedMusicSlot", [
      ...u.filter(he),
      o
    ]) : s.set("unlockedMusicShared", [
      ...l.filter(he),
      o
    ]);
  }
}));
Y(j, "removeMusicFromGallery", X({
  id: "remove-music-from-gallery",
  title: "移除音乐鉴赏",
  description: "从音乐鉴赏中移除指定音乐（全局与当前存档都会移除）",
  schema: {
    audio: {
      type: "asset",
      assetType: "audio",
      label: "音乐资源",
      required: !0
    }
  },
  run(e, r) {
    const a = E(r.audio);
    if (!a) return;
    const n = this.save, o = (s) => he(s) && s.audioUri !== a;
    n.set(
      "unlockedMusicShared",
      (n.get("unlockedMusicShared") ?? []).filter(o)
    ), n.set(
      "unlockedMusicSlot",
      (n.get("unlockedMusicSlot") ?? []).filter(o)
    );
  }
}));
Y(j, "addFragmentToGallery", X({
  id: "add-fragment-to-gallery",
  title: "加入片段鉴赏",
  description: "解锁一个剧情片段，玩家可在鉴赏界面重新播放",
  schema: {
    fragment: {
      type: "fragment",
      label: "剧情片段",
      required: !0,
      chapterField: "chapterId"
    },
    chapterId: { type: "string", label: "章节 ID（跨章节时填写）" },
    title: { type: "string", label: "标题（选填，默认用片段名）" },
    description: {
      type: "string",
      label: "片段说明（选填）",
      multiline: !0
    },
    cover: {
      type: "asset",
      assetType: "image",
      label: "封面图（选填）"
    }
  },
  async run(e, r) {
    const a = E(r.fragment);
    if (!a) {
      console.warn("[gallery] 「加入片段鉴赏」缺少剧情片段，已跳过");
      return;
    }
    let n = E(r.chapterId);
    const o = E(r.title);
    let s, l;
    const u = () => l ?? (l = e.story.getAllChapters());
    try {
      if (n && o)
        s = void 0;
      else {
        let M = n && typeof e.story.getChapter == "function" ? await e.story.getChapter(n) : null;
        if (!M) {
          const h = await u();
          M = n ? h.find((I) => I.id === n) : h.find(
            (I) => I.fragments.some((T) => T.id === a)
          );
        }
        const F = M == null ? void 0 : M.fragments.find(
          (h) => h.id === a
        );
        n = (M == null ? void 0 : M.id) ?? n, s = E(F == null ? void 0 : F.name);
      }
    } catch (M) {
      console.warn("[gallery] 读取片段标题失败，将使用片段 ID", M);
    }
    const c = U({
      entryId: `${n ?? "current"}:${a}`,
      title: o ?? s ?? a,
      fragmentId: a,
      chapterId: n,
      description: E(r.description),
      coverImage: E(r.cover)
    }), g = this.save, b = g.get("unlockedFragmentsShared") ?? [], f = g.get("unlockedFragmentsSlot") ?? [], d = `current:${c.fragmentId}`, m = [...b, ...f].some(
      (M) => (M == null ? void 0 : M.entryId) === d && M.fragmentId === c.fragmentId && !M.chapterId
    );
    let y = !1;
    if (c.chapterId && m)
      try {
        const M = (await u()).filter(
          (F) => F.fragments.some(
            (h) => h.id === c.fragmentId
          )
        );
        y = M.length === 1 && M[0].id === c.chapterId;
      } catch (M) {
        console.warn(
          "[gallery] 无法确认历史 current 条目所属章节，将保留原记录",
          M
        );
      }
    const v = Object.prototype.hasOwnProperty.call(r, "title") && r.title !== void 0, k = Object.prototype.hasOwnProperty.call(r, "description") && r.description !== void 0, _ = Object.prototype.hasOwnProperty.call(r, "cover") && r.cover !== void 0, C = (M) => {
      const F = [];
      let h = -1;
      if (M.forEach((p, O) => {
        if ((p == null ? void 0 : p.entryId) === c.entryId) {
          h = h < 0 ? O : h, F.push(O);
          return;
        }
        y && (p == null ? void 0 : p.entryId) === d && p.fragmentId === c.fragmentId && !p.chapterId && F.push(O);
      }), F.length === 0)
        return { entries: M, matched: !1, changed: !1 };
      const I = h >= 0 ? h : F[0];
      let T = {};
      for (const p of F)
        p !== I && (T = { ...T, ...M[p] });
      const z = M[I];
      T = { ...T, ...z };
      const B = U({
        ...T,
        entryId: c.entryId,
        title: v ? c.title : T.title,
        fragmentId: c.fragmentId,
        chapterId: c.chapterId,
        description: k ? c.description : T.description,
        coverImage: _ ? c.coverImage : T.coverImage
      });
      if (!(F.length > 1 || B.entryId !== z.entryId || B.title !== z.title || B.fragmentId !== z.fragmentId || B.chapterId !== z.chapterId || B.description !== z.description || B.coverImage !== z.coverImage || Object.keys(B).length !== Object.keys(z).length))
        return { entries: M, matched: !0, changed: !1 };
      const oe = new Set(F), x = [];
      return M.forEach((p, O) => {
        O === I ? x.push(B) : oe.has(O) || x.push(p);
      }), { entries: x, matched: !0, changed: !0 };
    }, R = C(b), w = C(f);
    if (R.changed && g.set("unlockedFragmentsShared", R.entries), w.changed && g.set("unlockedFragmentsSlot", w.entries), R.matched || w.matched)
      return;
    (e.settings.get("unlockScope") ?? "shared") === "slot" ? g.set("unlockedFragmentsSlot", [
      ...f.filter(xe),
      c
    ]) : g.set("unlockedFragmentsShared", [
      ...b.filter(xe),
      c
    ]);
  }
}));
Y(j, "removeFragmentFromGallery", X({
  id: "remove-fragment-from-gallery",
  title: "移除片段鉴赏",
  description: "从片段鉴赏中移除指定剧情片段（全局与当前存档都会移除）",
  schema: {
    fragment: {
      type: "fragment",
      label: "剧情片段",
      required: !0,
      chapterField: "chapterId"
    },
    chapterId: { type: "string", label: "章节 ID（选填）" }
  },
  run(e, r) {
    const a = E(r.fragment), n = E(r.chapterId);
    if (!a) return;
    const o = this.save, s = (l) => xe(l) && (l.fragmentId !== a || n !== void 0 && l.chapterId !== n);
    o.set(
      "unlockedFragmentsShared",
      (o.get("unlockedFragmentsShared") ?? []).filter(s)
    ), o.set(
      "unlockedFragmentsSlot",
      (o.get("unlockedFragmentsSlot") ?? []).filter(s)
    );
  }
}));
Y(j, "clearGallery", X({
  id: "clear-gallery",
  title: "清空鉴赏",
  description: "清空 CG、音乐与片段鉴赏的全部解锁记录（慎用）",
  run() {
    const e = this.save;
    e.set("unlockedShared", []), e.set("unlockedSlot", []), e.set("unlockedMusicShared", []), e.set("unlockedMusicSlot", []), e.set("unlockedFragmentsShared", []), e.set("unlockedFragmentsSlot", []);
  }
}));
j = Yr([
  Q({
    id: "gallery-screen",
    autonomous: !0,
    label: "鉴赏管理",
    exposeUI: !1,
    // 保留鉴赏方法和存档数据,React 版不再进入 UI 列表
    /** 声明本 UI 实现"鉴赏"槽位,Studio 系统槽位面板据此列为候选。 */
    supportsSlot: P.Gallery
  })
], j);
const $e = "avg-default-shell-toast-container", ea = 2400, ue = 220;
function fe(e) {
  const r = document.getElementById("game-view");
  if (!r) {
    e.style.left = "50%", e.style.bottom = "32px", e.style.top = "auto", e.style.right = "auto", e.style.width = "auto";
    return;
  }
  const a = r.getBoundingClientRect();
  e.style.left = `${a.left}px`, e.style.top = `${a.bottom - 32 - 64}px`, e.style.width = `${a.width}px`, e.style.bottom = "auto", e.style.right = "auto";
}
function ta() {
  if (typeof document > "u") return null;
  let e = document.getElementById($e);
  if (e)
    return fe(e), e;
  e = document.createElement("div"), e.id = $e, e.style.cssText = [
    "position: fixed",
    // 跟引擎 engine-mask 同款 max int 层级,确保压在 SaveScreen overlay 之上。
    // SaveScreen 自己用 position:absolute 没设 z-index,但被引擎 UISystem
    // 装进 topmost 容器后实际有高层级,普通 99999 可能被盖。
    "z-index: 2147483647",
    "display: flex",
    "flex-direction: column",
    "align-items: center",
    "justify-content: flex-end",
    "gap: 8px",
    "pointer-events: none"
  ].join(";"), document.body.appendChild(e), fe(e);
  const r = document.getElementById("game-view");
  return r && typeof ResizeObserver < "u" && new ResizeObserver(() => fe(e)).observe(r), e;
}
const ra = {
  info: "·",
  success: "✓",
  warn: "!",
  error: "×"
}, aa = {
  info: t.textMuted,
  success: t.accent,
  warn: t.accent,
  error: t.danger
};
function W(e, r = {}) {
  const a = ta();
  if (!a) return;
  const n = r.type ?? "info", o = r.durationMs ?? ea, s = document.createElement("div");
  s.style.cssText = [
    `font-family: ${t.fontUI}`,
    "font-size: 13px",
    "font-weight: 500",
    "letter-spacing: 0.04em",
    `color: ${t.textPrimary}`,
    "background: rgba(11, 13, 16, 0.88)",
    `border: 1px solid ${t.borderRegular}`,
    "border-radius: 8px",
    "padding: 10px 16px",
    "backdrop-filter: blur(12px)",
    "-webkit-backdrop-filter: blur(12px)",
    "box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4)",
    "display: flex",
    "align-items: center",
    "gap: 10px",
    "opacity: 0",
    "transform: translateY(8px)",
    `transition: opacity ${ue}ms ${t.easeOut}, transform ${ue}ms ${t.easeOut}`,
    "max-width: 480px",
    "pointer-events: none"
  ].join(";");
  const l = document.createElement("span");
  l.textContent = ra[n], l.style.cssText = [
    `color: ${aa[n]}`,
    "font-weight: 700",
    "font-size: 14px",
    "line-height: 1",
    "flex-shrink: 0"
  ].join(";"), s.appendChild(l);
  const u = document.createElement("span");
  u.textContent = e, s.appendChild(u), a.appendChild(s), s.offsetHeight, s.style.opacity = "1", s.style.transform = "translateY(0)", setTimeout(() => {
    s.style.opacity = "0", s.style.transform = "translateY(8px)", setTimeout(() => {
      s.remove(), a.childElementCount === 0 && a.remove();
    }, ue);
  }, o);
}
var oa = Object.defineProperty, na = Object.getOwnPropertyDescriptor, sa = (e, r, a) => r in e ? oa(e, r, { enumerable: !0, configurable: !0, writable: !0, value: a }) : e[r] = a, ia = (e, r, a, n) => {
  for (var o = n > 1 ? void 0 : n ? na(r, a) : r, s = e.length - 1, l; s >= 0; s--)
    (l = e[s]) && (o = l(o) || o);
  return o;
}, la = (e, r, a) => sa(e, r + "", a);
const ye = 6, Ce = "@avg.internal.default-shell/save-screen", da = ({ mode: e = "save", source: r = "game" }) => {
  const a = ee(), n = a.archive.useSlots(), o = a.settings.get("slotCount") ?? 30, s = a.settings.get("allowDelete") ?? !0, { phase: l, requestClose: u } = de(a, "save-screen"), [c, g] = $(0), [b, f] = $("right"), [d, m] = $(!1), y = V(!1), v = V(!1), k = V(!0);
  L(() => (k.current = !0, () => {
    k.current = !1;
  }), []);
  const _ = Math.max(1, Math.ceil(o / ye)), C = Pe(() => {
    const x = c * ye, p = [];
    for (let O = 0; O < ye; O++) {
      const q = x + O + 1;
      if (q > o) break;
      const pe = n.find((N) => N.id === q) ?? null;
      p.push({ id: q, slot: pe });
    }
    return p;
  }, [c, n, o]);
  L(() => {
    const x = (p) => {
      if (p.key === "Escape") {
        u();
        return;
      }
      p.key === "ArrowLeft" && R(), p.key === "ArrowRight" && w();
    };
    return window.addEventListener("keydown", x), () => window.removeEventListener("keydown", x);
  }, [c, _]);
  const R = () => {
    c > 0 && (f("left"), g((x) => x - 1));
  }, w = () => {
    c < _ - 1 && (f("right"), g((x) => x + 1));
  }, D = (x) => {
    y.current || (y.current = !0, m(!0), a.archive.save(x).then((p) => {
      p && W(`已保存到 #${String(x).padStart(2, "0")}`, { type: "success" });
    }).catch((p) => {
      console.error("[save-screen] save failed", p), W("保存失败", { type: "error" });
    }).finally(() => {
      y.current = !1, k.current && m(!1);
    }));
  }, M = (x) => {
    y.current || (y.current = !0, m(!0), a.archive.load(x).catch((p) => {
      console.error("[save-screen] load failed", p), W("读取失败", { type: "error" });
    }).finally(() => {
      y.current = !1, k.current && m(!1);
    }));
  }, F = (x) => {
    a.archive.delete(x).then(() => W(`已删除 #${String(x).padStart(2, "0")}`, { type: "info" })).catch((p) => {
      console.error("[save-screen] delete failed", p), W("删除失败", { type: "error" });
    });
  }, h = (x, p) => D(x), I = async (x, p) => {
    if (v.current) return;
    v.current = !0;
    let O = !1;
    const q = String(p).padStart(2, "0"), pe = x === "delete" ? {
      mode: "confirm",
      copyKey: "archive.delete",
      copyValues: { slot: q },
      title: `删除存档 #${q}`,
      message: "删除后无法恢复，是否继续？",
      confirmText: "删除",
      cancelText: "取消",
      tone: "danger",
      onResolve(N) {
        O = N === !0;
      }
    } : {
      mode: "confirm",
      copyKey: "archive.load",
      title: "提示",
      message: "是否要读取当前存档？",
      description: "读档后，正在进行的进度可能会丢失。",
      confirmText: "是",
      cancelText: "否",
      tone: "warning",
      onResolve(N) {
        O = N === !0;
      }
    };
    try {
      await a.system.invoke(P.Message, pe, {
        modal: !0
      });
    } catch (N) {
      console.error("[save-screen] standard confirmation failed", N);
    } finally {
      v.current = !1;
    }
    !O || !k.current || (x === "load" ? M(p) : F(p));
  }, T = (x) => {
    if (r === "title") {
      M(x);
      return;
    }
    I("load", x);
  }, z = (x) => {
    I("delete", x);
  }, B = le(l), te = A({
    hidden: { opacity: 0, transform: "translateY(14px)" },
    delay: 280
  });
  return /* @__PURE__ */ S(
    "div",
    {
      onContextMenu: (x) => {
        x.preventDefault(), u();
      },
      style: {
        position: "absolute",
        inset: 0,
        background: t.bgOverlay,
        backdropFilter: "blur(24px)",
        WebkitBackdropFilter: "blur(24px)",
        color: t.textPrimary,
        fontFamily: t.fontUI,
        display: "flex",
        flexDirection: "column",
        willChange: "opacity",
        ...B
      },
      children: [
        /* @__PURE__ */ i(
          ce,
          {
            eyebrow: e === "load" ? "Load" : "Save",
            title: e === "load" ? "读取存档" : "保存存档",
            phase: l,
            rightSlot: /* @__PURE__ */ S(re, { children: [
              /* @__PURE__ */ S(
                "span",
                {
                  style: {
                    fontFamily: t.fontMono,
                    fontSize: 14,
                    color: t.textMuted,
                    fontWeight: 600,
                    fontVariantNumeric: "tabular-nums",
                    marginRight: 4
                  },
                  children: [
                    String(c + 1).padStart(2, "0"),
                    " /",
                    " ",
                    String(_).padStart(2, "0")
                  ]
                }
              ),
              /* @__PURE__ */ i(ae, { onClick: u })
            ] })
          }
        ),
        /* @__PURE__ */ S(
          "div",
          {
            style: {
              flex: 1,
              display: "grid",
              gridTemplateColumns: "88px 1fr 88px",
              gap: 16,
              padding: "0 56px 24px",
              minHeight: 0,
              alignItems: "center"
            },
            children: [
              /* @__PURE__ */ i(
                Ie,
                {
                  dir: "left",
                  disabled: c === 0,
                  onClick: R,
                  delay: 160,
                  phase: l
                }
              ),
              /* @__PURE__ */ i(
                "div",
                {
                  "aria-busy": d || void 0,
                  style: {
                    display: "grid",
                    gridTemplateColumns: "repeat(3, 1fr)",
                    gridTemplateRows: "repeat(2, 1fr)",
                    gap: 24,
                    height: "100%",
                    animation: `${b === "right" ? "avg-page-slide-in-right" : "avg-page-slide-in-left"} ${t.durBase}ms ${t.easeOut}`
                  },
                  children: C.map(({ id: x, slot: p }, O) => /* @__PURE__ */ i(
                    pa,
                    {
                      id: x,
                      slot: p,
                      snapshotUrl: (p == null ? void 0 : p.snapshotDataUri) ?? null,
                      allowDelete: s,
                      mode: e,
                      busy: d,
                      onSave: () => h(x),
                      onLoad: () => T(x),
                      onDelete: () => z(x),
                      animationDelay: 120 + O * 40,
                      phase: l
                    },
                    x
                  ))
                },
                c
              ),
              /* @__PURE__ */ i(
                Ie,
                {
                  dir: "right",
                  disabled: c >= _ - 1,
                  onClick: w,
                  delay: 160,
                  phase: l
                }
              )
            ]
          }
        ),
        /* @__PURE__ */ i(
          "footer",
          {
            style: {
              padding: "16px 0 40px",
              display: "flex",
              justifyContent: "center",
              gap: 10,
              ...te
            },
            children: Array.from({ length: _ }).map((x, p) => /* @__PURE__ */ i(
              ca,
              {
                active: p === c,
                onClick: () => {
                  f(p > c ? "right" : "left"), g(p);
                },
                label: `第 ${p + 1} 页`
              },
              p
            ))
          }
        )
      ]
    }
  );
}, ca = ({ active: e, onClick: r, label: a }) => {
  const n = H();
  return /* @__PURE__ */ i(
    "button",
    {
      ...n.handlers,
      onClick: r,
      "aria-label": a,
      style: {
        appearance: "none",
        width: e ? 32 : 8,
        height: 8,
        borderRadius: 999,
        border: "none",
        padding: 0,
        background: e ? t.accent : t.borderRegular,
        cursor: "default",
        boxShadow: e ? `0 0 12px ${t.accentGlow}` : "none",
        transform: n.pressed ? "scale(0.85)" : "scale(1)",
        transition: `width ${t.durBase}ms ${t.easeOut}, background ${t.durBase}ms ${t.easeOut}, transform ${t.durFast}ms ${t.easeOut}, box-shadow ${t.durBase}ms ${t.easeOut}`
      }
    }
  );
}, pa = ({
  id: e,
  slot: r,
  snapshotUrl: a,
  allowDelete: n,
  mode: o,
  busy: s,
  onSave: l,
  onLoad: u,
  onDelete: c,
  animationDelay: g,
  phase: b
}) => {
  const [f, d] = $(!1), [m, y] = $(!1), v = H(), k = r === null, _ = o === "load" && k, C = !_ && !s, R = String(e).padStart(2, "0"), w = k ? o === "save" ? `保存到空槽位 #${R}` : `空槽位 #${R}` : o === "save" ? `覆盖存档 #${R}` : `读取存档 #${R}`, D = () => {
    C && (o === "save" ? l() : u());
  }, M = Pe(() => {
    const h = e * 37 % 360;
    return `linear-gradient(135deg,
      hsl(${h}, 12%, 22%) 0%,
      hsl(${(h + 50) % 360}, 10%, 16%) 100%)`;
  }, [e]), F = A({
    hidden: {
      opacity: 0,
      transform: "translateY(18px) scale(0.97)"
    },
    delay: g,
    duration: t.durSlow
  });
  return /* @__PURE__ */ i(
    "div",
    {
      style: { display: "flex", ...F },
      children: /* @__PURE__ */ S(
        "article",
        {
          onMouseEnter: () => {
            C && d(!0);
          },
          onMouseLeave: (h) => {
            d(!1), y(!1), v.handlers.onPointerLeave(h);
          },
          onPointerDown: (h) => {
            C && v.handlers.onPointerDown(h);
          },
          style: {
            flex: 1,
            position: "relative",
            background: t.bgSurface,
            border: `1.5px solid ${f && C ? t.borderAccent : t.borderSubtle}`,
            borderRadius: t.radiusLg,
            overflow: "hidden",
            display: "flex",
            flexDirection: "column",
            transform: v.pressed ? "translateY(-2px) scale(0.98)" : f && C ? "translateY(-6px) scale(1.01)" : "translateY(0) scale(1)",
            boxShadow: f && C ? "0 28px 56px rgba(0,0,0,0.55), 0 0 0 1px rgba(212,165,116,0.22), 0 0 32px rgba(212,165,116,0.10)" : "0 4px 16px rgba(0,0,0,0.25)",
            transition: `transform ${t.durFast}ms ${t.easeOut}, border-color ${t.durFast}ms ${t.easeOut}, box-shadow ${t.durBase}ms ${t.easeOut}`,
            cursor: C ? "default" : "not-allowed",
            // load 模式空槽位:整张卡灰化 + 不响应
            opacity: _ ? 0.45 : 1
          },
          children: [
            /* @__PURE__ */ i(
              "button",
              {
                type: "button",
                "aria-label": w,
                disabled: !C,
                onClick: D,
                style: {
                  position: "absolute",
                  inset: 0,
                  zIndex: 1,
                  appearance: "none",
                  border: "none",
                  padding: 0,
                  background: "transparent",
                  color: "transparent",
                  cursor: C ? "default" : "not-allowed"
                }
              }
            ),
            /* @__PURE__ */ S(
              "div",
              {
                style: {
                  position: "relative",
                  flex: "1 1 0",
                  minHeight: 0,
                  background: M,
                  overflow: "hidden"
                },
                children: [
                  a && /* @__PURE__ */ i(
                    "img",
                    {
                      src: a,
                      alt: "",
                      decoding: "async",
                      loading: "lazy",
                      draggable: !1,
                      style: {
                        position: "absolute",
                        inset: 0,
                        width: "100%",
                        height: "100%",
                        objectFit: "cover",
                        pointerEvents: "none",
                        userSelect: "none"
                      }
                    }
                  ),
                  /* @__PURE__ */ S(
                    "div",
                    {
                      style: {
                        position: "absolute",
                        top: 14,
                        left: 16,
                        fontFamily: t.fontMono,
                        fontSize: 13,
                        letterSpacing: "0.24em",
                        color: t.textPrimary,
                        textShadow: "0 1px 6px rgba(0,0,0,0.9)",
                        background: "rgba(0,0,0,0.45)",
                        padding: "5px 11px",
                        borderRadius: 6,
                        backdropFilter: "blur(8px)",
                        WebkitBackdropFilter: "blur(8px)",
                        fontWeight: 600
                      },
                      children: [
                        "#",
                        String(e).padStart(2, "0")
                      ]
                    }
                  ),
                  (r == null ? void 0 : r.isQuickSave) && /* @__PURE__ */ i(
                    "div",
                    {
                      style: {
                        position: "absolute",
                        top: 14,
                        right: 16,
                        fontFamily: t.fontMono,
                        fontSize: 11,
                        letterSpacing: "0.24em",
                        color: t.accent,
                        background: "rgba(0,0,0,0.45)",
                        padding: "5px 11px",
                        borderRadius: 6,
                        backdropFilter: "blur(8px)",
                        WebkitBackdropFilter: "blur(8px)",
                        fontWeight: 700
                      },
                      children: "QUICK"
                    }
                  ),
                  !k && n && !s && /* @__PURE__ */ i(
                    "button",
                    {
                      type: "button",
                      "aria-label": `删除存档 #${R}`,
                      "aria-hidden": !f,
                      tabIndex: f ? 0 : -1,
                      onClick: (h) => {
                        h.stopPropagation(), c();
                      },
                      onPointerDown: (h) => h.stopPropagation(),
                      onMouseEnter: (h) => {
                        h.stopPropagation(), y(!0);
                      },
                      onMouseLeave: (h) => {
                        h.stopPropagation(), y(!1);
                      },
                      onFocus: () => {
                        d(!0), y(!0);
                      },
                      onBlur: () => {
                        d(!1), y(!1);
                      },
                      style: {
                        position: "absolute",
                        top: 14,
                        right: r != null && r.isQuickSave ? 98 : 16,
                        zIndex: 3,
                        width: 42,
                        height: 42,
                        borderRadius: "50%",
                        border: `1.5px solid ${m ? "rgba(255,154,146,0.96)" : "rgba(255,126,116,0.82)"}`,
                        background: m ? "rgba(255,232,230,0.96)" : "rgba(255,246,245,0.88)",
                        color: t.danger,
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "center",
                        opacity: f ? 1 : 0,
                        visibility: f ? "visible" : "hidden",
                        transform: f ? `translateY(0) scale(${m ? 1.1 : 1}) rotate(${m ? 4 : 0}deg)` : "translateY(-4px) scale(0.92) rotate(0deg)",
                        pointerEvents: f ? "auto" : "none",
                        boxShadow: m ? "0 16px 34px rgba(0,0,0,0.38), 0 0 0 2px rgba(224,99,90,0.22), 0 0 30px rgba(224,99,90,0.38)" : "0 12px 26px rgba(0,0,0,0.30), 0 0 0 2px rgba(255,255,255,0.30), 0 0 22px rgba(224,99,90,0.22)",
                        backdropFilter: "blur(10px)",
                        WebkitBackdropFilter: "blur(10px)",
                        transition: `opacity ${t.durFast}ms ${t.easeOut}, visibility ${t.durFast}ms ${t.easeOut}, transform ${t.durFast}ms ${t.easeOut}, background ${t.durFast}ms ${t.easeOut}, box-shadow ${t.durFast}ms ${t.easeOut}`,
                        cursor: "default"
                      },
                      children: /* @__PURE__ */ S("svg", { width: "20", height: "20", viewBox: "0 0 20 20", "aria-hidden": "true", children: [
                        /* @__PURE__ */ i(
                          "path",
                          {
                            d: "M5 5l10 10M15 5 5 15",
                            fill: "none",
                            stroke: "rgba(255,255,255,0.98)",
                            strokeWidth: "4.8",
                            strokeLinecap: "round",
                            strokeLinejoin: "round"
                          }
                        ),
                        /* @__PURE__ */ i(
                          "path",
                          {
                            d: "M5 5l10 10M15 5 5 15",
                            fill: "none",
                            stroke: "currentColor",
                            strokeWidth: "2.6",
                            strokeLinecap: "round",
                            strokeLinejoin: "round"
                          }
                        )
                      ] })
                    }
                  ),
                  k && /* @__PURE__ */ i(
                    "div",
                    {
                      style: {
                        position: "absolute",
                        inset: 0,
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "center",
                        color: t.textFaint,
                        fontFamily: t.fontDisplay,
                        fontSize: 24,
                        fontWeight: 500,
                        letterSpacing: "0.08em"
                      },
                      children: "EMPTY"
                    }
                  )
                ]
              }
            ),
            /* @__PURE__ */ i(
              "div",
              {
                style: {
                  padding: "14px 18px 16px",
                  background: t.bgSunken,
                  borderTop: `1px solid ${t.borderSubtle}`,
                  minHeight: 72
                },
                children: r ? /* @__PURE__ */ S(re, { children: [
                  r.currentSpeaker && /* @__PURE__ */ i(
                    "div",
                    {
                      style: {
                        fontFamily: t.fontUI,
                        fontSize: 13,
                        fontWeight: 700,
                        letterSpacing: "0.04em",
                        color: t.accent,
                        marginBottom: 6
                      },
                      children: r.currentSpeaker
                    }
                  ),
                  /* @__PURE__ */ i(
                    "div",
                    {
                      style: {
                        fontSize: 14,
                        lineHeight: 1.55,
                        color: t.textPrimary,
                        display: "-webkit-box",
                        WebkitLineClamp: 2,
                        WebkitBoxOrient: "vertical",
                        overflow: "hidden",
                        textWrap: "pretty",
                        fontWeight: 400
                      },
                      children: r.currentDialogueText || "—"
                    }
                  ),
                  /* @__PURE__ */ i(
                    "div",
                    {
                      style: {
                        marginTop: 8,
                        fontFamily: t.fontMono,
                        fontSize: 11,
                        letterSpacing: "0.06em",
                        color: t.textFaint,
                        fontWeight: 500
                      },
                      children: ua(r.modifiedTime)
                    }
                  )
                ] }) : /* @__PURE__ */ i(
                  "div",
                  {
                    style: {
                      fontFamily: t.fontMono,
                      fontSize: 12,
                      letterSpacing: "0.20em",
                      color: t.textFaint,
                      textTransform: "uppercase",
                      fontWeight: 600
                    },
                    children: "no data"
                  }
                )
              }
            )
          ]
        }
      )
    }
  );
}, Ie = ({ dir: e, disabled: r, onClick: a, delay: n }) => {
  const [o, s] = $(!1), l = H(), u = A({
    hidden: { opacity: 0, transform: "translateY(14px)" },
    delay: n
  });
  return /* @__PURE__ */ i(
    "div",
    {
      style: { display: "flex", ...u },
      children: /* @__PURE__ */ i(
        "button",
        {
          onClick: a,
          disabled: r,
          onMouseEnter: () => s(!0),
          onMouseLeave: (c) => {
            s(!1), l.handlers.onPointerLeave(c);
          },
          onPointerDown: l.handlers.onPointerDown,
          "aria-label": e === "left" ? "上一页" : "下一页",
          style: {
            appearance: "none",
            background: o && !r ? t.accentSoft : "transparent",
            border: `1.5px solid ${o && !r ? t.borderAccent : t.borderSubtle}`,
            borderRadius: "50%",
            width: 64,
            height: 64,
            color: r ? t.textFaint : t.textPrimary,
            cursor: r ? "not-allowed" : "default",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            opacity: r ? 0.25 : 1,
            boxShadow: o && !r ? `0 8px 24px rgba(0,0,0,0.4), 0 0 24px ${t.accentGlow}` : "0 2px 8px rgba(0,0,0,0.2)",
            transform: l.pressed ? "scale(0.92)" : o && !r ? e === "left" ? "translateX(-6px) scale(1.05)" : "translateX(6px) scale(1.05)" : "translateX(0) scale(1)",
            transition: `border-color ${t.durFast}ms ${t.easeOut}, opacity ${t.durFast}ms ${t.easeOut}, transform ${t.durFast}ms ${t.easeOut}, background ${t.durFast}ms ${t.easeOut}, box-shadow ${t.durBase}ms ${t.easeOut}`
          },
          children: /* @__PURE__ */ i("svg", { width: "20", height: "20", viewBox: "0 0 20 20", "aria-hidden": !0, children: e === "left" ? /* @__PURE__ */ i(
            "path",
            {
              d: "M13 3L6 10l7 7",
              stroke: "currentColor",
              strokeWidth: "2",
              fill: "none",
              strokeLinecap: "round",
              strokeLinejoin: "round"
            }
          ) : /* @__PURE__ */ i(
            "path",
            {
              d: "M7 3l7 7-7 7",
              stroke: "currentColor",
              strokeWidth: "2",
              fill: "none",
              strokeLinecap: "round",
              strokeLinejoin: "round"
            }
          ) })
        }
      )
    }
  );
};
function ua(e) {
  const r = new Date(e), a = (Date.now() - e) / 6e4;
  return a < 1 ? "刚刚" : a < 60 ? `${Math.floor(a)} 分钟前` : a < 60 * 24 ? `${Math.floor(a / 60)} 小时前` : r.toLocaleString("zh-CN", {
    year: "2-digit",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit"
  });
}
let ve = class extends Z {
  /**
   * 注册快存/快读语义动作,然后订阅触发。键位由 KeyBindingSystem 管理:
   *   - default_keys: F5 / F9 (跟之前 settings 默认一致)
   *   - 玩家在"输入按键"tab 改键 → 自动生效,不需要 settings.subscribe
   *   - 跨存档持久化(走 GAME_SETTINGS_TABLE.userKeyBindings)
   */
  static onRegister(e) {
    e.archive.preloadSlots();
    let r = !0;
    e.visualUI.onBeforeOpen(Ce, async (a = {}) => {
      r = a.reuseSnapshot !== !0, !(a.mode === "load" || !r) && await e.archive.cacheGameSnapshot();
    }), e.visualUI.onOpen(Ce, (a) => {
      const n = r;
      r = !0, n && a.onClose(() => e.archive.clearGameSnapshot());
    }), e.input.registerAction({
      id: "avg.internal.default-shell.quick-save",
      label: "快速存档",
      defaultKeys: ["F5"]
    }), e.input.registerAction({
      id: "avg.internal.default-shell.quick-load",
      label: "快速读档",
      defaultKeys: ["F9"]
    }), e.input.onAction("avg.internal.default-shell.quick-save", () => {
      e.archive.quickSave().then(() => W("已快速存档 (F5)", { type: "success" })).catch((a) => {
        console.error("[save-screen] quickSave failed", a), W("快速存档失败", { type: "error" });
      });
    }), e.input.onAction("avg.internal.default-shell.quick-load", async () => {
      try {
        await e.archive.quickLoad() || W("没有可读取的快速存档 (F5 创建)", { type: "warn" });
      } catch (a) {
        console.error("[save-screen] quickLoad failed", a), W("快速读档失败", { type: "error" });
      }
    });
  }
  /**
   * onInit 在 React 把 SaveScreen 渲染进 DOM **之前**触发。
   * 此时画面上还没有 SaveScreen 自身覆盖,触发引擎截图正好拿到"打开存档画面
   * 之前"的纯游戏画面。缓存到 ArchiveSystem,后续点保存复用,完全不闪。
   *
   * 见 archive-system.ts cachedGameSnapshot 字段说明。
   */
  onInit() {
    var e, r;
    ((e = this.data) == null ? void 0 : e.mode) === "load" || ((r = this.data) == null ? void 0 : r.reuseSnapshot) === !0 || this.context.archive.cacheGameSnapshot();
  }
  /** onClose 清缓存,避免下次打开 SaveScreen 时还用着上次的旧画面。 */
  onClose() {
    var e;
    ((e = this.data) == null ? void 0 : e.reuseSnapshot) !== !0 && this.context.archive.clearGameSnapshot();
  }
  render() {
    const e = this.data, r = (e == null ? void 0 : e.mode) === "save" || (e == null ? void 0 : e.mode) === "load" ? e.mode : void 0, a = (e == null ? void 0 : e.source) === "title" || (e == null ? void 0 : e.source) === "game" ? e.source : void 0, n = (e == null ? void 0 : e.reuseSnapshot) === !0;
    return {
      component: da,
      props: { mode: r, source: a, reuseSnapshot: n }
    };
  }
};
la(ve, "settings", K((e) => ({
  slotCount: e.number("槽位数量").default(30).range(1, 200),
  allowDelete: e.boolean("允许删除存档").default(!0)
  // 注:F5 / F9 快捷键由 ctx.input.registerAction (走 KeyBindingSystem) 注册,
  // 玩家在个性化 → 输入按键 tab 改键。
})));
ve = ia([
  Q({
    id: "save-screen",
    label: "存档画面",
    exposeUI: !1,
    // 保留快存/快读和截图控制器,React 版不再进入 UI 列表
    autonomous: !0,
    // F5/F9 全局键由 onRegister 绑定
    /**
     * 2026-05 Internal Extension Points §11.2:SaveScreen 同时支持 save / load 两个 slot,
     * 通过 mode payload 区分(由 ctx.system.invoke 透传)。
     *
     * 2026-05-19 实装:ctx.system.invoke(Save) → payload 默认填 { mode: "save" };
     * ctx.system.invoke(Load) → 调用方应该传 { mode: "load" }。
     * 兼容:payload 为空时按 "save" 模式渲染(toolbar 现有调用没传 payload)。
     */
    supportsSlot: [P.Save, P.Load]
  })
], ve);
var fa = Object.defineProperty, ya = Object.getOwnPropertyDescriptor, ga = (e, r, a) => r in e ? fa(e, r, { enumerable: !0, configurable: !0, writable: !0, value: a }) : e[r] = a, ma = (e, r, a, n) => {
  for (var o = n > 1 ? void 0 : n ? ya(r, a) : r, s = e.length - 1, l; s >= 0; s--)
    (l = e[s]) && (o = l(o) || o);
  return o;
}, ba = (e, r, a) => ga(e, r + "", a);
const ha = () => {
  const e = ee(), r = e.history.useSnapshot(), a = e.settings.get("allowVoiceReplay") ?? !0, n = e.settings.get("maxEntries") ?? 200, { phase: o, requestClose: s } = de(e, "history-screen"), l = r.entries.slice(-n), u = V(null);
  L(() => {
    const y = u.current;
    if (!y) return;
    const v = window.setTimeout(() => {
      y.scrollTop = y.scrollHeight;
    }, 100);
    return () => window.clearTimeout(v);
  }, [l.length]), L(() => {
    const y = (k) => {
      k.key === "Escape" && s();
    }, v = (k) => {
      k.button === 1 && (k.preventDefault(), s());
    };
    return window.addEventListener("keydown", y), window.addEventListener("auxclick", v), () => {
      window.removeEventListener("keydown", y), window.removeEventListener("auxclick", v);
    };
  }, [s]);
  const g = Math.max(0, l.length - 12), b = le(o), f = A({
    hidden: { opacity: 0, transform: "scaleY(0)" },
    delay: 120,
    duration: t.durSlow + 80
  }), d = A({
    hidden: { opacity: 0, transform: "translateY(14px)" },
    delay: 180
  });
  return /* @__PURE__ */ S(
    "div",
    {
      onContextMenu: (y) => {
        y.preventDefault(), s();
      },
      style: {
        position: "absolute",
        inset: 0,
        background: t.bgOverlayStrong,
        backdropFilter: "blur(28px)",
        WebkitBackdropFilter: "blur(28px)",
        color: t.textPrimary,
        fontFamily: t.fontUI,
        display: "flex",
        flexDirection: "column",
        willChange: "opacity",
        ...b
      },
      children: [
        /* @__PURE__ */ i(
          ce,
          {
            eyebrow: "History",
            title: "历史回顾",
            phase: o,
            rightSlot: /* @__PURE__ */ S(re, { children: [
              /* @__PURE__ */ S(
                "span",
                {
                  style: {
                    fontFamily: t.fontMono,
                    fontSize: 14,
                    color: t.textMuted,
                    fontWeight: 600,
                    fontVariantNumeric: "tabular-nums",
                    marginRight: 4
                  },
                  children: [
                    l.length,
                    " 条"
                  ]
                }
              ),
              /* @__PURE__ */ i(ae, { onClick: s })
            ] })
          }
        ),
        /* @__PURE__ */ i(
          "div",
          {
            ref: u,
            className: "avg-shell-scrollbar",
            style: {
              flex: 1,
              overflowY: "auto",
              padding: "24px 80px 80px"
            },
            children: /* @__PURE__ */ S(
              "div",
              {
                style: {
                  maxWidth: 880,
                  margin: "0 auto",
                  position: "relative"
                },
                children: [
                  /* @__PURE__ */ i(
                    "div",
                    {
                      style: {
                        position: "absolute",
                        left: 156,
                        top: 8,
                        bottom: 8,
                        width: 1.5,
                        background: `linear-gradient(180deg, transparent 0%, ${t.borderRegular} 8%, ${t.borderRegular} 92%, transparent 100%)`,
                        transformOrigin: "top",
                        ...f
                      }
                    }
                  ),
                  l.length === 0 && /* @__PURE__ */ i(
                    "div",
                    {
                      style: {
                        textAlign: "center",
                        marginTop: 100,
                        fontFamily: t.fontDisplay,
                        fontSize: 22,
                        color: t.textFaint,
                        fontWeight: 500,
                        ...d
                      },
                      children: "暂无历史记录"
                    }
                  ),
                  l.map((y, v) => {
                    const k = v >= g, _ = k ? 140 + (v - g) * 30 : 0;
                    return /* @__PURE__ */ i(
                      xa,
                      {
                        speaker: y.name,
                        text: y.text,
                        voiceUri: a ? y.voiceUri : void 0,
                        isChoice: !!y.isChoice,
                        onReplay: (C) => void e.history.replayVoice(C),
                        animationDelay: _,
                        shouldAnimate: k
                      },
                      y.uuid ?? v
                    );
                  })
                ]
              }
            )
          }
        )
      ]
    }
  );
}, xa = ({
  speaker: e,
  text: r,
  voiceUri: a,
  isChoice: n,
  onReplay: o,
  animationDelay: s,
  shouldAnimate: l
}) => {
  const [u, c] = $(!1), g = A({
    hidden: l ? { opacity: 0, transform: "translateY(12px) scale(0.98)" } : {},
    delay: s
  });
  return /* @__PURE__ */ i("div", { style: l ? g : void 0, children: /* @__PURE__ */ S(
    "div",
    {
      onMouseEnter: () => c(!0),
      onMouseLeave: () => c(!1),
      style: {
        display: "grid",
        gridTemplateColumns: "144px 24px 1fr auto",
        gap: 16,
        padding: "18px 16px",
        position: "relative",
        alignItems: "start",
        borderRadius: t.radiusMd,
        background: u ? t.accentSoft : "transparent",
        marginLeft: -16,
        marginRight: -16,
        transition: `background ${t.durBase}ms ${t.easeOut}`
      },
      children: [
        /* @__PURE__ */ i(
          "div",
          {
            style: {
              fontFamily: t.fontUI,
              fontSize: 15,
              fontWeight: 700,
              letterSpacing: "0.02em",
              color: n ? t.accent : t.textPrimary,
              textAlign: "right",
              paddingTop: 2,
              paddingRight: 8
            },
            children: n ? "▸ 选择" : e || ""
          }
        ),
        /* @__PURE__ */ i(
          "div",
          {
            style: {
              position: "relative",
              height: "100%",
              display: "flex",
              justifyContent: "center"
            },
            children: /* @__PURE__ */ i(
              "div",
              {
                style: {
                  width: 10,
                  height: 10,
                  marginTop: 8,
                  borderRadius: "50%",
                  background: u || n ? t.accent : t.borderStrong,
                  border: `2.5px solid ${t.bgOverlayStrong}`,
                  transition: `background ${t.durFast}ms ${t.easeOut}, transform ${t.durFast}ms ${t.easeOut}`,
                  transform: u ? "scale(1.4)" : "scale(1)",
                  boxShadow: u ? `0 0 0 6px ${t.accentSoft}, 0 0 16px ${t.accentGlow}` : "none"
                }
              }
            )
          }
        ),
        /* @__PURE__ */ i(
          "div",
          {
            style: {
              fontSize: 16,
              lineHeight: 1.7,
              color: n ? t.accent : t.textPrimary,
              fontStyle: "normal",
              fontWeight: n ? 600 : 400,
              paddingTop: 0,
              textWrap: "pretty"
            },
            children: r
          }
        ),
        /* @__PURE__ */ i("div", { style: { paddingTop: 0 }, children: a && /* @__PURE__ */ i(
          va,
          {
            onClick: () => o(a),
            highlight: u
          }
        ) })
      ]
    }
  ) });
}, va = ({ onClick: e, highlight: r }) => {
  const a = H();
  return /* @__PURE__ */ i(
    "button",
    {
      onClick: e,
      onPointerDown: a.handlers.onPointerDown,
      onPointerLeave: a.handlers.onPointerLeave,
      "aria-label": "重播语音",
      title: "重播语音",
      style: {
        appearance: "none",
        width: 36,
        height: 36,
        borderRadius: "50%",
        border: `1.5px solid ${r ? t.borderAccent : t.borderSubtle}`,
        background: r ? t.accentSoft : "transparent",
        color: r ? t.accent : t.textMuted,
        cursor: "default",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        transform: a.pressed ? "scale(0.92)" : "scale(1)",
        transition: `all ${t.durFast}ms ${t.easeOut}`,
        boxShadow: r ? `0 0 12px ${t.accentGlow}` : "none"
      },
      children: /* @__PURE__ */ i("svg", { width: "13", height: "13", viewBox: "0 0 13 13", "aria-hidden": !0, children: /* @__PURE__ */ i(
        "path",
        {
          d: "M3 2.5v8l7-4z",
          fill: "currentColor",
          stroke: "currentColor",
          strokeWidth: "0.5",
          strokeLinejoin: "round"
        }
      ) })
    }
  );
};
let Se = class extends Z {
  /**
   * 注册"打开历史画面"语义动作 + 订阅触发。键位由 KeyBindingSystem 管理:
   *   - default_keys: middleclick (鼠标中键,跟之前 settings 默认一致)
   *   - 玩家在"输入按键"tab 改键 → 自动生效
   */
  static onRegister(e) {
    e.input.registerAction({
      id: "avg.internal.default-shell.open-history",
      label: "呼出历史画面",
      defaultKeys: ["middleclick"]
    }), e.input.onAction("avg.internal.default-shell.open-history", () => {
      G(
        e.system.invoke(P.History, void 0, {
          modal: !0
        })
      );
    });
  }
  render() {
    return { component: ha, props: {} };
  }
};
ba(Se, "settings", K((e) => ({
  maxEntries: e.number("最大历史条数").default(200).range(10, 1e3).step(10),
  allowVoiceReplay: e.boolean("允许语音重播").default(!0)
  // 注:呼出快捷键由 ctx.input.registerAction (走 KeyBindingSystem) 注册,
  // 玩家在个性化 → 输入按键 tab 改键。
})));
Se = ma([
  Q({
    id: "history-screen",
    label: "历史画面",
    exposeUI: !1,
    // 保留呼出快捷键,React 版不再进入 UI 列表
    autonomous: !0,
    // 全局打开历史快捷键由 onRegister 绑定
    /** 2026-05 Internal Extension Points §6.1:声明本 UI 实现"历史"槽位。 */
    supportsSlot: P.History
  })
], Se);
const Nt = 50, Sa = 100;
function Ma(e) {
  if (typeof e == "number")
    return Number.isFinite(e) ? e : null;
  if (typeof e != "string" || e.trim() === "") return null;
  const r = Number(e);
  return Number.isFinite(r) ? r : null;
}
function wa(e) {
  const r = Ma(e);
  return r === null ? Nt : Math.round(Math.max(0, Math.min(Sa, r)));
}
const Fe = Nt;
function ne(e) {
  return wa(e);
}
var ka = Object.defineProperty, _a = Object.getOwnPropertyDescriptor, $a = (e, r, a) => r in e ? ka(e, r, { enumerable: !0, configurable: !0, writable: !0, value: a }) : e[r] = a, Ca = (e, r, a, n) => {
  for (var o = n > 1 ? void 0 : n ? _a(r, a) : r, s = e.length - 1, l; s >= 0; s--)
    (l = e[s]) && (o = l(o) || o);
  return o;
}, Ia = (e, r, a) => $a(e, r + "", a);
const Fa = () => {
  const e = ee(), r = e.settings.get("allowReset") ?? !0, { phase: a, requestClose: n } = de(e, "settings-screen"), [o, s] = e.config.useValue("masterVolume"), [l, u] = e.config.useValue("bgmVolume"), [c, g] = e.config.useValue("seVolume"), [b, f] = e.config.useValue("voiceVolume"), [d, m] = e.config.useValue("textSpeed"), [y, v] = e.config.useValue("autoModeTextSpeed"), [k, _] = e.config.useValue("skipMode"), [C, R] = e.config.useValue(
    "stopVoiceOnNextDialogue"
  ), w = e.game.window.canFullscreen(), [D, M] = e.game.window.useFullscreen(), F = () => {
    e.config.reset();
  };
  L(() => {
    const p = (O) => {
      O.key === "Escape" && n();
    };
    return window.addEventListener("keydown", p), () => window.removeEventListener("keydown", p);
  }, [n]);
  const h = 120, I = 35, T = 80, z = h + T * 2, B = le(a), [te, oe] = $(!1);
  return L(() => {
    const p = window.setTimeout(() => oe(!0), 100);
    return () => window.clearTimeout(p);
  }, []), /* @__PURE__ */ S(
    "div",
    {
      onContextMenu: (p) => {
        p.preventDefault(), n();
      },
      style: {
        position: "absolute",
        inset: 0,
        background: t.bgOverlay,
        backdropFilter: te ? "blur(24px)" : "none",
        WebkitBackdropFilter: te ? "blur(24px)" : "none",
        color: t.textPrimary,
        fontFamily: t.fontUI,
        display: "flex",
        flexDirection: "column",
        ...B
      },
      children: [
        /* @__PURE__ */ i(
          ce,
          {
            eyebrow: "Preferences",
            title: "设置",
            phase: a,
            rightSlot: /* @__PURE__ */ S(re, { children: [
              r && /* @__PURE__ */ i(zr, { onClick: F, children: "恢复默认" }),
              /* @__PURE__ */ i(ae, { onClick: n })
            ] })
          }
        ),
        /* @__PURE__ */ i(
          "div",
          {
            className: "avg-shell-scrollbar",
            style: {
              flex: 1,
              overflowY: "auto",
              padding: "32px 80px 80px"
            },
            children: /* @__PURE__ */ S(
              "div",
              {
                style: {
                  maxWidth: 880,
                  margin: "0 auto",
                  display: "flex",
                  flexDirection: "column",
                  gap: 40
                },
                children: [
                  /* @__PURE__ */ S(ge, { title: "音量", sectionDelay: h - 40, phase: a, children: [
                    /* @__PURE__ */ i(
                      J,
                      {
                        label: "主音量",
                        value: o ?? 100,
                        onChange: (p) => s(p),
                        delay: h + I * 0,
                        phase: a
                      }
                    ),
                    /* @__PURE__ */ i(
                      J,
                      {
                        label: "背景音乐",
                        value: l ?? 100,
                        onChange: (p) => u(p),
                        delay: h + I * 1,
                        phase: a
                      }
                    ),
                    /* @__PURE__ */ i(
                      J,
                      {
                        label: "音效",
                        value: c ?? 100,
                        onChange: (p) => g(p),
                        delay: h + I * 2,
                        phase: a
                      }
                    ),
                    /* @__PURE__ */ i(
                      J,
                      {
                        label: "语音",
                        value: b ?? 100,
                        onChange: (p) => f(p),
                        delay: h + I * 3,
                        phase: a,
                        isLast: !0
                      }
                    )
                  ] }),
                  /* @__PURE__ */ S(ge, { title: "文本与播放", sectionDelay: h + T, phase: a, children: [
                    /* @__PURE__ */ i(
                      J,
                      {
                        label: "文本速度",
                        value: ne(
                          d ?? Fe
                        ),
                        onChange: (p) => m(ne(p)),
                        delay: h + T + I * 1,
                        phase: a
                      }
                    ),
                    /* @__PURE__ */ i(
                      J,
                      {
                        label: "自动播放速度",
                        value: ne(
                          y ?? Fe
                        ),
                        onChange: (p) => v(ne(p)),
                        delay: h + T + I * 2,
                        phase: a
                      }
                    ),
                    /* @__PURE__ */ i(se, { label: "跳过模式", delay: h + T + I * 3, phase: a, children: /* @__PURE__ */ i(
                      Te,
                      {
                        options: [
                          { value: "read", label: "只跳已读" },
                          { value: "all", label: "全部跳过" }
                        ],
                        value: k ?? "read",
                        onChange: (p) => _(p)
                      }
                    ) }),
                    /* @__PURE__ */ i(se, { label: "切换对话停止上句语音", delay: h + T + I * 4, phase: a, isLast: !0, children: /* @__PURE__ */ i(
                      Pa,
                      {
                        checked: !!C,
                        onChange: (p) => R(p)
                      }
                    ) })
                  ] }),
                  w && /* @__PURE__ */ i(
                    ge,
                    {
                      title: "显示",
                      sectionDelay: z,
                      phase: a,
                      children: /* @__PURE__ */ i(
                        se,
                        {
                          label: "屏幕模式",
                          delay: z + I,
                          phase: a,
                          isLast: !0,
                          children: /* @__PURE__ */ i(
                            Te,
                            {
                              options: [
                                { value: "windowed", label: "窗口" },
                                { value: "fullscreen", label: "全屏" }
                              ],
                              value: D ? "fullscreen" : "windowed",
                              onChange: (p) => M(p === "fullscreen")
                            }
                          )
                        }
                      )
                    }
                  )
                ]
              }
            )
          }
        )
      ]
    }
  );
}, ge = ({ title: e, sectionDelay: r, children: a }) => {
  const n = A({
    hidden: { opacity: 0, transform: "translateX(-16px)" },
    delay: r
  }), o = A({
    hidden: { opacity: 0, transform: "scaleX(0)" },
    delay: r + 60
  });
  return /* @__PURE__ */ S("section", { children: [
    /* @__PURE__ */ S(
      "div",
      {
        style: {
          display: "flex",
          alignItems: "baseline",
          gap: 16,
          marginBottom: 20,
          ...n
        },
        children: [
          /* @__PURE__ */ i(
            "h3",
            {
              style: {
                fontFamily: t.fontDisplay,
                fontSize: 24,
                fontWeight: 700,
                margin: 0,
                letterSpacing: "0.005em"
              },
              children: e
            }
          ),
          /* @__PURE__ */ i(
            "div",
            {
              style: {
                flex: 1,
                height: 1,
                background: `linear-gradient(90deg, ${t.borderRegular} 0%, transparent 100%)`,
                transformOrigin: "left",
                ...o
              }
            }
          )
        ]
      }
    ),
    /* @__PURE__ */ i(
      "div",
      {
        style: {
          background: t.bgSurface,
          border: `1px solid ${t.borderSubtle}`,
          borderRadius: t.radiusLg,
          padding: "8px 32px",
          boxShadow: "inset 0 1px 0 rgba(255,255,255,0.03)"
        },
        children: a
      }
    )
  ] });
}, se = ({ label: e, delay: r, isLast: a, children: n }) => {
  const o = A({
    hidden: { opacity: 0, transform: "translateY(12px) scale(0.98)" },
    delay: r
  });
  return /* @__PURE__ */ S(
    "div",
    {
      style: {
        display: "flex",
        alignItems: "center",
        gap: 24,
        padding: "20px 0",
        borderBottom: a ? "none" : `1px solid ${t.borderSubtle}`,
        ...o
      },
      children: [
        /* @__PURE__ */ i(
          "div",
          {
            style: {
              minWidth: 200,
              fontSize: 16,
              color: t.textPrimary,
              fontWeight: 500
            },
            children: e
          }
        ),
        /* @__PURE__ */ i(
          "div",
          {
            style: {
              flex: 1,
              display: "flex",
              justifyContent: "flex-end",
              alignItems: "center"
            },
            children: n
          }
        )
      ]
    }
  );
}, J = ({ label: e, value: r, onChange: a, delay: n, phase: o, isLast: s }) => {
  const l = Number.isFinite(r) ? Math.max(0, Math.min(100, r)) : 0;
  return /* @__PURE__ */ S(se, { label: e, delay: n, phase: o, isLast: s, children: [
    /* @__PURE__ */ i(Ta, { value: l, onChange: a, min: 0, max: 100 }),
    /* @__PURE__ */ i(
      "div",
      {
        style: {
          fontFamily: t.fontMono,
          fontSize: 14,
          color: t.textPrimary,
          minWidth: 48,
          textAlign: "right",
          paddingLeft: 20,
          fontVariantNumeric: "tabular-nums",
          fontWeight: 600
        },
        children: Math.round(l)
      }
    )
  ] });
}, Ta = ({ value: e, min: r, max: a, onChange: n }) => {
  const o = V(null), [s, l] = $(!1), [u, c] = $(!1), b = ((Number.isFinite(e) ? Math.max(r, Math.min(a, e)) : r) - r) / (a - r) * 100, f = (d) => {
    const m = o.current;
    if (!m) return;
    const y = m.getBoundingClientRect(), v = Math.max(0, Math.min(1, (d - y.left) / y.width));
    n(r + v * (a - r));
  };
  return L(() => {
    if (!s) return;
    const d = (y) => f(y.clientX), m = () => l(!1);
    return window.addEventListener("pointermove", d), window.addEventListener("pointerup", m), () => {
      window.removeEventListener("pointermove", d), window.removeEventListener("pointerup", m);
    };
  }, [s]), /* @__PURE__ */ S(
    "div",
    {
      ref: o,
      onPointerDown: (d) => {
        l(!0), f(d.clientX);
      },
      onMouseEnter: () => c(!0),
      onMouseLeave: () => c(!1),
      style: {
        position: "relative",
        flex: 1,
        height: 28,
        display: "flex",
        alignItems: "center",
        cursor: "default",
        userSelect: "none"
      },
      children: [
        /* @__PURE__ */ i(
          "div",
          {
            style: {
              position: "absolute",
              left: 0,
              right: 0,
              height: 5,
              background: t.borderSubtle,
              borderRadius: 999
            }
          }
        ),
        /* @__PURE__ */ i(
          "div",
          {
            style: {
              position: "absolute",
              left: 0,
              width: `${b}%`,
              height: 5,
              background: `linear-gradient(90deg, ${t.accent} 0%, ${t.accent} 100%)`,
              borderRadius: 999,
              boxShadow: u || s ? `0 0 12px ${t.accentGlow}` : "none",
              transition: s ? "none" : `width ${t.durFast}ms ${t.easeOut}, box-shadow ${t.durBase}ms ${t.easeOut}`
            }
          }
        ),
        /* @__PURE__ */ i(
          "div",
          {
            style: {
              position: "absolute",
              left: `${b}%`,
              width: 20,
              height: 20,
              marginLeft: -10,
              borderRadius: "50%",
              background: t.textPrimary,
              boxShadow: s || u ? `0 0 0 8px ${t.accentSoft}, 0 4px 12px rgba(0,0,0,0.5)` : "0 2px 8px rgba(0,0,0,0.4)",
              transform: s ? "scale(1.18)" : u ? "scale(1.08)" : "scale(1)",
              transition: s ? `box-shadow ${t.durFast}ms ${t.easeOut}, transform ${t.durFast}ms ${t.easeOut}` : `left ${t.durFast}ms ${t.easeOut}, box-shadow ${t.durFast}ms ${t.easeOut}, transform ${t.durFast}ms ${t.easeOut}`
            }
          }
        )
      ]
    }
  );
}, Te = ({ options: e, value: r, onChange: a }) => {
  const n = e.findIndex((s) => s.value === r), o = n >= 0 ? n : 0;
  return /* @__PURE__ */ S(
    "div",
    {
      style: {
        position: "relative",
        display: "inline-flex",
        background: t.bgSunken,
        border: `1px solid ${t.borderSubtle}`,
        borderRadius: t.radiusMd,
        padding: 4
      },
      children: [
        /* @__PURE__ */ i(
          "div",
          {
            style: {
              position: "absolute",
              top: 4,
              bottom: 4,
              left: `calc(${o} * (100% - 8px) / ${e.length} + 4px)`,
              width: `calc((100% - 8px) / ${e.length})`,
              background: t.accent,
              borderRadius: t.radiusSm,
              transition: `left ${t.durBase}ms ${t.easeOut}`,
              boxShadow: `0 2px 12px ${t.accentGlow}`
            }
          }
        ),
        e.map((s) => /* @__PURE__ */ i(
          Oa,
          {
            active: s.value === r,
            onClick: () => a(s.value),
            children: s.label
          },
          s.value
        ))
      ]
    }
  );
}, Oa = ({ active: e, onClick: r, children: a }) => {
  const n = H();
  return /* @__PURE__ */ i(
    "button",
    {
      ...n.handlers,
      onClick: r,
      style: {
        position: "relative",
        zIndex: 1,
        appearance: "none",
        background: "transparent",
        border: "none",
        padding: "10px 24px",
        fontSize: 14,
        fontFamily: t.fontUI,
        fontWeight: 600,
        letterSpacing: "0.02em",
        color: e ? t.textOnAccent : t.textMuted,
        cursor: "default",
        minWidth: 116,
        transform: n.pressed ? "scale(0.96)" : "scale(1)",
        transition: `color ${t.durFast}ms ${t.easeOut}, transform ${t.durFast}ms ${t.easeOut}`
      },
      children: a
    }
  );
}, Pa = ({ checked: e, onChange: r }) => {
  const a = H();
  return /* @__PURE__ */ i(
    "button",
    {
      ...a.handlers,
      onClick: () => r(!e),
      role: "switch",
      "aria-checked": e,
      style: {
        appearance: "none",
        position: "relative",
        width: 52,
        height: 30,
        borderRadius: 999,
        border: `1px solid ${e ? t.borderAccent : t.borderRegular}`,
        background: e ? t.accent : t.bgSunken,
        cursor: "default",
        padding: 0,
        transform: a.pressed ? "scale(0.94)" : "scale(1)",
        transition: `background ${t.durBase}ms ${t.easeOut}, border-color ${t.durBase}ms ${t.easeOut}, transform ${t.durFast}ms ${t.easeOut}`,
        boxShadow: e ? `0 0 16px ${t.accentGlow}` : "none"
      },
      children: /* @__PURE__ */ i(
        "div",
        {
          style: {
            position: "absolute",
            top: 3,
            left: e ? 24 : 3,
            width: 22,
            height: 22,
            borderRadius: "50%",
            background: e ? t.textOnAccent : t.textPrimary,
            boxShadow: "0 2px 6px rgba(0,0,0,0.5)",
            transition: `left ${t.durBase}ms ${t.easeOut}, background ${t.durBase}ms ${t.easeOut}`
          }
        }
      )
    }
  );
};
let Me = class extends Z {
  /**
   * 可视化设置界面(本扩展 ui/settings-screen.json)的控制器 ——
   * 扩展复合容器(视图/控制器)的第一个 dogfooding:布局住在 JSON
   * (编辑器可看可拷可改),动态行为在这里操作控件。
   * 「设置」槽位默认绑定 "ui:@avg.internal.default-shell/settings-screen"。
   * 本类只保留控制器职责,不再向 UI host 导出 React 版画面。
   */
  static onRegister(e) {
    e.visualUI.onOpen(
      "@avg.internal.default-shell/settings-screen",
      (r) => {
        var n;
        if (!e.game.window.canFullscreen())
          for (const o of [
            "display-card",
            "display-title",
            "display-label",
            "display-switch"
          ])
            (n = r.get(o)) == null || n.setHidden(!0);
        const a = r.get("reset-btn");
        a == null || a.on("click", () => {
          e.config.reset().catch((o) => {
            console.error("[settings-screen] 恢复默认设置失败", o);
          });
        });
      }
    );
  }
  render() {
    return { component: Fa, props: {} };
  }
};
Ia(Me, "settings", K((e) => ({
  allowReset: e.boolean("允许重置默认").default(!0)
})));
Me = Ca([
  Q({
    id: "settings-screen",
    label: "设置画面",
    exposeUI: !1,
    // 保留可视化界面控制器,React 版不再进入 UI 列表
    // 2026-05 Internal Extension Points §6.1:声明本 UI 实现"设置"槽位。
    supportsSlot: P.Settings
  })
], Me);
var Ra = Object.defineProperty, La = Object.getOwnPropertyDescriptor, Aa = (e, r, a) => r in e ? Ra(e, r, { enumerable: !0, configurable: !0, writable: !0, value: a }) : e[r] = a, za = (e, r, a, n) => {
  for (var o = n > 1 ? void 0 : n ? La(r, a) : r, s = e.length - 1, l; s >= 0; s--)
    (l = e[s]) && (o = l(o) || o);
  return o;
}, Ea = (e, r, a) => Aa(e, r + "", a);
const Wa = [
  { key: "skip", label: "跳过" },
  { key: "auto", label: "自动" },
  { key: "save", label: "存档" },
  { key: "load", label: "读档" },
  { key: "quickSave", label: "快存" },
  { key: "quickLoad", label: "快读" },
  { key: "history", label: "历史" },
  { key: "settings", label: "设置" },
  { key: "hide", label: "隐藏" }
], Ba = () => {
  const e = ee(), r = e.settings.useValue("showToolbar")[0] ?? !0, a = e.settings.useValue("showSkip")[0] ?? !0, n = e.settings.useValue("showAuto")[0] ?? !0, o = e.settings.useValue("showSave")[0] ?? !0, s = e.settings.useValue("showLoad")[0] ?? !0, l = e.settings.useValue("showQuickSave")[0] ?? !0, u = e.settings.useValue("showQuickLoad")[0] ?? !0, c = e.settings.useValue("showHistory")[0] ?? !0, g = e.settings.useValue("showSettings")[0] ?? !0, b = e.settings.useValue("showHide")[0] ?? !0, f = e.dialogue.useSkipMode(), d = e.dialogue.useAutoMode(), m = {
    skip: f ? "SKIP" : void 0,
    auto: d ? "AUTO" : void 0
  }, y = {
    skip: a,
    auto: n,
    save: o,
    load: s,
    quickSave: l,
    quickLoad: u,
    history: c,
    settings: g,
    hide: b
  }, [v, k] = $(!1);
  L(() => {
    const w = requestAnimationFrame(() => k(!0));
    return () => cancelAnimationFrame(w);
  }, []);
  const [_, C] = $(null);
  if (!r) return null;
  const R = (w) => {
    w === "skip" ? e.dialogue.toggleSkipMode() : w === "auto" ? e.dialogue.toggleAutoMode() : w === "settings" ? G(
      e.system.invoke(P.Settings, void 0, {
        modal: !0
      })
    ) : w === "save" ? G(
      e.system.invoke(
        P.Save,
        { mode: "save" },
        { modal: !0 }
      )
    ) : w === "load" ? G(
      e.system.invoke(
        P.Load,
        { mode: "load", source: "game" },
        { modal: !0 }
      )
    ) : w === "history" ? G(
      e.system.invoke(P.History, void 0, {
        modal: !0
      })
    ) : w === "quickSave" ? e.archive.quickSave().then(() => W("已快速存档", { type: "success" })).catch((D) => {
      console.error("[toolbar] quickSave failed", D), W("快速存档失败", { type: "error" });
    }) : w === "quickLoad" ? (async () => {
      try {
        await e.archive.quickLoad() || W("没有可读取的快速存档", { type: "warn" });
      } catch (D) {
        console.error("[toolbar] quickLoad failed", D), W("快速读档失败", { type: "error" });
      }
    })() : w === "hide" && e.dialogue.hideBox();
  };
  return /* @__PURE__ */ i(
    "div",
    {
      style: {
        position: "absolute",
        inset: 0,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        pointerEvents: "none"
      },
      children: /* @__PURE__ */ i(
        "div",
        {
          style: {
            pointerEvents: "auto",
            display: "flex",
            alignItems: "center",
            gap: 4,
            background: "rgba(11, 13, 16, 0.82)",
            backdropFilter: "blur(20px) saturate(160%)",
            WebkitBackdropFilter: "blur(20px) saturate(160%)",
            border: `1px solid ${t.borderSubtle}`,
            borderRadius: t.radiusPill,
            padding: "8px 12px",
            boxShadow: "0 18px 48px rgba(0,0,0,0.55), 0 1px 0 rgba(255,255,255,0.06) inset, 0 0 0 1px rgba(255,255,255,0.02)",
            transform: v ? "translateY(0)" : "translateY(20px)",
            opacity: v ? 1 : 0,
            transition: `transform ${t.durSlow}ms ${t.easeOut}, opacity ${t.durBase}ms ${t.easeOut}`
          },
          children: Wa.map((w) => y[w.key] ? /* @__PURE__ */ i(
            Da,
            {
              isHover: _ === w.key,
              activeBadge: m[w.key],
              onMouseEnter: () => C(w.key),
              onMouseLeave: () => C(null),
              onClick: () => R(w.key),
              children: w.label
            },
            w.key
          ) : null)
        }
      )
    }
  );
}, Da = ({
  isHover: e,
  activeBadge: r,
  onMouseEnter: a,
  onMouseLeave: n,
  onClick: o,
  children: s
}) => {
  const l = H(), u = !!r;
  return /* @__PURE__ */ S(
    "button",
    {
      onMouseEnter: a,
      onMouseLeave: (c) => {
        n(), l.handlers.onPointerLeave(c);
      },
      onPointerDown: l.handlers.onPointerDown,
      onClick: o,
      style: {
        position: "relative",
        appearance: "none",
        // active 态优先级高于 hover —— 让"自动播放中"始终以 accent 配色呈现,
        // 即便鼠标没悬停也能识别。
        background: u || e ? t.accentSoft : "transparent",
        border: "none",
        color: u || e ? t.accent : t.textPrimary,
        fontFamily: t.fontUI,
        fontSize: 14,
        fontWeight: 600,
        letterSpacing: "0.08em",
        padding: "10px 20px",
        borderRadius: t.radiusPill,
        cursor: "default",
        transform: l.pressed ? "scale(0.94) translateY(0)" : e ? "translateY(-2px) scale(1.02)" : "translateY(0) scale(1)",
        transition: `color ${t.durFast}ms ${t.easeOut}, background ${t.durFast}ms ${t.easeOut}, transform ${t.durFast}ms ${t.easeOut}`,
        // 呼吸动画只在 active 态运行;否则 animation:none 让 transition 接管样式。
        animation: u ? "avg-toolbar-active-breath 2.4s ease-in-out infinite" : "none"
      },
      children: [
        s,
        r && /* @__PURE__ */ i(
          "span",
          {
            "aria-hidden": !0,
            style: {
              position: "absolute",
              top: -4,
              right: -4,
              padding: "2px 6px",
              background: t.accent,
              color: t.textOnAccent,
              borderRadius: 999,
              fontFamily: t.fontMono,
              fontSize: 9,
              fontWeight: 700,
              letterSpacing: "0.12em",
              lineHeight: 1.1,
              boxShadow: `0 0 10px ${t.accentGlow}`,
              pointerEvents: "none"
            },
            children: r
          }
        )
      ]
    }
  );
}, Oe = /* @__PURE__ */ new WeakSet();
let we = class extends Z {
  /**
   * Toolbar 与对白生命周期解耦,注册后保持挂载。
   * 总开关与运行重建决定挂载；可视化文档默认跟随对白,也可关闭同步。
   */
  static onRegister(e) {
    const r = e.getHost(), a = r == null ? void 0 : r.application;
    if (a && Oe.has(a)) return;
    a && Oe.add(a);
    let n = !1, o = null, s = !1, l = 0, u = 0;
    const c = async () => {
      if (!s) {
        s = !0;
        try {
          for (; o === null || o !== n; ) {
            const f = n, d = l, m = u;
            try {
              if (f ? await e.system.invoke(P.Toolbar) : await e.system.close(P.Toolbar), m !== u) continue;
              o = f;
            } catch (y) {
              if (f !== n || d !== l)
                continue;
              console.warn(
                f ? "[toolbar] 工具栏系统槽位打开失败" : "[toolbar] 工具栏系统槽位关闭失败",
                y
              );
              return;
            }
          }
        } finally {
          s = !1;
        }
      }
    }, g = () => {
      const f = e.system.getBinding(P.Toolbar);
      return !!(f && !f.startsWith("ui:"));
    }, b = () => {
      n = (e.settings.get("showToolbar") ?? !0) && (!g() || e.dialogue.line() !== null), l += 1, c();
    };
    e.subscribe("runtime:started", () => {
      u += 1, o = null, b();
    }), e.subscribe("dialogue:changed", () => {
      g() && b();
    }), e.settings.subscribe("showToolbar", b), b();
  }
  render() {
    return { component: Ba, props: {} };
  }
};
Ea(we, "settings", K((e) => ({
  // 总开关:是否启用整个工具栏；对白同步由工具栏 UI 文档单独控制。
  // 关闭后,所有按钮一并隐藏 —— 这是相对下面按钮级开关更高一层的"模块级"开关。
  showToolbar: e.boolean("显示对话工具栏").default(!0),
  // 下面每个按钮级开关用 enabledWhen 挂到总开关上:总开关关掉时,
  // 它们在设置面板里置灰(不可点),但各自的值保持不变 —— 重开总开关后恢复。
  showSkip: e.boolean("显示跳过按钮").default(!0).enabledWhen("showToolbar"),
  showAuto: e.boolean("显示自动播放按钮").default(!0).enabledWhen("showToolbar"),
  showSave: e.boolean("显示存档按钮").default(!0).enabledWhen("showToolbar"),
  showLoad: e.boolean("显示读档按钮").default(!0).enabledWhen("showToolbar"),
  showQuickSave: e.boolean("显示快速存档按钮").default(!0).enabledWhen("showToolbar"),
  showQuickLoad: e.boolean("显示快速读档按钮").default(!0).enabledWhen("showToolbar"),
  showHistory: e.boolean("显示历史按钮").default(!0).enabledWhen("showToolbar"),
  showSettings: e.boolean("显示设置按钮").default(!0).enabledWhen("showToolbar"),
  showHide: e.boolean("显示隐藏对话框按钮").default(!0).enabledWhen("showToolbar")
})));
we = za([
  Q({
    id: "toolbar",
    label: "工具栏",
    exposeUI: !1,
    // 保留工具栏显隐控制器,React 版不再进入 UI 列表
    autonomous: !0
    // 工具栏独立挂载,文档决定是否跟随对白显隐
    // 本类只负责同步工具栏总开关；实际打开哪份工具栏由 Toolbar 系统槽位决定。
  })
], we);
const ja = /* @__PURE__ */ Object.assign({ "../ui/choice-dialog.json": qt, "../ui/dialogue-box.json": Kt, "../ui/gallery-screen.json": Zt, "../ui/history-screen.json": tr, "../ui/input-dialog.json": ar, "../ui/loading-screen.json": nr, "../ui/message-box.json": ir, "../ui/paragraph-cinematic-centered.json": dr, "../ui/paragraph-handwritten.json": pr, "../ui/paragraph-literary.json": fr, "../ui/paragraph-sharp.json": gr, "../ui/paragraph.json": br, "../ui/save-screen.json": xr, "../ui/settings-screen.json": Sr, "../ui/title-screen.json": wr, "../ui/toolbar.json": _r }), Ga = Object.fromEntries(
  Object.entries(ja).map(([e, r]) => [
    e.replace(/^.*\/([^/]+)\.json$/, "$1"),
    r.default
  ])
);
export {
  j as GalleryScreen,
  Se as HistoryScreen,
  ve as SaveScreen,
  Me as SettingsScreen,
  be as TitleScreen,
  we as Toolbar,
  ke as manifest,
  Ga as visualUI
};
