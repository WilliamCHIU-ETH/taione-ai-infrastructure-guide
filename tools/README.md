# 維護與重建

[← 閱讀入口](../README.md) · [來源索引](../SOURCES.md)

章節正文直接編輯 Markdown。每頁的 `BOOK-NAV` 區塊由工具重建；請勿把正文放進這個區塊。

## 圖片

圖解文字在 `sources/figures.json`；`build_figures.py` 生成獨立 SVG，`scenes.py` 提供事件紀錄、機器與資源分配等情境構圖。修改某張圖時需同步檢查情境構圖、替代文字、圖說和正文。

SVG 預設只輸出繪製內容加上留白：圖題與說明保留在 SVG 的 `<title>`／`<desc>`，結語由章節圖說承擔，圖高比帶標頭頁尾時約少四成。若某張圖需要圖內標頭（品牌行、圖題、副標）與頁尾（結語、示意聲明），在 `figures.json` 的條目加上 `"frame": "full"`。

章節嵌圖統一為 `<p align="center"><img src="…" width="560" alt="…"></p>`，桌面版限制顯示寬度，手機仍為滿版；下一段圖說固定為 `*圖 章-序｜圖題。說明* [SVG 原圖](…)`，圖題取自 `figures.json` 的 `title`。

```sh
python3 tools/build_figures.py
node tools/rasterize.cjs            # 全部
node tools/rasterize.cjs 06-a 06-b  # 只重出指定圖
```

PNG 轉換需可用的 Node.js `sharp` 套件和繁中字體。本次 PNG 使用 **Heiti TC**，以 2 倍尺寸渲染。若在其他作業系統重建，可安裝 Noto Sans TC，並用 Fontconfig 指定可寫入的快取目錄；字體替換後必須重新目視檢查。SVG 使用字體 fallback，PNG 保留既有輸出外觀。工具不會自行安裝套件或改系統字體。

## 導覽、來源與驗證

```sh
python3 tools/build_book.py
python3 tools/check_book.py
```

建構工具使用 `sources/references.json` 重建來源索引，並依章次產生前後章連結。檢查涵蓋章節數、引用登錄、本機相對連結與錨點、圖片存在、SVG 結構與收合標籤。URL 可連線不等於內容支持主張，事實更正仍要人工閱讀原始資料。

發布前，應另外在 GitHub 的 Markdown 預覽中核對圖片、前後章切換、桌面與窄螢幕閱讀。圖中數量僅供機制示意，不得當成實測規模或效能。
