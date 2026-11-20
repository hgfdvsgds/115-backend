"""Week 1：第一次模型呼叫。

把「請模型回答」還原成一次可觀察的 HTTP Request/Response。
對照 curl -v 的輸出：
  status -> Response Status Code
  reply  -> Response Body 的 choices[0].message.content
  usage  -> token 統計
"""

import json
import os

import requests

API_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
MODEL = "minimaxai/minimax-m3.1-flash"


def call_model(messages):
    api_key = os.environ["NVIDIA_API_KEY"]
    resp = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": MODEL,
            "messages": messages,
            "max_tokens": 512,
            "temperature": 1,
            "top_p": 0.95,
        },
        timeout=60,
    )
    print("status:", resp.status_code)
    data = resp.json()
    print(json.dumps(data, ensure_ascii=False, indent=2))
    if resp.ok:
        print("reply:", data["choices"][0]["message"]["content"])
    else:
        print("error:", data.get("error", data))
    return data


if __name__ == "__main__":
    call_model([{"role": "user", "content": "用一句話說明什麼是 HTTP"}])
