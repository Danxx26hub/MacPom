from notify import timer
import schedule
from config import get_settings
from logsettings import log_settings


@log_settings
def job():
    time = get_settings("dev").run_time
    timing = timer(time)
    timing.start()
    # timing.countdown()


schedule.every(get_settings("dev").run_time).minutes.do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
