ffmpeg -y -loop 1 -t 30 -framerate 30 -i $1/%d.png -hide_banner -crf 8 -preset slow -c:v libx264 -pix_fmt yuv420p -vf scale=1280:720 3d_render.mp4
