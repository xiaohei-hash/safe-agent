import json
import re


class ToolParser:

    def parse(self, text: str):

        # 提取第一个 JSON 对象
        match = re.search(r'\{.*\}', text, re.DOTALL)

        if not match:
            return None

        json_text = match.group()

        try:
            return json.loads(json_text)

        except Exception as e:

            print("JSON PARSE ERROR:", e)

            return None