import yt_dlp
import requests
import webbrowser

def get_video_download_url(video_url):
    ydl_opts = {
        'format': 'best',
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        video_download_url = info_dict.get('url', None)

    return video_download_url

# def send_to_telegram(bot_token, chat_id, mp4_url):
#     telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
#     data = {
#         'chat_id': chat_id,
#         'text': f"{mp4_url}",
#     }

#     response = requests.post(telegram_url, data=data)

#     if response.status_code == 200:
#         print("Message sent successfully!")
#     else:
#         print(f"Failed to send message, status code: {response.status_code}")

def open_video_in_browser(mp4_url):
    print(f"Opening video in browser: {mp4_url}")
    webbrowser.open(mp4_url) 

def main():
    video_url = 'https://www.youtube.com/watch?v=6G2xwWzJHnk'
    # Lấy link MP4
    mp4_url = get_video_download_url(video_url)
    # print("MP4 URL: ", mp4_url)
    
    # bot_token = '7819390933:AAGJKF3hmoajQ8q_-9_JX0cQb30DVc9bvMg'  
    # chat_id = '5823554565'
    # send_to_telegram(bot_token, chat_id, mp4_url)

    # Mở video trong trình duyệt
    open_video_in_browser(mp4_url)

if __name__ == "__main__":
    main()
