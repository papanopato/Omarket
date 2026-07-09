from typing import Dict, Any

class FinanceAgent:
    role = "CFO"

    def __init__(self):
        pass

    def run(self, task: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        cashflow = {"initial_budget": context.get("budget") if context else None}
        risk = {"currency": "MAD", "liquidity": "low"}
        roi = {"estimate": "low-confidence"}
        return {
            "summary": f"Finance overview for {task}",
            "cashflow": cashflow,
            "risk": risk,
            "roi": roi,
            "recommendations": [{"reduce_costs": True}, {"monitor": "weekly"}],
        }
