from flask import Flask, send_file, abort, request
from timetable_image import write_board_image
app = Flask(__name__)

@app.get("/board.png")
def board():
    
    if request.args.get("token") != "my-secret":
        abort(403)
    write_board_image()
    
    return send_file("board.png", mimetype="image/png")

app.run(host="0.0.0.0", port=8000)