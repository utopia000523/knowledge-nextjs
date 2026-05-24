#!/usr/bin/env python3
"""Generate April Dunford Sales Pitch expanded article JSON."""
import json
import os

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

article = {
    "id": "April-Dunford-Sales-Pitch-B2B\u9500\u552e\u53d9\u4e8b\u4e0e\u8d62\u5355\u65b9\u6cd5\u8bba",
    "category": "\u8425\u9500",
    "title": "April Dunford\u300aSales Pitch\u300bB2B\u9500\u552e\u53d9\u4e8b\u4e0e\u8d62\u5355\u65b9\u6cd5\u8bba",
    "keywords": [
        "April Dunford", "Sales Pitch", "B2B\u9500\u552e", "Positioning",
        "No Decision", "Champion", "Economic Buyer", "\u9500\u552e\u53d9\u4e8b",
        "Setup Follow-through", "\u53cc\u6bb5\u53d9\u4e8b", "\u4e70\u65b9\u51b3\u7b56", "\u5dee\u5f02\u5316\u4ef7\u503c"
    ],
    "summary": "\u2a2a\u2a2a\u6838\u5fc3\u4e3b\u9898\u2a2a\u2a2a\uff1a\u7528\u300cSetup\uff08\u5e02\u573a\u6d1e\u5bdf+\u66ff\u4ee3\u65b9\u6848+\u7406\u60f3\u89e3\uff09+ Follow-through\uff08\u4ea7\u54c1/\u4ef7\u503c/\u8bc1\u660e/\u5f02\u8bae/\u4e0b\u4e00\u6b65\uff09\u300d\u7684\u53cc\u6bb5\u53d9\u4e8b\u7ed3\u6784\uff0c\u5e2e\u52a9B2B\u4e70\u5bb6\u964d\u4f4e\u65e0\u51b3\u7b56\u98ce\u9669\uff0c\u628a\u5b9a\u4f4d\u8f6c\u5316\u6210\u771f\u6b63\u7684\u8d62\u5355\u5bf9\u8bdd\u3002",
    "importance": 5,
    "learned_at": "2026-05-14",
    "source": "April Dunford\u300aSales Pitch: How to Craft a Story to Stand Out and Win\u300b(2023)\uff1b\u516c\u5f00\u4e66\u8bc4\u4e0e\u65b9\u6cd5\u6458\u8981",
    "content": {
        "core_formula": "dummy",
        "layers": [{"level": 1, "title": "test", "content": "test"}],
        "updates": []
    }
}

print(f"Would write to: {DATA_DIR}")
print("Script loaded ok")
