from skills.todo_skill import ToDoSkill
from core.zeus_strike_loader import ZeusStrikeLoader

class DummySkill:
    def execute(self, **params):
        return f"Executed dummy skill with params: {params}"

class SkillTree:
    def __init__(self):
        self.skills = {
            "dummy_skill": DummySkill(),
            "todo_skill": ToDoSkill()
        }
        self.zeus_loader = ZeusStrikeLoader()
        self.skills.update(self.zeus_loader.plugins)

    def register_skill(self, name, skill_module):
        self.skills[name] = skill_module

    def plan(self, intent, context):
        intent_lower = intent.lower()
        plan = []
        if "add todo" in intent_lower:
            text = intent.split(":", 1)[-1].strip() if ":" in intent else intent
            plan.append({"skill": "todo_skill", "action": "add", "params": {"text": text}})
        elif "list todo" in intent_lower:
            plan.append({"skill": "todo_skill", "action": "list", "params": {}})
        elif "mark done" in intent_lower:
            try:
                todo_id = int(intent_lower.split()[-1])
                plan.append({"skill": "todo_skill", "action": "done", "params": {"todo_id": todo_id}})
            except:
                pass
        elif "remove todo" in intent_lower:
            try:
                todo_id = int(intent_lower.split()[-1])
                plan.append({"skill": "todo_skill", "action": "remove", "params": {"todo_id": todo_id}})
            except:
                pass
        elif "flash" in intent_lower:
            plan.append({"skill": "flash_task", "params": {}})
        elif "strike" in intent_lower:
            plan.append({"skill": "strike_of_lightning", "params": {}})
        else:
            plan.append({"skill": "dummy_skill", "params": {"intent": intent, "context": context}})
        return plan

    def execute(self, plan):
        results = []
        for step in plan:
            skill_name = step["skill"]
            action = step.get("action")
            params = step.get("params", {})
            if skill_name in self.skills:
                skill = self.skills[skill_name]
                if action:
                    results.append(getattr(skill, f"{action}_todo")(**params) if "todo" in skill_name else skill.execute(**params))
                else:
                    results.append(skill.execute(**params))
            elif self.zeus_loader.plugins.get(skill_name):
                results.append(self.zeus_loader.execute(skill_name, **params))
            else:
                results.append(f"Skill '{skill_name}' not found.")
        return results
