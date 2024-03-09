from module.automation import auto
from .rewardtemplate import RewardTemplate


class Assist(RewardTemplate):
    def run(self):
        if auto.click_element("./assets/images/share/reward/assist/gift.png", "image", 0.9):
            auto.click_element("./assets/images/zh_CN/base/click_close.png", "image", 0.8, max_retries=10)
