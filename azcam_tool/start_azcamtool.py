"""
Start AzCamTool on localhost using default port.
"""

import os

folder = os.path.normpath((os.path.dirname(__file__)))
exe = os.path.join(folder, "builds", "azcamtool.exe")
s = f"start {exe} -s localhost -p 2402"

os.system(s)
