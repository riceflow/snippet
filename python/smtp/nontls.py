import smtplib
from email.mime.text import MIMEText
 
# 送受信先指定
to_email = "送信先@hoge.com"
from_email = "送信元@fuga.com"
 
# メールの内容
message = "メール本文"
msg = MIMEText(message, "html")
msg["Subject"] = "メール表題"
msg["To"] = "hoge@hoge.com"
msg["From"] = "fuga@fuga.com"
 
# サーバ指定
server = smtplib.SMTP("localhost", 25)

# メール送信
server.send_message(msg)

# 切断
server.quit()