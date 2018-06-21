import os

# 平台
PLATFORM = 'Android'

# 设备名称 通过 adb devices -l 获取
DEVICE_NAME = 'QK1607'

# APP路径
APP = os.path.abspath('.') + '/weixin.apk'

# APP包名
APP_PACKAGE = 'com.cmcc.cmvideo'

# 入口类名
APP_ACTIVITY = 'com.cmcc.cmvideo.splash.SplashActivity'

# Appium地址
DRIVER_SERVER = 'http://localhost:4723/wd/hub'
# 等待元素加载时间
TIMEOUT = 300

# 滑动点
FLICK_START_X = 1000
FLICK_START_Y = 1000
FLICK_DISTANCE = 900

# MongoDB配置
MONGO_URL = 'localhost'
MONGO_DB = 'moments'
MONGO_COLLECTION = 'moments'

# 滑动间隔
SCROLL_SLEEP_TIME = 1
