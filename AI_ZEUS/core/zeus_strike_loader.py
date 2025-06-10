import importlib
import os
import sys
import threading
import requests

class ZeusStrikeLoader:
    def __init__(self, plugins_dir="plugins"):
        self.plugins_dir = plugins_dir
        self.plugins = {}
        self._discover_plugins()

    def _discover_plugins(self):
        if not os.path.exists(self.plugins_dir):
            os.makedirs(self.plugins_dir)
        if self.plugins_dir not in sys.path:
            sys.path.insert(0, self.plugins_dir)
        for fname in os.listdir(self.plugins_dir):
            if fname.endswith(".py") and not fname.startswith("_"):
                mod_name = fname[:-3]
                try:
                    mod = importlib.import_module(mod_name)
                    importlib.reload(mod)
                    if hasattr(mod, "Skill"):
                        self.plugins[mod_name] = mod.Skill()
                        print(f"[ZEUS] ⚡ Loaded skill: {mod_name}")
                except Exception as e:
                    print(f"[ZEUS] ⚡ Failed to load {mod_name}: {e}")

    def reload_plugins(self):
        self.plugins.clear()
        self._discover_plugins()

    def strike_from_github(self, raw_url):
        fname = raw_url.split("/")[-1]
        dest_path = os.path.join(self.plugins_dir, fname)
        try:
            r = requests.get(raw_url)
            r.raise_for_status()
            with open(dest_path, "wb") as f:
                f.write(r.content)
            print(f"[ZEUS] ⚡ Skill {fname} struck from the cloud!")
            self.reload_plugins()
        except Exception as e:
            print(f"[ZEUS] ⚡ Strike failed: {e}")

    def execute(self, skill_name, **kwargs):
        skill = self.plugins.get(skill_name)
        if not skill:
            return f"Skill '{skill_name}' not found."
        result = [None]
        def runner():
            try:
                result[0] = skill.execute(**kwargs)
            except Exception as e:
                result[0] = f"Error: {e}"
        t = threading.Thread(target=runner)
        t.start()
        t.join()
        return result[0]
