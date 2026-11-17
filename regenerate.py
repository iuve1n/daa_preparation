"""Rebuild all editable content sources, in dependency order."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).parent
for script in ['build_content.py','build_questions.py','expand.py','make_tasks.py']:
 subprocess.run([sys.executable,str(root/script)],cwd=root,check=True)
print('Rebuilt lessons, question bank, task metadata and runnable starters.')
