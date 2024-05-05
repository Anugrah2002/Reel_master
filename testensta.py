from ensta import Web

username = 'aryansolid'
password = 'Anugrah@0105'


host = Web(username, password)

video_id = host.upload_video_for_reel("reel/reel.mp4", thumbnail="reel/reel_thumbnail.png")

host.pub_reel(
    video_id,
    caption="Enjoying the winter! ⛄")