**專案目標 (Project Goal)** 我們要建立一個使用 Streamlit 驅動的 Web 應用程式，用於視覺化台股歷史股價。

**核心功能 (Core Features)**

1. **資料獲取**：能夠使用 `yfinance` 套件下載指定的台股歷史資料。
2. **專案資料夾**:lesson16
2. **互動介面**：
    - 提供股票選單，讓使用者可以選擇想查詢的股票。
    - 提供日期區間選擇器，讓使用者能篩選特定時間範圍的資料。
    - 以表格形式顯示篩選後的股價資料。
    - 以折線圖形式視覺化所選股票在指定時間內的價格走勢。

**開發流程與規則 (Development Workflow & Rules)**

1. **迭代開發**：我們將採用迭代（step-by-step）的方式完成這個專案。
2. **任務清單 (Todolist)**：在每一次的互動中，我會提供一個任務清單。
3. **您的任務**：
    - 請先檢查清單中已完成的項目 (`[x]`)。
    - 接著，請完成清單中**尚未**完成的項目 (`[]`)。
    - 完成後，請在您的回覆中更新任務清單，將您剛完成的項目打勾 (`[x]`)。

---

**本階段任務 (Current Task)**

**Todolist**

- [x] 目前每個圖表的 y 軸都是從 0 開始，這樣不利於觀察股價變化。請根據每張圖表實際要顯示的數值範圍，自動調整 y 軸的起始值（例如可從最小值附近開始），讓圖表更容易閱讀。

- [x] 請安裝plotly套件

- [x] 請將y軸的名稱改為`收盤價`