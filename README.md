To use this code you should:
1. Create file position_report.xlsx. Structure of this file should be the same as in example.
2. Login on https://app.dataforseo.com/api-dashboard and get credentials.
3. Create file .secure and add credentials like in example:
    AUTHORIZATION=Basic <!!!Here should be your token!!!>
4. Add email credentials in file .secure:
    sender_email=example@gmail.com
    app_password=password_from_app_gmail.com
    receiver_email=receiver_example@gmail.com
5. Create virtual environment and install packets from requirements.txt
6. Run file xls_worker.py
7. Result will be sent on email, which you put in .secure
8. If it necessarily refills you account - go to the dashboard: https://app.dataforseo.com/api-dashboard