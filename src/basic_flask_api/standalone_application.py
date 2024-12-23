import gunicorn.app.base

import logging
import psutil
from apscheduler.schedulers.background import BackgroundScheduler
apscheduler_logger = logging.getLogger("apscheduler")
apscheduler_logger.setLevel(logging.WARNING)


class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None, zombie_killer_sleep: int=5):
        self.options = options or {}
        self.application = app
        self.zombie_killer_sleep = zombie_killer_sleep
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

        # Include cleaner scheduler in post_fork
        if "post_fork" in config:
            post_fork_function = config["post_fork"]

            def post_fork(server, worker):
                self.setup_cleaner(worker.pid)
                post_fork_function(server, worker)

            self.cfg.set("post_fork", post_fork)
        else:
            def post_fork(server, worker):
                self.setup_cleaner(worker.pid)

            self.cfg.set("post_fork", post_fork)

    def load(self):
        return self.application
    
    # ====================================================

    def cleanup_zombies(self, worker_pid: int):

        logger = logging.getLogger(f"{worker_pid}.cleanup_zombies")
        logger.debug("Zombie cleaner wakeup")

        worker_process = psutil.Process(worker_pid)

        for process in worker_process.children():
            if process.status() == psutil.STATUS_ZOMBIE:
                logger.info(f"Terminating Zombie process {process.pid}")
                process.wait()

    def setup_cleaner(self, worker_pid: int):
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.cleanup_zombies, "interval", args=(worker_pid,), seconds=self.zombie_killer_sleep)
        scheduler.start()
    
