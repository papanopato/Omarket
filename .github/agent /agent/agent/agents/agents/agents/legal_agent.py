from typing import Dict, Any

class LegalAgent:
    role = "Legal Advisor"

    def __init__(self):
        pass

    def run(self, task: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        legal_risk = {"regulatory": "low-medium", "contracts": "template-needed"}
        compliance = {"data_privacy": "review_morocco_law"}
        return {
            "summary": f"Legal notes for {task}",
            "legal_risk": legal_risk,
            "contracts": ["nda_template", "tos_template"],
            "compliance": compliance,
            "recommendations": ["create standard contracts", "set-up legal review"],
        }
