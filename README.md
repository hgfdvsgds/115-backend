# 115-backend

網頁程式設計 115 — Agent Runtime 六週實作。

## Week 1：第一次模型呼叫

用 NVIDIA 的 OpenAI 相容端點，送出一次 Chat Completions 請求，並觀察
Response 的 `status`、`choices[0].message.content` 與 `usage`。

### 環境需求

- Python 3.9+
- NVIDIA API key（<https://build.nvidia.com/>）

### 安裝

```bash
pip install -r requirements.txt
```

### 設定金鑰

金鑰只從環境變數讀取，**不要寫進程式碼**：

```bash
export NVIDIA_API_KEY=YOUR_NVIDIA_API_KEY
```

或放在 `.env`（已在 `.gitignore` 中排除）。

### 執行

```bash
python3 week1_single_call.py
```

預期輸出：

```
status: 200
{ ...完整 Response JSON... }
reply: HTTP 是...
```

### 對照 `curl -v`

| 程式輸出 | HTTP 對應位置 |
| --- | --- |
| `status` | Response Status Code（`< HTTP/2 200`） |
| `reply` | Response Body 的 `choices[0].message.content` |
| `usage` | Response Body 的 token 統計 |
| 送出的 `messages` | Request Body（`-d` 的內容） |

若 status 非 2xx，改看印出的 `error` 欄位判斷是認證、model 名稱或 JSON 格式的問題。
