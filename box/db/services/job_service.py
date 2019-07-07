from ...models import Job

class JobService():
    def __init__(self, jobs_service):
        self._jobs_service = jobs_service

    def get(self, id: str) -> Job:
        return self._jobsService.get(id)
