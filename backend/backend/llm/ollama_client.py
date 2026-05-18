import requests


class OllamaClient:

    def generate(self, prompt):

        # ===== 固定问题 =====

        if "IND-CPA" in prompt:

            return """
IND-CPA（Indistinguishability under Chosen Plaintext Attack）

是现代密码学中的重要安全定义。

它要求：

攻击者即使能够自由选择明文，
也无法区分两个密文分别对应哪个明文。

IND-CPA 是现代对称加密方案的重要安全标准。
"""

        if "Capability" in prompt:

            return """
Capability Security 是一种基于 capability token 的安全模型。

主体只有持有 capability，
才能访问资源。

相比 ACL：

1. 更符合最小权限原则
2. 更容易实现权限隔离
3. 权限传播更加明确
"""

        if "随机预言机" in prompt:

            return """
随机预言机模型（Random Oracle Model）

是一种理论安全模型。

它把哈希函数视为：
真正随机函数。

密码学研究中：

很多协议都会首先证明：
在随机预言机模型下安全。
"""

        if "最小权限" in prompt:

            return """
最小权限原则（Least Privilege）

表示：

系统中的主体，
只应获得完成任务所需的最小权限。

这样可以：

1. 减少攻击面
2. 降低权限滥用风险
3. 增强系统安全性
"""

        if "可证明安全" in prompt:

            return """
可证明安全（Provable Security）

是现代密码学中的核心思想。

研究者通过数学证明：

说明一个密码方案的安全性，
可以归约到某个困难数学问题。

例如：

RSA 安全性与大整数分解困难相关。
"""

        # ===== 真正 AI 对话 =====

        try:

            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "qwen2.5:3b",
                    "prompt": f"""
你是密码学与可证明安全理论专家。

请使用中文简洁回答。

用户问题：
{prompt}
""",
                    "stream": False
                },
                timeout=120
            )

            data = response.json()

            return data["response"]

        except Exception as e:

            return f"""
本地模型连接失败。

错误：
{str(e)}
"""