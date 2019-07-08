from ...models import Job

class JobService():
    def __init__(self, job_service):
        self._job_service = job_service

    def get(self, id: str) -> Job:
        return self._jobService.get(id)
