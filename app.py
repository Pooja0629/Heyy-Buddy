import os, re, urllib.parse, urllib.request
from flask import Flask, abort, jsonify, render_template, request

app = Flask(__name__)

def get_vid(q):
    try:
        enc = urllib.parse.quote(q)
        url = f"https://www.youtube.com/results?search_query={enc}"     
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=5).read().decode()
        ids = re.findall(r"\"videoId\":\"([^\"]+)\"", data)
        return ids[0] if ids else None
    except Exception:
        return None

@app.route("/", methods=["GET"])        
def home():
    return render_template("index.html")

@app.route("/agent",methods=["POST"])
def ai_agent_router():      
    d = request.get_json(silent=True)
    if not d or ("command" not in d and "text_command" not in d):
        abort(400)

    cmd_raw = d.get("command") or d.get("text_command")
    cmd = cmd.raw.strip().lower()
    if "youtube" in cmd:
        q = cmd
        patterns = [
            "open youtube and search",
            "open youtube and play",
            "open youtube",
            "and play",
            "play",
            "on youtube"
        ]
        for p in patterns:
            q = q.replace(p,"")
        q = q.strip()
        vid = get_vid(q)
        if vid:
            target = f"https://youtube.com/embed/{vid}?autoplay=1&mute=1"
            msg = f"Playing{q}"
    elif any(k in cmd for k in ["gmail", "email", "mail", "message",]):
        to, body = "",""
        clean_cmd = re.sub(
            r'^(please\s+)?(open\s+)?(gmail|email|mail|message)\s*',
            '',
            cmd
        ).strip()
        
        clean_cmd = re.sub(r'\b(com(and|mand)?)\b', 'com', clean_cmd)
        parts = re.split(r'\b(type|write|saying|message|content|with body)\b', clean_cmd)
        recip_part = parts[0].strip()
        recip_part = re.sub(r'^(update\s+to|send\s+to|and\s+update\s+update\s+tp)\s*', '', recip_part).strip()
        if len(parts) > 1:
            body = parts[-1].strip()
            
            
            
        