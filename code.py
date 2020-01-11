start_msg_to_user = '''Приложение в разработке.
Введите ”videos” чтобы посмотреть список видео.
Введите “tags” чтобы посмотреть список тегов. 
Введите “playlists” чтобы посмотреть список плейлистов. 
Введите “about” чтобы получить информацию.\n'''

msg_to_user = ""

video_1_title = "Лекция №1"
video_1_link = "https://www.youtube.com/watch?v=KdZ4HF1SrFs&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0"

video_2_title = "#1 - Программирование на Python"
video_2_link = "https://www.youtube.com/watch?v=n0xtO0x81cg&list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu"

video_3_title = "#1 - основы"
video_3_link = "https://www.youtube.com/watch?v=PEKN8NtBDQ0&list=PLY4rE9dstrJyTdVJpv7FibSaXB4BHPInb"

tags = "Python, Git, алгоритмы, Хирьянов, Дударь, loftblog"

playlist_1_title = "Алгоритмы на Python 3"
playlist_2_title = "Уроки Python для начинающих"
playlist_3_title = "Git - для новичков"


user_command = input(start_msg_to_user)

if user_command == "videos":
    msg_to_user = "У нас есть 3 видео:\n" + \
    "{0}: {1} \n".format(video_1_title, video_1_link) + \
    "{0}: {1} \n".format(video_2_title, video_2_link) + \
    "{0}: {1} \n".format(video_3_title, video_3_link)
elif user_command == "tags":
    msg_to_user = "У нас есть 6 тегов: " + tags
elif user_command == "playlists":
    msg_to_user = "У нас есть 3 плейлиста: {0}, {1}, {2}".format(playlist_1_title, playlist_2_title, playlist_3_title)
elif user_command == "about":
    msg_to_user = "Stepik Media – О приложении. Это – кинотеатр полезных видео, посвященных программированию"
else: msg_to_user = "К сожалению, ничего не понятно!"
print(msg_to_user)