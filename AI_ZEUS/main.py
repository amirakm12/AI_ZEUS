from core.meta_orchestrator import MetaOrchestrator
from personas.persona_manager import PersonaManager
from skills.skill_tree import SkillTree
from automation.automation_mesh import AutomationMesh
from memory.omniscient_memory import OmniscientMemory
from compute.compute_fabric import ComputeFabric
from security.security_core import SecurityCore
from ui.ui_hub import UIHub
from world.world_connector import WorldConnector

def main():
    persona_manager = PersonaManager()
    persona_manager.create_persona("Zeus", ["god", "developer", "designer", "hacker", "artist", "guru"])

    skill_tree = SkillTree()
    automation_mesh = AutomationMesh()
    memory = OmniscientMemory()
    compute_fabric = ComputeFabric()
    security_core = SecurityCore()
    ui_hub = UIHub()
    world_connector = WorldConnector()

    orchestrator = MetaOrchestrator(
        persona_manager, skill_tree, memory, automation_mesh,
        compute_fabric, security_core, ui_hub, world_connector
    )

    print("⚡️ Adding a to-do...")
    result = orchestrator.process_intent({"type": "text", "content": "Add todo: Burn the competition"})
    ui_hub.render(result)

    print("⚡️ Listing to-dos...")
    result = orchestrator.process_intent({"type": "text", "content": "List todos"})
    ui_hub.render(result)

    print("⚡️ Marking todo as done...")
    result = orchestrator.process_intent({"type": "text", "content": "Mark done 1"})
    ui_hub.render(result)

    print("⚡️ Removing todo...")
    result = orchestrator.process_intent({"type": "text", "content": "Remove todo 1"})
    ui_hub.render(result)

    print("⚡️ Activating ZEUS plugin skill...")
    result = orchestrator.process_intent({"type": "text", "content": "flash"})
    ui_hub.render(result)

    print("⚡️ Activating STRIKE OF LIGHTNING plugin skill...")
    result = orchestrator.process_intent({"type": "text", "content": "strike"})
    ui_hub.render(result)

if __name__ == "__main__":
    main()
