import os

if os.system('python requests_games.py') == 0:
    if os.system('python selenium_games.py') == 0:
        print('SUCCESS')
        exit(0)

exit(1)
