@echo off
REM === AI ZEUS Project Structure Setup Script ===

REM Create main folder and enter it
mkdir AI_ZEUS
cd AI_ZEUS

REM Create all subfolders
mkdir core
mkdir personas
mkdir skills
mkdir automation
mkdir memory
mkdir compute
mkdir security
mkdir ui
mkdir world
mkdir plugins

REM Create all required files
type nul > main.py
type nul > requirements.txt
type nul > README.md

type nul > core\meta_orchestrator.py
type nul > core\zeus_strike_loader.py

type nul > personas\persona_manager.py

type nul > skills\skill_tree.py
type nul > skills\todo_skill.py

type nul > automation\automation_mesh.py
type nul > memory\omniscient_memory.py
type nul > compute\compute_fabric.py
type nul > security\security_core.py
type nul > ui\ui_hub.py
type nul > world\world_connector.py

type nul > plugins\flash_task.py
type nul > plugins\strike_of_lightning.py

echo.
echo AI ZEUS project structure created successfully!
echo Now open each file in your editor and paste the code.
pause